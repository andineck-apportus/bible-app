#!/usr/bin/env python3
"""Ordnet an Variantenstellen zu, welche Handschrift bzw. Ausgabe welche Lesart hat (automatische Kollation).

Aufruf: python3 scripts/collate_witnesses.py MRK.3.20-MRK.3.35

Eingaben (alle aus data/):
- Variantenstellen im Bereich (variant) mit Lesarten und base_tokens
- SBLGNT-Wörter (token_set) als Gerüst
- Transkriptionen (witness_transcription) der Handschriften und Ausgaben, Format MES (CNTR)

Verfahren (METHOD-AUTO-COLLATION-V1):
1. Für jede Lesart wird der Vers so gebildet, als stünde die Lesart im SBLGNT-Text.
2. Handschrift und Lesarten werden vereinfacht verglichen: ohne Akzente, Gross/Klein,
   Zeilenumbrüche und Abkürzungszeichen, mit vereinheitlichter Schreibung gleich klingender Laute
   (z. B. ει/ι, ω/ο, αι/ε), weil alte Schreiber oft nach Gehör schrieben.
3. Die Wörter einer Lesart müssen im Vers der Handschrift vorkommen (Ähnlichkeit mindestens 0,85);
   so stören Umstellungen in der Nachbarschaft weniger.
   Verglichen wird ein Fenster aus der Stelle und drei Wörtern Kontext links und rechts. Gewählt wird
   die Lesart mit der höchsten Ähnlichkeit, wenn sie hoch genug ist und sich klar von der nächsten abhebt;
   sonst «unklar» oder «andere Form».
4. Korrekturen werden als eigene Schichten verglichen: Erstschrift (x{…}) und korrigierter Text.
   Unterscheiden sich Lesarten nur in der Schreibweise (z. B. διαρπάσει/διαρπάσῃ), entscheidet die genaue
   Schreibung; bei Handschriften ist das unsicher, weil Schreiber gleich klingende Laute verwechselten.
5. Ist die Stelle beschädigt oder ergänzt (^, %, ~, +), wird das vermerkt.

Ergebnis: data/witness-readings/WREAD-CNTR-<BEREICH>.json (status imported_unreviewed). Kein Ergebnis
ist eine Prüfung am Faksimile.
"""
import datetime
import difflib
import json
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import refs  # noqa: E402

D = ROOT / "data"
THRESHOLD, MARGIN, K, CORE = 0.72, 0.012, 3, 0.85


def load_all(folder):
    return {r["id"]: r for r in (json.loads(p.read_text(encoding="utf-8")) for p in sorted((D / folder).rglob("*.json")))}


