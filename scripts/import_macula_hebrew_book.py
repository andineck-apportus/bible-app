#!/usr/bin/env python3
"""Import eines AT-Buchs: hebräischer Text (Westminster Leningrad Codex) als Token-Schicht und
MACULA-Hebrew-Annotation als eigene Schicht.

Aufruf:
    python3 scripts/import_macula_hebrew_book.py OBA --macula PFAD/macula-hebrew --macula-commit <sha> --tag TAG-OBADIAH

Quelle: github.com/Clear-Bible/macula-hebrew, WLC/lowfat/<NN>-<Buch>-<KKK>-lowfat.xml (CC BY 4.0, «MACULA Hebrew
Linguistic Datasets, available at https://github.com/Clear-Bible/macula-hebrew/»). Der hebräische Text ist der
Westminster Leningrad Codex (tanach.us, gemeinfrei); die Morphologie stammt aus der OpenScriptures Hebrew Bible
(CC BY 4.0), die englischen Glossen von Cherith Analytics (CC BY 4.0).

Token-Politik: ein Token je Morphem, wie MACULA es trennt (z. B. וְ «und» + צִיר «Bote»), damit die Wortzuordnung
Vorsilben wie «und», «in», «zu» einzeln zuordnen kann. «word_no» gibt das Wort (orthographische Einheit) im Vers an,
«text» ist das Morphem mit nachfolgendem Zeichen der Edition (z. B. Maqqef ־, Sof Pasuq ׃), «word» ohne dieses.
Morpheme ohne eigene Schreibung (z. B. der im ב verschmolzene Artikel) werden nicht als Token geführt, sondern in
«implicit_morphs» aufgeführt.

NICHT übernommen: sdbh, lexdomain, coredomain, sensenumber (Semantic Dictionary of Biblical Hebrew, UBS, nur
«used with permission») und mandarin.

Ausgabe je Kapitel:
    data/tokens/WLC-<BUCH>-<KKK>.json              (TOKSET-WLC-<BUCH>-<KKK>)
    data/annotations/MACULA-WLC-<BUCH>-<KKK>.json  (ANN-MACULA-WLC-<BUCH>-<KKK>)
    data/counts/WLC-<BUCH>.json                    (COUNT-WLC-<BUCH>)
"""
import argparse
import datetime
import hashlib
import json
import pathlib
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import refs  # noqa: E402
import versification  # noqa: E402

from ot_books import FILES  # noqa: E402
XID = "{http://www.w3.org/XML/1998/namespace}id"
KEEP = ["lemma", "stronglemma", "morph", "pos", "class", "type", "person", "gender", "number", "state", "stem", "role",
        "gloss", "english", "transliteration", "greek", "greekstrong", "strongnumberx", "frame", "subjref", "participantref"]
EXCLUDED = ["sdbh", "lexdomain", "coredomain", "sensenumber", "mandarin"]
LICENSE = ("CC BY 4.0, MACULA Hebrew Linguistic Datasets © Biblica; Text: Westminster Leningrad Codex (gemeinfrei); "
           "Morphologie: OpenScriptures Hebrew Bible (CC BY 4.0); Glossen: Cherith Glosses for the Hebrew Old Testament "
           "von Andi Wu, © 2022 Cherith Analytics (CC BY 4.0)")
ATTR = "MACULA Hebrew Linguistic Datasets, available at https://github.com/Clear-Bible/macula-hebrew/"

ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
ap.add_argument("book", choices=sorted(FILES))
ap.add_argument("--macula", type=pathlib.Path, required=True)
ap.add_argument("--macula-commit", required=True)
ap.add_argument("--tag", required=True)
args = ap.parse_args()
if not re.fullmatch(r"[0-9a-f]{40}", args.macula_commit):
    sys.exit("ERROR: --macula-commit muss eine vollständige 40-stellige Git-SHA sein")
today = datetime.date.today().isoformat()
D = ROOT / "data"
files = sorted((args.macula / "WLC" / "lowfat").glob(f"{FILES[args.book]}-*-lowfat.xml"))
if not files:
    sys.exit("ERROR: keine lowfat-Dateien gefunden")

totals, lemmas_all, by_chapter, ann_ids = 0, {}, {}, []
nav = json.loads((ROOT / "data/navigation/NAV-PROT66-KJV.json").read_text(encoding="utf-8"))
kjv = next(b["verses_per_chapter"] for b in nav["books"] if b["code"] == args.book)

