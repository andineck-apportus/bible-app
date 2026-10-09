#!/usr/bin/env python3
"""Technische Prüfung aller Datensätze in data/.

Prüft:
1. Schema (schema/record.schema.json) – ausgewertet wird die Teilmenge
   type, enum, pattern, required, properties, items, uniqueItems und lokale $ref.
2. Eindeutige IDs und definierte Tags.
3. Verweise auf andere Datensätze (inkl. Lesarten «VAR-…:R1») lösen auf.
4. Alle Bibelstellen sind kanonisch (docs/BIBELSTELLEN.md).

Ein PASS ist keine fachliche Freigabe. Nur Standardbibliothek.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import refs  # noqa: E402

SCHEMA = json.loads((ROOT / "schema" / "record.schema.json").read_text(encoding="utf-8"))

# Felder, die auf andere Datensätze verweisen
ID_FIELDS = ["work", "primary_unit", "subject", "principle", "context", "from", "edition"]
ID_LIST_FIELDS = ["based_on", "derived_from", "outputs", "evidence_objects", "related", "imported_records"]
READING_FIELDS = ["preferred_reading", "alternative", "based_on_variant"]
# Felder mit Bibelstellen (siehe docs/BIBELSTELLEN.md)
REF_FIELDS = ["reference", "to_ref", "range"]
REF_LIST_FIELDS = ["evidence_refs", "imported_scope"]

JSON_TYPES = {"object": dict, "array": list, "string": str, "null": type(None),
              "boolean": bool, "integer": int, "number": (int, float)}


def check_schema(value, schema, path, errors):
    if "$ref" in schema:
        name = schema["$ref"].removeprefix("#/$defs/")
        schema = {**SCHEMA["$defs"][name], **{k: v for k, v in schema.items() if k != "$ref"}}
    if "type" in schema:
        types = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
        if not any(isinstance(value, JSON_TYPES[t]) and not (t in ("integer", "number") and isinstance(value, bool))
                   for t in types):
            errors.append(f"{path}: erwartet {'/'.join(types)}")
            return
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: Wert {value!r} nicht erlaubt")
    if "pattern" in schema and isinstance(value, str) and not re.search(schema["pattern"], value):
        errors.append(f"{path}: {value!r} passt nicht zu {schema['pattern']}")
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{path}: Pflichtfeld {key!r} fehlt")
        for key, sub in schema.get("properties", {}).items():
            if key in value:
                check_schema(value[key], sub, f"{path}.{key}", errors)
    if isinstance(value, list):
        if schema.get("uniqueItems") and len(value) != len({json.dumps(v, sort_keys=True) for v in value}):
            errors.append(f"{path}: doppelte Einträge")
        if "items" in schema:
            for i, item in enumerate(value):
                check_schema(item, schema["items"], f"{path}[{i}]", errors)


def main():
    errors = []
    records = {}
    for path in sorted((ROOT / "data").rglob("*.json")):
        rel = path.relative_to(ROOT)
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{rel}: ungültiges JSON ({exc})")
            continue
        check_schema(record, SCHEMA, str(rel), errors)
        rid = record.get("id")
        if rid in records:
            errors.append(f"{rel}: doppelte ID {rid}")
        records[rid] = (rel, record)

    tags = {rid for rid, (_, r) in records.items() if r.get("type") == "tag"}
    readings = {f"{rid}:{rd['reading_id']}" for rid, (_, r) in records.items()
                if r.get("type") == "variant" for rd in r.get("readings", [])}

    def check_id(rel, field, target):
        if target is not None and target not in records:
            errors.append(f"{rel}: {field} verweist auf unbekannte ID {target!r}")

    def check_reading(rel, field, target):
        if target is not None and target not in readings:
            errors.append(f"{rel}: {field} verweist auf unbekannte Lesart {target!r}")

    def check_ref(rel, field, value):
        try:
            refs.parse(value)
        except refs.RefError as exc:
            errors.append(f"{rel}: {field}: {exc}")

    ref_count = 0
    for rid, (rel, r) in records.items():
        for tag in r.get("tags", []):
            if tag not in tags:
                errors.append(f"{rel}: unbekanntes Tag {tag}")
        for f in ID_FIELDS:
            check_id(rel, f, r.get(f))
        for f in ID_LIST_FIELDS:
            for target in r.get(f) or []:
                check_id(rel, f, target)
        for sup in (r.get("supersedes"), (r.get("knowledge") or {}).get("supersedes")):
            check_id(rel, "supersedes", sup)
        for f in READING_FIELDS:
            check_reading(rel, f, r.get(f))
        for i, a in enumerate(r.get("alignments") or []):
            check_reading(rel, f"alignments[{i}].depends_on_reading", a.get("depends_on_reading"))
        for f in REF_FIELDS:
            if f in r:
                check_ref(rel, f, r[f]); ref_count += 1
        for f in REF_LIST_FIELDS:
            for v in r.get(f) or []:
                check_ref(rel, f, v); ref_count += 1
        for key in (r.get("text_by_reference") or {}):
            check_ref(rel, "text_by_reference", key); ref_count += 1
        for i, tok in enumerate(r.get("tokens") or []):
            check_ref(rel, f"tokens[{i}].reference", tok.get("reference")); ref_count += 1
            check_id(rel, f"tokens[{i}].edition", tok.get("edition"))

    if errors:
        for e in errors:
            print("FAIL:", e)
        sys.exit(f"{len(errors)} Fehler")
    print(f"PASS: {len(records)} records, {len(tags)} defined tags; schema, unique IDs, "
          f"tag/ID/reading references and {ref_count} bible references valid")


if __name__ == "__main__":
    main()
