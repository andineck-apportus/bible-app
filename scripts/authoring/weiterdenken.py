#!/usr/bin/env python3
"""Autorenwerkzeug: Inhalte für «Weiterdenken» (docs/WEITERDENKEN.md).

Schreibt Fragen zum Weiterdenken (`reflection`, data/reflections/REFL-<BUCH>-nnnn.json) und Einträge «Wie man es gelesen hat»
(`reception`, data/receptions/RCPT-<BUCH>-nnnn.json) samt Züridüütsch-Lokalisierungen (data/localizations/gsw-u-sd-chzh/).
Eingabe: Datenmodule scripts/authoring/weiterdenken_daten/<BUCH>.py mit REFLECTIONS und RECEPTIONS.

Geschrieben wird nur bei inhaltlicher Änderung; die vorige Fassung geänderter Felder kommt mit Datum und Grund ins
revision_log (BIBLE_REVISION_DATE, BIBLE_REVISION_REASON).

    python3 scripts/authoring/weiterdenken.py [BUCH …]
"""
import importlib.util
import json
import os
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import localizations  # noqa: E402

SRC = pathlib.Path(__file__).resolve().parent / "weiterdenken_daten"
GSW = {"language": "gsw-u-sd-chzh", "target_context": "CTX-CH-ZH-GSW-2026"}
TRADITIONS = ("jewish", "church_fathers", "liturgy", "art", "music", "literature", "reformation", "modern_scholarship")
TEXT = {"reflection": ("question_de", "note_de"), "reception": ("period_de", "text_de")}


def _module(book):
    spec = importlib.util.spec_from_file_location(f"wd_{book}", SRC / f"{book}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _write(path, rec, keep=("revision_log",)):
    """Schreibt nur bei Änderung; geänderte Felder mit voriger Fassung ins revision_log."""
    if path.exists():
        old = json.loads(path.read_text(encoding="utf-8"))
        changed = {k: old.get(k) for k in rec if k not in ("revision_log", "knowledge") and old.get(k) != rec.get(k)}
        log = old.get("revision_log", [])
        if changed:
            log = log + [{"date": os.environ.get("BIBLE_REVISION_DATE", "2026-10-28"),
                          "change_de": os.environ.get("BIBLE_REVISION_REASON", "Überarbeitet"), "previous": changed}]
            rec["knowledge"] = {**rec["knowledge"], "asserted_at": old.get("knowledge", {}).get("asserted_at", rec["knowledge"]["asserted_at"])}
        if log:
            rec["revision_log"] = log
    txt = json.dumps(rec, ensure_ascii=False, indent=2) + "\n"
    if not path.exists() or path.read_text(encoding="utf-8") != txt:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(txt, encoding="utf-8")
        return 1
    return 0


def run(books):
    n = 0
    for book in books:
        m = _module(book)
        date, proc, author = m.DATE, m.PROCESS, m.AUTHORSHIP_DE
        for kind, items, folder in (("reflection", m.REFLECTIONS, "reflections"), ("reception", m.RECEPTIONS, "receptions")):
            for x in items:
                rec = {"id": x["id"], "type": kind, "status": "draft", "tags": x.get("tags", m.TAGS), "subject": x["subject"]}
                if kind == "reflection":
                    rec.update({"question_de": x["question_de"], **({"note_de": x["note_de"]} if x.get("note_de") else {}),
                                "order": x["order"]})
                else:
                    assert x["tradition"] in TRADITIONS, x["tradition"]
                    rec.update({"tradition": x["tradition"], "period_de": x["period_de"], "text_de": x["text_de"],
                                "sources_de": x.get("sources_de", []), "confidence": x["confidence"],
                                **({"uncertain_de": x["uncertain_de"]} if x.get("uncertain_de") else {}),
                                **({"source_check": x["source_check"]} if x.get("source_check") else {})})
                rec.update({"process": proc, "authorship_de": author, "knowledge": {"asserted_at": date, "supersedes": None}})
                n += _write(ROOT / "data" / folder / f"{x['id']}.json", rec)
                if x.get("gsw"):
                    fields = {k: v for k, v in x["gsw"].items() if k in TEXT[kind]}
                    loc = {"id": f"L10N-GSW-ZH-{x['id']}", "type": "localization", "status": "draft", "tags": [], "localizes": x["id"],
                           **GSW, "fields": fields, "source_fingerprint": {k: localizations.fingerprint(rec.get(k)) for k in fields},
                           "authorship_de": f"KI-Entwurf (Claude) vom {date}; aus dem Hochdeutschen in Züridüütsch gefasst; Mundart noch nicht muttersprachlich geprüft.",
                           "review_de": "Noch keine muttersprachliche Prüfung dokumentiert.",
                           "knowledge": {"asserted_at": date, "supersedes": None}}
                    n += _write(ROOT / "data/localizations/gsw-u-sd-chzh" / f"{loc['id']}.json", loc)
    print(f"PASS: Weiterdenken für {', '.join(books)}; {n} Dateien geschrieben")


if __name__ == "__main__":
    run(sys.argv[1:] or sorted(p.stem for p in SRC.glob("*.py")))
