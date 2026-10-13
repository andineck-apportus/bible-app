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

# Dateipräfixe von MACULA Hebrew (WLC/lowfat/<NN>-<Buch>-<KKK>-lowfat.xml) je Buchcode
FILES = {code: f"{i:02d}-{name}" for i, (code, name) in enumerate([
    ("GEN", "Gen"), ("EXO", "Exo"), ("LEV", "Lev"), ("NUM", "Num"), ("DEU", "Deu"), ("JOS", "Jos"), ("JDG", "Jdg"),
    ("RUT", "Rut"), ("1SA", "1Sa"), ("2SA", "2Sa"), ("1KI", "1Ki"), ("2KI", "2Ki"), ("1CH", "1Ch"), ("2CH", "2Ch"),
    ("EZR", "Ezr"), ("NEH", "Neh"), ("EST", "Est"), ("JOB", "Job"), ("PSA", "Psa"), ("PRO", "Pro"), ("ECC", "Ecc"),
    ("SNG", "Sng"), ("ISA", "Isa"), ("JER", "Jer"), ("LAM", "Lam"), ("EZK", "Ezk"), ("DAN", "Dan"), ("HOS", "HOS"),
    ("JOL", "Jol"), ("AMO", "Amo"), ("OBA", "Oba"), ("JON", "Jon"), ("MIC", "Mic"), ("NAM", "Nam"), ("HAB", "Hab"),
    ("ZEP", "Zep"), ("HAG", "Hag"), ("ZEC", "Zec"), ("MAL", "Mal")], start=1)}
# Bücher, deren hebräische Verszählung von der Navigationszählung (KJV) abweicht, brauchen vor dem Import eine
# Umrechnung (data/versification); bis dahin nur Bücher ohne Abweichung importieren.
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

nav = json.loads((ROOT / "data/navigation/NAV-PROT66-KJV.json").read_text(encoding="utf-8"))
kjv = next(b["verses_per_chapter"] for b in nav["books"] if b["code"] == args.book)
heb = {}
for f in files:
    for m in re.finditer(r'<milestone unit="verse" id="[1-3]?[A-Z]{2,3} (\d+):(\d+)"', f.read_text(encoding="utf-8")):
        heb[int(m.group(1))] = max(heb.get(int(m.group(1)), 0), int(m.group(2)))
if [heb.get(c, 0) for c in range(1, len(kjv) + 1)] != kjv or len(heb) != len(kjv):
    sys.exit(f"ERROR: {args.book}: hebräische Verszählung weicht von der Navigationszählung (KJV) ab; erst Umrechnung umsetzen")

totals, lemmas_all, by_chapter, ann_ids = 0, {}, {}, []
for f in files:
    raw = f.read_bytes()
    c = int(re.search(r"-(\d{3})-lowfat", f.name).group(1))
    tokens, entries, implicit = [], {}, []
    pos_in_verse = {}
    for w in ET.fromstring(raw).iter("w"):
        a = w.attrib
        m = re.fullmatch(r"([1-3]?[A-Z]{2,3}) (\d+):(\d+)!(\d+)", a["ref"])
        if not m or m.group(1) != args.book or int(m.group(2)) != c:
            sys.exit(f"ERROR: unerwartete Stelle {a['ref']}")
        v, word_no = int(m.group(3)), int(m.group(4))
        ref = f"{args.book}.{c}.{v}"
        refs.parse(ref)
        text = unicodedata.normalize("NFC", w.text or "")
        if not text:
            implicit.append({"macula_id": a[XID], "reference": ref, "word_no": word_no, "pos": a.get("pos"),
                             "gloss": a.get("gloss")})
            continue
        n = pos_in_verse[ref] = pos_in_verse.get(ref, 0) + 1
        tid = f"TOK-WLC-{args.book}-{c:03d}-{v:03d}-{n:03d}"
        after = a.get("after")
        tok = {"id": tid, "reference": ref, "position": n, "word_no": word_no,
               "text": text + (after if after and after.strip() else ""), "word": text}
        if after is not None:
            tok["after"] = after
        tokens.append(tok)
        e = {"macula_id": a[XID]}
        for k in KEEP:
            if a.get(k):
                e[k] = a[k]
        entries[tid] = e
        lemmas_all.setdefault(a.get("lemma"), 0)
        lemmas_all[a.get("lemma")] += 1
    src = {"url": "https://github.com/Clear-Bible/macula-hebrew", "upstream_commit": args.macula_commit,
           "file": f"WLC/lowfat/{f.name}", "sha256": hashlib.sha256(raw).hexdigest(), "license": LICENSE, "attribution": ATTR}
    ts_id, an_id = f"TOKSET-WLC-{args.book}-{c:03d}", f"ANN-MACULA-WLC-{args.book}-{c:03d}"
    (D / "tokens").mkdir(exist_ok=True)
    (D / "tokens" / f"WLC-{args.book}-{c:03d}.json").write_text(json.dumps({
        "id": ts_id, "type": "token_set", "status": "imported_unreviewed", "tags": [args.tag], "edition": "ED-WLC",
        "reference": f"{args.book}.{c}", "language": "he",
        "token_policy": "Ein Token je Morphem nach MACULA Hebrew; «word_no» = Wort im Vers; «text» mit folgendem Maqqef bzw. "
                        "Sof Pasuq, «word» ohne. Morpheme ohne eigene Schreibung stehen in «implicit_morphs».",
        "source": src, "import": {"tool": "scripts/import_macula_hebrew_book.py", "imported_on": today},
        "implicit_morphs": implicit, "tokens": tokens}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (D / "annotations" / f"MACULA-WLC-{args.book}-{c:03d}.json").write_text(json.dumps({
        "id": an_id, "type": "annotation_set", "status": "imported_unreviewed", "tags": [args.tag], "annotates": ts_id,
        "reference": f"{args.book}.{c}", "layers": ["morphology", "lemma", "syntax_role", "referents", "semantic_frame", "gloss",
                                                     "transliteration", "septuagint_equivalent"],
        "source": {**src, "excluded_fields": EXCLUDED,
                   "excluded_reason": "Semantic Dictionary of Biblical Hebrew (UBS) nur «used with permission»; mandarin nicht benötigt"},
        "import": {"tool": "scripts/import_macula_hebrew_book.py", "imported_on": today},
        "entries": entries}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    by_chapter[f"{args.book}.{c}"] = {"tokens": len(tokens), "words": len({(t["reference"], t["word_no"]) for t in tokens}),
                                      "unique_lemmas": len({e.get("lemma") for e in entries.values()})}
    totals += len(tokens)
    ann_ids.append(an_id)
(D / "counts" / f"WLC-{args.book}.json").write_text(json.dumps({
    "id": f"COUNT-WLC-{args.book}", "type": "lemma_count", "status": "imported_unreviewed", "tags": [args.tag],
    "edition": "ED-WLC", "reference": args.book, "based_on_annotations": ann_ids,
    "count_policy": "Tokens = Morpheme mit eigener Schreibung (MACULA Hebrew); Lemmata = verschiedene MACULA-Lemmata.",
    "token_count": totals, "unique_lemmas": len(lemmas_all), "by_chapter": by_chapter,
    "import": {"tool": "scripts/import_macula_hebrew_book.py", "imported_on": today},
    "lemma_counts": dict(sorted(lemmas_all.items(), key=lambda kv: (-kv[1], kv[0] or "")))}, ensure_ascii=False, indent=1) + "\n",
    encoding="utf-8")
print(f"PASS: {args.book}: {totals} Morphem-Tokens in {len(files)} Kapitel(n), {len(lemmas_all)} Lemmata")
