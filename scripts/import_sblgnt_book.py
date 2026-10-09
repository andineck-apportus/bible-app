#!/usr/bin/env python3
"""Import eines NT-Buchs: SBLGNT-Text als Token-Schicht + MACULA-Greek-Annotation als eigene Schicht.

Aufruf:
    python3 scripts/import_sblgnt_book.py MRK \
        --sblgnt PFAD/Faithlife-SBLGNT --sblgnt-commit <sha> \
        --macula PFAD/macula-greek --macula-commit <sha>

Quellen:
- Text: github.com/Faithlife/SBLGNT, data/sblgnt/text/<Buch>.txt (CC BY 4.0). Die Zeichen ⸀ ⸁ ⸂⸃ ⸄⸅
  (Apparatstellen), Interpunktion und Klammern bleiben im Feld «text» erhalten.
- Annotation: github.com/Clear-Bible/macula-greek, SBLGNT/tsv/macula-greek-SBLGNT.tsv (CC BY 4.0).
  Übernommen: Lemma, Morphologie, Wortart, Syntaxrolle, Referenten, semantischer Rahmen, Strong,
  Glossen (Berean: gemeinfrei; Cherith: CC BY 4.0). NICHT übernommen: domain/ln (MARBLE,
  nur «used with permission»).

Die Wortgrenzen beider Quellen müssen übereinstimmen (Vergleich ohne Interpunktion und
Apparatzeichen und Elisionszeichen, Unicode NFC). Abweichungen in Akzenten werden protokolliert, eine
abweichende Wortzahl führt zum Abbruch. Ausgabe je Kapitel:
    data/tokens/SBLGNT-<BUCH>-<KKK>.json        (TOKSET-SBLGNT-<BUCH>-<KKK>)
    data/annotations/MACULA-SBLGNT-<BUCH>-<KKK>.json (ANN-MACULA-SBLGNT-<BUCH>-<KKK>)
    data/counts/SBLGNT-<BUCH>.json               (COUNT-SBLGNT-<BUCH>, nach MACULA-Lemmata)
"""
import argparse
import collections
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
MARKS = "⸀⸁⸂⸃⸄⸅⟦⟧"
MACULA_FIELDS = {  # TSV-Spalte -> Feldname in der Annotation
    "lemma": "lemma", "normalized": "normalized", "morph": "morph", "class": "pos", "type": "subtype",
    "person": "person", "number": "number", "gender": "gender", "case": "case", "tense": "tense",
    "voice": "voice", "mood": "mood", "degree": "degree", "strong": "strong", "role": "role",
    "frame": "frame", "gloss": "gloss_berean", "english": "gloss_cherith_en",
}
MACULA_ID_FIELDS = {"subjref": "subject_ref", "referent": "referent"}

ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
ap.add_argument("book", choices=sorted(BOOKS))
ap.add_argument("--sblgnt", type=pathlib.Path, required=True)
ap.add_argument("--sblgnt-commit", required=True)
ap.add_argument("--macula", type=pathlib.Path, required=True)
ap.add_argument("--macula-commit", required=True)
ap.add_argument("--tag", action="append", default=[], help="Tag-ID(s) für alle erzeugten Datensätze, z. B. TAG-MARK")
args = ap.parse_args()
for c in (args.sblgnt_commit, args.macula_commit):
    if not re.fullmatch(r"[0-9a-f]{40}", c):
        sys.exit("ERROR: Commits müssen vollständige 40-stellige Git-SHAs sein")

code = args.book
name, macnum = BOOKS[code]
text_file = args.sblgnt / "data/sblgnt/text" / f"{name}.txt"
tsv_file = args.macula / "SBLGNT/tsv/macula-greek-SBLGNT.tsv"


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def bare(w):
    w = unicodedata.normalize("NFC", w)
    w = "".join(ch for ch in w if ch not in MARKS)
    return re.sub(r"[,.·;:!?()—“”‘«»\[\]]", "", w)


def comparable(w):
    """Vergleichsform: MACULA führt das Elisionszeichen nicht im Wort, sondern in «after»."""
    return bare(w).replace("ʼ", "").replace("’", "")


def strip_accents(w):
    return "".join(ch for ch in unicodedata.normalize("NFD", w) if not unicodedata.combining(ch))


