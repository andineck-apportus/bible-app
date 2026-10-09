#!/usr/bin/env python3
"""Import der SBLGNT-Apparateinträge eines Buchs als Variantenstellen auf Editionsebene.

Aufruf:
    python3 scripts/import_sblgnt_apparatus.py MRK PFAD/Faithlife-SBLGNT --upstream-commit <git-sha>

Quelle: github.com/Faithlife/SBLGNT, data/sblgntapp/text/<Buch>.txt (CC BY 4.0).
Der Apparat vergleicht den SBLGNT-Text mit anderen Editionen (Siglen WH, Treg, NA28, RP …).
Er ist KEIN Handschriftenbeleg; die Datensätze werden daher als
evidence_level = "edition_apparatus" geführt und nicht mit Zeugenangaben vermischt.

Jeder Eintrag wird an die SBLGNT-Tokens (data/tokens/SBLGNT-<BUCH>-<KKK>.json) gebunden: Die Zeichen
⸀/⸁ (ein Wort) bzw. ⸂…⸃ und ⸄…⸅ (Wortgruppe) im SBLGNT-Text markieren die Apparatstellen eines
Verses in derselben Reihenfolge. Der Importer prüft, dass die Wörter des Lemmas mit den markierten
Tokens übereinstimmen. Nicht sicher zuordenbare Einträge werden NICHT importiert, sondern in
reports/sblgntapp-<BUCH>-nicht-zugeordnet.json aufgeführt.
"""
import argparse
import datetime
import hashlib
import json
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from nt_books import BOOKS  # noqa: E402

# Bereits vorhandene Variantenstellen (Handschriftenebene), die dieselbe Stelle betreffen
SAME_UNIT = {("MRK", 3, 29, 1): "VAR-MRK-003-029-001"}
SIGLA = {
    "WH": "ED-WH", "WHmarg": None, "WHapp": None, "Treg": "ED-TREG", "Tregmarg": None,
    "NIV": None, "NA28": "ED-NA28", "RP": "ED-RP", "TR": None, "SBL": None,
    "Holmes": None,      # Lesart des SBLGNT-Herausgebers, von keiner der verglichenen Editionen gestützt
    "Greeven": None,     # Greeven (Synopse); keine eigene Edition im Projekt
    "⟦WH⟧": "ED-WH",     # Westcott-Hort, im Text in doppelten eckigen Klammern
}
SINGLE, OPEN, CLOSE = "⸀⸁", {"⸂": "⸃", "⸄": "⸅"}, "⸃⸅"

ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
ap.add_argument("book")
ap.add_argument("sblgnt", type=pathlib.Path, help="Pfad zum Faithlife/SBLGNT-Repository")
ap.add_argument("--upstream-commit", required=True)
ap.add_argument("--source-url", default="https://github.com/Faithlife/SBLGNT")
ap.add_argument("--tag", action="append", default=[])
args = ap.parse_args()
if not re.fullmatch(r"[0-9a-f]{40}", args.upstream_commit):
    sys.exit("ERROR: --upstream-commit muss ein vollständiger 40-stelliger Git-SHA sein")
code = args.book
name = BOOKS[code][0]
source = args.sblgnt / "data/sblgntapp/text" / f"{name}.txt"


def norm(word):
    word = unicodedata.normalize("NFC", word).replace("ʼ", "’")
    return re.sub(r"[⸀-⸅,.·;:!?()—⟦⟧]", "", word)


def split_sigla(segment):
    """'δύναται RP' -> ('δύναται', ['RP']); Siglen stehen am Ende des Segments."""
    words = segment.split()
    sigla = []
    while words and words[-1].rstrip(".") in SIGLA:
        sigla.insert(0, words.pop().rstrip("."))
    if not sigla:
        raise ValueError(f"keine Siglen in {segment!r}")
    return " ".join(words), sigla


def parse_entry(text):
    lemma_part, _, readings_part = text.partition(" ] ")
    if not readings_part:
        raise ValueError(f"kein ']' in {text!r}")
    lemma, lemma_sigla = split_sigla(lemma_part)
    readings = [split_sigla(seg.strip()) for seg in readings_part.split(";")]
    return lemma, lemma_sigla, readings


# Apparat lesen: {(kapitel, vers): [rohzeile, ...]}
entries, key = {}, None
for line in source.read_text(encoding="utf-8").splitlines():
    line = re.sub(r"\s+", " ", line.replace("\xa0", " ")).strip()
    m = re.fullmatch(rf"{re.escape(name)} (\d+):(\d+)", line)
    if m:
        key = (int(m.group(1)), int(m.group(2)))
        continue
    if key is None or not line or " ] " not in line:
        continue
    entries.setdefault(key, []).append(re.sub(r"^(?:\d+(?::\d+)?|•)\s+", "", line))

# Tokens lesen
by_verse = {}
for p in sorted((ROOT / "data/tokens").glob(f"SBLGNT-{code}-[0-9][0-9][0-9].json")):
    for tok in json.loads(p.read_text(encoding="utf-8"))["tokens"]:
        _, ch, v = tok["reference"].split(".")
        by_verse.setdefault((int(ch), int(v)), []).append(tok)


