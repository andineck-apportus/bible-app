#!/usr/bin/env python3
"""Import gemeinfreier deutscher Vergleichsübersetzungen für einzelne Bücher (nur zum Vergleich).

Aufruf:
    python3 scripts/import_comparison_bibles.py TIT --open-bibles PFAD/open-bibles --bible-databases PFAD/bible_databases

Quellen (Prüfsummen fest verdrahtet; bei Abweichung Abbruch):
- Lutherbibel 1912: github.com/seven1m/open-bibles, deu-luther1912.osis.xml, Commit f257a355…, gemeinfrei.
- Elberfelder 1905: github.com/scrollmapper/bible_databases, formats/json/GerElb1905.json, Commit e1b254ce…,
  CrossWire-Modul GerElb1905, gemeinfrei.

Ausgabe: data/translations/TRANS-LUT1912-<BUCH>.json, TRANS-ELB1905-<BUCH>.json (translation_kind
historical_comparison, status imported_unreviewed). Der Text wird unverändert übernommen.
"""
import argparse
import datetime
import hashlib
import json
import pathlib
import re
import sys
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import refs  # noqa: E402

LUT = {"file": "deu-luther1912.osis.xml", "commit": "f257a3559025c3f873b48a75019f53a9354ed7de",
       "sha256": "5df33f4bf3e086b6490b467cf8ddbf4cf95126b2826efaddf17b223ddd07f92b"}
ELB = {"file": "formats/json/GerElb1905.json", "commit": "e1b254cef86d0e65b1a5d1a94b8b112d0f296a2c",
       "sha256": "c3bc2115750db82fb7c9ab650fcd05e22251d29fbb1c7870db6e81c6a1b54557"}
OSIS = {"TIT": "Titus", "OBA": "Obad"}
NAMES = {"TIT": "Titus", "OBA": "Obadiah"}
TAGS = {"TIT": "TAG-TITUS", "OBA": "TAG-OBADIAH"}
NOTES = {
    "LUT": "Die Fassung 1912 übersetzt im Neuen Testament nach dem Textus Receptus, im Alten nach dem hebräischen Text der Rabbinerbibeln; Sprache und Wortwahl gehen auf Luther zurück.",
    "ELB": "Sehr wörtliche Übersetzung; im Neuen Testament berücksichtigt sie schon kritische Textausgaben des 19. Jahrhunderts.",
}

ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
ap.add_argument("book", choices=sorted(OSIS))
ap.add_argument("--open-bibles", type=pathlib.Path, required=True)
ap.add_argument("--bible-databases", type=pathlib.Path, required=True)
args = ap.parse_args()
today = datetime.date.today().isoformat()


def checked(path, want):
    raw = path.read_bytes()
    got = hashlib.sha256(raw).hexdigest()
    if got != want:
        sys.exit(f"ERROR: {path} hat SHA-256 {got}, erwartet {want}")
    return raw


# Luther 1912 (OSIS)
raw = checked(args.open_bibles / LUT["file"], LUT["sha256"])
ns = {"o": "http://www.bibletechnologies.net/2003/OSIS/namespace"}
root = ET.fromstring(raw)
lut = {}
for v in root.iter("{%s}verse" % ns["o"]):
    oid = v.get("osisID", "")
    if oid.startswith(OSIS[args.book] + "."):
        _, c, n = oid.split(".")
        text = re.sub(r"\s+", " ", "".join(v.itertext())).strip()
        lut[f"{args.book}.{int(c)}.{int(n)}"] = text
# Elberfelder 1905 (JSON)
raw = checked(args.bible_databases / ELB["file"], ELB["sha256"])
data = json.loads(raw)
book = next(b for b in data["books"] if b["name"] == NAMES[args.book])
elb = {f"{args.book}.{ch['chapter']}.{v['verse']}": v["text"].strip() for ch in book["chapters"] for v in ch["verses"]}

for key, title, texts, src, url in (
        ("LUT1912", "Lutherbibel, revidierte Fassung 1912", lut, LUT, "https://github.com/seven1m/open-bibles"),
        ("ELB1905", "Elberfelder Bibel, unrevidierte Fassung 1905", elb, ELB, "https://github.com/scrollmapper/bible_databases")):
    if not texts:
        sys.exit(f"ERROR: {key}: keine Verse für {args.book}")
    for r in texts:
        refs.parse(r)
    chapters = sorted({int(r.split(".")[1]) for r in texts})
    last = max((r for r in texts if int(r.split(".")[1]) == chapters[-1]), key=lambda r: int(r.split(".")[2]))
    rec = {"id": f"TRANS-{key}-{args.book}", "title": title, "type": "translation", "status": "imported_unreviewed",
           "tags": [TAGS[args.book]], "language": "de", "translation_kind": "historical_comparison",
           "imported_scope": [f"{args.book}.{chapters[0]}.1-{last}"],
           "purpose_de": "Nur zum Vergleich: Zeigt, wie ältere deutsche Übersetzungen dieselben Verse wiedergeben. Keine Grundlage der eigenen Arbeitsübersetzung.",
           "source": {"url": url, "path": src["file"], "upstream_commit": src["commit"], "sha256": src["sha256"],
                      "license": "gemeinfrei (Public Domain laut Quelle)" if key == "LUT1912" else "gemeinfrei (CrossWire-Modul GerElb1905)",
                      "imported_at": today},
           "note_de": NOTES[key[:3]],
           "text_by_reference": dict(sorted(texts.items(), key=lambda kv: (int(kv[0].split(".")[1]), int(kv[0].split(".")[2]))))}
    p = ROOT / "data" / "translations" / f"{rec['id']}.json"
    p.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: {rec['id']}: {len(texts)} Verse")