# SBLGNT-Text lesen
verses = {}
for line in text_file.read_text(encoding="utf-8").splitlines():
    m = re.fullmatch(rf"{re.escape(name)} (\d+):(\d+)\t(.*)", line.strip("﻿"))
    if m:
        verses[(int(m.group(1)), int(m.group(2)))] = m.group(3).split()

# MACULA lesen
mac = collections.defaultdict(list)
with tsv_file.open(encoding="utf-8") as fh:
    header = fh.readline().rstrip("\n").split("\t")
    col = {h: i for i, h in enumerate(header)}
    for line in fh:
        c = line.rstrip("\n").split("\t")
        m = re.fullmatch(rf"{code} (\d+):(\d+)!(\d+)", c[col["ref"]])
        if m:
            mac[(int(m.group(1)), int(m.group(2)))].append(c)

if set(verses) != set(mac):
    sys.exit(f"ERROR: Versbestand verschieden: nur SBLGNT {sorted(set(verses)-set(mac))[:5]}, nur MACULA {sorted(set(mac)-set(verses))[:5]}")


def tok_id(ch, v, n):
    return f"TOK-SBLGNT-{code}-{ch:03d}-{v:03d}-{n:03d}"


def macula_to_tok(mid):
    m = re.fullmatch(rf"n{macnum}(\d{{3}})(\d{{3}})(\d{{3}})", mid)
    return tok_id(*map(int, m.groups())) if m else None


accent_diffs, problems = [], []
chapters = collections.defaultdict(lambda: {"tokens": [], "ann": {}})
for (ch, v) in sorted(verses):
    words = [w for w in verses[(ch, v)] if bare(w)]
    rows = mac[(ch, v)]
    if len(words) != len(rows):
        problems.append(f"{code}.{ch}.{v}: {len(words)} SBLGNT-Wörter, {len(rows)} MACULA-Wörter")
        continue
    for n, (w, r) in enumerate(zip(words, rows), 1):
        tid = tok_id(ch, v, n)
        if macula_to_tok(r[col["xml:id"]]) != tid:
            problems.append(f"{tid}: MACULA-ID {r[col['xml:id']]} passt nicht")
            continue
        a, b = comparable(w), comparable(r[col["text"]])
        if a != b:
            if strip_accents(a) == strip_accents(b):
                accent_diffs.append({"token": tid, "sblgnt": bare(w), "macula": r[col["text"]]})
            else:
                problems.append(f"{tid}: SBLGNT {w!r} ≠ MACULA {r[col['text']]!r}")
                continue
        chapters[ch]["tokens"].append({"id": tid, "reference": f"{code}.{ch}.{v}", "position": n,
                                       "text": w, "word": bare(w)})
        entry = {"macula_id": r[col["xml:id"]]}
        for src, dst in MACULA_FIELDS.items():
            if r[col[src]]:
                entry[dst] = r[col[src]]
        if "frame" in entry:  # MACULA-IDs im Rahmen («A0:n41…») in Token-IDs umsetzen
            entry["frame"] = re.sub(r"n\d{11}", lambda m: macula_to_tok(m.group(0)) or "unresolved", entry["frame"])
        for src, dst in MACULA_ID_FIELDS.items():
            raw_ids = r[col[src]].split() if r[col[src]] else []
            ids = [macula_to_tok(x) for x in raw_ids if macula_to_tok(x)]
            unresolved = [x for x in raw_ids if not macula_to_tok(x)]
            if ids:
                entry[dst] = ids
            if unresolved:  # z. B. Platzhalter n00000000000 = «kein Referent angegeben»
                entry[f"{dst}_unresolved"] = True
        chapters[ch]["ann"][tid] = entry

if problems:
    sys.exit("ERROR: " + "; ".join(problems[:10]) + f" ({len(problems)} Probleme); no output written")

today = datetime.date.today().isoformat()
src_text = {"url": "https://github.com/Faithlife/SBLGNT", "upstream_commit": args.sblgnt_commit,
            "file": f"data/sblgnt/text/{name}.txt", "sha256": sha(text_file),
            "license": "CC BY 4.0, © 2010 Society of Biblical Literature und Logos Bible Software"}
