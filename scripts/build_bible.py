#!/usr/bin/env python3
"""Baut die App (app/bible/index.html) aus Vorlage und Projektdaten.

Eingebettet werden:
- Navigationsgerüst (data/navigation/NAV-PROT66-KJV.json)
- Zusammenfassungen (data/summaries/*.json)
- Studienprojektion der ausgearbeiteten Abschnitte (scripts/project_study.py)
- Hintergrundnotizen (data/background/*.json), Stellen für die Anzeige aufbereitet
- Quellen zu den Lesarten: Handschriften (data/witnesses), Zuordnungen (data/witness-readings),
  Ausgaben (data/editions) sowie Wortbedeutungen und Erklärungen aus den Übersetzungs-Alternativen
- Wörterbuch-Einträge (data/lexica: UBS, STEPBible TBESG/TBESH), Ausgaben je Wort (STEPBible TAGNT) und
  Ketiv/Qere (STEPBible TAHOT) aus data/tagged-alignments, je Buch in den Paketen b/<BUCH>

Die Vorlage app/bible/template.html bearbeiten, danach dieses Skript ausführen.
Erzeugte Datei nicht von Hand ändern.
"""
import base64
import gzip
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import refs  # noqa: E402
from project_study import project  # noqa: E402
import localizations  # noqa: E402

# Ausgearbeitete Abschnitte ergeben sich aus den Daten (Texteinheiten mit Arbeitsübersetzung), in Bibelreihenfolge
study = project()
nav = json.loads((ROOT / "data/navigation/NAV-PROT66-KJV.json").read_text(encoding="utf-8"))
nav_counts = {b["code"]: b["verses_per_chapter"] for b in nav["books"]}
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
merged_into = {m: sec["id"] for sec in study["sections"] for m in sec.get("merged", [])}  # Zwischenebenen (z. B. Mt 6,5–15)
section_of.update(merged_into)
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
                         **({"check": {k: b["source_check"][k] for k in ("date", "result")}} if b.get("source_check") else {}),
                         "i18n": i18n(b["id"], {"topic_de": "topic", "text_de": "text", "uncertain_de": "uncertain", "terms": "terms"})})
        continue
    if b["subject"] not in section_of:
        continue  # Notiz zu einem Abschnitt, der in der App noch nicht ausgearbeitet ist
    if b["subject"] in merged_into:
        b = {**b, "subject": merged_into[b["subject"]]}
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
                       **({"check": {k: b["source_check"][k] for k in ("date", "result")}} if b.get("source_check") else {}),
                       "dated": (b.get("source_check") or {}).get("date") or (b.get("knowledge") or {}).get("asserted_at"),
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
for key in ("findings", "interpretations", "principles", "applications", "questions", "reflections", "receptions"):
    for x in study[key]:
        b = book_of_id[x["subject"]]
        x = dict(x)
        for lg, f in (x.pop("i18n", None) or {}).items():
            bundle(f"l/{lg}/{b}").setdefault("i18n", {})[x["id"]] = f
        bundle(f"b/{b}").setdefault(key, []).append(x)
for x in study["relations"]:
    bundle(f"b/{book_of_id[x['from']]}").setdefault("relations", []).append(x)
# Prozesse (docs/PROZESSE.md): alle Fassungen in den Kern; Inhalte verweisen auf «PROC-…@Fassung», nach der sie entstanden sind
procs = {}
for f in sorted((ROOT / "data/processes").glob("PROC-*.json")):
    pr_ = json.loads(f.read_text(encoding="utf-8"))
    procs[pr_["id"]] = {k: pr_[k] for k in ("names", "group", "purpose_de", "current", "versions")}


def proc_at(pid, datum):
    """Fassung eines Prozesses, die an einem Datum galt."""
    vs = procs[pid]["versions"]
    gilt = [v for v in vs if v["valid_from"] <= (datum or "9999")]
    return f"{pid}@{(gilt[-1] if gilt else vs[0])['version']}"


# Kernanalysen (docs/VERDICHTUNG.md) für «Verstehen» auf Kapitel- und Buchebene; nur Hochdeutsch (noch keine Lokalisierungen)
for f in sorted((ROOT / "data/core-analyses").glob("CORE-*.json")):
    c = json.loads(f.read_text(encoding="utf-8"))
    # Buchebene im Übersichtspaket, damit «Vertiefen» auf Buch- und höheren Ebenen sie ohne das ganze Buchpaket kennt
    bundle("b/_overview" if c["level"] == "book" else f"b/{c['reference'].split('.')[0]}").setdefault("core", []).append({
        "id": c["id"], "level": c["level"], "ref": c["reference"], "core": c["core_de"], "gist": c.get("gist_de"), "purpose": c.get("purpose_de"),
        "mode": c.get("mode"), "moments": [{"ref": m["reference"], "text": m["text_de"]} for m in c["moments"]],
        "omitted": c.get("omitted_de", []), "checked": bool(c.get("review")),
        "proc": proc_at("PROC-VERDICHTUNG", (c.get("knowledge") or {}).get("asserted_at"))})