# 1. Alle Morpheme in hebräischer Zählung lesen
morphs = []  # (quellvers, wort_nr, attrib, text)
raws = {}
for f in files:
    raw = f.read_bytes()
    raws[f.name] = raw
    for w in ET.fromstring(raw).iter("w"):
        a = w.attrib
        m = re.fullmatch(r"([1-3]?[A-Z]{2,3}) (\d+):(\d+)!(\d+)", a["ref"])
        if not m or m.group(1) != args.book:
            sys.exit(f"ERROR: unerwartete Stelle {a['ref']}")
        morphs.append((f"{args.book}.{int(m.group(2))}.{int(m.group(3))}", int(m.group(4)), a,
                       unicodedata.normalize("NFC", w.text or "")))
words = {}
for ref, wn, _, text in morphs:
    words.setdefault(ref, {}).setdefault(wn, "")
    words[ref][wn] += text
verses = {r: [ws[k] for k in sorted(ws)] for r, ws in words.items()}
wordkeys = {r: sorted(ws) for r, ws in words.items()}

# 2. In die Navigationszählung (KJV) umrechnen (TVTMS, scripts/versification.py)
plan, empty = versification.heb_to_kjv(args.book, verses)
target = {}  # (quellvers, wort_nr) -> (zielvers, neue wort_nr, art)
for dst, items in versification.apply(args.book, verses, plan).items():
    # Wortnummern bleiben wie in MACULA; kommen Wörter aus mehreren Quellversen, werden spätere Teile verschoben.
    offset, prev_src, top = 0, None, 0
    for src, wi, kind in items:
        wn = wordkeys[src][wi]
        if src != prev_src:
            offset, prev_src = (top if prev_src is not None else 0), src
        target[(src, wn)] = (dst, wn + offset, kind)
        top = max(top, wn + offset)
got = {}
for dst, _, _ in target.values():
    _, c, v = dst.split(".")
    got.setdefault(int(c), set()).add(int(v))
for r in empty:
    _, c, v = r.split(".")
    got.setdefault(int(c), set()).add(int(v))
if got != {c + 1: set(range(1, n + 1)) for c, n in enumerate(kjv)}:
    sys.exit(f"ERROR: {args.book}: Umrechnung ergibt nicht die Verszahlen der Navigation (KJV)")
converted = sum(1 for p in plan.values() if p[0][3] != "same" or len(p) > 1)

# 3. Tokens und Annotation je Kapitel der Navigationszählung
src_files = {}
for f in files:
    for m in re.finditer(rb'<milestone unit="verse" id="[1-3]?[A-Z]{2,3} (\d+):(\d+)"', raws[f.name]):
        src_files[f"{args.book}.{int(m.group(1))}.{int(m.group(2))}"] = f.name
chapters = {}
pos_in_verse = {}
for src, wn, a, text in morphs:
    dst, new_wn, kind = target[(src, wn)]
    c = int(dst.split(".")[1])
    ch = chapters.setdefault(c, {"tokens": [], "entries": {}, "implicit": [], "files": set()})
    ch["files"].add(src_files[src])
    moved = dst != src or new_wn != wn
    if not text:
        im = {"macula_id": a[XID], "reference": dst, "word_no": new_wn, "pos": a.get("pos"), "gloss": a.get("gloss")}
        if moved:
            im.update({"source_reference": src, "source_word_no": wn})
        ch["implicit"].append(im)
        continue
    _, _, v = dst.split(".")
    n = pos_in_verse[dst] = pos_in_verse.get(dst, 0) + 1
    tid = f"TOK-WLC-{args.book}-{c:03d}-{int(v):03d}-{n:03d}"
    after = a.get("after")
    tok = {"id": tid, "reference": dst, "position": n, "word_no": new_wn,
           "text": text + (after if after and after.strip() else ""), "word": text}
    if after is not None:
        tok["after"] = after
    if moved:
        tok["source_reference"] = src
        tok["source_word_no"] = wn
    if kind == "title":
        tok["title"] = True
    ch["tokens"].append(tok)
    e = {"macula_id": a[XID]}
    for k in KEEP:
        if a.get(k):
            e[k] = a[k]
    ch["entries"][tid] = e
    lemmas_all.setdefault(a.get("lemma"), 0)
    lemmas_all[a.get("lemma")] += 1

