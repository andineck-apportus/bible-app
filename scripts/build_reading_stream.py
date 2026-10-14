#!/usr/bin/env python3
"""Baut den Lesestrom (app/reading-stream/index.html) aus Vorlage und Projektdaten.

Eingebettet werden:
- Navigationsgerüst (data/navigation/NAV-PROT66-KJV.json)
- Zusammenfassungen (data/summaries/*.json)
- Studienprojektion der ausgearbeiteten Abschnitte (scripts/project_study.py)
- Hintergrundnotizen (data/background/*.json), Stellen für die Anzeige aufbereitet
- Quellen zu den Lesarten: Handschriften (data/witnesses), Zuordnungen (data/witness-readings),
  Ausgaben (data/editions) sowie Wortbedeutungen und Erklärungen aus den Übersetzungs-Alternativen
- Wörterbuch-Einträge (data/lexica: UBS, STEPBible TBESG/TBESH), Ausgaben je Wort (STEPBible TAGNT) und
  Ketiv/Qere (STEPBible TAHOT) aus data/tagged-alignments, je Buch in den Paketen b/<BUCH>

Die Vorlage app/reading-stream/template.html bearbeiten, danach dieses Skript ausführen.
Erzeugte Datei nicht von Hand ändern.
"""
import base64
import gzip
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import refs  # noqa: E402
from project_study import project  # noqa: E402
import localizations  # noqa: E402

# Ausgearbeitete Abschnitte ergeben sich aus den Daten (Texteinheiten mit Arbeitsübersetzung), in Bibelreihenfolge
study = project()
nav = json.loads((ROOT / "data/navigation/NAV-PROT66-KJV.json").read_text(encoding="utf-8"))
sum_recs = {r["id"]: r for r in (json.loads(p.read_text(encoding="utf-8")) for p in sorted((ROOT / "data/summaries").glob("*.json")))}
bg_recs = {r["id"]: r for r in (json.loads(p.read_text(encoding="utf-8")) for p in sorted((ROOT / "data/background").rglob("*.json")))}
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
overview = []  # Hintergrund der oberen Ebenen (Bibel, Testament, Buchgruppe, Buch)
for b in bg_recs.values():
    if b.get("scope") in ("bible", "testament", "book_group", "book"):
        overview.append({"id": b["id"], "scope": b["scope"], "testament": b.get("testament"), "group": b.get("group"),
                         "book": b.get("reference") if b["scope"] == "book" else None,
                         "topic": b["topic_de"], "text": b["text_de"], "uncertain": b.get("uncertain_de"),
                         "confidence": b.get("confidence"), "chapter": "", "ref_de": "", "readers": False,
                         "evidence": [refs.display_de(r) for r in b.get("evidence_refs", [])],
                         "sources": b.get("sources_de", []), "status": b["status"], "terms": b.get("terms", []),
                         "i18n": i18n(b["id"], {"topic_de": "topic", "text_de": "text", "uncertain_de": "uncertain", "terms": "terms"})})
        continue
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
        if "readings" in a:
            alt_extra.setdefault(lang, {})[vid] = {"words": a["readings"], "origin": a.get("origin", []), "related": a.get("related_variants", [])}
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

xref_payload = {"verses": crossrefs, "books": refbooks,
                "attribution": "Querverweise: OpenBible.info (CC BY), nach Stimmen der Nutzer sortiert; keine fachliche Prüfung."}

# ---------------------------------------------------------------- Aufteilung in Kern und Pakete
# Kern (immer in index.html): Gerüst, Navigation, Abschnitte (hochdeutsche Titel), Sprachschichten ohne Inhalt,
# hochdeutsche Zusammenfassungen, Quellenbeschreibungen. Pakete (nachladbar, gzip):
#   b/<BUCH>        sprachunabhängig: griechische Wörter, Varianten, Befunde/Deutungen/… (Original), Hintergrund,
#                   Querverweise, Handschriften-Zuordnungen, Wörterbuch-Einträge (lex), Ketiv/Qere (ketiv, kq_only),
#                   Wörter anderer Ausgaben (ed_extra)
#   l/<Sprache>/<BUCH>   Übersetzungsschicht des Buchs, Vergleichsübersetzungen dieser Sprache, Lesarten-Erklärungen,
#                   Lokalisierungen der Objekte des Buchs
#   l/<Sprache>/common   Lokalisierte Titel/Zusammenfassungen der Abschnitte und aller Zusammenfassungen
# So wächst nichts mit der Zahl der Sprachen oder Bücher, was nicht gebraucht wird.
book_of_id = {}
for sec in study["sections"]:
    b = sec["range"].split(".")[0]
    book_of_id[sec["id"]] = b
    for part in sec["parts"]:
        book_of_id[part["id"]] = b
