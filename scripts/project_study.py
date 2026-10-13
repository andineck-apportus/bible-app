"""Studienprojektion für den Lesestrom: ausgearbeitete Abschnitte aus dem freien Kern (data/).

Verwendung: from project_study import project; data = project(["TU-MRK-003-020-035", ...])

Pro Abschnitt (text_unit mit oder ohne parts) werden gesammelt: deutsche Arbeitsübersetzung je Vers,
Alternativen mit Bewertung, griechische Wörter mit MACULA- (und, wo vorhanden, MorphGNT-) Angaben,
Wortzuordnung, Variantenstellen, Befunde, Deutungen, Grundsätze, Anwendungen, offene Fragen und
Beziehungen. Alle Schlüssel sind kanonische Bibelstellen (z. B. «MAT.6.11»). Die Projektion erzeugt
keine Inhalte; sie formatiert nur.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import refs  # noqa: E402
import localizations  # noqa: E402

D = ROOT / "data"
KEEP = ["lemma", "pos", "subtype", "person", "number", "gender", "case", "tense", "voice", "mood", "degree",
        "role", "gloss_berean", "gloss_cherith_en", "subject_ref", "referent", "morph"]


def _all(folder):
    out = {}
    for p in sorted((D / folder).rglob("*.json")):
        r = json.loads(p.read_text(encoding="utf-8"))
        out[r["id"]] = r
    return out


def _span(rng):
    """'MAT.6.5-MAT.6.15' -> ('MAT', 6, 5, 15)"""
    a, _, z = rng.partition("-")
    b, c, v = a.split(".")
    return b, int(c), int(v), int(z.split(".")[2]) if z else int(v)


def project(section_ids):
    tu = _all("text-units")
    variants = _all("variants")
    translations = _all("translations")
    assess = {}
    for p in sorted((D / "assessments").rglob("*.json")):
        for a in json.loads(p.read_text(encoding="utf-8")).get("assessments", []):
            assess[a["assesses"]] = a
    findings, ints, prin, apps = _all("findings"), _all("interpretations"), _all("principles"), _all("applications")
    ctx, rels, qs = _all("contexts"), _all("relations"), _all("questions")
    method = json.loads((D / "methods/METHOD-EDITION-AGREEMENT-V1.json").read_text(encoding="utf-8"))
    editions = {k: {"title": v["title"], "year": v.get("year")} for k, v in _all("editions").items()}

    sections, scope, subjects = [], {}, set()
    for sid in section_ids:
        s = tu[sid]
        parts = [tu[p] for p in s.get("parts", [])] or [s]
        def names(u):
            return {"titles": {"de": u["title"], **{k.split("-")[0]: v for k, v in (u.get("title_by_language") or {}).items()}},
                    "summaries": {"de": u.get("summary_de"), **{k.split("-")[0]: v for k, v in (u.get("summary_by_language") or {}).items()}}}
        sections.append({"id": s["id"], "range": s["range"], "title": s["title"], "summary": s.get("summary_de"), **names(s),
                         "parts": [{"id": p["id"], "range": p["range"], "title": p["title"], "summary": p.get("summary_de"), **names(p)}
                                   for p in parts]})
        b, c, v0, v1 = _span(s["range"])
        scope.setdefault((b, c), set()).update(range(v0, v1 + 1))
        subjects.update([s["id"]] + [p["id"] for p in parts])

    def in_scope(ref):
        try:
            b, c, v, _ = _span(ref)
        except (ValueError, IndexError):
            return False
        return v in scope.get((b, c), set())

    compare = {}
    for tid, t in sorted(translations.items()):
        if t.get("translation_kind") == "historical_comparison":
            for r, txt in t.get("text_by_reference", {}).items():
                if in_scope(r):
                    compare.setdefault(r, []).append({"id": tid, "title": t.get("title", tid), "text": txt,
                                                      "lang": (t.get("language") or "de").split("-")[0],
                                                      "notes": t.get("notes_by_reference", {}).get(r, []),
                                                      "license": t.get("source", {}).get("license")})
    # Übersetzungsschichten je Sprache (BCP-47-Grundtag): de, gsw, …; jede mit Text, Quelle, Entscheidungen,
    # Alternativen und Wortzuordnung. «de» ist die Kontroll- und Standardschicht.
    LABELS = {"de": "Hochdeutsch", "gsw": "Züridüütsch"}
    layers = {}

    def layer(lang, t=None):
        if lang not in layers:
            layers[lang] = {"lang": lang, "label": (t or {}).get("language_label_de") or LABELS.get(lang, lang),
                            "text": {}, "source": {}, "decisions": {}, "alternatives": [], "align": {},
                            "orthography": (t or {}).get("orthography_de"), "register": (t or {}).get("register_de"),
                            "review": (t or {}).get("review_de"),
                            # Vergleichsübersetzungen sind sprachgebunden: welche Sprachen der Zielkontext zum Vergleich
                            # heranzieht, steht im context-Datensatz (comparison_languages), sonst nur die eigene Sprache
                            "compare_languages": ctx.get((t or {}).get("target_context"), {}).get("comparison_languages") or [lang]}
        return layers[lang]

    for tid, t in sorted(translations.items()):
        if t.get("status") == "deprecated" or t.get("translation_kind") != "literal_original_working":
            continue
        refs_in = [r for r in t.get("text_by_reference", {}) if in_scope(r)]
        if not refs_in:
            continue
        lang = (t.get("language") or "de").split("-")[0]
        L = layer(lang, t)
        de, de_source, decisions, alternatives = L["text"], L["source"], L["decisions"], L["alternatives"]
        for r in refs_in:
            if r not in de or len(t.get("text_by_reference", {})) > 1:  # Abschnittsübersetzung vor Einzelvers
                de[r] = t["text_by_reference"][r]
                de_source[r] = tid
        for dc in t.get("decisions", []):
            if in_scope(dc["reference"]):
                decisions.setdefault(dc["reference"], []).append({k: dc.get(k) for k in ("target", "kind", "grc", "more_literal_de", "other_options_de", "note_de") if dc.get(k)})
        for alt in t.get("alternatives", []):
            vid, rid = alt["reading"].split(":")
            res = next((x for x in assess.get(vid, {}).get("results", []) if x["reading"].endswith(":" + rid)), None)
            base = next((x for x in assess.get(vid, {}).get("results", []) if x["reading"].endswith(":R1")), None)
            alternatives.append({"ref": alt["reference"], "from": alt["de_from"], "to": alt["de_to"],
                                 "effect": alt["effect"], "note": alt.get("note_de"), "variant": vid,
                                 "support": res["support"] if res else None,
                                 "base_support": base["support"] if base else None,
                                 "of": res["of"] if res else None,
                                 "basis": "editions" if res else "manuscripts_reported"})

    words = []
    for (b, c), vs in sorted(scope.items()):
        toks = json.loads((D / f"tokens/SBLGNT-{b}-{c:03d}.json").read_text(encoding="utf-8"))["tokens"]
        mac = json.loads((D / f"annotations/MACULA-SBLGNT-{b}-{c:03d}.json").read_text(encoding="utf-8"))["entries"]
        counts = json.loads((D / f"counts/SBLGNT-{b}.json").read_text(encoding="utf-8"))["lemma_counts"]
        mg = {}
        for p in (D / "annotations").glob(f"MORPHGNT-SBLGNT-{b}-{c:03d}*.json"):
            mg.update(json.loads(p.read_text(encoding="utf-8"))["entries"])
        for t in toks:
            if int(t["reference"].split(".")[2]) not in vs:
                continue
            a = mac.get(t["id"], {})
            wd = {"id": t["id"], "ref": t["reference"], "n": t["position"], "text": t["text"], "word": t["word"],
                  "mac": {k: a[k] for k in KEEP if k in a}, "freq": counts.get(a.get("lemma"), 0)}
            if t["id"] in mg:
                m = mg[t["id"]]
                wd["mgnt"] = {"lemma": m["lemma"], "pos": m["pos"], "parsing": m["parsing"]}
            words.append(wd)
    for al in _all("alignments").values():
        if al.get("coverage") != "complete" or al.get("status") == "deprecated":
            continue
        tok_de = layer((al.get("target_language") or "de").split("-")[0])["align"]
        for a in al["alignments"]:
            if not in_scope(a["reference"]):
                continue
            for i, t in enumerate(a["source_tokens"]):
                tok_de[t] = {"target": a["target"], "kind": a["kind"], "note": a.get("note_de"), "first": i == 0}
    base = layer("de")

    units = []
    for vid, v in sorted(variants.items()):
        if not in_scope(v.get("reference", "")):
            continue
        u = {"id": vid, "ref": v["reference"], "level": v.get("evidence_level", "manuscripts_reported"),
             "readings": [{"id": r["reading_id"], "text": r["text"], "editions": r.get("editions", []),
                           "witnesses": r.get("witnesses_reported", [])} for r in v["readings"]],
             "note": v.get("note_de") or v.get("editorial_note")}
        if vid in assess:
            u["assessment"] = [{"reading": r["reading"].split(":")[1], "support": r["support"], "of": r["of"],
                                "level": r["level"], "editions": r["supporting_editions"]} for r in assess[vid]["results"]]
        units.append(u)

    L10N = localizations.load({**findings, **ints, **prin, **apps, **qs})

    def i18n(rid, mapping):
        """Lokalisierte Felder je Sprache unter den Schlüsseln der Projektion (nur aktuelle Felder)."""
        out = {}
        for lang, f in L10N.get(rid, {}).items():
            m = {dst: f[src] for src, dst in mapping.items() if src in f}
            if m:
                out[lang] = m
        return out

    fs = {k: v for k, v in findings.items() if v.get("subject") in subjects}
    ins = {k: v for k, v in ints.items() if v.get("subject") in subjects}
    known = set(fs) | set(ins)
    prs = {k: v for k, v in prin.items() if set(v.get("derived_from", [])) & known}
    aps = {k: v for k, v in apps.items() if v.get("principle") in prs}

    def subject_of_principle(p):
        for x in p.get("derived_from", []):
            if x in fs:
                return fs[x]["subject"]
            if x in ins:
                return ins[x]["subject"]
        return None

    return {
        "built_from": "bible-app data/ (freier Kern)",
        "sections": sections,
        "layers": layers, "layer_order": ["de"] + sorted(k for k in layers if k != "de"),
        # Kurzformen der Standardschicht (Hochdeutsch), auch für die Tests
        "de": base["text"], "de_source": base["source"], "alternatives": base["alternatives"], "decisions": base["decisions"],
        "compare": compare, "words": words, "tok_de": base["align"], "variants": units,
        "findings": [{"id": k, "claim": v["claim_de"], "kind": v.get("kind"), "confidence": v.get("confidence"),
                      "subject": v.get("subject"), "caveat": v.get("confidence_rationale_de"),
                      "i18n": i18n(k, {"claim_de": "claim", "confidence_rationale_de": "caveat"})} for k, v in sorted(fs.items())],
        "interpretations": [{"id": k, "claim": v["claim_de"], "confidence": v.get("confidence"), "caveat": v.get("caveat_de"),
                             "counter": v.get("counterarguments_de", []), "subject": v.get("subject"), "terms": v.get("terms", []),
                             "i18n": i18n(k, {"claim_de": "claim", "caveat_de": "caveat", "counterarguments_de": "counter", "terms": "terms"})}
                            for k, v in sorted(ins.items())],
        "principles": [{"id": k, "text": v["statement_de"], "confidence": v.get("confidence"),
                        "subject": subject_of_principle(v), "i18n": i18n(k, {"statement_de": "text"})} for k, v in sorted(prs.items())],
        "applications": [{"id": k, "text": v["statement_de"], "limits": v.get("limitations_de"),
                          "subject": subject_of_principle(prs[v["principle"]]),
                          "context": ctx.get(v.get("context"), {}).get("audience"), "confidence": v.get("confidence"),
                          "i18n": i18n(k, {"statement_de": "text", "limitations_de": "limits"})}
                         for k, v in sorted(aps.items())],
        "relations": [{"from": v["from"], "from_ref": tu.get(v["from"], {}).get("range"), "to": v["to_ref"], "to_de": refs.display_de(v["to_ref"]), "kind": v["relation"],
                       "confidence": v.get("confidence")} for v in sorted(rels.values(), key=lambda r: r["id"])
                      if v.get("from") in subjects],
        "questions": [{"id": v["id"], "q": v["question_de"], "finding": v.get("finding_de"), "subject": v.get("subject"),
                       "i18n": i18n(v["id"], {"question_de": "q", "finding_de": "finding"})}
                      for v in sorted(qs.values(), key=lambda r: r["id"]) if v.get("subject") in subjects],
        "method": {"name": method["name_de"], "question": method["question_de"], "limits": method["assumptions_and_limits_de"]},
        "editions": editions,
    }
