#!/usr/bin/env python3
"""Migration v0.30 -> v0.31 (2026-10-13): Daten für viele Sprachen und die ganze Bibel vorbereiten.

1. Übersetzungsschichten (translation mit translation_kind = literal_original_working) und Wortzuordnungen:
   Felder, deren Inhalt in der Zielsprache der Schicht steht, bekommen sprachneutrale Namen
   (de_from -> from_text, de_to -> to_text, note_de -> note, readings_de -> readings mit {grc, text, note},
   origin_de -> origin, more_literal_de -> more_literal, other_options_de -> other_options,
   alternatives_origin_note_de -> alternatives_origin_note). Dokumentationsfelder für das Team
   (method_de, authorship_de, review_de, *_note_de auf Datensatzebene …) bleiben Hochdeutsch mit _de.
2. Titel und Zusammenfassungen der Texteinheiten je Sprache (title_by_language, summary_by_language)
   wandern in eigene Lokalisierungen (data/localizations/<Sprache>/<ID>.json).
3. Bibelstellen im Fliesstext werden zu sprachneutralen Marken [[MAT.6.34]] (scripts/prose_refs.py).
   Lokalisierungen, die vor der Migration aktuell waren, bekommen den neuen Fingerabdruck ihres Originals
   (reine Formatänderung, Inhalt unverändert).

Jede Änderung steht mit altem und neuem Wert in provenance/migrations/2026-10-13-v0.31.json.
Idempotent: ein zweiter Lauf ändert nichts.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import localizations  # noqa: E402
import prose_refs  # noqa: E402

D = ROOT / "data"
LOG = ROOT / "provenance" / "migrations" / "2026-10-13-v0.31.json"
DATE = "2026-10-13"
changes = []
files = {}  # Pfad -> Datensatz (geändert)


def load_all():
    out = {}
    for p in sorted(D.rglob("*.json")):
        out[p] = json.loads(p.read_text(encoding="utf-8"))
    return out


recs = load_all()
by_id = {r["id"]: (p, r) for p, r in recs.items()}


def log(path, field, old, new, reason):
    changes.append({"file": str(path.relative_to(ROOT)), "field": field, "old": old, "new": new, "reason": reason})
    files[path] = recs.get(path) or files.get(path)


def note_revision(rec, text):
    lg = rec.setdefault("revision_log", [])
    if not any(x.get("change_de") == text and x.get("date") == DATE for x in lg):
        lg.append({"date": DATE, "change_de": text, "reason_de": "Migration v0.31: Daten für viele Sprachen und die ganze Bibel",
                   "migration": "scripts/migrations/v0_31.py"})


# Stand der Lokalisierungen vor der Migration: welche Felder waren aktuell?
current_before = {}
for p, r in recs.items():
    if r.get("type") == "localization" and r["localizes"] in by_id:
        orig = by_id[r["localizes"]][1]
        stale = set(localizations.stale_fields(r, orig))
        current_before[p] = [k for k in r["fields"] if k not in stale]

# ---------------------------------------------------------------- 1. neutrale Feldnamen
RENAME_ALT = {"de_from": "from_text", "de_to": "to_text", "note_de": "note", "origin_de": "origin"}
RENAME_DEC = {"more_literal_de": "more_literal", "other_options_de": "other_options", "note_de": "note"}
R1 = "Inhalt in der Sprache der Schicht: sprachneutraler Feldname"
for p, r in recs.items():
    if r.get("type") == "translation" and r.get("translation_kind") == "literal_original_working":
        changed = False
        for i, a in enumerate(r.get("alternatives", [])):
            for old, new in RENAME_ALT.items():
                if old in a:
                    log(p, f"alternatives[{i}].{old}", old, new, R1)
                    a[new] = a.pop(old); changed = True
            if "readings_de" in a:
                rd = {k: [{"grc": w["grc"], "text": w["de"], **({"note": w["note_de"]} if w.get("note_de") else {})} for w in v]
                      for k, v in a.pop("readings_de").items()}
                log(p, f"alternatives[{i}].readings_de", "readings_de{grc,de,note_de}", "readings{grc,text,note}", R1)
                a["readings"] = rd; changed = True
            # Reihenfolge der Schlüssel stabil halten
            r["alternatives"][i] = {k: a[k] for k in ["reading", "reference", "from_text", "to_text", "effect", "note", "readings",
                                                       "origin", "related_variants"] if k in a} | {k: v for k, v in a.items()}
        for i, d in enumerate(r.get("decisions", [])):
            for old, new in RENAME_DEC.items():
                if old in d:
                    log(p, f"decisions[{i}].{old}", old, new, R1)
                    d[new] = d.pop(old); changed = True
        if "alternatives_origin_note_de" in r:
            log(p, "alternatives_origin_note_de", "alternatives_origin_note_de", "alternatives_origin_note", R1)
            r["alternatives_origin_note"] = r.pop("alternatives_origin_note_de"); changed = True
        if changed:
            note_revision(r, "Feldnamen der Inhalte in der Zielsprache sprachneutral (from_text, to_text, note, readings, origin, more_literal, other_options); Werte unverändert")
    if r.get("type") == "alignment":
        changed = False
        for i, a in enumerate(r.get("alignments", [])):
            if "note_de" in a:
                log(p, f"alignments[{i}].note_de", "note_de", "note", R1)
                a["note"] = a.pop("note_de"); changed = True
        if changed:
            note_revision(r, "Anmerkungen der Zuordnungen als note (sprachneutral); Werte unverändert")

# ---------------------------------------------------------------- 2. Titel der Texteinheiten -> Lokalisierungen
CODE = {"gsw-u-sd-chzh": "GSW-ZH"}
for p, r in list(recs.items()):
    if r.get("type") != "text_unit":
        continue
    tbl, sbl = r.get("title_by_language") or {}, r.get("summary_by_language") or {}
    if not tbl and not sbl:
        continue
    for lang in sorted(set(tbl) | set(sbl)):
        fields = {}
        if lang in tbl:
            fields["title"] = tbl[lang]
        if lang in sbl:
            fields["summary_de"] = sbl[lang]
        out = D / "localizations" / lang / f"{r['id']}.json"
        ctx = next((x["id"] for x in recs.values() if x.get("type") == "context" and lang in (x.get("language_context") or [])), None)
        loc = {"id": f"L10N-{CODE.get(lang, lang.upper())}-{r['id']}", "type": "localization", "status": r.get("status", "draft"),
               "tags": [], "localizes": r["id"], "language": lang, "target_context": ctx, "fields": fields,
               "source_fingerprint": {k: localizations.fingerprint(r.get(k)) for k in fields},
               "authorship_de": r.get("by_language_authorship_de") or "Übernommen aus title_by_language/summary_by_language.",
               "review_de": "Noch keine muttersprachliche Prüfung dokumentiert.",
               "knowledge": {"asserted_at": DATE, "supersedes": None},
               "revision_log": [{"date": DATE, "change_de": f"Aus {r['id']} (title_by_language/summary_by_language) übernommen; Text unverändert",
                                 "migration": "scripts/migrations/v0_31.py"}]}
        if not loc["target_context"]:
            del loc["target_context"]
        recs[out] = loc
        files[out] = loc
        current_before[out] = list(fields)
        log(out, "(neu)", None, fields, "Titel/Zusammenfassung je Sprache als eigene Lokalisierung")
    for k in ("title_by_language", "summary_by_language", "by_language_authorship_de"):
        if k in r:
            log(p, k, r[k], None, "in Lokalisierung verschoben")
            del r[k]
    note_revision(r, "title_by_language/summary_by_language in Lokalisierungen (data/localizations) verschoben")

by_id = {r["id"]: (p, r) for p, r in recs.items()}

# ---------------------------------------------------------------- 3. Bibelstellen im Fliesstext -> Marken
PROSE_TYPES = {"finding", "interpretation", "principle", "application", "open_question", "background_note", "summary", "text_unit"}
DOC_KEYS = {"authorship_de", "review_de", "summary_authorship_de", "i18n_authorship_de", "language_label_de", "language_name_de",
            "orthography_de", "register_de", "method_de", "coverage_de", "target_convention_de", "name_de"}


def book_of(rec):
    """Buch für Stellen ohne Buchangabe."""
    t = rec.get("type")
    if t == "localization":
        orig = by_id.get(rec["localizes"])
        return book_of(orig[1]) if orig else None
    if t == "summary":
        parts = rec["id"].split("-")
        return parts[2] if parts[1] in ("BOOK", "CH") else None
    for k in ("reference", "range"):
        if rec.get(k):
            return rec[k].split(".")[0]
    subj = rec.get("subject")
    if subj and subj in by_id:
        return book_of(by_id[subj][1])
    for x in rec.get("derived_from", []):
        if x in by_id:
            b = book_of(by_id[x][1])
            if b:
                return b
    if rec.get("principle") in by_id:
        return book_of(by_id[rec["principle"]][1])
    return None


def mark_value(v, ctx, path, field):
    if isinstance(v, str):
        new, ch = prose_refs.mark(v, ctx)
        if ch:
            log(path, field, v, new, "Bibelstellen im Fliesstext als Marken [[…]]")
        return new
    if isinstance(v, list):
        return [mark_value(x, ctx, path, f"{field}[{i}]") for i, x in enumerate(v)]
    return v


for p, r in list(recs.items()):
    t = r.get("type")
    before = json.dumps(r, ensure_ascii=False, sort_keys=True)
    ctx = book_of(r)
    if t in PROSE_TYPES:
        for k in list(r):
            if k.endswith("_de") and k not in DOC_KEYS and k != "sources_de":
                r[k] = mark_value(r[k], ctx, p, k)
        for i, tm in enumerate(r.get("terms") or []):
            if tm.get("de"):
                tm["de"] = mark_value(tm["de"], None, p, f"terms[{i}].de")
    elif t == "localization":
        for k in list(r["fields"]):
            if k != "title":
                r["fields"][k] = mark_value(r["fields"][k], ctx if k != "terms" else None, p, f"fields.{k}")
    elif t == "alignment":
        for i, a in enumerate(r.get("alignments", [])):
            if "note" in a:
                a["note"] = mark_value(a["note"], (a.get("reference") or r.get("reference") or "").split(".")[0] or None, p, f"alignments[{i}].note")
    elif t == "translation" and r.get("translation_kind") == "literal_original_working":
        for i, a in enumerate(r.get("alternatives", [])):
            c = a["reference"].split(".")[0]
            for k in ("note", "origin"):
                if k in a:
                    a[k] = mark_value(a[k], c, p, f"alternatives[{i}].{k}")
            for rid, ws in (a.get("readings") or {}).items():
                for j, w in enumerate(ws):
                    if "note" in w:
                        w["note"] = mark_value(w["note"], c, p, f"alternatives[{i}].readings.{rid}[{j}].note")
        for i, d in enumerate(r.get("decisions", [])):
            if "note" in d:
                d["note"] = mark_value(d["note"], d["reference"].split(".")[0], p, f"decisions[{i}].note")
        if "alternatives_origin_note" in r:
            r["alternatives_origin_note"] = mark_value(r["alternatives_origin_note"], None, p, "alternatives_origin_note")
    if json.dumps(r, ensure_ascii=False, sort_keys=True) != before:
        files[p] = r
        if t != "localization":
            note_revision(r, "Bibelstellen im Fliesstext als sprachneutrale Marken [[…]]; Inhalt unverändert")

# Gezielte Korrekturen nach Durchsicht (Stellen ohne Einleitungswort; fremde Werke nicht als Bibelstelle)
FIXES = [
    ("BG-MRK-0008", "Tobit ([[MRK.8.3]])", "Tobit ([[TOB.8.3]])"),
    ("TRANS-MAT-006-005-015-DE-WORKING", "Lukas ([[MAT.11.4]]", "Lukas ([[LUK.11.4]]"),
    ("TRANS-MAT-006-005-015-GSW-ZH-WORKING", "Lukas ([[MAT.11.4]]", "Lukas ([[LUK.11.4]]"),
    ("TRANS-MAT-006-005-015-GSW-ZH-WORKING", "wiederholt 6,14.", "wiederholt [[MAT.6.14]]."),
    ("INT-LP-0001", "das 6,34 verlangt", "das [[MAT.6.34]] verlangt"),
    ("INT-LP-0001", "wo 6,34 verlangt", "wo [[MAT.6.34]] verlangt"),
    ("FIND-MRK-0004", "; 3,23–27 ", "; [[MRK.3.23-MRK.3.27]] "),
    ("FIND-MRK-0004", " und 3,28–30", " und [[MRK.3.28-MRK.3.30]]"),
    ("INT-MRK-0003", ", 3,21)", ", [[MRK.3.21]])"),
    ("INT-MRK-0003", ", 3,22)", ", [[MRK.3.22]])"),
    ("INT-MRK-0003", ". 3,35 ", ". [[MRK.3.35]] "),
    ("TRANS-MRK-003-022-030-DE-WORKING", "könnten 3,25 ", "könnten [[MRK.3.25]] "),
    ("TRANS-MRK-003-020-035-GSW-ZH-WORKING", "chönnted 3,25 ", "chönnted [[MRK.3.25]] "),
    ("TU-LUK-011-001-004", "nur 11,1–4 ", "nur [[LUK.11.1-LUK.11.4]] "),
]


def fix_value(v, rid, path, field):
    if isinstance(v, str):
        new = v
        for fid, old, rep in FIXES:
            if fid == rid and old in new:
                new = new.replace(old, rep)
        if new != v:
            log(path, field, v, new, "Bibelstelle nach Durchsicht korrigiert/markiert")
        return new
    if isinstance(v, list):
        return [fix_value(x, rid, path, f"{field}[{i}]") for i, x in enumerate(v)]
    if isinstance(v, dict):
        return {k: (fix_value(x, rid, path, f"{field}.{k}") if k not in ("revision_log", "source_fingerprint") else x) for k, x in v.items()}
    return v


fix_ids = {f[0] for f in FIXES}
for p, r in list(recs.items()):
    rid = r.get("localizes") if r.get("type") == "localization" else r.get("id")
    if rid not in fix_ids:
        continue
    before = json.dumps(r, ensure_ascii=False, sort_keys=True)
    for k in list(r):
        if k not in ("id", "revision_log", "source_fingerprint", "text_by_reference", "knowledge"):
            r[k] = fix_value(r[k], rid, p, k)
    if json.dumps(r, ensure_ascii=False, sort_keys=True) != before:
        files[p] = r
        if r.get("type") != "localization":
            note_revision(r, "Bibelstellen im Fliesstext als sprachneutrale Marken [[…]]; Inhalt unverändert")

# Fingerabdrücke der vor der Migration aktuellen Lokalisierungen nachführen
for p, keys in current_before.items():
    r = recs[p]
    orig = by_id.get(r["localizes"], (None, None))[1]
    if orig is None:
        continue
    upd = {k: localizations.fingerprint(orig.get(k) if k != "terms" else orig.get(k)) for k in keys}
    if any(r["source_fingerprint"].get(k) != v for k, v in upd.items()):
        log(p, "source_fingerprint", {k: r["source_fingerprint"].get(k) for k in upd}, upd,
            "Original nur im Format geändert (Marken, Feldnamen); Übersetzung war aktuell")
        r["source_fingerprint"].update(upd)
        files[p] = r
    if p in files:
        note_revision(r, "Migration v0.31: Bibelstellen als Marken [[…]], Fingerabdruck nach Formatänderung des Originals nachgeführt; Übersetzung inhaltlich unverändert")

for p, r in files.items():
    p.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(r, ensure_ascii=False, indent=2) + "\n"
    if not p.exists() or p.read_text(encoding="utf-8") != text:
        p.write_text(text, encoding="utf-8")

if changes:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    prev = json.loads(LOG.read_text(encoding="utf-8"))["changes"] if LOG.exists() else []
    LOG.write_text(json.dumps({"migration": "v0.31", "date": DATE, "script": "scripts/migrations/v0_31.py",
                               "note": __doc__.strip().splitlines()[0], "changes": prev + changes},
                              ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"{len(changes)} Änderungen" + (f", Protokoll: {LOG.relative_to(ROOT)}" if changes else " (bereits migriert)"))
