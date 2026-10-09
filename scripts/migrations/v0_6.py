#!/usr/bin/env python3
"""Migration v0.5 -> v0.6 (2026-10-09).

1. Bibelstellen auf die kanonische Form (docs/BIBELSTELLEN.md) umstellen.
2. Typnamen vereinheitlichen: studie -> study, text-unit -> text_unit.
3. Offensichtlichen Tippfehler in einem Statuswert korrigieren.
4. Fehlende Ergebnisse der Pilotstudie in `outputs` nachtragen.

Jede Änderung wird mit altem und neuem Wert in
provenance/migrations/2026-10-09-v0.6.json protokolliert. Die Originale
bleiben in archive/packages/ und in der Git-Historie erhalten.
Idempotent: ein zweiter Lauf ändert nichts.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import refs  # noqa: E402

LOG = ROOT / "provenance" / "migrations" / "2026-10-09-v0.6.json"
TYPE_RENAMES = {"studie": "study", "text-unit": "text_unit"}
STUDY_OUTPUTS_ADD = [
    "FIND-MRK-0003", "FIND-MRK-0004", "VAR-MRK-003-029-001", "VAR-MRK-003-029-002",
    "DEC-MRK-003-029-001", "TRANS-MRK-003-029-DE-WORKING", "ALIGN-MRK-003-029-001",
    "TEXT-MRK-003-029-030-WORKING", "REL-MRK-0001", "REL-MRK-0002", "REL-MRK-0003",
    "QUESTION-MRK-0001",
]

changes = []


def record(path, field, old, new, reason):
    changes.append({"file": str(path.relative_to(ROOT)), "field": field,
                    "old": old, "new": new, "reason": reason})


def canon(value, book):
    return refs.canonical(value, default_book=book)


for path in sorted((ROOT / "data").rglob("*.json")):
    data = json.loads(path.read_text(encoding="utf-8"))
    before = json.dumps(data, ensure_ascii=False)
    book = "MRK" if "TAG-MARK" in data.get("tags", []) else None

    if data.get("type") in TYPE_RENAMES:
        new = TYPE_RENAMES[data["type"]]
        record(path, "type", data["type"], new, "kanonischer Typname gemäss Schema")
        data["type"] = new

    if isinstance(data.get("reference"), str) and not refs.is_canonical(data["reference"]):
        new = canon(data["reference"], book)
        record(path, "reference", data["reference"], new, "Bibelstellen-Konvention v0.6")
        data["reference"] = new

    if isinstance(data.get("to_ref"), str) and not refs.is_canonical(data["to_ref"]):
        new = canon(data["to_ref"], book)
        record(path, "to_ref", data["to_ref"], new, "Bibelstellen-Konvention v0.6")
        data["to_ref"] = new

    if isinstance(data.get("evidence_refs"), list):
        new = [r if refs.is_canonical(r) else canon(r, book) for r in data["evidence_refs"]]
        if new != data["evidence_refs"]:
            record(path, "evidence_refs", data["evidence_refs"], new, "Bibelstellen-Konvention v0.6")
            data["evidence_refs"] = new

    rng = data.get("range")
    if isinstance(rng, dict) and set(rng) == {"start", "end"}:
        work_book = data.get("work", "").removeprefix("WORK-") or book
        start, end = (f"{work_book}." + rng[k].replace(":", ".") for k in ("start", "end"))
        new = f"{start}-{end}"
        refs.parse(new)
        record(path, "range", rng, new, "Bibelstellen-Konvention v0.6; Bereich als eine kanonische Stelle")
        data["range"] = new

    if data.get("evidence_status") == "secondary_transcription_checked_not_primary_facsímile":
        new = "secondary_transcription_checked_not_primary_facsimile"
        record(path, "evidence_status", data["evidence_status"], new, "Tippfehler (í) im Statuswert")
        data["evidence_status"] = new

    if data.get("id") == "STUDY-MRK-0001":
        missing = [x for x in STUDY_OUTPUTS_ADD if x not in data["outputs"]]
        if missing:
            new = data["outputs"] + missing
            record(path, "outputs", data["outputs"], new,
                   "später hinzugekommene Ergebnisse der Pilotstudie nachgetragen (Roadmap-Lücke 3)")
            data["outputs"] = new

    if json.dumps(data, ensure_ascii=False) != before:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

if changes:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    LOG.write_text(json.dumps({
        "migration": "v0.5 -> v0.6",
        "date": "2026-10-09",
        "script": "scripts/migrations/v0_6.py",
        "note": "Inhaltliche Aussagen, Status, Konfidenz und IDs wurden nicht verändert. "
                "Die Prüfsummen in provenance/v0.5-files.json beschreiben weiterhin die v0.5-Originale.",
        "changes": changes,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"{len(changes)} Änderungen" + (f", Protokoll: {LOG.relative_to(ROOT)}" if changes else " (bereits migriert)"))
