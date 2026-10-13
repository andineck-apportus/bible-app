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
import hebrew_translit  # noqa: E402

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


def worked_sections(root=ROOT):
    """Ausgearbeitete Abschnitte: Texteinheiten oberster Ebene (nicht Teil einer anderen), deren Bereich eine
    Arbeitsübersetzung aus dem Urtext hat; sortiert nach Bibelreihenfolge."""
    tu = _all("text-units")
    inner = {p for u in tu.values() for p in u.get("parts", [])}
    covered = set()
    for t in _all("translations").values():
        if t.get("translation_kind") == "literal_original_working" and t.get("status") != "deprecated":
            covered.update(t.get("text_by_reference", {}))
    order = {code: i for i, (code, _, _) in enumerate(refs.BOOKS)}
    out = []
    for k, u in tu.items():
        if k in inner or u.get("status") == "deprecated":
            continue
        b, c, v0, v1 = _span(u["range"])
        if any(f"{b}.{c}.{v}" in covered for v in range(v0, v1 + 1)):
            out.append((order.get(b, 999), c, v0, k))
    return [k for *_, k in sorted(out)]


def project(section_ids=None):
    section_ids = section_ids or worked_sections()
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

    L10N = localizations.load({**tu, **findings, **ints, **prin, **apps, **qs})
    sections, scope, subjects = [], {}, set()
    for sid in section_ids:
        s = tu[sid]
        parts = [tu[p] for p in s.get("parts", [])] or [s]

        def names(u):
            loc = L10N.get(u["id"], {})
            return {"titles": {"de": u["title"], **{lg: f["title"] for lg, f in loc.items() if "title" in f}},
                    "summaries": {"de": u.get("summary_de"), **{lg: f["summary_de"] for lg, f in loc.items() if "summary_de" in f}}}
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
        for r in refs_in:  # Überschneidungen gleicher Sprache verbietet der Validator
            de[r] = t["text_by_reference"][r]
            de_source[r] = tid
        for dc in t.get("decisions", []):
            if in_scope(dc["reference"]):
                decisions.setdefault(dc["reference"], []).append({**{k: dc.get(k) for k in ("target", "kind", "grc", "heb", "more_literal", "other_options", "note") if dc.get(k)},
                                                                  **({"heb_tr": hebrew_translit.translit(dc["heb"])} if dc.get("heb") else {})})
        for alt in t.get("alternatives", []):
            vid, rid = alt["reading"].split(":")
            res = next((x for x in assess.get(vid, {}).get("results", []) if x["reading"].endswith(":" + rid)), None)
            base = next((x for x in assess.get(vid, {}).get("results", []) if x["reading"].endswith(":R1")), None)
            alternatives.append({"ref": alt["reference"], "from": alt["from_text"], "to": alt["to_text"],
                                 "effect": alt["effect"], "note": alt.get("note"), "variant": vid,
                                 "support": res["support"] if res else None,
                                 "base_support": base["support"] if base else None,
                                 "of": res["of"] if res else None,
                                 "basis": "editions" if res else "manuscripts_reported"})

    words = []
    HEB_KEEP = {"lemma": "lemma", "pos": "pos", "person": "person", "number": "number", "gender": "gender", "state": "state",
                "stem": "stem", "type": "subtype", "role": "role", "morph": "morph", "english": "gloss_cherith_en", "gloss": "gloss",
                "transliteration": "translit_academic", "greek": "lxx", "stronglemma": "stronglemma"}
    for (b, c), vs in sorted(scope.items()):
        if not (D / f"tokens/SBLGNT-{b}-{c:03d}.json").exists():
            # Hebräisch (WLC + MACULA Hebrew): ein Token je Morphem; Wortgruppe über word_no
            toks = json.loads((D / f"tokens/WLC-{b}-{c:03d}.json").read_text(encoding="utf-8"))["tokens"]
            mac = json.loads((D / f"annotations/MACULA-WLC-{b}-{c:03d}.json").read_text(encoding="utf-8"))["entries"]
            counts = json.loads((D / f"counts/WLC-{b}.json").read_text(encoding="utf-8"))["lemma_counts"]
            whole = {}
            for t in toks:
                whole.setdefault((t["reference"], t["word_no"]), []).append(t)
            for t in toks:
                if int(t["reference"].split(".")[2]) not in vs:
                    continue
                a = mac.get(t["id"], {})
                parts = whole[(t["reference"], t["word_no"])]
                full = "".join(p["text"] for p in parts)
                words.append({"id": t["id"], "ref": t["reference"], "n": t["position"], "text": t["text"], "word": t["word"],
                              "lang": "he", "word_no": t["word_no"], "wfull": full, "wtr": hebrew_translit.translit(full),
                              "mac": {dst: a[src] for src, dst in HEB_KEEP.items() if a.get(src)}, "freq": counts.get(a.get("lemma"), 0),
                              "_strong": a.get("strongnumberx"), "_sref": t.get("source_reference")})
            continue
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
                  "mac": {k: a[k] for k in KEEP if k in a}, "freq": counts.get(a.get("lemma"), 0), "_strong": a.get("strong")}
            if t["id"] in mg:
                m = mg[t["id"]]
                wd["mgnt"] = {"lemma": m["lemma"], "pos": m["pos"], "parsing": m["parsing"]}
            words.append(wd)
    lexicon, ketiv, ketiv_only, ed_extra = _enrich_words(words, in_scope)
    for al in _all("alignments").values():
        if al.get("coverage") != "complete" or al.get("status") == "deprecated":
            continue
        tok_de = layer((al.get("target_language") or "de").split("-")[0])["align"]
        for a in al["alignments"]:
            if not in_scope(a["reference"]):
                continue
            for i, t in enumerate(a["source_tokens"]):
                tok_de[t] = {"target": a["target"], "kind": a["kind"], "note": a.get("note"), "first": i == 0}
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
        # Wörterbuch-Einträge (Schlüssel aus words[].lx), Ketiv/Qere (words[].kq), Ausgaben je Wort (words[].ed) und
        # Wörter anderer Ausgaben bzw. Ketiv ohne Qere je Vers
        "lexicon": lexicon, "ketiv": ketiv, "ketiv_only": ketiv_only, "ed_extra": ed_extra,
    }