ref_book = lambda r: (r or "").split(".")[0]
word_book = {w["id"]: ref_book(w["ref"]) for w in study["words"]}
bundles = {}


def bundle(name):
    return bundles.setdefault(name, {})


langs = study["layer_order"]
core_layers = {}
for lg, L in study["layers"].items():
    core_layers[lg] = {k: L[k] for k in ("lang", "label", "orthography", "register", "review", "compare_languages")}
    core_layers[lg].update({"text": {}, "source": {}, "decisions": {}, "alternatives": [], "align": {}})
    for key in ("text", "source", "decisions"):
        for r, v in L[key].items():
            bundle(f"l/{lg}/{ref_book(r)}").setdefault("layer", {}).setdefault(key, {})[r] = v
    for a in L["alternatives"]:
        bundle(f"l/{lg}/{ref_book(a['ref'])}").setdefault("layer", {}).setdefault("alternatives", []).append(a)
    for t, v in L["align"].items():
        bundle(f"l/{lg}/{word_book[t]}").setdefault("layer", {}).setdefault("align", {})[t] = v
for r, items in study["compare"].items():
    for c in items:
        bundle(f"l/{c['lang']}/{ref_book(r)}").setdefault("compare", {}).setdefault(r, []).append(c)
for lg, alts in sources_payload["alts"].items():
    for vid, x in alts.items():
        bundle(f"l/{lg}/{ref_book(variants_extra[vid]['ref'])}").setdefault("alts", {})[vid] = x
for key in ("words", "variants"):
    for x in study[key]:
        bundle(f"b/{ref_book(x['ref'])}").setdefault(key, []).append(x)
# Wörterbuch-Einträge, Ketiv/Qere und Ausgabenbefund (STEPBible, UBS) nur im Paket des Buchs, dessen Wörter sie brauchen
for w in study["words"]:
    b = bundle(f"b/{ref_book(w['ref'])}")
    for k in (w.get("lx") or {}).values():
        if isinstance(k, str):
            b.setdefault("lex", {})[k] = study["lexicon"][k]
    if w.get("kq"):
        b.setdefault("ketiv", {})[w["kq"]] = study["ketiv"][w["kq"]]
for key, dst in (("ed_extra", "ed_extra"), ("ketiv_only", "kq_only")):
    for r, v in study[key].items():
        bundle(f"b/{ref_book(r)}").setdefault(dst, {})[r] = v
for key in ("findings", "interpretations", "principles", "applications", "questions"):
    for x in study[key]:
        b = book_of_id[x["subject"]]
        x = dict(x)
        for lg, f in (x.pop("i18n", None) or {}).items():
            bundle(f"l/{lg}/{b}").setdefault("i18n", {})[x["id"]] = f
        bundle(f"b/{b}").setdefault(key, []).append(x)
for x in study["relations"]:
    bundle(f"b/{book_of_id[x['from']]}").setdefault("relations", []).append(x)
for x in background:
    b = x["chapter"].split(".")[0]
    x = dict(x)
    for lg, f in (x.pop("i18n", None) or {}).items():
        bundle(f"l/{lg}/{b}").setdefault("i18n", {})[x["id"]] = f
    bundle(f"b/{b}").setdefault("bg", []).append(x)
for x in overview:
    x = dict(x)
    for lg, f in (x.pop("i18n", None) or {}).items():
        bundle(f"l/{lg}/common").setdefault("i18n", {})[x["id"]] = f
    bundle("b/_overview").setdefault("bg", []).append(x)
for r, v in crossrefs.items():
    bundle(f"b/{ref_book(r)}").setdefault("xref", {})[r] = v
for vid, rows in wit_readings.items():
    bundle(f"b/{ref_book(variants_extra[vid]['ref'])}").setdefault("readings", {})[vid] = rows
for vid, v in variants_extra.items():
    bundle(f"b/{ref_book(v['ref'])}").setdefault("src_variants", {})[vid] = v
