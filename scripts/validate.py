#!/usr/bin/env python3
"""Technische Prüfung aller Datensätze in data/ (freier Kern) und data-nc/ (Studienschicht).

Prüft:
1. Schema (schema/record.schema.json) – ausgewertet wird die Teilmenge
   type, enum, pattern, required, properties, items, uniqueItems und lokale $ref.
2. Eindeutige IDs und definierte Tags.
3. Verweise auf andere Datensätze (inkl. Lesarten «VAR-…:R1» und Token-IDs) lösen auf.
4. Alle Bibelstellen sind kanonisch (docs/BIBELSTELLEN.md).
5. Alignments mit coverage = "complete": jedes Token im Bereich genau einmal zugeordnet,
   jeder Zieltext kommt im Wortlaut der verknüpften Übersetzung vor.
6. Annotationen verweisen nur auf Tokens des annotierten Token-Sets; Bewertungen auf
   vorhandene Variantenstellen und Lesarten.
7. Lizenzschichten: Datensätze in data/ verweisen nie auf Datensätze in data-nc/.

Ein PASS ist keine fachliche Freigabe. Nur Standardbibliothek.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__import__("os").environ.get("BIBLE_APP_ROOT") or pathlib.Path(__file__).resolve().parents[1])
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import refs  # noqa: E402

SCHEMA = json.loads((pathlib.Path(__file__).resolve().parents[1] / "schema" / "record.schema.json").read_text(encoding="utf-8"))

# Felder, die auf andere Datensätze verweisen
ID_FIELDS = ["work", "primary_unit", "subject", "principle", "context", "from", "edition",
             "base_edition", "apparatus", "same_variation_unit_as", "incorporates", "based_on_edition",
             "based_on_tokens", "source_tokens_set", "target_translation", "bibliographic_source",
             "annotates", "method", "superseded_by", "annotation_moved_to", "based_on_annotation"]
ID_LIST_FIELDS = ["based_on", "derived_from", "outputs", "evidence_objects", "related", "imported_records",
                  "based_on_annotations"]
LAYERS = {"data": "core", "data-nc": "nc"}
READING_FIELDS = ["preferred_reading", "alternative", "based_on_variant"]
READING_LIST_FIELDS = ["follows_readings"]
# Felder mit Token-IDs (Tokens liegen innerhalb eines token_set)
TOKEN_LIST_FIELDS = ["base_tokens"]
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
    layer_of = {}
    paths = [(p, layer) for d, layer in LAYERS.items() if (ROOT / d).exists()
             for p in sorted((ROOT / d).rglob("*.json"))]
    for path, layer in paths:
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
        layer_of[rid] = layer

    tags = {rid for rid, (_, r) in records.items() if r.get("type") == "tag"}
    readings = {f"{rid}:{rd['reading_id']}" for rid, (_, r) in records.items()
                if r.get("type") == "variant" for rd in r.get("readings", [])}

    current_layer = {"value": "core"}

    def check_id(rel, field, target):
        if target is not None and target not in records:
            errors.append(f"{rel}: {field} verweist auf unbekannte ID {target!r}")
        elif target is not None and current_layer["value"] == "core" and layer_of.get(target) == "nc":
            errors.append(f"{rel}: {field} verweist aus dem freien Kern auf NC-Datensatz {target!r}")

    def check_reading(rel, field, target):
        if target is not None and target not in readings:
            errors.append(f"{rel}: {field} verweist auf unbekannte Lesart {target!r}")

    def check_ref(rel, field, value):
        try:
            refs.parse(value)
        except refs.RefError as exc:
            errors.append(f"{rel}: {field}: {exc}")

    token_sets = {rid: [t["id"] for t in r.get("tokens", [])]
                  for rid, (_, r) in records.items() if r.get("type") == "token_set"}
    token_ids = {}
    for set_id, ids in token_sets.items():
        for tid in ids:
            if tid in token_ids or tid in records:
                errors.append(f"Token-ID {tid} nicht eindeutig")
            token_ids[tid] = set_id

    def check_tokens(rel, field, ids):
        for tid in ids or []:
            if tid not in token_ids:
                errors.append(f"{rel}: {field} verweist auf unbekanntes Token {tid!r}")

    def check_alignment_coverage(rel, r):
        """coverage = complete: jedes Token des token_set im Bereich genau einmal; Zieltexte im Übersetzungstext."""
        start, end = refs.parse(r["reference"])
        in_scope = [t for t in token_sets.get(r.get("source_tokens_set"), [])
                    if (start[1], start[2]) <= tuple(int(x) for x in t.rsplit("-", 3)[1:3]) <= (end[1], end[2])]
        used = [t for a in r.get("alignments", []) for t in a.get("source_tokens", [])]
        dupes = sorted({t for t in used if used.count(t) > 1})
        missing = [t for t in in_scope if t not in used]
        if dupes:
            errors.append(f"{rel}: Tokens mehrfach zugeordnet: {dupes[:5]}")
        if missing:
            errors.append(f"{rel}: Tokens ohne Zuordnung: {missing[:5]}")
        trans = records.get(r.get("target_translation"), (None, {}))[1].get("text_by_reference", {})
        for i, a in enumerate(r.get("alignments", [])):
            if a.get("target") is None:
                if a.get("kind") != "untranslated":
                    errors.append(f"{rel}: alignments[{i}] ohne target, aber nicht als untranslated markiert")
                continue
            text = trans.get(a.get("reference"), "")
            for part in a["target"].split(" … "):
                if part not in text:
                    errors.append(f"{rel}: alignments[{i}] Zieltext {part!r} nicht in Übersetzung {a.get('reference')}")

    ref_count = token_ref_count = 0
    token_set_members = {sid: set(ids) for sid, ids in token_sets.items()}
    annotation_count = assessment_count = 0
    for rid, (rel, r) in records.items():
        current_layer["value"] = layer_of[rid]
        if r.get("type") == "annotation_set":
            members = token_set_members.get(r.get("annotates"), set())
            for tid, entry in (r.get("entries") or {}).items():
                annotation_count += 1
                if tid not in members:
                    errors.append(f"{rel}: Annotation für Token {tid!r}, das nicht in {r.get('annotates')} liegt")
                for f in ("subject_ref", "referent"):
                    for t in entry.get(f, []):
                        if not t.startswith("TOK-"):
                            errors.append(f"{rel}: entries[{tid}].{f} enthält keine Token-ID: {t!r}")
                        else:
                            check_tokens(rel, f"entries[{tid}].{f}", [t])
        if r.get("type") == "assessment_set":
            for i, a in enumerate(r.get("assessments") or []):
                assessment_count += 1
                check_id(rel, f"assessments[{i}].assesses", a.get("assesses"))
                for res in a.get("results", []):
                    check_reading(rel, f"assessments[{i}].results.reading", res.get("reading"))
                    for ed in res.get("supporting_editions", []):
                        check_id(rel, f"assessments[{i}].supporting_editions", ed)
                for h in a.get("highest_support") or []:
                    check_reading(rel, f"assessments[{i}].highest_support", h)
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
        for f in READING_LIST_FIELDS:
            for target in r.get(f) or []:
                check_reading(rel, f, target)
        for f in TOKEN_LIST_FIELDS:
            check_tokens(rel, f, r.get(f)); token_ref_count += len(r.get(f) or [])
        for i, rd in enumerate(r.get("readings") or []):
            for ed in rd.get("editions") or []:
                check_id(rel, f"readings[{i}].editions", ed)
        for i, a in enumerate(r.get("alignments") or []):
            check_reading(rel, f"alignments[{i}].depends_on_reading", a.get("depends_on_reading"))
            check_tokens(rel, f"alignments[{i}].source_tokens", a.get("source_tokens"))
            token_ref_count += len(a.get("source_tokens") or [])
        if r.get("type") == "alignment" and r.get("coverage") == "complete":
            check_alignment_coverage(rel, r)
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
          f"tag/ID/reading references, {token_ref_count} token references, {ref_count} bible references, "
          f"{annotation_count} annotations, {assessment_count} assessments valid "
          f"({sum(v == 'nc' for v in layer_of.values())} records in data-nc)")


if __name__ == "__main__":
    main()
