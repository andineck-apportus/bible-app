#!/usr/bin/env python3
"""Baut den Lesestrom (app/reading-stream/index.html) aus Vorlage und Projektdaten.

Eingebettet werden:
- Navigationsgerüst (data/navigation/NAV-PROT66-KJV.json)
- Zusammenfassungen (data/summaries/*.json)
- Studienprojektion der ausgearbeiteten Abschnitte (scripts/project_study.py)
- Hintergrundnotizen (data/background/*.json), Stellen für die Anzeige aufbereitet
- Quellen zu den Lesarten: Handschriften (data/witnesses), Zuordnungen (data/witness-readings),
  Ausgaben (data/editions) sowie Wortbedeutungen und Erklärungen aus den Übersetzungs-Alternativen

Die Vorlage app/reading-stream/template.html bearbeiten, danach dieses Skript ausführen.
Erzeugte Datei nicht von Hand ändern.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import refs  # noqa: E402
from project_study import project  # noqa: E402
import localizations  # noqa: E402

# Ausgearbeitete Abschnitte (Texteinheiten), in Lesereihenfolge der Bibel
SECTIONS = ["TU-MAT-006-005-015", "TU-MRK-003-020-035", "TU-LUK-011-001-004"]
study = project(SECTIONS)
nav = json.loads((ROOT / "data/navigation/NAV-PROT66-KJV.json").read_text(encoding="utf-8"))
sum_recs = {r["id"]: r for r in (json.loads(p.read_text(encoding="utf-8")) for p in sorted((ROOT / "data/summaries").glob("*.json")))}
bg_recs = {r["id"]: r for r in (json.loads(p.read_text(encoding="utf-8")) for p in sorted((ROOT / "data/background").glob("*.json")))}
L10N = localizations.load({**sum_recs, **bg_recs})


def i18n(rid, mapping):
    out = {}
    for lang, f in L10N.get(rid, {}).items():
        m = {dst: f[src] for src, dst in mapping.items() if src in f}
        if m:
            out[lang] = m
    return out


summaries = {}
for s in sum_recs.values():
    summaries[s["id"]] = {"text": s["text_de"], "status": s["status"], "i18n": i18n(s["id"], {"text_de": "text"})}

section_of = {}
for sec in study["sections"]:
    section_of[sec["id"]] = sec["id"]
    for part in sec["parts"]:
        section_of[part["id"]] = sec["id"]
background = []
for b in bg_recs.values():
    if b["subject"] not in section_of:
        continue  # Notiz zu einem Abschnitt, der im Lesestrom noch nicht ausgearbeitet ist
    ref = b["reference"]
    a, _, z = ref.partition("-")
    book, ch, v0 = a.split(".")
    background.append({"id": b["id"], "topic": b["topic_de"], "text": b["text_de"], "uncertain": b.get("uncertain_de"),
                       "confidence": b.get("confidence"), "subject": b["subject"], "section": section_of[b["subject"]],
                       "wide": b["subject"] == section_of[b["subject"]] and any(
                           len(sec["parts"]) > 1 for sec in study["sections"] if sec["id"] == b["subject"]),
                       "chapter": f"{book}.{ch}", "from": int(v0), "to": int((z or a).split(".")[2]),
                       "ref_de": refs.display_de(ref), "readers": "READERS" in b["context"],
                       "evidence": [refs.display_de(r) for r in b.get("evidence_refs", [])],
                       "sources": b.get("sources_de", []), "status": b["status"], "terms": b.get("terms", []),
                       "i18n": i18n(b["id"], {"topic_de": "topic", "text_de": "text", "uncertain_de": "uncertain", "terms": "terms"})})


def folder(name):
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted((ROOT / "data" / name).rglob("*.json"))]


wit_meta = {w["id"]: {k: w.get(k) for k in ("gregory_aland", "symbol", "name_de", "century", "date_de", "material_de",
                                              "languages", "location_de", "about_de", "facsimile", "catalog_url")}
            for w in folder("witnesses")}
editions = {e["id"]: {"title": e["title"], "year": e.get("year"), "about": e.get("about_de")} for e in folder("editions")}
wanted = set()
alt_extra = {}  # je Sprachschicht: {"de": {Variante: …}, "gsw": {…}}
for t in folder("translations"):
    lang = (t.get("language") or "de").split("-")[0]
    for a in t.get("alternatives", []):
        vid = a["reading"].split(":")[0]
        if "readings_de" in a:
            alt_extra.setdefault(lang, {})[vid] = {"words": a["readings_de"], "origin": a.get("origin_de", []), "related": a.get("related_variants", [])}
        wanted.add(vid)
        wanted.update(a.get("related_variants", []))
wit_readings = {}
for ws in folder("witness-readings"):
    for e in ws["entries"]:
        if e["variant"] in wanted:
            wit_readings.setdefault(e["variant"], []).append(
                {k: e[k] for k in ("source", "hand", "result", "witness_text", "damaged", "supplied", "note_de") if k in e})
variants_extra = {}
for v in folder("variants"):
    if v["id"] in wanted:
        variants_extra[v["id"]] = {"ref": v["reference"], "readings": [{"id": r["reading_id"], "text": r["text"],
                                   "editions": r.get("editions", []), "reported": r.get("witnesses_reported", [])} for r in v["readings"]]}
sources_payload = {"witnesses": wit_meta, "editions": editions, "readings": wit_readings, "alts": alt_extra,
                   "variants": variants_extra,
                   "attribution": "Handschriftentexte: Alan Bunning, Center for New Testament Restoration, Electronic Transcriptions (CC BY-SA 4.0), github.com/Center-for-New-Testament-Restoration/transcriptions. Zuordnung zu den Lesarten maschinell (METHOD-AUTO-COLLATION-V1), nicht am Faksimile geprüft."}

# Querverweise (OpenBible.info, CC BY) für alle Verse der ausgearbeiteten Kapitel, je Vers die bestbewerteten
xref_chapters = {".".join(sec["range"].split("-")[0].split(".")[:2]) for sec in study["sections"]}
crossrefs = {}
for ch in sorted(xref_chapters):
    book = ch.split(".")[0]
    rec = json.loads((ROOT / f"data/crossrefs/XREF-OPENBIBLE-{book}.json").read_text(encoding="utf-8"))
    for frm, items in rec["entries"].items():
        if frm.startswith(ch + "."):
            crossrefs[frm] = [[t, v] for t, v, *_ in items if v > 0][:10]
refbooks = [[code, de, more] for code, de, more in refs.BOOKS]

template = (ROOT / "app/reading-stream/template.html").read_text(encoding="utf-8")
dump = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
for marker, payload in (("/*__STUDY__*/null", study), ("/*__NAV__*/null", nav), ("/*__SUMMARIES__*/null", summaries),
                        ("/*__BACKGROUND__*/null", background), ("/*__SOURCES__*/null", sources_payload), ("/*__XREF__*/null", {"verses": crossrefs, "books": refbooks,
                         "attribution": "Querverweise: OpenBible.info (CC BY), nach Stimmen der Nutzer sortiert; keine fachliche Prüfung."})):
    assert template.count(marker) == 1, marker
    template = template.replace(marker, dump(payload))
(ROOT / "app/reading-stream/index.html").write_text(template, encoding="utf-8")
print(f"PASS: Lesestrom gebaut: {len(nav['books'])} Bücher, {len(summaries)} Zusammenfassungen, {len(background)} Hintergrundnotizen, ausgearbeitet: {', '.join(refs.display_de(x['range']) for x in study['sections'])}.")