# Bildsprache (docs/BILDSPRACHE.md): Bildlexikon (Namen, Merkmale) und Stile (Darstellungen, Bausteinbibliothek) im Kern;
# Bilder samt Bildauftrag (Felder, Deutungshinweis) im Paket ihres Buchs (Buchebene in b/_overview).
# Schlüssel im Lesestrom: Bibel, Testamente, Buchgruppen = ID der Zusammenfassung; Buch «JHN», Kapitel «JHN.2», Abschnitt = ID der Texteinheit.
import localizations as _l10n  # noqa: E402
ill_recs = {}
for p in sorted((ROOT / "data/illustrations").rglob("*.json")):
    r = json.loads(p.read_text(encoding="utf-8"))
    if r.get("status") != "deprecated":
        ill_recs[r["id"]] = r
ill_core = {"styles": {}, "items": {}, "lexicon": {}}
for rid, r in ill_recs.items():
    if r["type"] == "figure":
        ill_core["lexicon"][rid] = {"kind": r["kind"], "name": r["names"], "traits": [t["trait_de"] for t in r.get("traits", [])]}
    elif r["type"] == "illustration_style":
        ill_core["styles"][r["key"]] = {"id": rid, "label": r["labels"], "description": r.get("description_de"),
                                        "renderings": r.get("renderings", {}), "library": (ROOT / r["library"]).read_text(encoding="utf-8")}
ill_l10n = _l10n.load(ill_recs)
for rid, r in ill_recs.items():
    if r["type"] != "illustration":
        continue
    st, br = ill_recs[r["style"]], ill_recs[r["brief"]]
    key = r["target"] if r["level"] in ("section", "bible", "testament", "group") else r["reference"]
    item = {"id": rid, "brief": br["id"], "style": st["key"], "level": r["level"], "ref": r.get("reference"), "depicts": r.get("depicts", []),
            "alt": r["alt_de"], "note": br.get("interpretation_note_de"), "check": (r.get("check") or {}).get("result_de"),
            "panels": [{"n": p_["n"], "ref": p_["reference"], "action": p_["action_de"]} for p_ in br["panels"]],
            "svg": (ROOT / r["file"]).read_text(encoding="utf-8").strip()}
    bname = "b/_overview" if r["level"] in ("bible", "testament", "group", "book") else f"b/{ref_book(r['reference'])}"
    bundle(bname).setdefault("ill", {}).setdefault(key, {})[st["key"]] = item
    for lg, f in ill_l10n.get(rid, {}).items():
        if "alt_de" in f:
            bundle(f"l/{lg}/common").setdefault("i18n", {}).setdefault(rid, {})["alt"] = f["alt_de"]
    for lg, f in ill_l10n.get(br["id"], {}).items():
        m = {}
        if "interpretation_note_de" in f:
            m["note"] = f["interpretation_note_de"]
        if "actions_de" in f:
            m["actions"] = f["actions_de"]
        if m:
            bundle(f"l/{lg}/common").setdefault("i18n", {}).setdefault(rid, {}).update(m)
core_sums = {}
for sid, x in summaries.items():
    for lg, f in (x.get("i18n") or {}).items():
        bundle(f"l/{lg}/common").setdefault("i18n", {})[sid] = f
    core_sums[sid] = {"text": x["text"], "status": x["status"]}
core_sections = []
for sec in study["sections"]:
    def strip(u):
        for lg in set(u["titles"]) | set(u["summaries"]):
            if lg == "de":
                continue
            f = {k: v for k, v in (("title", u["titles"].get(lg)), ("summary", u["summaries"].get(lg))) if v}
            if f:
                bundle(f"l/{lg}/common").setdefault("i18n", {})[u["id"]] = f
        return {**{k: v for k, v in u.items() if k not in ("titles", "summaries", "parts")},
                "titles": {"de": u["titles"]["de"]}, "summaries": {"de": u["summaries"]["de"]}}
    core_sections.append({**strip(sec), "parts": [strip(p) for p in sec["parts"]]})
for name, d in bundles.items():
    kind, *rest = name.split("/")
    d["name"] = name
    if kind == "l":
        d["lang"] = rest[0]
    else:
        d["book"] = rest[0]

core_study = {"built_from": study["built_from"], "sections": core_sections, "layers": core_layers, "layer_order": langs,
              "compare": {}, "words": [], "variants": [], "findings": [], "interpretations": [], "principles": [],
              "applications": [], "relations": [], "questions": [], "method": study["method"], "editions": study["editions"],
              "lexicon": {}, "ketiv": {}, "ketiv_only": {}, "ed_extra": {}}