POLICY = ("Ein Token je Morphem nach MACULA Hebrew; «word_no» = Wort im Vers; «text» mit folgendem Maqqef bzw. "
          "Sof Pasuq, «word» ohne. Morpheme ohne eigene Schreibung stehen in «implicit_morphs».")
VPOLICY = ("Stellen in der Navigationszählung (KJV), aus der hebräischen Zählung des WLC umgerechnet nach TVTMS "
           "(scripts/versification.py). Wo umgerechnet wurde, stehen hebräische Stelle und Wortnummer in "
           "«source_reference»/«source_word_no»; Psalmüberschriften (eigener hebräischer Vers) sind dem ersten Vers "
           "vorangestellt und mit «title» markiert.")
for c in sorted(chapters):
    ch = chapters[c]
    names = sorted(ch["files"])
    src = {"url": "https://github.com/Clear-Bible/macula-hebrew", "upstream_commit": args.macula_commit,
           "file": f"WLC/lowfat/{names[0]}" if len(names) == 1 else [f"WLC/lowfat/{n}" for n in names],
           "sha256": hashlib.sha256(raws[names[0]]).hexdigest() if len(names) == 1
           else [hashlib.sha256(raws[n]).hexdigest() for n in names],
           "license": LICENSE, "attribution": ATTR}
    ts_id, an_id = f"TOKSET-WLC-{args.book}-{c:03d}", f"ANN-MACULA-WLC-{args.book}-{c:03d}"
    rec = {"id": ts_id, "type": "token_set", "status": "imported_unreviewed", "tags": [args.tag], "edition": "ED-WLC",
           "reference": f"{args.book}.{c}", "language": "he", "token_policy": POLICY}
    if converted:
        rec["versification"] = "KJV"
        rec["versification_policy"] = VPOLICY
    rec.update({"source": src, "import": {"tool": "scripts/import_macula_hebrew_book.py", "imported_on": today},
                "implicit_morphs": ch["implicit"], "tokens": ch["tokens"]})
    (D / "tokens").mkdir(exist_ok=True)
    (D / "tokens" / f"WLC-{args.book}-{c:03d}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1) + "\n",
                                                               encoding="utf-8")
    (D / "annotations" / f"MACULA-WLC-{args.book}-{c:03d}.json").write_text(json.dumps({
        "id": an_id, "type": "annotation_set", "status": "imported_unreviewed", "tags": [args.tag], "annotates": ts_id,
        "reference": f"{args.book}.{c}", "layers": ["morphology", "lemma", "syntax_role", "referents", "semantic_frame", "gloss",
                                                     "transliteration", "septuagint_equivalent"],
        "source": {**src, "excluded_fields": EXCLUDED,
                   "excluded_reason": "Semantic Dictionary of Biblical Hebrew (UBS) nur «used with permission»; mandarin nicht benötigt"},
        "import": {"tool": "scripts/import_macula_hebrew_book.py", "imported_on": today},
        "entries": ch["entries"]}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    by_chapter[f"{args.book}.{c}"] = {"tokens": len(ch["tokens"]),
                                      "words": len({(t["reference"], t["word_no"]) for t in ch["tokens"]}),
                                      "unique_lemmas": len({e.get("lemma") for e in ch["entries"].values()})}
    totals += len(ch["tokens"])
    ann_ids.append(an_id)
files = list(chapters)
(D / "counts" / f"WLC-{args.book}.json").write_text(json.dumps({
    "id": f"COUNT-WLC-{args.book}", "type": "lemma_count", "status": "imported_unreviewed", "tags": [args.tag],
    "edition": "ED-WLC", "reference": args.book, "based_on_annotations": ann_ids,
    "count_policy": "Tokens = Morpheme mit eigener Schreibung (MACULA Hebrew); Lemmata = verschiedene MACULA-Lemmata.",
    "token_count": totals, "unique_lemmas": len(lemmas_all), "by_chapter": by_chapter,
    "import": {"tool": "scripts/import_macula_hebrew_book.py", "imported_on": today},
    "lemma_counts": dict(sorted(lemmas_all.items(), key=lambda kv: (-kv[1], kv[0] or "")))}, ensure_ascii=False, indent=1) + "\n",
    encoding="utf-8")
print(f"PASS: {args.book}: {totals} Morphem-Tokens in {len(files)} Kapitel(n), {len(lemmas_all)} Lemmata")