for x in background:
    b = x["chapter"].split(".")[0]
    x = dict(x)
    x["proc"] = proc_at("PROC-STUDIE", x.pop("dated", None))
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
# Schlüssel in der App: Bibel, Testamente, Buchgruppen = ID der Zusammenfassung; Buch «JHN», Kapitel «JHN.2», Abschnitt = ID der Texteinheit.
import localizations as _l10n  # noqa: E402
ill_recs = {}
for p in sorted((ROOT / "data/illustrations").rglob("*.json")):
    r = json.loads(p.read_text(encoding="utf-8"))
    if r.get("status") != "deprecated":
        ill_recs[r["id"]] = r
ill_core = {"styles": {}, "items": {}, "lexicon": {}}
for rid, r in ill_recs.items():
    if r["type"] == "figure":
        ill_core["lexicon"][rid] = {"kind": r["kind"], "group": r.get("display_group", r["kind"]), "name": r["names"], "traits": [t["trait_de"] for t in r.get("traits", [])], **({"legend": r["legend"]} if r.get("legend") else {})}
    elif r["type"] == "illustration_style":
        ill_core["styles"][r["key"]] = {"id": rid, "label": r["labels"], "description": r.get("description_de"),
                                        "renderings": r.get("renderings", {}), "library": (ROOT / r["library"]).read_text(encoding="utf-8") if r.get("library") else ""}
ill_l10n = _l10n.load(ill_recs)


def _check_text(c):
    """Kurzer Prüfvermerk für die Legende; automatische Prüfung (docs/BILDSTIL.md, Abschnitt 8) oder alter Blindtest."""
    if "stufe" not in c:
        return c.get("result_de")
    f = [x for x in c.get("felder", []) if x.get("regeln")]
    if not f:
        return "Noch nicht geprüft."
    n = sum(len(x["regeln"]) for x in f)
    datum = max((x.get("datum") or "") for x in f)
    if c["stufe"] in ("ki-geprueft", "fachlich-geprueft"):
        return f"Geprüft am {datum}: alle Pflichtregeln erfüllt ({n} Prüfungen in {len(f)} Feldern, durch weitere Instanzen; die erste beschreibt das Bild blind, ohne den Auftrag zu kennen)."
    offen = len(c.get("open_de") or [])
    return f"In Prüfung (Stand {datum}): {offen} offene Punkte."


def _ill_svg(fp):
    """SVG eines Bildes; gemalte Bilder (<image href="img/…">) als data:-Adresse einbetten, damit Einzeldatei und Pakete sie tragen."""
    svg = fp.read_text(encoding="utf-8").strip()
    def _emb(m):
        f = fp.parent / m.group(1)
        typ = {"webp": "image/webp", "jpg": "image/jpeg", "png": "image/png"}[f.suffix[1:]]
        return f'href="data:{typ};base64,{base64.b64encode(f.read_bytes()).decode()}"'
    return re.sub(r'href="(img/[^"]+)"', _emb, svg)


for rid, r in ill_recs.items():
    if r["type"] != "illustration" or r["style"] not in ill_recs:  # eingestellter Stil (deprecated, z. B. «Symbol» seit 2026-10-23)
        continue
    st, br = ill_recs[r["style"]], ill_recs[r["brief"]]
    key = r["target"] if r["level"] in ("section", "bible", "testament", "group") else r["reference"]
    item = {"id": rid, "brief": br["id"], "style": st["key"], "level": r["level"], "ref": r.get("reference"), "depicts": r.get("depicts", []),
            "alt": r["alt_de"], "note": r.get("note_de") or br.get("interpretation_note_de"), "check": _check_text(r.get("check") or {}),
            "panels": [{"n": p_["n"], "ref": p_["reference"], "action": p_["action_de"]} for p_ in br["panels"]], "captions": br.get("captions_de"),
            "svg": _ill_svg(ROOT / r["file"])}
    if r.get("evidence"):  # Aquarellstil (docs/BILDSTIL.md): Belege je Feld (B/R/I) für die Legende
        item["evidence"] = r["evidence"]
    item["proc"] = (r.get("check") or {}).get("process") or proc_at("PROC-BILD-ZEICHNUNG", (r.get("check") or {}).get("date") or (r.get("knowledge") or {}).get("asserted_at"))
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
        if "captions_de" in f:
            m["captions"] = f["captions_de"]
        if m:
            bundle(f"l/{lg}/common").setdefault("i18n", {}).setdefault(rid, {}).update(m)