def strip(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn")
    s = s.replace("ς", "σ").replace("ϲ", "σ").replace("¯", "ν")
    return re.sub(r"[^α-ω]", "", s)


def phon(w):
    for a, b in (("ει", "ι"), ("οι", "ι"), ("η", "ι"), ("υ", "ι"), ("ω", "ο"), ("αι", "ε"), ("γγ", "γ"),
                 ("λλ", "λ"), ("σσ", "σ"), ("ττ", "τ"), ("νν", "ν"), ("ρρ", "ρ"), ("μμ", "μ")):
        w = w.replace(a, b)
    return w[:-1] if len(w) > 2 and w.endswith("ν") else w


GROUP = re.compile(r"([xab]?)\{([^}]*)\}")


def layers(mes):
    """Gibt {Schicht: [(roh, sauber), …]} zurück. Schichten: 'first' (Erstschrift) und ggf. 'corr'."""
    if mes is None or mes.strip() == "-":
        return {}
    parts, pos, sets = [], 0, []
    for m in GROUP.finditer(mes):
        parts.append(("text", mes[pos:m.start()]))
        parts.append(("group", (m[1], m[2])))
        pos = m.end()
    parts.append(("text", mes[pos:]))
    # benachbarte Gruppen (nur durch Leerraum getrennt) bilden eine Alternative
    merged = []
    for kind, val in parts:
        if kind == "group" and merged and merged[-1][0] == "alt" and merged[-1][2]:
            merged[-1][1].append(val)
        elif kind == "group":
            merged.append(["alt", [val], True])
        elif merged and merged[-1][0] == "alt" and not val.strip():
            continue
        else:
            merged.append(["text", val, False])
            if merged[-2:-1] and merged[-2][0] == "alt":
                merged[-2][2] = False
    out = {}
    for layer, prio in (("first", ["x", ""]), ("corr", ["b", "a", "", "x"])):
        text = []
        for kind, val, _ in merged:
            if kind == "text":
                text.append(val)
            else:
                alt = dict(val)
                pick = next((alt[p] for p in prio if p in alt), "")
                if layer == "first" and "x" not in alt and "" not in alt:
                    pick = ""
                text.append(" " + pick + " ")
        raw = re.sub(r"[/\\|]", "", " ".join(text))
        words = [(w, strip(w)) for w in raw.split()]
        out[layer] = [(w, c) for w, c in words if c]
    if out.get("corr") == out.get("first"):
        out.pop("corr")
    return out


def reading_words(text, base_words):
    text = text.strip()
    if text in ("–", "-", "om.", ""):
        return []
    if text.startswith("+"):
        return base_words + [strip(w) for w in text[1:].split() if strip(w)]
    toks = text.split()
    if "…" in toks:
        i = toks.index("…")
        a, b = strip(toks[i - 1]), strip(toks[i + 1])
        ia, ib = base_words.index(a), base_words.index(b)
        filled = [strip(t) for t in toks[:i]] + base_words[ia + 1:ib] + [strip(t) for t in toks[i + 1:]]
        return [w for w in filled if w]
    return [strip(t) for t in toks if strip(t)]


def ratio(cand, span, f):
    return difflib.SequenceMatcher(None, " ".join(f(w) for w in cand), " ".join(f(c) for _, c in span)).ratio()


def best_window(cand, wit):
    target = " ".join(phon(w) for w in cand)
    best = (0.0, 0, 0)
    for s in range(len(wit)):
        for ln in range(max(1, len(cand) - 2), len(cand) + 3):
            if s + ln > len(wit):
                break
            sc = difflib.SequenceMatcher(None, target, " ".join(phon(c) for _, c in wit[s:s + ln])).ratio()
            if sc > best[0]:
                best = (sc, s, s + ln)
    return best


def main():
    scope = refs.canonical(sys.argv[1])
    a, _, z = scope.partition("-")
    book, ch, v0 = a.split("."); v1 = z.split(".")[2] if z else v0
    ch, v0, v1 = int(ch), int(v0), int(v1)
    tokens = json.loads((D / f"tokens/SBLGNT-{book}-{ch:03d}.json").read_text(encoding="utf-8"))["tokens"]
    by_verse = {}
    for t in tokens:
        by_verse.setdefault(t["reference"], []).append(t)
    variants = [v for v in load_all("variants").values()
                if v.get("reference", "").startswith(f"{book}.{ch}.") and v.get("base_tokens")
                and v0 <= int(v["reference"].split(".")[2].split("-")[0]) <= v1]
    texts = [t for t in load_all("witness-texts").values() if t["type"] == "witness_transcription"]
    entries, checks = [], []
    for v in sorted(variants, key=lambda x: x["id"]):
        ref = v["reference"]
        vt = by_verse[ref]
        words = [strip(t["word"]) for t in vt]
        idx = [i for i, t in enumerate(vt) if t["id"] in v["base_tokens"]]
        i0, i1 = min(idx), max(idx)
        base = words[i0:i1 + 1]
        cands, cores = {}, {}
        for r in v["readings"]:
            rw = reading_words(r["text"], base)
            full = words[:i0] + rw + words[i1 + 1:]
            cands[r["reading_id"]] = full[max(0, i0 - K): i0 + len(rw) + K]
            cores[r["reading_id"]] = rw
        # Lesarten, die vereinfacht gleich aussehen, lassen sich nicht unterscheiden
        for t in texts:
            src = t.get("witness") or t.get("edition")
            mes = t["verses"].get(ref)
            if t.get("edition"):
                ls = {"first": [(w, strip(w)) for w in re.sub(r"[/\\|]", "", mes or "").split() if strip(w)]} if mes else {}
            else:
                ls = layers(mes)
            if not ls:
                entries.append({"variant": v["id"], "source": src, "hand": "first", "result": "lacuna",
                                "note_de": "Vers in dieser Handschrift nicht erhalten."})
                continue
            for layer, wit in ls.items():
                # 1. Fundstelle: jede Lesart sucht ihr bestes Fenster; verglichen wird dann mit der
                #    Vereinigung aller Fenster, damit eine Auslassung nicht in einem kürzeren Fenster «passt».
                wins = [best_window(c, wit) for c in cands.values()]
                s, e = min(w[1] for w in wins), max(w[2] for w in wins)
                span = wit[s:e]
                scores = {rid: (ratio(c, span, phon), ratio(c, span, lambda x: x)) for rid, c in cands.items()}
                # 2. Die Wörter der Lesart selbst müssen im Vers vorkommen (wichtig bei Umstellungen in der Nähe).
                core_ok = {rid: (not cores[rid]) or best_window(cores[rid], wit)[0] >= CORE for rid in cands}
                order = sorted(scores.items(), key=lambda kv: (not core_ok[kv[0]], -kv[1][0], -kv[1][1]))
                if order and not core_ok[order[0][0]]:
                    scores = {rid: (0.0, 0.0) for rid in scores}
                    order = sorted(scores.items())
                rid, (sc, strict) = order[0]
                second = max((sc2 for r2, (sc2, _) in order[1:] if core_ok[r2]), default=0)
                if len(order) > 1 and sc - second < MARGIN and strict - order[1][1][1] >= MARGIN:
                    second = sc - MARGIN  # nur in der Schreibweise unterscheidbar: genaue Schreibung entscheidet
                raw = [w for w, _ in wit[s:e]]
                damaged = any(re.search(r"[\^%&*]", w) for w in raw)
                supplied = any(re.search(r"[~+]", w) for w in raw)
                if sc < THRESHOLD:
                    result = "other"
                elif sc - second < MARGIN:
                    result = "unclear"
                else:
                    result = rid
                e_ = {"variant": v["id"], "source": src, "hand": layer, "result": result,
                      "score": round(sc, 3), "margin": round(sc - second, 3),
                      "witness_text": " ".join(raw)}
                if damaged:
                    e_["damaged"] = True
                if supplied:
                    e_["supplied"] = True
                if layer == "corr" and entries and entries[-1].get("source") == src and \
                        entries[-1].get("result") == result and entries[-1].get("witness_text") == e_["witness_text"]:
                    continue  # Korrektur betrifft eine andere Stelle des Verses
                entries.append(e_)
                if t.get("edition") in ("ED-WH", "ED-RP"):
                    expect = [r["reading_id"] for r in v["readings"] if t["edition"] in r.get("editions", [])]
                    if v.get("evidence_level") == "edition_apparatus":
                        checks.append((v["id"], t["edition"], expect, result))
    today = datetime.date.today().isoformat()
    sid = f"WREAD-CNTR-{book}-{ch:03d}-{v0:03d}-{v1:03d}"
    rec = {"id": sid, "type": "witness_reading_set", "status": "imported_unreviewed",
           "tags": ["TAG-TEXT-CRITICISM", "TAG-MARK"], "reference": scope, "method": "METHOD-AUTO-COLLATION-V1",
           "based_on": sorted({t["id"] for t in texts}), "created_at": today,
           "hands_de": {"first": "Erstschrift bzw. Ausgabentext", "corr": "korrigierter Text (Korrektur des Schreibers oder späterer Hände)"},
           "results_de": {"R…": "Lesart der Variantenstelle", "other": "liest anders als alle erfassten Lesarten",
                          "unclear": "keine eindeutige Zuordnung möglich", "lacuna": "Stelle nicht erhalten"},
           "entries": entries}
    out = D / "witness-readings" / f"{sid}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rec, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    ok = sum(1 for _, _, exp, res in checks if res in exp)
    bad = [(vid, ed, exp, res) for vid, ed, exp, res in checks if res not in exp]
    print(f"Abgleich mit SBLGNT-Apparat (WH, RP): {ok}/{len(checks)} übereinstimmend")
    for b in bad:
        print("  abweichend:", *b)
    print(f"PASS: {len(entries)} Zuordnungen für {len(variants)} Variantenstellen -> {out.relative_to(ROOT)}")


main()
