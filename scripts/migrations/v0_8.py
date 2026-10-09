#!/usr/bin/env python3
"""Migration v0.7 -> v0.8 (2026-10-09): Text und Annotation trennen.

Bis v0.7 lagen die SBLGNT-Wörter von Mk 3,22–30 zusammen mit der MorphGNT-Annotation im
Token-Set TOKSET-SBLGNT-MRK-003-022-030. Ab v0.8:
- Wörter des ganzen Kapitels in TOKSET-SBLGNT-MRK-003 (aus der SBLGNT-Edition selbst; gleiche Token-IDs).
- MorphGNT-Annotation als eigene Schicht ANN-MORPHGNT-SBLGNT-MRK-003-022-030 (CC BY-SA 3.0).
- TOKSET-SBLGNT-MRK-003-022-030 bleibt als ID bestehen (Status deprecated, superseded_by), ohne Tokens.
- Verweise (Übersetzung, Alignment, Edition, Studie, Zählung) werden umgestellt.

Vorher wird geprüft, dass alle 140 Token-IDs in beiden Fassungen dasselbe Wort bezeichnen.
Protokoll: provenance/migrations/2026-10-09-v0.8.json. Idempotent.
"""
import json
import pathlib
import re
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2]
LOG = ROOT / "provenance/migrations/2026-10-09-v0.8.json"
OLD_ID, NEW_ID = "TOKSET-SBLGNT-MRK-003-022-030", "TOKSET-SBLGNT-MRK-003"
OLD = ROOT / "data/tokens/SBLGNT-MRK-003-022-030.json"
NEW = ROOT / "data/tokens/SBLGNT-MRK-003.json"
ANN_ID = "ANN-MORPHGNT-SBLGNT-MRK-003-022-030"
ANN = ROOT / "data/annotations/MORPHGNT-SBLGNT-MRK-003-022-030.json"
changes = []


def load(p):
    return json.loads(p.read_text(encoding="utf-8"))


def save(p, d):
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def cmp(w):
    w = unicodedata.normalize("NFC", w)
    return re.sub(r"[⸀-⸅,.·;:ʼ’]", "", w)


def log(path, field, old, new, reason):
    changes.append({"file": str(path.relative_to(ROOT)), "field": field, "old": old, "new": new, "reason": reason})


old = load(OLD)
new_tokens = {t["id"]: t for t in load(NEW)["tokens"]}
if old.get("tokens"):
    # 1. Gleichheit der Wörter prüfen
    for t in old["tokens"]:
        nt = new_tokens[t["id"]]
        assert cmp(t["word"]) == cmp(nt["word"]), (t["id"], t["word"], nt["word"])
    # 2. MorphGNT-Annotation als eigene Schicht
    ann = {
        "id": ANN_ID, "type": "annotation_set", "status": "imported_unreviewed", "tags": old["tags"],
        "annotates": NEW_ID, "reference": old["reference"], "layers": ["morphology", "lemma"],
        "source": old["source"], "import": old["import"],
        "migrated_from": OLD_ID,
        "note_de": "Bis v0.7 Teil von TOKSET-SBLGNT-MRK-003-022-030; Werte unverändert übernommen. «morphgnt_text» und «morphgnt_word» sind die Wortformen, wie MorphGNT sie führt (Apostroph ’ statt ʼ der Edition).",
        "entries": {t["id"]: {"lemma": t["lemma"], "pos": t["pos"], "parsing": t["parsing"],
                              "normalized": t["normalized"], "morphgnt_text": t["text"], "morphgnt_word": t["word"]}
                    for t in old["tokens"]},
    }
    ANN.parent.mkdir(parents=True, exist_ok=True)
    save(ANN, ann)
    log(ANN, "(neu)", None, ANN_ID, "MorphGNT-Annotation aus dem Pilot-Token-Set als eigene Schicht ausgelagert")
    # 3. Altes Token-Set als abgelöst kennzeichnen
    n = len(old["tokens"])
    log(OLD, "status, tokens", {"status": old["status"], "tokens": f"{n} Tokens"},
        {"status": "deprecated", "tokens": None, "superseded_by": NEW_ID, "annotation_moved_to": ANN_ID},
        "Text und Annotation getrennt; Tokens mit identischen IDs jetzt in TOKSET-SBLGNT-MRK-003 (aus der Edition), Annotation in ANN-MORPHGNT-…")
    old["status"] = "deprecated"
    del old["tokens"]
    old["superseded_by"] = NEW_ID
    old["annotation_moved_to"] = ANN_ID
    old["note_de"] = f"Bis v0.7 enthielt dieser Datensatz {n} Tokens mit MorphGNT-Annotation. Fassung in der Git-Historie (v0.7) rekonstruierbar."
    save(OLD, old)

# 4. Verweise umstellen
updates = [
    ("data/translations/TRANS-MRK-003-022-030-DE-WORKING.json", "based_on_tokens"),
    ("data/alignments/ALIGN-MRK-003-022-030-001.json", "source_tokens_set"),
]
for rel, field in updates:
    p = ROOT / rel
    d = load(p)
    if d.get(field) == OLD_ID:
        log(p, field, OLD_ID, NEW_ID, "Token-Set abgelöst (gleiche Token-IDs)")
        d[field] = NEW_ID
        save(p, d)

p = ROOT / "data/editions/ED-SBLGNT.json"
d = load(p)
target_scope = ["MRK.1-MRK.16"]
target_records = [f"TOKSET-SBLGNT-MRK-{c:03d}" for c in range(1, 17)] + ["COUNT-SBLGNT-MRK"]
if d.get("imported_scope") != target_scope:
    log(p, "imported_scope, imported_records", {"imported_scope": d.get("imported_scope"), "imported_records": d.get("imported_records")},
        {"imported_scope": target_scope, "imported_records": target_records}, "ganzes Markusevangelium importiert")
    d["imported_scope"], d["imported_records"] = target_scope, target_records
    save(p, d)

p = ROOT / "data/counts/SBLGNT-MRK-003-022-030.json"
d = load(p)
if "based_on_annotation" not in d:
    log(p, "based_on_annotation", None, ANN_ID, "Zählung beruht auf MorphGNT-Lemmata; Herkunft explizit gemacht")
    d["based_on_annotation"] = ANN_ID
    save(p, d)

p = ROOT / "data/studies/STUDY-MRK-0001.json"
d = load(p)
add = [x for x in (NEW_ID, ANN_ID, "ANN-MACULA-SBLGNT-MRK-003") if x not in d["outputs"]]
if add:
    log(p, "outputs", None, add, "neue Token- und Annotationsschichten der Pilotperikope")
    d["outputs"] += add
    save(p, d)

if changes:
    LOG.write_text(json.dumps({"migration": "v0.7 -> v0.8", "date": "2026-10-09", "script": "scripts/migrations/v0_8.py",
                               "note": "Token-IDs unverändert; MorphGNT-Werte unverändert in eigene Annotationsschicht verschoben.",
                               "changes": changes}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"{len(changes)} Änderungen" + (f", Protokoll: {LOG.relative_to(ROOT)}" if changes else " (bereits migriert)"))