src_mac = {"url": "https://github.com/Clear-Bible/macula-greek", "upstream_commit": args.macula_commit,
           "file": "SBLGNT/tsv/macula-greek-SBLGNT.tsv", "sha256": sha(tsv_file),
           "license": "CC BY 4.0, MACULA Greek Linguistic Datasets © Biblica; Glossen: Berean Interlinear (gemeinfrei), Cherith Glosses for the Greek New Testament von Andi Wu, © 2023 Cherith Analytics (CC BY 4.0)",
           "attribution": "MACULA Greek Linguistic Datasets, available at https://github.com/Clear-Bible/macula-greek/",
           "excluded_fields": ["domain", "ln"],
           "excluded_reason": "MARBLE-Wortbedeutungen nur «used with permission», keine offene Lizenz"}
imp = {"tool": "scripts/import_sblgnt_book.py", "imported_on": today}


def dump(obj, list_key, path):
    """JSON mit einem Eintrag pro Zeile für die grosse Liste/Map (lesbare Git-Diffs)."""
    head = {k: v for k, v in obj.items() if k != list_key}
    body = json.dumps(head, ensure_ascii=False, indent=2)[:-2]
    items = obj[list_key]
    if isinstance(items, dict):
        lines = [f"    {json.dumps(k, ensure_ascii=False)}: {json.dumps(v, ensure_ascii=False)}" for k, v in items.items()]
        block = "{\n" + ",\n".join(lines) + "\n  }"
    else:
        block = "[\n" + ",\n".join("    " + json.dumps(x, ensure_ascii=False) for x in items) + "\n  ]"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f'{body},\n  "{list_key}": {block}\n}}\n', encoding="utf-8")
    json.loads(path.read_text(encoding="utf-8"))  # Kontrolle


lemma_total = collections.Counter()
by_chapter = {}
for ch, d in sorted(chapters.items()):
    first, last = d["tokens"][0]["reference"], d["tokens"][-1]["reference"]
    tokset = {"id": f"TOKSET-SBLGNT-{code}-{ch:03d}", "type": "token_set", "status": "imported_unreviewed",
              "tags": args.tag, "edition": "ED-SBLGNT", "reference": f"{code}.{ch}",
              "token_policy": "Ein Token pro SBLGNT-Wort (Leerzeichentrennung). «text» unverändert aus der Edition inkl. Interpunktion und Apparatzeichen; «word» ohne diese Zeichen.",
              "source": src_text, "import": imp, "tokens": d["tokens"]}
    ann = {"id": f"ANN-MACULA-SBLGNT-{code}-{ch:03d}", "type": "annotation_set", "status": "imported_unreviewed",
           "tags": args.tag, "annotates": tokset["id"], "reference": f"{code}.{ch}",
           "layers": ["morphology", "lemma", "syntax_role", "referents", "semantic_frame", "gloss"],
           "source": src_mac, "import": imp, "entries": d["ann"]}
    dump(tokset, "tokens", ROOT / f"data/tokens/SBLGNT-{code}-{ch:03d}.json")
    dump(ann, "entries", ROOT / f"data/annotations/MACULA-SBLGNT-{code}-{ch:03d}.json")
    lem = collections.Counter(e["lemma"] for e in d["ann"].values() if "lemma" in e)
    lemma_total.update(lem)
    by_chapter[f"{code}.{ch}"] = {"tokens": len(d["tokens"]), "unique_lemmas": len(lem)}

counts = {"id": f"COUNT-SBLGNT-{code}", "type": "lemma_count", "status": "imported_unreviewed", "tags": args.tag,
          "edition": "ED-SBLGNT", "reference": code,
          "based_on_annotations": [f"ANN-MACULA-SBLGNT-{code}-{ch:03d}" for ch in sorted(chapters)],
          "count_policy": "Tokens = SBLGNT-Wörter; Lemmata = verschiedene MACULA-Lemmata.",
          "token_count": sum(c["tokens"] for c in by_chapter.values()),
          "unique_lemmas": len(lemma_total), "by_chapter": by_chapter,
          "accent_differences_sblgnt_vs_macula": accent_diffs,
          "source": {"text": src_text, "annotation": src_mac}, "import": imp,
          "lemma_counts": dict(sorted(lemma_total.items()))}
p = ROOT / f"data/counts/SBLGNT-{code}.json"
p.write_text(json.dumps(counts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"PASS: {code}: {counts['token_count']} Tokens in {len(by_chapter)} Kapiteln, {counts['unique_lemmas']} Lemmata, "
      f"{len(accent_diffs)} Akzentabweichung(en) SBLGNT/MACULA protokolliert")
