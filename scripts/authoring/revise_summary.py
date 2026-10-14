#!/usr/bin/env python3
"""Zusammenfassung (oder ein anderes Textfeld) eines bestehenden Datensatzes überarbeiten, samt Mundart-Lokalisierung.

Für Datensätze, die kein laufendes Autorenwerkzeug erzeugt (z. B. SUM-BOOK-*, SUM-GROUP-*, ältere Texteinheiten).
Wird ein Datensatz von einem Autorenwerkzeug erzeugt (scripts/authoring/<buch>_text.py, *_study.py), dort ändern
und das Werkzeug neu ausführen, sonst überschreibt es die Änderung.

Aufruf:
    python3 scripts/authoring/revise_summary.py SUM-BOOK-OBA text_de "Neuer Text" --gsw "Neue Mundart" \
        --reason "Zusammenfassung überprüft: …"
Schreibt die vorige Fassung ins revision_log (Datum, Grund, vorheriger Wert) und erneuert in der Lokalisierung
(L10N-GSW-ZH-<ID>) Feld und Quellen-Fingerabdruck; ohne --gsw wird nur geprüft, dass die Mundart nicht veraltet.
"""
import argparse
import datetime
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import localizations  # noqa: E402

LANG = "gsw-u-sd-chzh"


def find(rid):
    hits = [p for p in (ROOT / "data").rglob(f"{rid}.json") if "localizations" not in p.parts]
    if len(hits) != 1:
        sys.exit(f"ERROR: {rid}: {len(hits)} Dateien gefunden")
    return hits[0]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("id")
    ap.add_argument("field")
    ap.add_argument("text")
    ap.add_argument("--gsw")
    ap.add_argument("--reason", required=True)
    a = ap.parse_args()
    today = datetime.date.today().isoformat()
    path = find(a.id)
    rec = json.loads(path.read_text(encoding="utf-8"))
    if a.field not in rec:
        sys.exit(f"ERROR: {a.id}: Feld {a.field} fehlt")
    if rec[a.field] != a.text:
        rec.setdefault("revision_log", []).append({"date": today, "change_de": a.reason, "previous": {a.field: rec[a.field]}})
        rec[a.field] = a.text
        path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lp = ROOT / "data/localizations" / LANG / f"{a.id}.json"
    if lp.exists():
        loc = json.loads(lp.read_text(encoding="utf-8"))
        if a.field in loc["fields"]:
            if a.gsw is None:
                if loc["source_fingerprint"].get(a.field) != localizations.fingerprint(rec[a.field]):
                    sys.exit(f"ERROR: {a.id}: Mundart veraltet; --gsw angeben")
            elif loc["fields"][a.field] != a.gsw or loc["source_fingerprint"][a.field] != localizations.fingerprint(rec[a.field]):
                loc.setdefault("revision_log", []).append({"date": today, "change_de": a.reason,
                                                            "previous": {a.field: loc["fields"][a.field]}})
                loc["fields"][a.field] = a.gsw
                loc["source_fingerprint"][a.field] = localizations.fingerprint(rec[a.field])
                lp.write_text(json.dumps(loc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    elif a.gsw is not None:
        sys.exit(f"ERROR: {a.id}: keine Mundart-Lokalisierung vorhanden")
    print(f"PASS: {a.id}.{a.field} überarbeitet")


if __name__ == "__main__":
    main()
