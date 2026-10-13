"""Negativtests für scripts/validate.py: Kopie der Daten mit gezielt eingebauten Fehlern."""
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]


def run(root):
    return subprocess.run([sys.executable, str(ROOT / "scripts/validate.py")], capture_output=True, text=True,
                          env={**os.environ, "BIBLE_APP_ROOT": str(root)})


def case(name, mutate, expect):
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        shutil.copytree(ROOT / "data", root / "data")
        (root / "data-nc").mkdir()
        mutate(root)
        res = run(root)
        out = res.stdout + res.stderr
        assert res.returncode != 0 and expect in out, (name, out[-500:])


def write(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False), encoding="utf-8")


def core_refs_nc(root):
    write(root / "data-nc/x/SRC-NC-TEST.json", {"id": "SRC-NC-TEST", "type": "source", "status": "draft", "tags": []})
    p = root / "data/works/WORK-MRK.json"
    d = json.loads(p.read_text())
    d["related"] = ["SRC-NC-TEST"]
    write(p, d)


def bad_annotation(root):
    p = root / "data/annotations/MACULA-SBLGNT-MRK-001.json"
    d = json.loads(p.read_text())
    d["entries"]["TOK-SBLGNT-MRK-002-001-001"] = {"lemma": "x"}
    write(p, d)


def bad_assessment(root):
    p = root / "data/assessments/edition-agreement-mrk/ASMSET-EDA-MRK-003.json"
    d = json.loads(p.read_text())
    d["assessments"][0]["results"][0]["reading"] = "VAR-SBLGNTAPP-MRK-003-025-01:R9"
    write(p, d)


def bad_ref(root):
    p = root / "data/relations/REL-MRK-0001.json"
    d = json.loads(p.read_text())
    d["to_ref"] = "Mt 12:22-32"
    write(p, d)


def bad_background(root):
    p = root / "data/background/BG-MRK-0001.json"
    d = json.loads(p.read_text())
    d["context"] = "TU-MRK-003-020-035"
    del d["text_de"]
    write(p, d)


def bad_decision(root):
    p = root / "data/translations/TRANS-MAT-006-005-015-DE-WORKING.json"
    d = json.loads(p.read_text())
    d["decisions"][0]["target"] = "steht nicht im Text"
    d["decisions"][1]["kind"] = "frei"
    d["decisions"][2]["grc"] = "οὐρανοῖς ἀγάπη"
    write(p, d)


def bad_localization(root):
    p = root / "data/localizations/gsw-u-sd-chzh/INT-LP-0001.json"
    d = json.loads(p.read_text())
    d["fields"]["counterarguments_de"] = d["fields"]["counterarguments_de"][:1]
    d["fields"]["gibts_nicht_de"] = "x"
    write(p, d)


def stale_localization(root):
    p = root / "data/findings/FIND-LP-0001.json"
    d = json.loads(p.read_text())
    d["claim_de"] += " (geändert)"
    write(p, d)


baseline = run(ROOT)
assert baseline.returncode == 0, baseline.stdout + baseline.stderr
case("Kern verweist auf NC", core_refs_nc, "verweist aus dem freien Kern auf NC-Datensatz")
case("Annotation fremdes Token", bad_annotation, "das nicht in TOKSET-SBLGNT-MRK-001 liegt")
case("Bewertung unbekannte Lesart", bad_assessment, "unbekannte Lesart")
case("Bibelstelle nicht kanonisch", bad_ref, "to_ref")
case("Hintergrundnotiz ohne Text", bad_background, "background_note ohne text_de")
case("Hintergrundnotiz ohne Kontext", bad_background, "ist kein context-Datensatz")
case("Entscheidung ohne Zieltext", bad_decision, "Zieltext nicht in der Übersetzung")
case("Entscheidung unbekannte Art", bad_decision, "unbekannte Art")
case("Entscheidung falsches Griechisch", bad_decision, "nicht im Vers")
case("Lokalisierung Listenlänge", bad_localization, "passt nicht zum Original")
case("Lokalisierung unbekanntes Feld", bad_localization, "fehlt im Original")
with tempfile.TemporaryDirectory() as tmp:
    root = pathlib.Path(tmp)
    shutil.copytree(ROOT / "data", root / "data")
    stale_localization(root)
    res = run(root)
    assert res.returncode == 0 and "FIND-LP-0001.json: Feld claim_de veraltet" in res.stdout, res.stdout[-500:]
    sys.path.insert(0, str(ROOT / "scripts"))
    import localizations
    assert "claim_de" not in localizations.load_all(root).get("FIND-LP-0001", {}).get("gsw", {}), "veraltetes Feld ausgeliefert"
print("PASS: validator negative tests (NC-Trennung, Annotation, Bewertung, Bibelstelle, Hintergrund, Übersetzungsentscheidung, Lokalisierung inkl. veraltet)")
