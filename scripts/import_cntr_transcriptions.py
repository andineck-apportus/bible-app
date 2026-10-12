#!/usr/bin/env python3
"""Import von Handschriften- und Editionstranskriptionen des CNTR für ein Buch.

Aufruf:
    python3 scripts/import_cntr_transcriptions.py MRK PFAD/transcriptions --upstream-commit <sha>

Quelle: github.com/Center-for-New-Testament-Restoration/transcriptions (Alan Bunning, Center for
New Testament Restoration), CC BY-SA 4.0. Format: Manuscript Encoding Specification (MES), eine Zeile
je Vers «BBCCCVVV text». Der Text wird unverändert übernommen (inklusive Zeilenumbrüchen «/»,
Korrekturen «x{…} {…}», Ergänzungen «~» usw.); er ist eine Sekundärtranskription des CNTR und keine
eigene Prüfung am Faksimile.

Ausgabe:
    data/witnesses/WIT-GA-<Nr>.json                 Metadaten der Handschrift (nur für bekannte Zeugen)
    data/witness-texts/CNTR-<Kürzel>-<BUCH>.json    Transkription je Zeuge bzw. Ausgabe
"""
import argparse
import datetime
import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
BOOKNUM = {"MRK": 41}
SOURCE = "SRC-CNTR-TRANSCRIPTIONS"
UPSTREAM = "https://github.com/Center-for-New-Testament-Restoration/transcriptions"

# Handschriften, deren Transkription importiert wird. Datierung nach gängiger Einordnung
# (INTF, Kurzgefasste Liste); nicht eigens am Katalog geprüft.
WITNESSES = {
    "01": {"symbol": "א", "name_de": "Codex Sinaiticus", "century": "IV", "date_de": "4. Jahrhundert",
           "material_de": "Pergament", "languages": ["grc"],
           "location_de": "Grösstenteils British Library London; Teile in Leipzig, St. Petersburg und im Katharinenkloster (Sinai)",
           "about_de": "Eine der ältesten vollständigen Bibelhandschriften; mehrere spätere Korrektoren haben den Text bearbeitet.",
           "facsimile": ["https://codexsinaiticus.org/"]},
    "02": {"symbol": "A", "name_de": "Codex Alexandrinus", "century": "V", "date_de": "5. Jahrhundert",
           "material_de": "Pergament", "languages": ["grc"], "location_de": "British Library London (Royal MS 1 D VIII)",
           "about_de": "Vollbibel; in den Evangelien steht der Text dem späteren byzantinischen Mehrheitstext nahe.",
           "facsimile": []},
    "03": {"symbol": "B", "name_de": "Codex Vaticanus", "century": "IV", "date_de": "4. Jahrhundert",
           "material_de": "Pergament", "languages": ["grc"], "location_de": "Biblioteca Apostolica Vaticana (Vat. gr. 1209)",
           "about_de": "Eine der ältesten fast vollständigen Bibelhandschriften; wichtige Grundlage vieler kritischer Ausgaben.",
           "facsimile": ["https://digi.vatlib.it/view/MSS_Vat.gr.1209"]},
    "04": {"symbol": "C", "name_de": "Codex Ephraemi Rescriptus", "century": "V", "date_de": "5. Jahrhundert",
           "material_de": "Pergament, später überschrieben (Palimpsest)", "languages": ["grc"],
           "location_de": "Bibliothèque nationale de France, Paris (Grec 9)",
           "about_de": "Der Bibeltext wurde abgeschabt und mit Schriften Ephräms des Syrers überschrieben; er ist daher stellenweise schwer lesbar.",
           "facsimile": []},
    "05": {"symbol": "D", "name_de": "Codex Bezae", "century": "V", "date_de": "um 400 bzw. 5. Jahrhundert",
           "material_de": "Pergament", "languages": ["grc", "lat"], "location_de": "Cambridge University Library (Nn. 2.41)",
           "about_de": "Zweisprachig griechisch-lateinisch; weicht oft eigenständig von anderen Handschriften ab.",
           "facsimile": ["https://cudl.lib.cam.ac.uk/view/MS-NN-00002-00041"]},
    "032": {"symbol": "W", "name_de": "Codex Washingtonianus", "century": "IV/V", "date_de": "4./5. Jahrhundert",
            "material_de": "Pergament", "languages": ["grc"],
            "location_de": "Smithsonian, National Museum of Asian Art (Freer), Washington",
            "about_de": "Evangelienhandschrift mit wechselndem Texttyp; in Markus teilweise eigenständig.",
            "facsimile": ["https://manuscripts.csntm.org/Manuscript/Group/GA_032"]},
}
# Ausgaben aus «critical texts»; ED-WH und ED-RP dienen auch dem Abgleich mit dem SBLGNT-Apparat.
EDITIONS = {"WH": "ED-WH", "RP": "ED-RP", "ST": "ED-ST", "KJTR": "ED-KJTR", "SR": "ED-SR"}

ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
ap.add_argument("book", choices=sorted(BOOKNUM))
ap.add_argument("repo", type=pathlib.Path)
ap.add_argument("--upstream-commit", required=True)
args = ap.parse_args()
if not re.fullmatch(r"[0-9a-f]{40}", args.upstream_commit):
    sys.exit("ERROR: --upstream-commit muss eine vollständige 40-stellige Git-SHA sein")