core_src = {k: v for k, v in sources_payload.items() if k not in ("readings", "alts", "variants")}
core_src.update({"readings": {}, "alts": {lg: {} for lg in langs}, "variants": {}})
core_xref = {**xref_payload, "verses": {}}
# Nicht kommerzielle Studienschicht (data-nc/): eigene Pakete n/<BUCH>, nie mit Kernpaketen vermischt.
# BIBLE_APP_NO_NC=1 baut ohne diese Schicht (z. B. für eine Nutzung ausserhalb des gemeinnützigen Betriebs).
import os  # noqa: E402
if not os.environ.get("BIBLE_APP_NO_NC"):
    nc_wit = {}
    for p in sorted((ROOT / "data-nc/witnesses").glob("WIT-DSS-*.json")):
        w = json.loads(p.read_text(encoding="utf-8"))
        nc_wit[w["id"]] = {"name": w.get("name_de"), "place": w.get("location_de"), "date": w.get("date_de")}
    for p in sorted((ROOT / "data-nc/witness-texts").glob("DSS-*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        w = nc_wit.get(d["witness"], {})
        for ref, v in d["verses"].items():
            b = bundle(f"n/{ref_book(ref)}")
            b.setdefault("nc", {"license": d["source"]["license"], "attribution": d["source"]["attribution"],
                                "method": d["comparison_method_de"]})
            b.setdefault("dss", {}).setdefault(ref, []).append({"id": d["id"], "name": w.get("name"), "place": w.get("place"),
                                                               "loc": v["loc"], "words": v["words"]})
manifest = {"books": sorted({n.split("/")[1] for n in bundles if n.startswith("b/")}),
            "nc": sorted({n.split("/")[1] for n in bundles if n.startswith("n/")}),
            "lang": {lg: sorted(n.split("/")[2] for n in bundles if n.startswith(f"l/{lg}/")) for lg in langs}}

sys.path.insert(0, str(ROOT / "scripts"))
from build_source_map import catalog as _catalog  # noqa: E402
catalog = [{k: v for k, v in s.items() if k != "checked"} for s in _catalog()]
template = (ROOT / "app/reading-stream/template.html").read_text(encoding="utf-8")
dump = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def page(inline):
    t = template
    for marker, payload in (("/*__STUDY__*/null", core_study), ("/*__NAV__*/null", nav), ("/*__SUMMARIES__*/null", core_sums),
                            ("/*__BACKGROUND__*/null", []), ("/*__SOURCES__*/null", core_src), ("/*__XREF__*/null", core_xref),
                            ("/*__MANIFEST__*/null", manifest), ("/*__INLINE__*/null", inline), ("/*__CATALOG__*/null", catalog), ("/*__ILL__*/null", ill_core)):
        assert t.count(marker) == 1, marker
        t = t.replace(marker, dump(payload))
    return t


# Einzeldatei (offline, Tests): alle Pakete eingebettet
(ROOT / "app/reading-stream/index.html").write_text(page(bundles), encoding="utf-8")
# Aufgeteilte Fassungen zum Veröffentlichen (deterministisches gzip):
#   build/reading-stream/        Pakete als .json.gz (übliche Webserver)
#   build/reading-stream-txt/    Pakete als gzip in Base64 (.gz.txt) für Hosts, die keine Binärdateien ausliefern
sizes = {}
for folder, ext in (("reading-stream", ".json.gz"), ("reading-stream-txt", ".gz.txt")):
    out = ROOT / "build" / folder
    out.mkdir(parents=True, exist_ok=True)
    manifest["ext"] = ext
    (out / "index.html").write_text(page(None), encoding="utf-8")
    for name, d in bundles.items():
        raw = json.dumps(d, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        gz = gzip.compress(raw, compresslevel=9, mtime=0)
        f = out / f"{name}{ext}"
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_bytes(gz if ext.endswith(".gz") else base64.b64encode(gz) + b"\n")
        sizes[name] = (len(raw), len(gz))
    (out / "manifest.json").write_text(json.dumps({"ext": ext, "bundles": {k: {"bytes": a, "gzip": b} for k, (a, b) in sorted(sizes.items())}},
                                                  ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
manifest.pop("ext")
out = ROOT / "build/reading-stream"
print(f"PASS: Lesestrom gebaut: {len(nav['books'])} Bücher, {len(summaries)} Zusammenfassungen, {len(background)} Hintergrundnotizen zu Abschnitten, {len(overview)} zu oberen Ebenen, "
      f"ausgearbeitet: {', '.join(refs.display_de(x['range']) for x in study['sections'])}; "
      f"{len(bundles)} Pakete ({sum(b for _, b in sizes.values()) // 1024} KB gzip, Kern {len((out / 'index.html').read_bytes()) // 1024} KB).")
