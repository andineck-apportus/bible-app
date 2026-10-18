"""Gemeinsamer Ablauf der Studien-Autorenwerkzeuge (titus_study.py, obadja_study.py): schreibt Kontext, Befunde,
Deutungen, Grundsätze, Anwendungen, Fragen, Beziehungen, Hintergrund, Zusammenfassungen und die Studie, jeweils mit
Züridüütsch-Lokalisierung. Fachwörter: (Sprache, Wort, Bedeutung) oder (Sprache, Wort, Bedeutung, Umschrift)."""
from _lib import D, localize, write

DATE = "2026-10-13"
AUTH = "KI-Entwurf (Claude) vom 2026-10-13 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt."
AUTH_GSW = "KI-Entwurf (Claude) vom 2026-10-13; aus dem Hochdeutschen in Züridüütsch gefasst; Mundart noch nicht muttersprachlich geprüft."
L = ("gsw-u-sd-chzh", "GSW-ZH", "CTX-CH-ZH-GSW-2026")


def _kn():
    return {"asserted_at": DATE, "supersedes": None}


def _terms(terms):
    return [{"lang": t[0], "word": t[1], **({"translit": t[3]} if len(t) > 3 else {}), "de": t[2]} for t in terms]


def write_study(cfg, label):
    TAGS = cfg["TAGS"]
    n = write(D / "contexts" / f"{cfg['CONTEXT']['id']}.json", dict(cfg["CONTEXT"]))
    for fid, subj, kind, claim, ev, conf, rat, g_claim, g_rat in cfg["FINDINGS"]:
        rec = {"id": fid, "type": "finding", "status": "draft", "tags": TAGS, "subject": subj, "kind": kind, "claim_de": claim,
               "evidence_refs": ev, "confidence": conf, "confidence_rationale_de": rat, "authorship_de": AUTH, "knowledge": _kn()}
        n += write(D / "findings" / f"{fid}.json", rec)
        n += localize(fid, rec, {"claim_de": g_claim, "confidence_rationale_de": g_rat}, *L, AUTH_GSW, DATE)
    for iid, subj, based, claim, conf, cav, counter, terms, g_claim, g_cav, g_counter, g_terms in cfg["INTERPRETATIONS"]:
        rec = {"id": iid, "type": "interpretation", "status": "draft", "tags": TAGS, "subject": subj, "based_on": based, "claim_de": claim,
               "confidence": conf, "caveat_de": cav, "counterarguments_de": counter, **({"terms": _terms(terms)} if terms else {}),
               "authorship_de": AUTH, "knowledge": _kn()}
        n += write(D / "interpretations" / f"{iid}.json", rec)
        n += localize(iid, rec, {"claim_de": g_claim, "caveat_de": g_cav, "counterarguments_de": g_counter, **({"terms": g_terms} if terms else {})},
                      *L, AUTH_GSW, DATE)
    for pid, der, st, conf, g_st in cfg["PRINCIPLES"]:
        rec = {"id": pid, "type": "principle", "status": "draft", "tags": TAGS + ["TAG-CULTURAL-TRANSFER"], "derived_from": der,
               "statement_de": st, "confidence": conf, "authorship_de": AUTH}
        n += write(D / "principles" / f"{pid}.json", rec)
        n += localize(pid, rec, {"statement_de": g_st}, *L, AUTH_GSW, DATE)
    for aid, prin, st, lim, g_st, g_lim in cfg["APPLICATIONS"]:
        rec = {"id": aid, "type": "application", "status": "draft", "tags": TAGS + ["TAG-CULTURAL-TRANSFER"], "principle": prin,
               "context": "CTX-CH-DE-2026", "statement_de": st, "limitations_de": lim, "confidence": "possible", "authorship_de": AUTH}
        n += write(D / "applications" / f"{aid}.json", rec)
        n += localize(aid, rec, {"statement_de": g_st, "limitations_de": g_lim}, *L, AUTH_GSW, DATE)
    for qid, subj, q, fnd, g_q, g_f in cfg["QUESTIONS"]:
        rec = {"id": qid, "type": "open_question", "status": "draft", "tags": TAGS + ["TAG-UNCERTAINTY"], "subject": subj,
               "question_de": q, "finding_de": fnd, "status_of_answer": "open", "knowledge": _kn()}
        n += write(D / "questions" / f"{qid}.json", rec)
        n += localize(qid, rec, {"question_de": g_q, "finding_de": g_f}, *L, AUTH_GSW, DATE)
    for rid, frm, to, kind, conf in cfg["RELATIONS"]:
        n += write(D / "relations" / f"{rid}.json", {"id": rid, "type": "relation", "status": "draft", "tags": TAGS, "from": frm,
                                                    "to_ref": to, "relation": kind, "confidence": conf})
    for (bid, subj, ref, ctx, conf, topic, text, unc, ev, src, terms, g_topic, g_text, g_unc, g_terms) in cfg["BACKGROUND"]:
        rec = {"id": bid, "type": "background_note", "status": "draft", "tags": TAGS + ["TAG-HISTORICAL-BACKGROUND"]}
        if subj:
            rec["subject"] = subj
        else:
            rec["scope"] = "book"
        rec.update({"context": ctx, "reference": ref, "topic_de": topic, "text_de": text, "confidence": conf,
                    **({"uncertain_de": unc} if unc else {}), "evidence_refs": ev, **({"sources_de": src} if src else {}),
                    **({"terms": _terms(terms)} if terms else {}), "authorship_de": AUTH, "knowledge": _kn()})
        if bid in cfg.get("SOURCE_CHECKS", {}):  # Prüfung der genannten ausserbiblischen Quellen am Text (siehe docs/QUELLENPRUEFUNG.md)
            rec["source_check"] = cfg["SOURCE_CHECKS"][bid]
        folder = D / "background" / ("overview" if not subj else "")
        n += write(folder / f"{bid}.json", rec)
        n += localize(bid, rec, {"topic_de": g_topic, "text_de": g_text, **({"uncertain_de": g_unc} if unc else {}),
                                 **({"terms": g_terms} if terms else {})}, *L, AUTH_GSW, DATE)
    for sid, text, g_text in cfg["SUMMARIES"]:
        rec = {"id": sid, "type": "summary", "status": "draft", "tags": TAGS, "scope": "chapter", "language": "de",
               "text_de": text, "authorship_de": AUTH, "knowledge": _kn()}
        n += write(D / "summaries" / f"{sid}.json", rec)
        n += localize(sid, rec, {"text_de": g_text}, *L, AUTH_GSW, DATE)
    sid, title, primary, extra, oq = cfg["STUDY"]
    outputs = [x[0] for k in ("FINDINGS", "INTERPRETATIONS", "PRINCIPLES", "APPLICATIONS", "QUESTIONS", "RELATIONS", "BACKGROUND")
               for x in cfg[k]] + extra
    n += write(D / "studies" / f"{sid}.json", {"id": sid, "type": "study", "status": "draft", "tags": TAGS, "title": title,
                                              "primary_unit": primary, "outputs": outputs, "open_questions": oq,
                                              "authorship_de": AUTH, "knowledge": _kn()})
    print(f"PASS: {label}-Studieninhalte; {n} Dateien geschrieben")
