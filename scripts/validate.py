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
7. Hintergrundnotizen (background_note) haben Thema, Text, Stelle, Herkunft und einen
   historischen Kontext.
8. Lokalisierungen (localization): Felder existieren im Original (gleicher Typ, gleiche Listenlänge);
   veraltete Felder (Original seit der Übersetzung geändert) werden als WARN gemeldet, nicht als Fehler.
9. Bibelstellen im Fliesstext: jede Marke [[…]] ist kanonisch; unmarkierte Stellen in deutscher Schreibweise
   werden als WARN gemeldet (scripts/prose_refs.py).
10. Arbeitsübersetzungen derselben Sprache überschneiden sich nicht (sonst wäre der Vorrang unklar).
11. Lizenzschichten: Datensätze in data/ verweisen nie auf Datensätze in data-nc/.
12. Weiterdenken (reflection, reception): ID, Bezug auf Texteinheit oder Zusammenfassung, Frage bzw. Tradition,
    Quellenprüfung wie bei Hintergrund; Prozessverweise «PROC-…@Fassung» lösen auf.

Ein PASS ist keine fachliche Freigabe. Nur Standardbibliothek.
"""
import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__import__("os").environ.get("BIBLE_APP_ROOT") or pathlib.Path(__file__).resolve().parents[1])
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import refs  # noqa: E402
import localizations  # noqa: E402
import prose_refs  # noqa: E402

SCHEMA = json.loads((pathlib.Path(__file__).resolve().parents[1] / "schema" / "record.schema.json").read_text(encoding="utf-8"))

# Felder, die auf andere Datensätze verweisen
ID_FIELDS = ["witness", "target_context", "control_translation", "work", "primary_unit", "subject", "principle", "context", "from", "edition",
             "base_edition", "apparatus", "same_variation_unit_as", "incorporates", "based_on_edition",
             "based_on_tokens", "source_tokens_set", "target_translation", "bibliographic_source",
             "annotates", "localizes", "method", "superseded_by", "annotation_moved_to", "based_on_annotation"]
ID_LIST_FIELDS = ["based_on", "derived_from", "outputs", "evidence_objects", "related", "imported_records", "parts",
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


def strip_marks(word):
    """Vergleichsform eines griechischen Worts: NFC, ohne Apparatzeichen, Interpunktion und Elisionsvarianten."""
    import unicodedata
    w = unicodedata.normalize("NFC", word).replace("’", "ʼ").replace("'", "ʼ")
    return re.sub(r"[⸀-⸅,.·;:!?()—⟦⟧\[\]]", "", w)


def heb_cons(word):
    """Vergleichsform eines hebräischen Worts: nur Konsonanten (ohne Vokale, Akzente, Maqqef, Sof Pasuq)."""
    return re.sub(r"[^\u05D0-\u05EA]", "", word or "")


def main():
    errors = []
    warnings = []
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

    # Verszahlen der Navigationszählung (KJV, data/navigation): Stellen ausserhalb gelten als andere Versifikation
    nav = next((r for _, r in records.values() if r.get("type") == "navigation_structure"), None)
    verse_counts = {b["code"]: b["verses_per_chapter"] for b in (nav or {}).get("books", [])}
    current_record = {}

    def outside_nav(ref):
        for (b, c, v) in refs.parse(ref):
            if b in verse_counts and c and (c > len(verse_counts[b]) or (v and v > verse_counts[b][c - 1])):
                return True
        return False

    def check_ref(rel, field, value):
        try:
            refs.parse(value)
        except refs.RefError as exc:
            errors.append(f"{rel}: {field}: {exc}")
            return
        r = current_record.get("r") or {}
        declared = r.get("versification") or "KJV"
        if verse_counts and declared.startswith("KJV") and r.get("type") != "versification_map" and outside_nav(value):
            warnings.append(f"{rel}: {field} {value} gibt es in der Navigationszählung (KJV) nicht; andere Versifikation? "
                            "(Feld versification setzen oder Stelle umrechnen, siehe docs/BIBELSTELLEN.md)")

    tokens_by_set = {rid: r.get("tokens", []) for rid, (_, r) in records.items() if r.get("type") == "token_set"}
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
        current_record["r"] = r
        if r.get("type") == "summary" and r.get("group"):
            nav_groups = {g["id"] for _, nr in records.values() if nr.get("type") == "navigation_structure" for g in nr.get("groups", [])}
            if r["group"] not in nav_groups:
                errors.append(f"{rel}: group {r['group']!r} in keiner Navigationsstruktur")
        if r.get("type") == "translation":
            for i, dcs in enumerate(r.get("decisions", [])):
                if dcs.get("kind") not in ("literal", "adapted", "interpretive", "traditional"):
                    errors.append(f"{rel}: decisions[{i}] unbekannte Art {dcs.get('kind')!r}")
                if dcs.get("grc") and r.get("based_on_tokens") in token_sets:
                    vw = {strip_marks(t["word"]) for t in tokens_by_set.get(r["based_on_tokens"], []) if t["reference"] == dcs.get("reference")}
                    missing = [x for x in dcs["grc"].split() if strip_marks(x) not in vw]
                    if missing:
                        errors.append(f"{rel}: decisions[{i}] griechische Wörter {missing} nicht im Vers {dcs.get('reference')}")
                if dcs.get("heb") and r.get("based_on_tokens") in token_sets:
                    vt = [t for t in tokens_by_set.get(r["based_on_tokens"], []) if t["reference"] == dcs.get("reference")]
                    forms = {heb_cons(t["word"]) for t in vt}
                    words = {}
                    for t in vt:
                        words[t.get("word_no")] = words.get(t.get("word_no"), "") + heb_cons(t["word"])
                    forms |= set(words.values())
                    missing = [x for x in dcs["heb"].split() if heb_cons(x) not in forms]
                    if missing:
                        errors.append(f"{rel}: decisions[{i}] hebräische Wörter {missing} nicht im Vers {dcs.get('reference')}")
                if dcs.get("target", "\0") not in (r.get("text_by_reference") or {}).get(dcs.get("reference"), ""):
                    errors.append(f"{rel}: decisions[{i}] Zieltext nicht in der Übersetzung von {dcs.get('reference')}")
        for i, tm in enumerate(r.get("terms", []) if isinstance(r.get("terms"), list) else []):
            if tm.get("lang") not in ("grc", "heb", "arc", "lat") or not tm.get("word") or not tm.get("de"):
                errors.append(f"{rel}: terms[{i}] braucht lang (grc/heb/arc/lat), word und de")
            elif tm["lang"] != "grc" and not tm.get("translit"):
                errors.append(f"{rel}: terms[{i}] ohne translit (nur Griechisch wird automatisch umgeschrieben)")
        if r.get("type") == "versification_map":
            for i, e in enumerate(r.get("entries") or []):
                for f in ("source_ref", "standard_ref"):
                    if f in e:
                        check_ref(rel, f"entries[{i}].{f}", e[f]); ref_count += 1
        if r.get("type") == "tagged_text_alignment":
            # Zuordnung fremder getaggter Texte (STEPBible TAGNT/TAHOT) zu unseren Tokens: alle Token-IDs müssen existieren
            for tid, e in (r.get("entries") or {}).items():
                check_tokens(rel, "entries", [tid] + list(e.get("tokens") or []))
                token_ref_count += 1 + len(e.get("tokens") or [])
            check_tokens(rel, "dstrong", list(r.get("dstrong") or {}))
            for i, x in enumerate((r.get("extra_words") or []) + (r.get("ketiv_without_qere") or [])):
                if x.get("after"):
                    check_tokens(rel, f"extra_words/ketiv_without_qere[{i}].after", [x["after"]])
                check_ref(rel, f"extra_words/ketiv_without_qere[{i}].ref", x.get("ref")); ref_count += 1
        if r.get("type") == "illustration":
            # Bild: Zeichnung, Stil, Bildauftrag; gezeigte Lexikon-Einträge haben im Stil eine Darstellung
            if not (ROOT / str(r.get("file", ""))).is_file():
                errors.append(f"{rel}: Bilddatei {r.get('file')} fehlt")
            st = records.get(r.get("style"), (None, {}))[1]
            if st.get("type") != "illustration_style":
                errors.append(f"{rel}: Stil {r.get('style')} fehlt")
            else:
                for d in r.get("depicts") or []:
                    if d not in (st.get("renderings") or {}):
                        errors.append(f"{rel}: {d} hat im Stil {r.get('style')} keine Darstellung")
            if records.get(r.get("brief"), (None, {}))[1].get("type") != "illustration_brief":
                errors.append(f"{rel}: Bildauftrag {r.get('brief')} fehlt")
            if r.get("level") not in ("bible", "testament", "group", "book", "chapter", "section", "verse"):
                errors.append(f"{rel}: level {r.get('level')!r} ungültig")
            # Gemalte Bilder (docs/BILDSTIL.md): Bilddateien, Belege B/R/I je Feld, Prüfstufe mit Fingerabdruck des Bildes
            if r.get("scenes"):
                def _vs(ref_):  # 'JHN.2.3-JHN.2.5' → ((2,3),(2,5)); Kapitelangabe 'JHN.2' → ganze Spanne
                    a_, _, z_ = str(ref_).partition("-")
                    def p1(x, ende):
                        t = x.split(".")
                        if len(t) < 2 or not t[1].isdigit():
                            return None
                        return (int(t[1]), int(t[2]) if len(t) > 2 else (999 if ende else 0))
                    v0, v1 = p1(a_, False), p1(z_ or a_, True)
                    return (v0, v1) if v0 and v1 else None
                base_ = (ROOT / str(r.get("file", ""))).parent
                for i_, sc_ in enumerate(r["scenes"]):
                    img_ = base_ / str(sc_.get("image", ""))
                    if not img_.is_file():
                        errors.append(f"{rel}: Bild {sc_.get('image')} fehlt")
                    span_ = _vs(sc_.get("reference")) if sc_.get("reference") else None
                    for e_ in (r.get("evidence") or [[]] * len(r["scenes"]))[i_]:
                        if e_.get("s") not in ("B", "R", "I"):
                            errors.append(f"{rel}: Feld {i_ + 1}: Beleg ohne gültige Stufe B/R/I")
                        if e_.get("s") == "B" and not e_.get("ref"):
                            errors.append(f"{rel}: Feld {i_ + 1}: B-Beleg ohne Bibelstelle")
                        if e_.get("ref"):
                            check_ref(rel, f"evidence[{i_}].ref", e_["ref"]); ref_count += 1
                            ev_ = _vs(e_["ref"])
                            if span_ and ev_ and e_.get("s") == "B" and (ev_[0] < span_[0] or ev_[1] > span_[1]):
                                warnings.append(f"{rel}: Feld {i_ + 1}: B-Beleg {e_['ref']} liegt ausserhalb der Stelle {sc_.get('reference')}")
                    for sp_ in sc_.get("speech") or []:
                        check_ref(rel, f"scenes[{i_}].speech.ref", sp_.get("ref")); ref_count += 1
                c_ = r.get("check") or {}
                st_ = c_.get("stufe")
                if st_ not in (None, "entwurf", "ki-geprueft", "fachlich-geprueft"):
                    errors.append(f"{rel}: check.stufe {st_!r} ungültig")
                if st_ == "fachlich-geprueft" and not (c_.get("fachlich") or {}).get("name"):
                    errors.append(f"{rel}: «fachlich-geprueft» ohne Namen der prüfenden Person")
                if st_ in ("ki-geprueft", "fachlich-geprueft"):
                    imgs_ = {sc_["scene"]: base_ / sc_["image"] for sc_ in r["scenes"]}
                    for f_ in c_.get("felder") or []:
                        p_img = imgs_.get(f_.get("scene"))
                        if f_.get("ergebnis") != "bestanden" or (f_.get("schluss") or {}).get("ergebnis") != "bestanden":
                            errors.append(f"{rel}: Stufe {st_}, aber Feld {f_.get('scene')} nicht bestanden")
                        elif p_img and p_img.is_file() and hashlib.sha256(p_img.read_bytes()).hexdigest()[:16] != f_.get("bild_sha"):
                            errors.append(f"{rel}: Prüfung veraltet – Bild {f_.get('scene')} hat sich seit der Prüfung geändert")
                    if {f_.get("scene") for f_ in c_.get("felder") or []} != set(imgs_):
                        errors.append(f"{rel}: Stufe {st_}, aber nicht jedes Feld geprüft")
        if r.get("type") == "process":
            # Prozesse (docs/PROZESSE.md): Fassungen aufsteigend, Rollen gültig, Rücksprünge auf vorhandene Schritte
            vs_ = r.get("versions") or []
            if [v.get("valid_from") for v in vs_] != sorted(v.get("valid_from") for v in vs_):
                errors.append(f"{rel}: Fassungen nicht nach Datum geordnet")
            if vs_ and r.get("current") != vs_[-1].get("version"):
                errors.append(f"{rel}: current ist nicht die letzte Fassung")
            for v in vs_:
                ids_ = {st_.get("id") for st_ in v.get("steps") or []}
                for st_ in v.get("steps") or []:
                    if st_.get("role") not in ("bearbeitung", "pruefung", "werkzeug", "modell", "herausgabe"):
                        errors.append(f"{rel}: Fassung {v.get('version')}, Schritt {st_.get('id')}: Rolle {st_.get('role')!r} ungültig")
                    if st_.get("back") and st_["back"].get("to") not in ids_:
                        errors.append(f"{rel}: Fassung {v.get('version')}, Schritt {st_.get('id')}: Rücksprung auf unbekannten Schritt")
        if isinstance(r.get("process"), str):
            # Prozessverweis «PROC-…@Fassung» bei Erklärtexten (z. B. reflection, reception; docs/PROZESSE.md)
            pid_, _, pv_ = r["process"].partition("@")
            pr_ = records.get(pid_, (None, {}))[1]
            if pr_.get("type") != "process" or pv_ not in {v.get("version") for v in pr_.get("versions") or []}:
                errors.append(f"{rel}: process {r['process']!r} unbekannt")
        if r.get("type") in ("reflection", "reception"):
            # Weiterdenken (docs/WEITERDENKEN.md): Frage zum Weiterdenken bzw. «Wie man es gelesen hat»
            kind_ = r["type"]
            pre_ = "REFL" if kind_ == "reflection" else "RCPT"
            if not re.match(rf"^{pre_}-[1-3]?[A-Z]{{2,3}}-\d{{4}}$", rid or ""):
                errors.append(f"{rel}: ID muss {pre_}-<BUCH>-nnnn sein")
            sj_ = records.get(r.get("subject"), (None, {}))[1]
            if sj_ and sj_.get("type") not in ("text_unit", "summary"):
                errors.append(f"{rel}: subject muss eine Texteinheit (TU-…) oder Zusammenfassung einer Ebene (SUM-…) sein")
            if not r.get("subject"):
                errors.append(f"{rel}: {kind_} ohne subject")
            if not r.get("authorship_de"):
                errors.append(f"{rel}: {kind_} ohne authorship_de")
            if kind_ == "reflection":
                if not r.get("question_de") or not str(r["question_de"]).rstrip().endswith("?"):
                    errors.append(f"{rel}: question_de fehlt oder ist keine Frage")
                if not isinstance(r.get("order"), int):
                    errors.append(f"{rel}: order (Ganzzahl) fehlt")
            else:
                if r.get("tradition") not in ("jewish", "church_fathers", "liturgy", "art", "music", "literature", "reformation", "modern_scholarship"):
                    errors.append(f"{rel}: tradition {r.get('tradition')!r} unbekannt")
                for f_ in ("period_de", "text_de"):
                    if not r.get(f_):
                        errors.append(f"{rel}: reception ohne {f_}")
                if r.get("confidence") not in ("high", "probable", "possible"):
                    errors.append(f"{rel}: confidence muss high, probable oder possible sein")
                sc_ = r.get("source_check")
                if sc_ is not None and (not isinstance(sc_, dict) or sc_.get("result") not in ("confirmed", "corrected", "partly", "unverifiable")
                                        or not re.match(r"^\d{4}-\d{2}-\d{2}$", str(sc_.get("date", ""))) or not sc_.get("method_de")):
                    errors.append(f"{rel}: source_check braucht date, result (confirmed/corrected/partly/unverifiable), method_de, checked[]")
        if r.get("type") == "illustration" and (r.get("check") or {}).get("process"):
            pid_, _, pv_ = r["check"]["process"].partition("@")
            pr_ = records.get(pid_, (None, {}))[1]
            if pr_.get("type") != "process" or pv_ not in {v.get("version") for v in pr_.get("versions") or []}:
                errors.append(f"{rel}: check.process {r['check']['process']!r} unbekannt")
        if r.get("type") == "illustration_style":
            if r.get("library") and not (ROOT / r["library"]).is_file():
                errors.append(f"{rel}: Bibliothek {r['library']} fehlt")
            for fid in r.get("renderings") or {}:
                if records.get(fid, (None, {}))[1].get("type") != "figure":
                    errors.append(f"{rel}: Darstellung für {fid}, der nicht im Bildlexikon steht")
        if r.get("type") == "illustration_brief":
            # Nur Lexikon-Einträge; Gleichlauf mit dem Text über Fingerabdrücke (veraltet = Fehler, bis erneut geprüft)
            for p_ in r.get("panels") or []:
                ids_ = [*p_.get("figures", []), *p_.get("objects", []), *p_.get("signs", [])]
                for sp in p_.get("speech") or []:
                    ids_ += [sp.get("from"), sp.get("to"), *sp.get("icons", [])]
                for x in ids_:
                    if records.get(x, (None, {}))[1].get("type") != "figure":
                        errors.append(f"{rel}: {x} nicht im Bildlexikon")
                check_ref(rel, f"panels[{p_.get('n')}].reference", p_.get("reference")); ref_count += 1
                # Worte im Bild: Stichwörter stehen so im Text (Hochdeutsch; ohne Satzzeichen und Gross-/Kleinschreibung)
                kw_ = (p_.get("keywords") or {}).get("de") if isinstance(p_.get("keywords"), dict) else p_.get("keywords")
                if kw_:
                    norm_ = lambda s: " ".join(re.sub(r"[^\w\s]", " ", s.lower()).split())  # noqa: E731
                    txt_ = ""
                    for b_ in r.get("basis") or []:
                        if b_.get("field") != "summary":
                            tbr_ = records.get(b_.get("record"), (None, {}))[1].get("text_by_reference") or {}
                            a_, _, z_ = str(p_.get("reference", "")).partition("-")
                            bk_, c_, v1_ = (a_.split(".") + ["", "", ""])[:3]
                            c2_, v2_ = (z_.split(".")[1], z_.split(".")[2]) if z_ else (c_, v1_)
                            for k_, s_ in tbr_.items():
                                kb_, kc_, kv_ = (k_.split(".") + ["", "", ""])[:3]
                                if kb_ == bk_ and kv_.isdigit() and c_.isdigit() and (int(c_), int(v1_ or 0)) <= (int(kc_), int(kv_)) <= (int(c2_), int(v2_ or 0)):
                                    txt_ += " " + s_
                    if txt_ and norm_(kw_) not in norm_(txt_):
                        warnings.append(f"{rel}: Feld {p_.get('n')}: Stichwort «{kw_}» steht so nicht im Text {p_.get('reference')}")
            if r.get("target") not in records:
                errors.append(f"{rel}: Ziel {r.get('target')} unbekannt")
            for b_ in r.get("basis") or []:
                src = records.get(b_.get("record"), (None, {}))[1]
                if b_.get("field") == "summary":
                    cur = src.get("summary_de") or src.get("text_de")
                else:
                    a_, _, z_ = str(b_.get("reference", "")).partition("-")
                    bk_, c_, v1_ = (a_.split(".") + ["", "", ""])[:3]
                    v2_ = z_.split(".")[2] if z_ else v1_
                    tbr = src.get("text_by_reference") or {}
                    cur = " ".join(tbr[f"{bk_}.{c_}.{v}"] for v in range(int(v1_ or 0), int(v2_ or 0) + 1) if f"{bk_}.{c_}.{v}" in tbr)
                if localizations.fingerprint(cur) != b_.get("fingerprint") and r.get("rework"):
                    warnings.append(f"{rel}: Bild wird neu erstellt ({r['rework'].get('reason_de', '')}); Text {b_.get('record')} {b_.get('reference', '')} geändert")
                elif localizations.fingerprint(cur) != b_.get("fingerprint"):
                    errors.append(f"{rel}: Bildauftrag veraltet – Text {b_.get('record')} {b_.get('reference', '')} hat sich geändert; Auftrag und Bilder prüfen, dann mit BIBLE_BRIEF_CONFIRM=1 bestätigen")
        if r.get("core_basis"):
            # Zusammenfassung aus der Kernanalyse (docs/VERDICHTUNG.md): veraltet, wenn sich die Kernanalyse geändert hat
            cb = r["core_basis"]
            core = records.get(cb.get("core"), (None, {}))[1]
            if not core:
                errors.append(f"{rel}: core_basis verweist auf unbekannte Kernanalyse {cb.get('core')}")
            elif localizations.fingerprint(json.dumps({k: core.get(k) for k in ("core_de", "moments", "structure") if k != "structure" or core.get(k)}, ensure_ascii=False, sort_keys=True)) != cb.get("fingerprint"):
                warnings.append(f"{rel}: Zusammenfassung veraltet – Kernanalyse {cb.get('core')} hat sich geändert; mit scripts/authoring/zusammenfassungen.py erneuern")
        if r.get("type") == "lexicon" and not isinstance(r.get("entries"), dict):
            errors.append(f"{rel}: lexicon braucht entries als Objekt (Schlüssel → Eintrag)")
        if r.get("type") == "crossref_set":
            parsed = set()
            for frm, items in (r.get("entries") or {}).items():
                if frm not in parsed:
                    check_ref(rel, f"entries[{frm}]", frm); parsed.add(frm)
                for it in items:
                    if it[0] not in parsed:
                        check_ref(rel, f"entries[{frm}]", it[0]); parsed.add(it[0])
                    ref_count += 1
        if r.get("type") == "witness_reading_set":
            for i, e in enumerate(r.get("entries", [])):
                var = records.get(e.get("variant"), (None, {}))[1]
                if not var:
                    errors.append(f"{rel}: entries[{i}] unbekannte Variantenstelle {e.get('variant')!r}")
                elif e.get("result", "").startswith("R") and e["result"] not in {x["reading_id"] for x in var.get("readings", [])}:
                    errors.append(f"{rel}: entries[{i}] unbekannte Lesart {e['result']!r}")
                if e.get("source") not in records:
                    errors.append(f"{rel}: entries[{i}] unbekannte Quelle {e.get('source')!r}")
        if r.get("type") == "witness_transcription":
            if bool(r.get("witness")) == bool(r.get("edition")):
                errors.append(f"{rel}: witness_transcription braucht genau eines von witness/edition")
            for k in (r.get("verses") or {}):
                check_ref(rel, f"verses[{k}]", k); ref_count += 1
        if r.get("type") == "localization":
            orig = records.get(r.get("localizes"), (None, None))[1]
            if orig is not None:
                for k, val in (r.get("fields") or {}).items():
                    ov = [t.get("de") for t in orig.get("terms", [])] if k == "terms" else orig.get(k)
                    if ov is None:
                        errors.append(f"{rel}: Feld {k} fehlt im Original {r['localizes']}")
                    elif type(ov) is not type(val) or (isinstance(val, list) and len(val) != len(ov)):
                        errors.append(f"{rel}: Feld {k} passt nicht zum Original (Typ/Länge)")
                for k in localizations.stale_fields(r, orig):
                    warnings.append(f"{rel}: Feld {k} veraltet (Original seit der Übersetzung geändert)")
        if r.get("type") == "background_note":
            # Übersichtsnotizen (scope bible/testament/book_group) haben keine einzelne Stelle
            scope = r.get("scope")
            need = ("topic_de", "text_de", "context", "authorship_de") + (() if scope in ("bible", "testament", "book_group") else ("reference",))
            for f in need:
                if not r.get(f):
                    errors.append(f"{rel}: background_note ohne {f}")
            sc = r.get("source_check")
            if sc is not None:
                if not isinstance(sc, dict) or sc.get("result") not in ("confirmed", "corrected", "partly", "unverifiable") \
                        or not re.match(r"^\d{4}-\d{2}-\d{2}$", str(sc.get("date", ""))) or not sc.get("method_de") or not isinstance(sc.get("checked", []), list):
                    errors.append(f"{rel}: source_check braucht date, result (confirmed/corrected/partly/unverifiable), method_de, checked[]")
            if scope not in (None, "bible", "testament", "book_group", "book"):
                errors.append(f"{rel}: unbekannter scope {scope!r}")
            if scope == "testament" and r.get("testament") not in ("OT", "NT"):
                errors.append(f"{rel}: testament muss OT oder NT sein")
            if scope == "book_group" and r.get("group") not in {g["id"] for g in (nav or {}).get("groups", [])}:
                errors.append(f"{rel}: group {r.get('group')!r} in keiner Navigationsstruktur")
            if scope == "book" and not (r.get("reference") and "." not in r["reference"]):
                errors.append(f"{rel}: scope book braucht reference = Buchcode")
            ctx = records.get(r.get("context"), (None, {}))[1]
            if ctx and ctx.get("type") != "context":
                errors.append(f"{rel}: context {r.get('context')!r} ist kein context-Datensatz")
        if r.get("type") == "navigation_structure":
            for b in r.get("books", []):
                check_ref(rel, f"books[{b.get('code')}].code", b.get("code")); ref_count += 1
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
        for i, alt in enumerate(r.get("alternatives") or []):
            check_reading(rel, f"alternatives[{i}].reading", alt.get("reading"))
            check_ref(rel, f"alternatives[{i}].reference", alt.get("reference")); ref_count += 1
            if alt.get("from_text") and alt["from_text"] not in (r.get("text_by_reference") or {}).get(alt.get("reference"), ""):
                errors.append(f"{rel}: alternatives[{i}].from_text kommt im Übersetzungstext nicht vor")
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

    # Marken im Fliesstext und Überschneidungen von Arbeitsübersetzungen
    mark_count = 0
    skip_keys = {"text_by_reference", "revision_log", "tokens", "knowledge", "source_fingerprint", "from_text", "to_text",
                 "more_literal", "other_options", "target", "grc", "title", "notes_by_reference", "readings", "entries",
                 "sources_de", "authorship_de", "method_de", "translation_notes"}

    def walk(v, path, rel):
        nonlocal mark_count
        if isinstance(v, str):
            for m in prose_refs.marks(v):
                mark_count += 1
                if not refs.is_canonical(m):
                    errors.append(f"{rel}: {path} Marke [[{m}]] ist keine kanonische Stelle")
            for u in prose_refs.unmarked(v):
                warnings.append(f"{rel}: {path} Stelle «{u}» nicht als [[…]] markiert")
        elif isinstance(v, list):
            for i, x in enumerate(v):
                walk(x, f"{path}[{i}]", rel)
        elif isinstance(v, dict):
            for k, x in v.items():
                if k not in skip_keys:
                    walk(x, f"{path}.{k}" if path else k, rel)

    prose_types = {"finding", "interpretation", "principle", "application", "open_question", "background_note", "summary", "reflection", "reception",
                   "text_unit", "localization", "alignment"}
    covered = {}
    for rid, (rel, r) in records.items():
        current_record["r"] = r
        if r.get("type") in prose_types or (r.get("type") == "translation" and r.get("translation_kind") == "literal_original_working"):
            walk(r, "", rel)
        if r.get("type") == "translation" and r.get("translation_kind") == "literal_original_working" and r.get("status") != "deprecated":
            lg = (r.get("language") or "de").split("-")[0]
            for ref in r.get("text_by_reference") or {}:
                other = covered.setdefault((lg, ref), rid)
                if other != rid:
                    errors.append(f"{rel}: {ref} ist schon in {other} ({lg}) übersetzt; Überschneidung gleicher Sprache "
                                  "(einen Datensatz auf deprecated setzen oder Bereich teilen)")

    # Quellenkatalog (source.catalog): Nutzungsrecht und Verwendung; jede Herkunftsadresse in Datensätzen muss im
    # Katalog stehen, verwendete Quellen müssen auf vorhandene Dateien zeigen (docs/QUELLEN.md, AGENTS.md).
    CAT_ENUM = {"area": {"at", "lxx", "nt", "versions", "all"},
                "layer": {"manuscripts", "editions", "language_data", "lexica", "context", "translations", "aux"},
                "rights": {"free", "sa", "nc", "ask", "prot"}, "use": {"used", "cited", "nc_planned", "not_used"}}
    catalog_urls, catalog_count = set(), 0
    for rid, (rel, r) in records.items():
        cat = r.get("catalog") if r.get("type") in ("source", "dataset") else None
        if not cat:
            continue
        catalog_count += 1
        for k, allowed in CAT_ENUM.items():
            if cat.get(k) not in allowed:
                errors.append(f"{rel}: catalog.{k} {cat.get(k)!r} nicht erlaubt")
        if not cat.get("why_de"):
            errors.append(f"{rel}: catalog.why_de fehlt (wofür verwendet bzw. weshalb nicht)")
        if cat.get("use") == "used":
            if not cat.get("used_in"):
                errors.append(f"{rel}: catalog.used_in fehlt bei verwendeter Quelle")
            for pat in cat.get("used_in", []):
                if not list(ROOT.glob(pat)):
                    errors.append(f"{rel}: catalog.used_in {pat!r} passt auf keine Datei")
        if cat.get("rights") == "nc" and cat.get("use") == "used" and any(not p.startswith("data-nc/") for p in cat.get("used_in", [])):
            errors.append(f"{rel}: nicht kommerzielle Quelle im freien Kern verwendet")
        if cat.get("rights") in ("ask", "prot") and cat.get("use") == "used":
            errors.append(f"{rel}: Quelle auf Anfrage/geschützt als verwendet markiert")
        catalog_urls.update(u.rstrip("/") for u in cat.get("urls", []))

    def provenance_urls(value, key=None):
        if isinstance(value, dict):
            for k, v in value.items():
                yield from provenance_urls(v, k)
        elif isinstance(value, list):
            for v in value:
                yield from provenance_urls(v, key)
        elif isinstance(value, str) and key in ("url", "repository", "source_url") and value.startswith("http"):
            yield value
    if catalog_count:
        missing_src = {}
        for rid, (rel, r) in records.items():
            if r.get("type") in ("source", "dataset"):
                continue
            for u in provenance_urls({k: v for k, v in r.items() if k not in ("catalog",)}):
                if u.rstrip("/") not in catalog_urls:
                    missing_src.setdefault(u, rel)
        for u, rel in sorted(missing_src.items()):
            errors.append(f"{rel}: Herkunft {u} fehlt im Quellenkatalog (data/sources/, catalog.urls)")

    for w in warnings:
        print("WARN:", w)
    if errors:
        for e in errors:
            print("FAIL:", e)
        sys.exit(f"{len(errors)} Fehler")
    print(f"PASS: {len(records)} records, {len(tags)} defined tags; schema, unique IDs, "
          f"tag/ID/reading references, {token_ref_count} token references, {ref_count} bible references, "
          f"{annotation_count} annotations, {assessment_count} assessments valid "
          f"({sum(v == 'nc' for v in layer_of.values())} records in data-nc; "
          f"{sum(r.get('type') == 'localization' for _, r in records.values())} localizations, {mark_count} Stellen-Marken, {catalog_count} Quellen im Katalog, {len(warnings)} Warnungen)")


if __name__ == "__main__":
    main()
