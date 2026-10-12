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
BOOKNUM = {"MAT": 40, "MRK": 41, "LUK": 42}
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
# Weitere Zeugen: Papyri (Gregory-Aland) und Texte auf Amuletten u. ä. (Trismegistos-Nummer, CNTR «class 2»).
# Angaben zu Datierung, Ort und Sammlung nach DCLP/papyri.info (TM-Datensätze), Stand 2026-10-12.
PAPYRI = {
    "P75": {"symbol": "𝔓75", "name_de": "Papyrus 75 (Bodmer XIV–XV)", "century": "III/IV",
            "date_de": "um 175–225 nach älterer Einordnung; neuere Studien schlagen das 4. Jahrhundert vor",
            "material_de": "Papyrus", "languages": ["grc"], "location_de": "Biblioteca Apostolica Vaticana (Hanna Papyrus 1)",
            "about_de": "Einer der ältesten Textzeugen für Lukas und Johannes; steht dem Codex Vaticanus sehr nahe.",
            "facsimile": [], "catalog_docid": 10075},
    "P45": {"symbol": "𝔓45", "name_de": "Papyrus 45 (Chester Beatty I)", "century": "III",
            "date_de": "3. Jahrhundert", "material_de": "Papyrus", "languages": ["grc"],
            "location_de": "Chester Beatty Library, Dublin; ein Blatt in Wien",
            "about_de": "Früher Papyruscodex mit Teilen der vier Evangelien und der Apostelgeschichte; stark beschädigt.",
            "facsimile": [], "catalog_docid": 10045},
}
AMULETS = {
    "64206": {"name_de": "P. Antinoopolis 2.54", "century": "III/IV", "date_de": "um 275–325",
              "material_de": "Papyrus, Miniaturformat", "location_de": "Oxford, Sackler Library (P. Ant. 54); gefunden in Antinoopolis (Ägypten)",
              "about_de": "Kleines Blatt mit dem Vaterunser, laut DCLP als Gebet/Amulett eingeordnet."},
    "64491": {"name_de": "P. Oxyrhynchus 60.4010", "century": "IV", "date_de": "4. Jahrhundert",
              "material_de": "Papyrus", "location_de": "Oxford, Sackler Library (P. Oxy. 4010); gefunden in Oxyrhynchos (Ägypten)",
              "about_de": "Vaterunser innerhalb eines Gebets, laut DCLP als Gebet/Amulett eingeordnet."},
    "64372": {"name_de": "Vaterunser auf Ton aus Megara", "century": "IV", "date_de": "4. Jahrhundert",
              "material_de": "Ton (Keramik)", "location_de": "Athen, Nationalmuseum 12227; gefunden in Megara (Griechenland)",
              "about_de": "Vaterunser auf Keramik; laut DCLP als Gebet/Amulett eingeordnet. Schreibweise stark nach Gehör (z. B. ειμιν statt ημιν)."},
    "64605": {"name_de": "P. Princeton 2.107", "century": "IV–VI", "date_de": "zwischen etwa 350 und 550",
              "material_de": "Papyrus", "location_de": "Princeton University Library (AM 8963); Ägypten",
              "about_de": "Amulett mit Bibelversen (u. a. Psalmen, Jesaja) und dem Anfang des Vaterunsers, frei und fehlerhaft wiedergegeben."},
    "61840": {"name_de": "P. Schøyen 1.16", "century": "V/VI", "date_de": "zwischen etwa 450 und 600",
              "material_de": "Papyrus", "location_de": "Oslo, Sammlung Schøyen (MS 244/4) bzw. Universitätsbibliothek (P. 1644); gefunden in Oxyrhynchos",
              "about_de": "Amulett mit Psalmversen und dem Vaterunser; laut DCLP Gebet/Amulett."},
    "61617": {"name_de": "PSI 6.719", "century": "VI", "date_de": "6. Jahrhundert",
              "material_de": "Papyrus", "location_de": "Florenz, Biblioteca Medicea Laurenziana; aus Oxyrhynchos",
              "about_de": "Amulett mit Psalmversen und dem Anfang des Vaterunsers."},
    "33368": {"name_de": "P. Erlangen Diospolis 1", "century": "IV", "date_de": "313–314",
              "material_de": "Papyrus", "location_de": "Universitätsbibliothek Erlangen; aus Diospolis Parva (Ägypten)",
              "about_de": "Ein Wirtschafts- und Rechnungsbuch; darin die Anfangsworte des Vaterunsers."},
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


def scope(verses):
    chs = sorted({int(k.split(".")[1]) for k in verses})
    if len(chs) > 1:
        return f"{args.book}.{chs[0]}-{args.book}.{chs[-1]}"
    vs = sorted(int(k.split(".")[2]) for k in verses)
    return f"{args.book}.{chs[0]}.{vs[0]}" + (f"-{args.book}.{chs[0]}.{vs[-1]}" if vs[-1] > vs[0] else "")


def write(rel, rec):
    p = ROOT / "data" / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(rec, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


written = []
todo = [("class 1", ga, f"WIT-GA-{ga}", {"gregory_aland": ga, **m,
         "catalog_url": f"https://ntvmr.uni-muenster.de/manuscript-workspace?docID={20000 + int(ga)}",
         "date_source_de": "Gängige Datierung nach INTF (Kurzgefasste Liste); nicht eigens am Katalog geprüft."})
        for ga, m in WITNESSES.items()]
todo += [("class 1", ga, f"WIT-GA-{ga}", {"gregory_aland": ga, **{k: v for k, v in m.items() if k != "catalog_docid"},
          "catalog_url": f"https://ntvmr.uni-muenster.de/manuscript-workspace?docID={m['catalog_docid']}",
          "date_source_de": "Datierung umstritten bzw. nach gängiger Einordnung; nicht eigens geprüft."})
         for ga, m in PAPYRI.items()]
todo += [("class 2", tm, f"WIT-TM-{tm}", {"trismegistos": tm, "symbol": "TM " + tm, "languages": ["grc"], **m, "facsimile": [],
          "catalog_url": f"https://papyri.info/dclp/{tm}" if tm != "33368" else "https://www.trismegistos.org/text/33368",
          "date_source_de": "Angaben nach DCLP/papyri.info bzw. HGV (Trismegistos); nicht eigens geprüft."})
         for tm, m in AMULETS.items()]
for folder, key, wid, meta in todo:
    path = args.repo / folder / f"{key}.txt"
    raw, verses = read(path)
    if not verses:
        continue
    write(f"witnesses/{wid}.json", {
        "id": wid, "type": "witness", "status": "draft", "tags": ["TAG-TEXT-CRITICISM"], **meta,
        "authorship_de": f"Metadaten zusammengestellt {today} (KI-Entwurf, Claude); ungeprüft.",
    })
    ga = key
    tid = f"CNTR-{'GA' if folder == 'class 1' else 'TM'}{key}-{args.book}"
    write(f"witness-texts/{tid}.json", {
        "id": tid, "type": "witness_transcription", "status": "imported_unreviewed",
        "tags": ["TAG-TEXT-CRITICISM", "TAG-MARK"], "witness": wid, "bibliographic_source": SOURCE,
        "encoding": "MES (Manuscript Encoding Specification, CNTR)",
        "imported_scope": [scope(verses)],
        "verse_count": len(verses),
        "source": {"url": UPSTREAM, "path": f"{folder}/{key}.txt", "upstream_commit": args.upstream_commit,
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
