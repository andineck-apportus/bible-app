"""Hilfen für Autorenwerkzeuge: Übersetzung mit Wortzuordnung in einer Auszeichnung, Datensätze schreiben,
Lokalisierungen anlegen.

Auszeichnung je Vers (Zielsprache in der Reihenfolge des Übersetzungstexts):
    «Paulus{1}, [ein Knecht]{2} Gottes{3}, … ~5»
- ``Wort{n}`` bzw. ``[mehrere Wörter]{n}`` ordnet den Zieltext den Tokens n (Position im Vers) zu; mehrere Tokens
  ``{3,4}`` oder ``{3-5}``.
- Erscheint dieselbe Tokengruppe an mehreren Stellen («hat … gesagt»), wird sie zu einer Zuordnung «hat … gesagt».
- Text ohne Klammern sind Ergänzungen der Zielsprache (z. B. Artikel); sie gehören zum Übersetzungstext.
- ``~n`` (am Ende) bzw. ``~n(Hinweis)``: Token n ist nicht eigens wiedergegeben.
- ``{n:idiom}``: Zuordnung als Redewendung (kind idiom).
Der Übersetzungstext entsteht aus der Auszeichnung; so stimmen Text und Wortzuordnung immer überein.
"""
import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
D = ROOT / "data"
sys.path.insert(0, str(ROOT / "scripts"))
import localizations  # noqa: E402

GROUP = re.compile(r"\[([^\]]+)\]\{([^}]+)\}|([^\s\[\]{}~]+?)\{([^}]+)\}")
SKIP = re.compile(r"\s*~(\d+)(?:\(([^)]*)\))?")


def _positions(spec):
    kind = "phrase"
    if ":" in spec:
        spec, kind = spec.split(":", 1)
    out = []
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-")
            out += list(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return tuple(out), kind


def parse(markup):
    """-> (Text, [(Positionen, Zieltext, Art)], {Position: Hinweis} für nicht Wiedergegebenes)"""
    skips = {}
    body = markup
    for m in list(SKIP.finditer(markup)):
        skips[int(m.group(1))] = m.group(2) or None
    body = SKIP.sub("", markup).strip()
    links, order = {}, []

    def repl(m):
        target = m.group(1) or m.group(3)
        lead = ""
        if m.group(3):  # vorangestellte Satzzeichen («, „, () gehören zum Text, nicht zur Zuordnung
            lead = re.match(r"^[«»„“\"'(–-]*", target).group(0)
            target = target[len(lead):]
        pos, kind = _positions(m.group(2) or m.group(4))
        if pos not in links:
            links[pos] = {"targets": [], "kind": kind}
            order.append(pos)
        links[pos]["targets"].append(target)
        if kind != "phrase":
            links[pos]["kind"] = kind
        return lead + target

    text = GROUP.sub(repl, body)
    text = re.sub(r"\s+", " ", text).strip()
    return text, [(p, " … ".join(links[p]["targets"]), links[p]["kind"]) for p in order], skips


def alignment_entries(ref, markup, tokens, tokid):
    """tokens: {Position: Wortlaut}; tokid(Position) -> Token-ID."""
    text, links, skips = parse(markup)
    used = [p for pos, _, _ in links for p in pos]
    dup = {p for p in used if used.count(p) > 1}
    if dup:
        raise SystemExit(f"{ref}: Tokens mehrfach: {sorted(dup)}")
    missing = sorted(set(tokens) - set(used) - set(skips))
    extra = sorted((set(used) | set(skips)) - set(tokens))
    if missing or extra:
        raise SystemExit(f"{ref}: ohne Zuordnung {missing}, unbekannt {extra}")
    out = []
    for pos, target, kind in links:
        e = {"reference": ref, "source_tokens": [tokid(p) for p in pos], "source": " ".join(tokens[p] for p in pos),
             "target": target, "kind": "idiom" if kind == "idiom" else ("lexical" if len(pos) == 1 else "phrase")}
        for part in target.split(" … "):
            if part not in text:
                raise SystemExit(f"{ref}: Zieltext {part!r} nicht im Vers")
        out.append(e)
    for p, note in sorted(skips.items()):
        out.append({"reference": ref, "source_tokens": [tokid(p)], "source": tokens[p], "target": None,
                    "kind": "untranslated", "note": note or "nicht eigens wiedergegeben"})
    out.sort(key=lambda e: min(int(t.rsplit("-", 1)[1]) for t in e["source_tokens"]))
    return text, out


def write(path, rec, change_de="Inhalt überarbeitet"):
    """Schreibt nur bei inhaltlicher Änderung; frühere Fassung kommt ins revision_log."""
    path = pathlib.Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        old = json.loads(path.read_text(encoding="utf-8"))
        cmp = lambda r: {k: v for k, v in r.items() if k not in ("revision_log", "knowledge")}
        if cmp(old) == cmp(rec):
            return False
        prev = {k: v for k, v in cmp(old).items() if cmp(rec).get(k) != v}
        rec["revision_log"] = old.get("revision_log", []) + [{"date": rec.get("knowledge", {}).get("asserted_at", ""),
                                                               "change_de": change_de, "previous": prev}]
        rec["knowledge"] = old.get("knowledge", rec.get("knowledge"))
    path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return True


def localize(rid, original, fields, lang, code, ctx, authorship, date):
    """Lokalisierung eines Originaldatensatzes schreiben (Feldnamen wie im Original)."""
    for k, v in fields.items():
        ov = [t.get("de") for t in original.get("terms", [])] if k == "terms" else original.get(k)
        if ov is None or type(ov) is not type(v) or (isinstance(v, list) and len(v) != len(ov)):
            raise SystemExit(f"{rid}: Feld {k} passt nicht zum Original")
    loc = {"id": f"L10N-{code}-{rid}", "type": "localization", "status": "draft", "tags": [], "localizes": rid,
           "language": lang, "target_context": ctx, "fields": fields,
           "source_fingerprint": {k: localizations.fingerprint(original.get(k)) for k in fields},
           "authorship_de": authorship, "review_de": "Noch keine muttersprachliche Prüfung dokumentiert.",
           "knowledge": {"asserted_at": date, "supersedes": None}}
    return write(D / "localizations" / lang / f"{rid}.json", loc, "Fassung erneuert")


def load_tokens(path):
    t = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    by_ref = {}
    for k in t["tokens"]:
        by_ref.setdefault(k["reference"], {})[k["position"]] = k
    return t["id"], by_ref