# Merkverse (Bilder der Ebene «verse»): Liste im Kern, damit Menü und Lernmodus sie kennen, bevor ein Buch geladen ist
_bo = {code: i for i, (code, _, _) in enumerate(refs.BOOKS)}
ill_core["merk"] = sorted({r["reference"] for r in ill_recs.values() if r["type"] == "illustration" and r["level"] == "verse"},
                          key=lambda x: (_bo.get(x.split(".")[0], 999), int(x.split(".")[1]), int(x.split(".")[2])))
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
# ---------------------------------------------------------------- Vertiefen (docs/LESEN-UND-VERTIEFEN.md)
# Fragen und Rezeption der oberen Ebenen (subject = Zusammenfassung der Ebene, SUM-…): Buch und höher im Übersichtspaket,
# Kapitel (SUM-CH-…) im Buchpaket. Schlüssel wie bei den Bildern: SUM-BIBLE, SUM-OT/NT, SUM-GROUP-nn, Buchcode, «LUK.15».
def _sum_key(sid):
    if sid.startswith("SUM-BOOK-"):
        return sid[9:]
    if sid.startswith("SUM-CH-"):
        b_, c_ = sid[7:].rsplit("-", 1)
        return f"{b_}.{int(c_)}"
    return sid


refl_all = {r["id"]: r for r in folder("reflections")} if (ROOT / "data/reflections").exists() else {}
rcpt_all = {r["id"]: r for r in folder("receptions")} if (ROOT / "data/receptions").exists() else {}
up_l10n = localizations.load({**refl_all, **rcpt_all})
for kind, recs in (("reflections", refl_all), ("receptions", rcpt_all)):
    for r in sorted(recs.values(), key=lambda r: (r.get("order", 0), r["id"])):
        if not r["subject"].startswith("SUM-") or r.get("status") == "deprecated":
            continue
        key = _sum_key(r["subject"])
        if kind == "reflections":
            x = {"id": r["id"], "q": r["question_de"], "note": r.get("note_de"), "subject": key, "order": r.get("order", 0), "proc": r.get("process")}
            mp = {"question_de": "q", "note_de": "note"}
        else:
            x = {"id": r["id"], "subject": key, "tradition": r["tradition"], "period": r.get("period_de"), "text": r["text_de"],
                 "sources": r.get("sources_de", []), "confidence": r.get("confidence"), "proc": r.get("process"),
                 **({"check": {k: r["source_check"][k] for k in ("date", "result")}} if r.get("source_check") else {})}
            mp = {"period_de": "period", "text_de": "text"}
        bname = f"b/{key.split('.')[0]}" if "." in key else "b/_overview"
        for lg, f in up_l10n.get(r["id"], {}).items():
            m = {dst: f[src] for src, dst in mp.items() if src in f}
            if m:
                bundle(f"l/{lg}/{key.split('.')[0]}" if "." in key else f"l/{lg}/common").setdefault("i18n", {})[r["id"]] = m
        bundle(bname).setdefault(kind, []).append(x)

# Index im Kern: welche Ebenen etwas zum Vertiefen haben (Punkt am Knopf) und die erste Frage je Ebene (Tür von oben),
# damit obere Ebenen ohne alle Buchpakete wissen, was darunter liegt.
_group_of = {b_: g["id"] for g in nav["groups"] for b_ in g["books"]}
_testament_of = {g["id"]: g["testament"] for g in nav["groups"]}
part_info = {}  # Teil-ID -> (Abschnitts-ID, Buch, Kapitel)
for sec in study["sections"]:
    for part in sec["parts"]:
        b_, c_ = part["range"].split("-")[0].split(".")[:2]
        part_info[part["id"]] = (sec["id"], b_, int(c_))
whole_chapter = {}  # Abschnitt, der ein ganzes Kapitel umfasst -> «LUK.15»
for sec in study["sections"]:
    a_, _, z_ = sec["range"].partition("-")
    b_, c_, v_ = a_.split(".")
    cnt_ = nav_counts.get(b_) or []
    if v_ == "1" and z_ and z_.split(".")[:2] == [b_, c_] and int(c_) <= len(cnt_) and int(z_.split(".")[2]) == cnt_[int(c_) - 1]:
        whole_chapter[sec["id"]] = f"{b_}.{int(c_)}"
has = set()


