#!/usr/bin/env python3
"""Import MorphGNT SBLGNT Markus 3,22–30 aus einer lokal bereitgestellten Upstream-Datei.

Aufruf:
    python3 scripts/import_morphgnt.py PFAD/62-Mk-morphgnt.txt \
        --upstream-commit <git-sha> [--upstream-ref 6.12] [--source-url URL]

Format (MorphGNT-README): 7 durch Leerzeichen getrennte Spalten
    Buch/Kapitel/Vers (BBCCVV, Markus = 02) · Wortart · Parsing ·
    Text inkl. Interpunktion · Wort ohne Interpunktion · normalisiertes Wort · Lemma
Kein Netzwerkzugriff; bricht ab statt unvollständige oder erfundene Daten zu schreiben.
"""
import argparse
import collections
import datetime
import hashlib
import json
import pathlib
import re
import sys

TOOL_VERSION = "0.6"
BOOK_NUMBER, BOOK_CODE, CHAPTER, VERSES = "02", "MRK", 3, range(22, 31)

ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
ap.add_argument("source", type=pathlib.Path)
ap.add_argument("--upstream-commit", help="Git-Commit der Upstream-Datei (Pflicht für einen nachweisbaren Import)")
ap.add_argument("--upstream-ref", default=None, help="Tag/Branch, z. B. 6.12")
ap.add_argument("--source-url", default="https://github.com/morphgnt/sblgnt")
ap.add_argument("--allow-unpinned", action="store_true", help="nur für Tests: ohne Upstream-Commit importieren")
args = ap.parse_args()

if not args.source.is_file():
    sys.exit("ERROR: input file missing")
if not args.upstream_commit and not args.allow_unpinned:
    sys.exit("ERROR: --upstream-commit fehlt; ohne nachweisbare Quellversion wird nichts geschrieben")
if args.upstream_commit and not re.fullmatch(r"[0-9a-f]{40}", args.upstream_commit):
    sys.exit("ERROR: --upstream-commit muss ein vollständiger 40-stelliger Git-SHA sein")

root = pathlib.Path(__file__).resolve().parents[1]
ref_re = re.compile(rf"{BOOK_NUMBER}{CHAPTER:02d}(\d\d)")
tokens, verse_counts, bad = [], collections.Counter(), []
for line_number, line in enumerate(args.source.read_text(encoding="utf-8-sig").splitlines(), 1):
    parts = line.split()
    if not parts:
        continue
    m = ref_re.fullmatch(parts[0])
    if not m or int(m.group(1)) not in VERSES:
        continue
    if len(parts) != 7:
        bad.append(line_number)
        continue
    _, pos, parsing, text, word, normalized, lemma = parts
    verse = int(m.group(1))
    verse_counts[verse] += 1
    idx = verse_counts[verse]
    tokens.append({
        "id": f"TOK-SBLGNT-{BOOK_CODE}-{CHAPTER:03d}-{verse:03d}-{idx:03d}",
        "reference": f"{BOOK_CODE}.{CHAPTER}.{verse}",
        "position": idx,
        "text": text,
        "word": word,
        "normalized": normalized,
        "lemma": lemma,
        "pos": pos,
        "parsing": parsing,
        "edition": "ED-SBLGNT",
    })
if bad:
    sys.exit(f"ERROR: malformed rows at lines {bad[:10]}; no output written")
missing = sorted(set(VERSES) - set(verse_counts))
if missing:
    sys.exit(f"ERROR: missing verses {missing}; no output written")

source_info = {
    "dataset": "SRC-MORPHGNT-612",
    "url": args.source_url,
    "upstream_ref": args.upstream_ref,
    "upstream_commit": args.upstream_commit,
    "file": args.source.name,
    "sha256": hashlib.sha256(args.source.read_bytes()).hexdigest(),
    "license": {
        "text": "SBLGNT, CC BY 4.0, © 2010 Society of Biblical Literature und Logos Bible Software (laut github.com/Faithlife/SBLGNT, Stand v1.1)",
        "annotation": "MorphGNT-Morphologie und Lemmatisierung, CC BY-SA 3.0 (laut MorphGNT-README)",
        "attribution": "Tauber, J. K., ed. (2017) MorphGNT: SBLGNT Edition. Version 6.12. DOI 10.5281/zenodo.376200",
        "note": "Das MorphGNT-README verweist für den Text noch auf die SBLGNT EULA; massgeblich ist die aktuelle Lizenz des Rechteinhabers. Vor Veröffentlichung erneut prüfen.",
    },
}
import_info = {"tool": "scripts/import_morphgnt.py", "tool_version": TOOL_VERSION,
              "imported_on": datetime.date.today().isoformat()}
scope = f"{BOOK_CODE}.{CHAPTER}.{VERSES[0]}-{BOOK_CODE}.{CHAPTER}.{VERSES[-1]}"
suffix = f"SBLGNT-{BOOK_CODE}-{CHAPTER:03d}-{VERSES[0]:03d}-{VERSES[-1]:03d}"
common = {"status": "imported_unreviewed", "tags": ["TAG-MARK"], "edition": "ED-SBLGNT",
          "reference": scope, "source": source_info, "import": import_info}

token_set = {"id": f"TOKSET-{suffix}", "type": "token_set", **common,
             "token_policy": "Ein Token pro MorphGNT-Zeile; Textkritische Zeichen (⸀, ⸂ …) der SBLGNT bleiben in «text» erhalten.",
             "tokens": tokens}
lemmas = collections.Counter(t["lemma"] for t in tokens)
forms = collections.Counter(t["normalized"] for t in tokens)
counts = {"id": f"COUNT-{suffix}", "type": "lemma_count", **common,
          "count_policy": "Tokens = MorphGNT-Zeilen; Wortformen = verschiedene normalisierte Formen; Lemmata = verschiedene MorphGNT-Lemmata.",
          "verse_count": len(VERSES),
          "token_count": len(tokens),
          "tokens_by_verse": {f"{BOOK_CODE}.{CHAPTER}.{v}": verse_counts[v] for v in VERSES},
          "unique_forms": len(forms),
          "unique_lemmas": len(lemmas),
          "lemma_counts": dict(sorted(lemmas.items()))}

for folder, obj in (("tokens", token_set), ("counts", counts)):
    target = root / "data" / folder / f"{suffix}.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"PASS: imported {len(tokens)} tokens / {len(forms)} forms / {len(lemmas)} lemmas, sha256={source_info['sha256']}")