def _norm(s):
    import unicodedata
    return unicodedata.normalize("NFC", s or "")


def _load_lexica():
    """Wörterbücher aus data/lexica: UBS (nach Lemma und Strong-Nummer) und STEPBible TBESG/TBESH (nach dStrong)."""
    out = {}
    for p in sorted((D / "lexica").glob("LEX-*.json")):
        r = json.loads(p.read_text(encoding="utf-8"))
        lang = "grc" if r["language"] == "grc" else "heb"
        kind = "ubs" if r["id"].startswith("LEX-UBS-") else "step"
        x = out.setdefault((kind, lang), {"entries": r["entries"], "by_lemma": {}, "by_strong": {}, "by_estrong": {}})
        for k, e in r["entries"].items():
            if kind == "ubs":
                x["by_lemma"].setdefault(_norm(e["lemma"]), k)
                for s in e.get("strong", []):
                    x["by_strong"].setdefault(s, []).append(k)
                    base = s.rstrip("abcdefghijklmnopqrstuvwxyz")
                    if base != s:
                        x["by_strong"].setdefault(base, []).append(k)
            else:
                x["by_estrong"].setdefault(e["estrong"].lower(), []).append(k)
    return out


def _enrich_words(words, in_scope):
    """Ergänzt die Wörter um Wörterbuch-Schlüssel (lx), Ausgabenbefund (ed, TAGNT) und Ketiv (kq, TAHOT).
    Nur Zuordnung vorhandener Daten; keine eigene Bewertung."""
    import re
    lex = _load_lexica()
    tal = {}
    for p in sorted((D / "tagged-alignments").glob("TALIGN-*.json")):
        r = json.loads(p.read_text(encoding="utf-8"))
        tal[(r["kind"], r["book"])] = r
    lexicon, ketiv, ketiv_only, ed_extra = {}, {}, {}, {}
    main8 = None

    def ubs_key(lang, lemma, strong_keys):
        x = lex.get(("ubs", lang))
        if not x:
            return None
        cands = list(dict.fromkeys(k for s in strong_keys for k in x["by_strong"].get(s, [])))
        by_l = x["by_lemma"].get(_norm(lemma))
        if lang == "heb":
            cands = [k for k in cands + ([by_l] if by_l else []) if _cons(x["entries"][k]["lemma"]) == _cons(lemma)]
            return cands[0] if cands else None
        if lang == "grc" and by_l:
            return by_l
        if by_l and by_l in cands:
            return by_l
        if cands:
            return cands[0] if len(set(cands)) == 1 else (by_l if by_l in cands else cands[0])
        return by_l

    def step_key(lang, estrong, dstrong, lemma=None):
        """Kandidaten: dStrong aus TAGNT/TAHOT, dann alle Zeilen der erweiterten Strong-Nummer (auch a/b/…);
        beim Hebräischen gilt nur ein Eintrag mit denselben Konsonanten wie das MACULA-Lemma."""
        x = lex.get(("step", lang))
        if not x:
            return None
        cands = [dstrong] if dstrong and dstrong in x["entries"] else []
        e = (estrong or "").lower()
        rows = x["by_estrong"].get(e, []) or [k for es, ks in x["by_estrong"].items() if e and re.sub(r"[a-z]$", "", es) == e for k in ks]
        cands += [k for k in rows if not x["entries"][k].get("relation")] + [k for k in rows if x["entries"][k].get("relation")]
        if lang == "heb":
            cands = [k for k in cands if _cons(x["entries"][k].get("lemma")) == _cons(lemma)]
        return cands[0] if cands else None

    def put(key, lang, kind):
        if key is None:
            return None
        # kurze, eindeutige Schlüssel für die Pakete (UBS-IDs sind nur je Wörterbuch eindeutig: Sprache im Schlüssel)
        k = ("U" + lang[0] + key.rstrip("0") if kind == "ubs" else "T" + key)
        if k not in lexicon:
            e = lex[(kind, lang)]["entries"][key]
            if kind == "ubs":
                lexicon[k] = {"src": f"ubs-{lang}", "l": e["lemma"], "p": ", ".join(e.get("pos", [])),
                              "s": [{"d": s.get("definition", ""), "g": s.get("glosses", []),
                                     "f": " › ".join(x for x in (s.get("domains", [""])[:1] + s.get("subdomains", [])[:1]) if x),
                                     **({"ai": True} if s.get("ai_generated") else {})} for s in e["senses"]]}
            else:
                lexicon[k] = {"src": f"step-{lang}", "l": e.get("lemma", ""), "tr": e.get("translit", ""), "g": e.get("gloss", "")}
        return k

    for w in words:
        b = w["ref"].split(".")[0]
        m = w.get("mac", {})
        if w.get("lang") == "he":
            a = tal.get(("ketiv_qere", b), {})
            sx = re.match(r"^(\d+)([a-z]?)$", w.pop("_strong", None) or "")
            est = "H%04d%s" % (int(sx[1]), sx[2]) if sx else None
            ds = a.get("dstrong", {}).get(w["id"])
            keys = [k for k in (est, "H%04d" % int(sx[1]) if sx else None, re.sub(r"[A-Z]$", "", ds or "") or None) if k]
            u = ubs_key("heb", m.get("lemma"), keys)
            t = step_key("heb", "H%04d" % int(sx[1]) if sx else None, ds, m.get("lemma"))
            # Schutz: Strong-Nummern von MACULA (z. B. für Vorsilben und Endungen), UBS und STEPBible decken sich nicht
            # immer; ein Eintrag gilt nur, wenn seine Grundform dieselben Konsonanten hat wie das MACULA-Lemma (in
            # ubs_key/step_key geprüft).

            lx = {}
            uk, tk = put(u, "heb", "ubs"), put(t, "heb", "step")
            if uk:
                lx["u"] = uk
                senses = lex[("ubs", "heb")]["entries"][u]["senses"]
                ref = w.get("_sref") or w["ref"]
                here = [i for i, s in enumerate(senses) if ref in s.get("occurrences", [])]
                if here and len(senses) > 1:
                    lx["h"] = here
            if tk:
                lx["t"] = tk
            if lx:
                w["lx"] = lx
            for key, e in a.get("entries", {}).items():
                if w["id"] in e.get("tokens", []):
                    w["kq"] = key
                    ketiv.setdefault(key, {"type": e["type"], "ketiv": e["ketiv"].get("text", ""),
                                           "ketiv_tr": e["ketiv"].get("translit", ""), "gloss": e["ketiv"].get("gloss_en", ""),
                                           "qere": e["qere"], "src": e["src"], "words": e["qere"].count("/ /") + 1})
            w.pop("_sref", None)
            continue
        a = tal.get(("edition_presence", b), {})
        main8 = main8 or a.get("main_editions")
        e = a.get("entries", {}).get(w["id"], {})
        strong = [p for p in (w.pop("_strong", None) or "").split("+") if p.isdigit()]
        est = "G%04d" % int(strong[0]) if strong else None
        u = ubs_key("grc", m.get("lemma"), ["G%04d" % int(p) for p in strong])
        t = step_key("grc", est, e.get("dstrong"))
        lx = {}
        uk, tk = put(u, "grc", "ubs"), put(t, "grc", "step")
        if uk:
            lx["u"] = uk
            senses = lex[("ubs", "grc")]["entries"][u]["senses"]
            here = [i for i, s in enumerate(senses) if w["ref"] in s.get("occurrences", [])]
            if here and len(senses) > 1:
                lx["h"] = here
        if tk:
            lx["t"] = tk
        if lx:
            w["lx"] = lx
        if a and w["id"] in a.get("unmatched", {}).get("tokens", []):
            w["ed"] = {"unmatched": True}
        elif e.get("editions") is not None:
            eds = e["editions"]
            if not set(a["main_editions"]) <= set(eds) or e.get("alt") or e.get("moved"):
                w["ed"] = {k: v for k, v in (("type", e.get("type")), ("eds", eds), ("moved", e.get("moved")),
                                             ("alt", [{"grc": x["grc"], "eds": x["editions"]} for x in e.get("alt", [])]),
                                             ("sbl_not_listed", e.get("sbl_not_listed")), ("via_variant", e.get("via_variant")))
                           if v}
    for (kind, b), a in tal.items():
        if kind == "edition_presence":
            for x in a.get("extra_words", []):
                if in_scope(x["ref"]):
                    lst = ed_extra.setdefault(x["ref"], [])
                    # aufeinanderfolgende Wörter mit gleicher Ausgabenliste zu einer Wendung zusammenfassen
                    if lst and lst[-1]["after"] == x["after"] and lst[-1]["eds"] == x["editions"] and lst[-1]["last"] == _prev_src(x["src"]):
                        lst[-1]["grc"] += " " + x["grc"]
                        lst[-1]["last"] = x["src"]
                    else:
                        lst.append({"after": x["after"], "grc": x["grc"], "eds": x["editions"], "type": x["type"], "last": x["src"]})
        else:
            for x in a.get("ketiv_without_qere", []):
                if in_scope(x["ref"]):
                    ketiv_only.setdefault(x["ref"], []).append({"after": x["after"], "ketiv": x["ketiv"].get("text", ""),
                                                                "ketiv_tr": x["ketiv"].get("translit", ""),
                                                                "gloss": x["ketiv"].get("gloss_en", ""), "src": x["src"]})
    for lst in ed_extra.values():
        for x in lst:
            x.pop("last", None)
    return lexicon, ketiv, ketiv_only, ed_extra


def _cons(s):
    return "".join(ch for ch in (s or "") if "\u05d0" <= ch <= "\u05ea")


def _prev_src(src):
    """«Mrk.1.1#07» -> «Mrk.1.1#06» (vorangehendes TAGNT-Wort im selben Vers)."""
    head, _, n = src.rpartition("#")
    return f"{head}#{int(n) - 1:02d}" if n.isdigit() else None