def _mark(key, b_=None, c_=None):
    has.add(key)
    if b_:
        if c_:
            has.add(f"{b_}.{c_}")
        has.update([b_, _group_of.get(b_, ""), _testament_of.get(_group_of.get(b_), ""), "BIBLE"])


for key in ("findings", "interpretations", "principles", "relations", "questions", "reflections", "receptions"):
    for x in study[key]:
        for sj in (x.get("subjects") or [x.get("subject") or x.get("from")]):
            if sj in part_info:
                _mark(sj, *part_info[sj][1:])
            elif sj in whole_chapter or any(v[0] == sj for v in part_info.values()):
                for pid, (sid, b_, c_) in part_info.items():
                    if sid == sj:
                        _mark(pid, b_, c_)
for x in background:
    for pid, (sid, b_, c_) in part_info.items():
        if x["subject"] in (pid,) or (x["subject"] == sid and x.get("wide")):
            _mark(pid, b_, c_)
for f in sorted((ROOT / "data/core-analyses").glob("CORE-*.json")):
    c = json.loads(f.read_text(encoding="utf-8"))
    ref_ = c["reference"]
    if c["level"] == "book":
        _mark(ref_, ref_)
    elif c["level"] == "chapter":
        b_, c_ = ref_.split("-")[0].split(".")[:2]
        _mark(f"{b_}.{int(c_)}", b_, int(c_))
    else:
        tgt = c.get("target")
        if tgt in part_info:
            _mark(tgt, *part_info[tgt][1:])
for x in overview:
    if x["scope"] == "bible":
        has.add("BIBLE")
    elif x["scope"] == "testament":
        has.update([x["testament"], "BIBLE"])
    elif x["scope"] == "book_group":
        has.update([x["group"], _testament_of.get(x["group"], ""), "BIBLE"])
    elif x["scope"] == "book" and x["book"]:
        _mark(x["book"], x["book"])
has.discard("")
_SUMKEY = {"SUM-BIBLE": "BIBLE", "SUM-OT": "OT", "SUM-NT": "NT"}
firstq = {}


def _fq(key, x):
    firstq.setdefault(key, {"id": x["id"], "q": x["q"]})


up_refl = [x for n_, d in bundles.items() if n_.startswith("b/") for x in d.get("reflections", []) if not x["subject"].startswith("TU-")]
for x in up_refl:  # eigene Fragen der oberen Ebenen zuerst
    k_ = _SUMKEY.get(x["subject"], x["subject"].removeprefix("SUM-"))  # SUM-GROUP-nn -> GROUP-nn (Schlüssel der App)
    _fq(k_, x)
    has.add(k_)
_order = {code: i for i, (code, _, _) in enumerate(refs.BOOKS)}
for x in study["reflections"]:  # Fragen eines Abschnitts, der das ganze Kapitel umfasst = Fragen des Kapitels
    if x["subject"] in whole_chapter:
        _fq(whole_chapter[x["subject"]], x)
for x in sorted(study["reflections"], key=lambda x: (_order.get(part_info.get(x["subject"], (None, "ZZZ", 0))[1], 999),
                                                     part_info.get(x["subject"], (None, None, 0))[2], x["subject"], x.get("order", 0))):
    sj = x["subject"]
    for pid, (sid, b_, c_) in part_info.items():
        if pid == sj:
            _fq(pid, x)
            _fq(f"{b_}.{c_}", x)
            break
# Obere Ebenen ohne eigene Frage: erste Frage darunter, in Bibelreihenfolge (Kapitel → Buch → Buchgruppe → Testament → Bibel)
for code, *_ in refs.BOOKS:
    if code not in firstq:
        hit = next((firstq[f"{code}.{c_}"] for c_ in range(1, len(nav_counts.get(code, [])) + 1) if f"{code}.{c_}" in firstq), None)
        if hit:
            firstq[code] = hit
for g in nav["groups"]:
    hit = next((firstq[b_] for b_ in g["books"] if b_ in firstq), None)
    if hit and g["id"] not in firstq:
        firstq[g["id"]] = hit
for tm in ("OT", "NT"):
    hit = next((firstq[g["id"]] for g in nav["groups"] if g["testament"] == tm and g["id"] in firstq), None)
    if hit and tm not in firstq:
        firstq[tm] = hit
hit = next((firstq[k_] for k_ in ("OT", "NT") if k_ in firstq), None)
if hit and "BIBLE" not in firstq:
    firstq["BIBLE"] = hit
for x in study["reflections"]:
    for lg, f in (x.get("i18n") or {}).items():
        if "q" in f:
            bundle(f"l/{lg}/common").setdefault("i18n", {}).setdefault(x["id"], {})["q"] = f["q"]