num = BOOKNUM[args.book]
today = datetime.date.today().isoformat()


def read(path):
    raw = path.read_bytes()
    verses = {}
    for line in raw.decode("utf-8").splitlines():
        m = re.fullmatch(r"(\d{2})(\d{3})(\d{3}) (.*)", line.strip())
        if not m:
            continue
        b, c, v, text = int(m[1]), int(m[2]), int(m[3]), m[4]
        if b == num:
            ref = f"{args.book}.{c}.{v}"
            if ref in verses:
                sys.exit(f"ERROR: {path.name}: Vers {ref} doppelt")
            verses[ref] = text
    return raw, verses


def write(rel, rec):
    p = ROOT / "data" / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(rec, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


written = []
for ga, meta in WITNESSES.items():
    path = args.repo / "class 1" / f"{ga}.txt"
    raw, verses = read(path)
    if not verses:
        print(f"WARN: {ga} enthält {args.book} nicht")
        continue
    wid = f"WIT-GA-{ga}"
    write(f"witnesses/{wid}.json", {
        "id": wid, "type": "witness", "status": "draft", "tags": ["TAG-TEXT-CRITICISM"],
        "gregory_aland": ga, **meta,
        "catalog_url": f"https://ntvmr.uni-muenster.de/manuscript-workspace?docID={20000 + int(ga)}",
        "date_source_de": "Gängige Datierung nach INTF (Kurzgefasste Liste); nicht eigens am Katalog geprüft.",
        "authorship_de": f"Metadaten zusammengestellt {today} (KI-Entwurf, Claude); ungeprüft.",
    })
    tid = f"CNTR-GA{ga}-{args.book}"
    write(f"witness-texts/{tid}.json", {
        "id": tid, "type": "witness_transcription", "status": "imported_unreviewed",
        "tags": ["TAG-TEXT-CRITICISM", "TAG-MARK"], "witness": wid, "bibliographic_source": SOURCE,
        "encoding": "MES (Manuscript Encoding Specification, CNTR)",
        "imported_scope": [f"{args.book}.{min(int(k.split('.')[1]) for k in verses)}-{args.book}.{max(int(k.split('.')[1]) for k in verses)}"],
        "verse_count": len(verses),
        "source": {"url": UPSTREAM, "path": f"class 1/{ga}.txt", "upstream_commit": args.upstream_commit,
                   "sha256": hashlib.sha256(raw).hexdigest(), "license": "CC BY-SA 4.0",
                   "attribution": "Alan Bunning, Center for New Testament Restoration", "imported_at": today},
        "verification_de": "Sekundärtranskription des CNTR; nicht am Faksimile geprüft.",
        "verses": verses,
    })
    written.append(tid)

for short, edid in EDITIONS.items():
    path = args.repo / "critical texts" / f"{short}.txt"
    raw, verses = read(path)
    tid = f"CNTR-{short}-{args.book}"
    write(f"witness-texts/{tid}.json", {
        "id": tid, "type": "witness_transcription", "status": "imported_unreviewed",
        "tags": ["TAG-TEXT-CRITICISM", "TAG-MARK"], "edition": edid, "bibliographic_source": SOURCE,
        "encoding": "Ausgabentext mit Akzenten (CNTR)", "verse_count": len(verses),
        "source": {"url": UPSTREAM, "path": f"critical texts/{short}.txt", "upstream_commit": args.upstream_commit,
                   "sha256": hashlib.sha256(raw).hexdigest(), "license": "CC BY-SA 4.0",
                   "attribution": "Alan Bunning, Center for New Testament Restoration", "imported_at": today},
        "verification_de": "Elektronischer Ausgabentext des CNTR; nicht an der gedruckten Ausgabe geprüft.",
        "verses": verses,
    })
    written.append(tid)
print(f"PASS: {len(written)} Transkriptionen für {args.book} importiert: {', '.join(written)}")
