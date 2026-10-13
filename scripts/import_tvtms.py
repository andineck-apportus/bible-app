#!/usr/bin/env python3
"""Import der Versifikations-Zuordnungen TVTMS (STEPBible, Tyndale House Cambridge, CC BY 4.0).

Aufruf:
    python3 scripts/import_tvtms.py PFAD/TVTMS….txt --upstream-commit SHA

Quelle: github.com/STEPBible/STEPBible-Data, Versification/«TVTMS - Translators Versification Traditions with
Methodology for Standardisation for Eng+Heb+Lat+Grk+Others - STEPBible.org CC BY.txt». Übernommen wird der
Teil «Expanded» (#DataStart(Expanded) … #DataEnd(Expanded)): je Zeile eine Versnummer einer Bibel in einer
Zähltradition (SourceType: Hebrew, Latin, Greek, Eng-KJV …), die entsprechende Nummer in der Standardzählung
(StandardRef, englische Tradition NRSV/KJV), die Handlung (Action), die Notizmarke, die Angaben zu den alten
Versionen und die Tests, unter denen die Zeile gilt.

Umformatierung (vom Lizenzgeber ausdrücklich erlaubt, «reformat it for your application»): Spalten als Felder,
aufgeteilt nach Buch der SourceRef; die beiden englischen Notiztexte (Reversification/Versification Note) werden
nicht übernommen. Sonst keine inhaltliche Änderung: alle Werte stehen wörtlich (`*_raw`); zusätzlich, wo eindeutig,
die kanonische Stelle (USFM) und der Teilvers. Die Tests werden nicht ausgewertet; dafür braucht es die Verszahlen
bzw. den Text der jeweiligen Ausgabe.

Ausgabe: data/versification/VRS-TVTMS-<BUCH>.json (Typ versification_map).
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import refs  # noqa: E402

SHA256 = "63058e0f20201af4bdaa7d830da5be8f493455d947c5f147d84840b33db9ddf8"
REPO = "https://github.com/STEPBible/STEPBible-Data"
PATH = ("Versification/TVTMS - Translators Versification Traditions with Methodology for Standardisation for "
        "Eng+Heb+Lat+Grk+Others - STEPBible.org CC BY.txt")
ATTRIBUTION = "Data created by www.STEPBible.org based on work at Tyndale House Cambridge (CC BY 4.0)"

ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
ap.add_argument("file", type=pathlib.Path)
ap.add_argument("--upstream-commit", required=True)
args = ap.parse_args()

raw = args.file.read_bytes()
digest = hashlib.sha256(raw).hexdigest()
if digest != SHA256:
    sys.exit(f"Prüfsumme weicht ab: {digest} (erwartet {SHA256}); Quelle prüfen und Importer bewusst anpassen.")
lines = raw.decode("utf-8-sig").splitlines()
start = next(i for i, l in enumerate(lines) if l.startswith("#DataStart(Expanded)"))
end = next(i for i, l in enumerate(lines) if l.startswith("#DataEnd(Expanded)"))

REF = re.compile(r"^([1-4]?[A-Za-z]{2,3})\.(\d+):(\d+)(?:!([a-z0-9]+))?$")


def canon(text):
    """«Gen.32:1!a» -> ("GEN.32.1", "a"); sonst (None, None)."""
    m = REF.match((text or "").strip())
    if not m:
        return None, None
    code = m.group(1).upper()
    if code not in refs.CODES:
        return None, None
    return f"{code}.{int(m.group(2))}.{int(m.group(3))}", m.group(4)


by_book, unknown, n = {}, set(), 0
for line in lines[start + 1:end]:
    cols = line.split("\t")
    if len(cols) < 4 or not cols[0].strip() or cols[0].startswith(("#", "'")) or cols[0] == "SourceType":
        continue
    cols += [""] * (9 - len(cols))
    stype, sref, stdref, action, marker, _rev, _ver, ancient, tests = (c.strip() for c in cols[:9])
    book = sref.split(".")[0]
    code = book.upper() if book.upper() in refs.CODES else None
    if not code:
        unknown.add(book)
    entry = {"source_type": stype, "source_ref_raw": sref, "standard_ref_raw": stdref, "action": action}
    s, ssub = canon(sref)
    t, tsub = canon(stdref)
    if s:
        entry["source_ref"] = s
        if ssub:
            entry["source_sub"] = ssub
    if t:
        entry["standard_ref"] = t
        if tsub:
            entry["standard_sub"] = tsub
    if marker:
        entry["note_marker"] = marker
    if ancient:
        entry["ancient_versions"] = ancient
    if tests:
        entry["tests"] = tests
    by_book.setdefault(code or book.upper(), []).append(entry)
    n += 1

out = ROOT / "data" / "versification"
out.mkdir(parents=True, exist_ok=True)
for book, entries in sorted(by_book.items()):
    rid = "VRS-TVTMS-" + re.sub(r"[^A-Z0-9]", "", book)
    rec = {"id": rid, "type": "versification_map", "status": "imported_unreviewed", "tags": [],
           "book": book if book in refs.CODES else None, "book_raw": book,
           "standard_versification": "TVTMS Standard (englische Tradition, NRSV/KJV)",
           "source": {"repository": REPO, "commit": args.upstream_commit, "path": PATH, "sha256": SHA256,
                      "license": "CC BY 4.0", "attribution": ATTRIBUTION,
                      "changes_de": "Teil «Expanded» als Felder umformatiert, nach Buch aufgeteilt; englische Notiztexte "
                                    "(Reversification/Versification Note) weggelassen; Werte sonst wörtlich."},
           "entries": entries,
           "knowledge": {"asserted_at": "2026-10-13", "supersedes": None}}
    if rec["book"] is None:
        del rec["book"]
    # Kopf eingerückt, Einträge je eine Zeile (kompakt und gut vergleichbar)
    head = json.dumps({k: v for k, v in rec.items() if k != "entries"}, ensure_ascii=False, indent=1)
    body = ",\n".join(json.dumps(e, ensure_ascii=False, separators=(",", ":")) for e in entries)
    (out / f"{rid}.json").write_text(head[:-2] + ',\n "entries": [\n' + body + "\n ]\n}\n", encoding="utf-8")
print(f"PASS: {n} Zeilen in {len(by_book)} Dateien; Bücher ausserhalb der USFM-Liste in refs.py: {', '.join(sorted(unknown)) or '–'}")