deep_index = {"has": sorted(has), "firstq": firstq}

for name, d in bundles.items():
    kind, *rest = name.split("/")
    d["name"] = name
    if kind == "l":
        d["lang"] = rest[0]
    else:
        d["book"] = rest[0]

core_study = {"built_from": study["built_from"], "sections": core_sections, "layers": core_layers, "layer_order": langs,
              "compare": {}, "words": [], "variants": [], "findings": [], "interpretations": [], "principles": [],
              "applications": [], "relations": [], "questions": [], "reflections": [], "receptions": [], "deep": deep_index,
              "method": study["method"], "editions": study["editions"],
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
template = (ROOT / "app/bible/template.html").read_text(encoding="utf-8")
dump = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def page(inline):
    t = template
    for marker, payload in (("/*__STUDY__*/null", core_study), ("/*__NAV__*/null", nav), ("/*__SUMMARIES__*/null", core_sums),
                            ("/*__BACKGROUND__*/null", []), ("/*__SOURCES__*/null", core_src), ("/*__XREF__*/null", core_xref),
                            ("/*__MANIFEST__*/null", manifest), ("/*__INLINE__*/null", inline), ("/*__CATALOG__*/null", catalog), ("/*__ILL__*/null", ill_core),
                            ("/*__PROC__*/null", procs)):
        assert t.count(marker) == 1, marker
        t = t.replace(marker, dump(payload))
    return t


# Einzeldatei (offline, Tests): alle Pakete eingebettet
(ROOT / "app/bible/index.html").write_text(page(bundles), encoding="utf-8")
# Aufgeteilte Fassungen zum Veröffentlichen (deterministisches gzip):
#   build/bible/        Pakete als .json.gz (übliche Webserver)
#   build/bible-txt/    Pakete als gzip in Base64 (.gz.txt) für Hosts, die keine Binärdateien ausliefern
import hashlib  # noqa: E402
sizes, packed = {}, {}
for name, d in bundles.items():
    raw = json.dumps(d, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    gz = gzip.compress(raw, compresslevel=9, mtime=0)
    packed[name] = gz
    sizes[name] = (len(raw), len(gz))
# Version je Paket (Prüfsumme): die App lädt «<paket><ext>?v=<version>», damit Pakete lange im Cache bleiben dürfen
# und eine neue Fassung trotzdem sofort ankommt (siehe _headers).
versions = {name: hashlib.sha256(gz).hexdigest()[:12] for name, gz in sorted(packed.items())}
HEADERS = """# Cloudflare Pages: Cache und Sicherheit (erzeugt von scripts/build_bible.py)
/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
/
  Cache-Control: no-cache
/index.html
  Cache-Control: no-cache
/manifest.json
  Cache-Control: no-cache
/b/*
  Cache-Control: public, max-age=31536000, immutable
/l/*
  Cache-Control: public, max-age=31536000, immutable
/n/*
  Cache-Control: public, max-age=31536000, immutable
"""
for folder, ext in (("bible", ".json.gz"), ("bible-txt", ".gz.txt")):
    out = ROOT / "build" / folder
    out.mkdir(parents=True, exist_ok=True)
    manifest["ext"] = ext
    if folder == "bible":  # nur die Fassung für Cloudflare Pages; bible-txt (Claude-Artefakt) ohne Adresszusatz
        manifest["v"] = versions
    else:
        manifest.pop("v", None)
    (out / "index.html").write_text(page(None), encoding="utf-8")
    for name, gz in packed.items():
        f = out / f"{name}{ext}"
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_bytes(gz if ext.endswith(".gz") else base64.b64encode(gz) + b"\n")
    (out / "manifest.json").write_text(json.dumps({"ext": ext, "bundles": {k: {"bytes": a, "gzip": b} for k, (a, b) in sorted(sizes.items())}},
                                                  ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    if folder == "bible":
        (out / "_headers").write_text(HEADERS, encoding="utf-8")
manifest.pop("ext")
manifest.pop("v", None)
out = ROOT / "build/bible"
print(f"PASS: App gebaut: {len(nav['books'])} Bücher, {len(summaries)} Zusammenfassungen, {len(background)} Hintergrundnotizen zu Abschnitten, {len(overview)} zu oberen Ebenen, "
      f"ausgearbeitet: {', '.join(refs.display_de(x['range']) for x in study['sections'])}; "
      f"{len(bundles)} Pakete ({sum(b for _, b in sizes.values()) // 1024} KB gzip, Kern {len((out / 'index.html').read_bytes()) // 1024} KB).")