def marked_spans(tokens):
    """Markierte Stellen in der Reihenfolge ihres Beginns; Spannen dürfen verschachtelt sein."""
    spans, stack = [], []
    for i, tok in enumerate(tokens):
        t = tok["text"]
        for ch in t:
            if ch in SINGLE:
                spans.append((i, [tok]))
            elif ch in OPEN:
                stack.append((ch, i, len(spans)))
                spans.append(None)  # Platzhalter in Reihenfolge des Beginns
            elif ch in CLOSE:
                if not stack or OPEN[stack[-1][0]] != ch:
                    return None
                _, start, slot = stack.pop()
                spans[slot] = (start, tokens[start:i + 1])
    if stack or any(s is None for s in spans):
        return None
    return [s[1] for s in spans]


def lemma_matches(lemma, span):
    words = [norm(w) for w in lemma.split()]
    toks = [norm(t["text"]) for t in span]
    if "…" not in words:
        return toks == words
    # Lemma mit Auslassungen: Teile müssen in Reihenfolge vorkommen, erster am Anfang, letzter am Ende
    parts, cur = [], []
    for w in words:
        if w == "…":
            parts.append(cur)
            cur = []
        else:
            cur.append(w)
    parts.append(cur)
    if toks[:len(parts[0])] != parts[0] or (parts[-1] and toks[len(toks) - len(parts[-1]):] != parts[-1]):
        return False
    pos = len(parts[0])
    for part in parts[1:-1]:
        for i in range(pos, len(toks) - len(part) + 1):
            if toks[i:i + len(part)] == part:
                pos = i + len(part)
                break
        else:
            return False
    return pos <= len(toks) - len(parts[-1])


source_sha = hashlib.sha256(source.read_bytes()).hexdigest()
out_dir = ROOT / "data/variants" / f"sblgntapp-{code.lower()}"
records, unmapped = [], []
for (ch, v) in sorted(set(entries) | set(by_verse)):
    raw = entries.get((ch, v), [])
    if not raw:
        continue
    tokens = by_verse.get((ch, v), [])
    spans = marked_spans(tokens)
    ref = f"{code}.{ch}.{v}"
    if spans is None or len(raw) != len(spans):
        reason = "Markierungen nicht auswertbar" if spans is None else f"{len(raw)} Apparateinträge, aber {len(spans)} markierte Stellen"
        unmapped += [{"reference": ref, "entry": t, "reason": reason} for t in raw]
        continue
    for n, (text, span) in enumerate(zip(raw, spans), 1):
        try:
            lemma, lemma_sigla, readings = parse_entry(text)
        except ValueError as exc:
            unmapped.append({"reference": ref, "entry": text, "reason": str(exc)})
            continue
        if not lemma_matches(lemma, span):
            unmapped.append({"reference": ref, "entry": text,
                             "reason": f"Lemma passt nicht zu markierten Tokens {[t['text'] for t in span]}"})
            continue

        def reading(rid, txt, sigla, base=False):
            kind = "addition" if txt.startswith("+") else "omission" if txt.startswith("–") else "unclassified"
            eds = [SIGLA[s] for s in sigla if SIGLA.get(s)]
            r = {"reading_id": rid, "text": txt, "is_sblgnt_text": base,
                 **({"sblgnt_editor_only": True} if base and "Holmes" in sigla else {}),
                 **({"no_counted_edition": True} if not eds else {}),
                 "editions": eds,
                 "sigla": sigla}
            if not base:
                r["relation_to_sblgnt"] = kind
            return r

        rec = {
            "id": f"VAR-SBLGNTAPP-{code}-{ch:03d}-{v:03d}-{n:02d}",
            "type": "variant",
            "status": "imported_unreviewed",
            "tags": args.tag + ["TAG-TEXT-CRITICISM"],
            "reference": ref,
            "evidence_level": "edition_apparatus",
            "apparatus": "SRC-SBLGNT-APPARATUS",
            "base_edition": "ED-SBLGNT",
            "base_tokens": [t["id"] for t in span],
            "readings": [reading("R1", lemma, lemma_sigla, base=True)]
                        + [reading(f"R{i}", t, s) for i, (t, s) in enumerate(readings, 2)],
            "apparatus_entry": text,
            **({"same_variation_unit_as": SAME_UNIT[(code, ch, v, n)]} if (code, ch, v, n) in SAME_UNIT else {}),
            "note_de": "Vergleich gedruckter Editionen laut SBLGNT-Apparat; keine Handschriftenbelege.",
            "source": {"url": args.source_url, "upstream_commit": args.upstream_commit,
                       "file": f"data/sblgntapp/text/{name}.txt", "sha256": source_sha,
                       "license": "CC BY 4.0, © 2010 Society of Biblical Literature und Logos Bible Software"},
            "import": {"tool": "scripts/import_sblgnt_apparatus.py",
                       "imported_on": datetime.date.today().isoformat()},
        }
        records.append(rec)

out_dir.mkdir(parents=True, exist_ok=True)
for old in out_dir.glob("VAR-SBLGNTAPP-*.json"):
    old.unlink()
for rec in records:
    (out_dir / f"{rec['id']}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
report = ROOT / "reports" / f"sblgntapp-{code}-nicht-zugeordnet.json"
report.write_text(json.dumps({"book": code, "source_sha256": source_sha, "imported": len(records),
                              "not_imported": len(unmapped), "entries": unmapped},
                             ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
total = sum(map(len, entries.values()))
print(f"PASS: {len(records)} von {total} Apparateinträgen für {code} importiert; "
      f"{len(unmapped)} nicht sicher zuordenbar (siehe {report.relative_to(ROOT)}); sha256={source_sha}")
