#!/usr/bin/env python3
"""Import der SBLGNT-Apparateinträge für Markus 3,22–30 als Variantenstellen auf Editionsebene.

Aufruf:
    python3 scripts/import_sblgnt_apparatus.py PFAD/data/sblgntapp/text/Mark.txt \
        --upstream-commit <git-sha>

Quelle: github.com/Faithlife/SBLGNT, data/sblgntapp/text/Mark.txt (CC BY 4.0).
Der Apparat vergleicht den SBLGNT-Text mit anderen Editionen (Siglen WH, Treg, NA28, RP …).
Er ist KEIN Handschriftenbeleg; die Datensätze werden daher als
evidence_level = "edition_apparatus" geführt und nicht mit Zeugenangaben vermischt.

Jeder Eintrag wird an die SBLGNT-Tokens gebunden: Die Zeichen ⸀ (ein Wort) bzw. ⸂…⸃ (Wortgruppe)
im SBLGNT-Text markieren die Apparatstellen eines Verses in derselben Reihenfolge. Der Importer
prüft, dass die Wörter des Lemmas mit den markierten Tokens übereinstimmen, und bricht sonst ab.
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
BOOK, BOOK_EN, CHAPTER, VERSES = "MRK", "Mark", 3, range(22, 31)
TOKENS = ROOT / "data/tokens/SBLGNT-MRK-003-022-030.json"
# Bereits vorhandene Variantenstellen (Handschriftenebene), die dieselbe Stelle betreffen
SAME_UNIT = {(29, 1): "VAR-MRK-003-029-001"}
SIGLA = {
    "WH": "ED-WH", "WHmarg": None, "WHapp": None, "Treg": "ED-TREG", "Tregmarg": None,
    "NIV": None, "NA28": "ED-NA28", "RP": "ED-RP", "TR": None, "SBL": None,
}

ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
ap.add_argument("source", type=pathlib.Path)
ap.add_argument("--upstream-commit", required=True)
ap.add_argument("--source-url", default="https://github.com/Faithlife/SBLGNT")
args = ap.parse_args()
if not re.fullmatch(r"[0-9a-f]{40}", args.upstream_commit):
    sys.exit("ERROR: --upstream-commit muss ein vollständiger 40-stelliger Git-SHA sein")


def norm(word):
    word = unicodedata.normalize("NFC", word).replace("ʼ", "’")
    return re.sub(r"[⸀-⸅,.·;:!?]", "", word)


def split_sigla(segment):
    """'δύναται RP' -> ('δύναται', ['RP']); Siglen stehen am Ende des Segments."""
    words = segment.split()
    sigla = []
    while words and words[-1] in SIGLA:
        sigla.insert(0, words.pop())
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


# Apparat lesen: {vers: [rohzeile, ...]}
entries, verse = {}, None
for line in args.source.read_text(encoding="utf-8").splitlines():
    line = re.sub(r"\s+", " ", line.replace("\xa0", " ")).strip()
    m = re.fullmatch(rf"{BOOK_EN} (\d+):(\d+)", line)
    if m:
        verse = int(m.group(2)) if int(m.group(1)) == CHAPTER and int(m.group(2)) in VERSES else None
        continue
    if verse is None or not line:
        continue
    text = re.sub(r"^(?:\d+(?::\d+)?|•)\s+", "", line)
    entries.setdefault(verse, []).append(text)

tokset = json.loads(TOKENS.read_text(encoding="utf-8"))
by_verse = {}
for tok in tokset["tokens"]:
    by_verse.setdefault(int(tok["reference"].split(".")[-1]), []).append(tok)


def marked_spans(tokens):
    spans, open_span = [], None
    for tok in tokens:
        t = tok["text"]
        if "⸀" in t:
            spans.append([tok])
        if "⸂" in t:
            open_span = [tok]
        elif open_span is not None:
            open_span.append(tok)
        if "⸃" in t and open_span is not None:
            spans.append(open_span)
            open_span = None
    return spans


def lemma_matches(lemma, span):
    words = [norm(w) for w in lemma.split()]
    toks = [norm(t["text"]) for t in span]
    if "…" in words:
        i = words.index("…")
        return toks[:i] == words[:i] and toks[len(toks) - (len(words) - i - 1):] == words[i + 1:]
    return toks == words


source_sha = hashlib.sha256(args.source.read_bytes()).hexdigest()
out_dir = ROOT / "data/variants"
records, problems = [], []
for v in VERSES:
    raw = entries.get(v, [])
    spans = marked_spans(by_verse[v])
    if len(raw) != len(spans):
        problems.append(f"{BOOK}.{CHAPTER}.{v}: {len(raw)} Apparateinträge, aber {len(spans)} markierte Stellen")
        continue
    for n, (text, span) in enumerate(zip(raw, spans), 1):
        lemma, lemma_sigla, readings = parse_entry(text)
        if not lemma_matches(lemma, span):
            problems.append(f"{BOOK}.{CHAPTER}.{v} Eintrag {n}: Lemma {lemma!r} passt nicht zu "
                            f"{[t['text'] for t in span]}")
            continue

        def reading(rid, txt, sigla, base=False):
            kind = "addition" if txt.startswith("+") else "omission" if txt.startswith("–") else "unclassified"
            r = {"reading_id": rid, "text": txt.replace("ʼ", "’"), "is_sblgnt_text": base,
                 "editions": [SIGLA[s] for s in sigla if SIGLA.get(s)],
                 "sigla": sigla}
            if not base:
                r["relation_to_sblgnt"] = kind
            return r

        rec = {
            "id": f"VAR-SBLGNTAPP-{BOOK}-{CHAPTER:03d}-{v:03d}-{n:02d}",
            "type": "variant",
            "status": "imported_unreviewed",
            "tags": ["TAG-MARK", "TAG-TEXT-CRITICISM"],
            "reference": f"{BOOK}.{CHAPTER}.{v}",
            "evidence_level": "edition_apparatus",
            "apparatus": "SRC-SBLGNT-APPARATUS",
            "base_edition": "ED-SBLGNT",
            "base_tokens": [t["id"] for t in span],
            "readings": [reading("R1", lemma, lemma_sigla, base=True)]
                        + [reading(f"R{i}", t, s) for i, (t, s) in enumerate(readings, 2)],
            "apparatus_entry": text,
            **({"same_variation_unit_as": SAME_UNIT[(v, n)]} if (v, n) in SAME_UNIT else {}),
            "note_de": "Vergleich gedruckter Editionen laut SBLGNT-Apparat; keine Handschriftenbelege.",
            "source": {"url": args.source_url, "upstream_commit": args.upstream_commit,
                       "file": "data/sblgntapp/text/Mark.txt", "sha256": source_sha,
                       "license": "CC BY 4.0, © 2010 Society of Biblical Literature und Logos Bible Software"},
            "import": {"tool": "scripts/import_sblgnt_apparatus.py",
                       "imported_on": datetime.date.today().isoformat()},
        }
        records.append(rec)

if problems:
    sys.exit("ERROR: " + "; ".join(problems) + "; no output written")
for rec in records:
    (out_dir / f"{rec['id']}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"PASS: {len(records)} Variantenstellen (Editionsebene) für {BOOK}.{CHAPTER}.{VERSES[0]}-{BOOK}.{CHAPTER}.{VERSES[-1]}, sha256={source_sha}")
