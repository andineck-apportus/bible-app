#!/usr/bin/env python3
"""Berechnet Gesichertheitsbewertungen nach METHOD-EDITION-AGREEMENT-V1 für alle Variantenstellen
auf Editionsebene eines Buchs. Deterministisch; ein erneuter Lauf erzeugt dieselben Daten.

Aufruf: python3 scripts/assess_edition_agreement.py MRK
Ausgabe: data/assessments/edition-agreement-<buch>/ASMSET-EDA-<BUCH>-<KKK>.json (eine Datei je Kapitel)
"""
import collections
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
METHOD = "METHOD-EDITION-AGREEMENT-V1"
EDITIONS = ["ED-SBLGNT", "ED-WH", "ED-TREG", "ED-NA28", "ED-RP"]
LEVELS = [(4, "breit"), (3, "mehrheitlich"), (2, "geteilt"), (1, "vereinzelt"), (0, "keine")]

code = sys.argv[1]
var_dir = ROOT / "data/variants" / f"sblgntapp-{code.lower()}"
out_dir = ROOT / "data/assessments" / f"edition-agreement-{code.lower()}"
by_chapter = collections.defaultdict(list)
for p in sorted(var_dir.glob("VAR-SBLGNTAPP-*.json")):
    var = json.loads(p.read_text(encoding="utf-8"))
    results = []
    for r in var["readings"]:
        eds = sorted(set(r["editions"]) | ({"ED-SBLGNT"} if r.get("is_sblgnt_text") else set()), key=EDITIONS.index)
        n = len(eds)
        results.append({"reading": f"{var['id']}:{r['reading_id']}", "text": r["text"],
                        "supporting_editions": eds, "support": n, "of": len(EDITIONS),
                        "level": next(lbl for lim, lbl in LEVELS if n >= lim)})
    best = max(x["support"] for x in results)
    top = [x["reading"] for x in results if x["support"] == best]
    by_chapter[int(var["reference"].split(".")[1])].append({
        "assesses": var["id"], "reference": var["reference"], "results": results,
        "highest_support": top,
        "tie": len(top) > 1,
    })

out_dir.mkdir(parents=True, exist_ok=True)
for old in out_dir.glob("ASMSET-*.json"):
    old.unlink()
for ch, items in sorted(by_chapter.items()):
    rec = {"id": f"ASMSET-EDA-{code}-{ch:03d}", "type": "assessment_set", "status": "draft",
           "tags": ["TAG-TEXT-CRITICISM", "TAG-UNCERTAINTY"], "reference": f"{code}.{ch}",
           "method": METHOD, "computed_by": "scripts/assess_edition_agreement.py",
           "note_de": "Maschinell berechnet; misst Herausgeberkonsens, keine Handschriftenbezeugung (siehe Methode). Keine Entscheidung über richtig/falsch.",
           "assessments": items}
    (out_dir / f"{rec['id']}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
levels = collections.Counter(next(r["level"] for r in a["results"] if r["reading"].endswith(":R1"))
                             for items in by_chapter.values() for a in items)
ties = sum(a["tie"] for items in by_chapter.values() for a in items)
print(f"PASS: {sum(map(len, by_chapter.values()))} Stellen in {len(by_chapter)} Kapiteln bewertet; "
      f"SBLGNT-Lesart: {dict(levels)}; Gleichstände: {ties}")
