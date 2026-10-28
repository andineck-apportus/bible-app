#!/usr/bin/env python3
"""Autorenwerkzeug: Inhalte für «Weiterdenken» (docs/WEITERDENKEN.md).

Schreibt Fragen zum Weiterdenken (`reflection`, data/reflections/REFL-<BUCH>-nnnn.json) und Einträge «Wie man es gelesen hat»
(`reception`, data/receptions/RCPT-<BUCH>-nnnn.json) samt Züridüütsch-Lokalisierungen (data/localizations/gsw-u-sd-chzh/).
Eingabe: Datenmodule scripts/authoring/weiterdenken_daten/<BUCH>.py mit REFLECTIONS und RECEPTIONS.

Geschrieben wird nur bei inhaltlicher Änderung; die vorige Fassung geänderter und gestrichener Felder kommt mit Datum und
Grund ins revision_log (BIBLE_REVISION_DATE, BIBLE_REVISION_REASON). Mehrere Läufe am selben Tag mit demselben Grund ergeben
einen Eintrag (die älteste Fassung bleibt). Dateien, die Git noch nicht erfasst hat (neuer Entwurf), werden ohne
revision_log überschrieben.

Datenmodul: DATE, PROCESS, TAGS, AUTHORSHIP_DE; je Eintrag optional eigene `authorship_de` und `check`. Prüfvermerk für alle
Einträge eines Moduls: CHECK = {"date", "by", "limits_de", optional "process"} und CHECK_CORRECTED = [IDs, die in der Prüfung
berichtigt wurden] (result corrected, sonst confirmed). Traditionen: TRADITIONS (Schema `receptionTradition`).

    python3 scripts/authoring/weiterdenken.py [BUCH …]
"""
import datetime
import importlib.util
import json
import os
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import localizations  # noqa: E402

SRC = pathlib.Path(__file__).resolve().parent / "weiterdenken_daten"
GSW = {"language": "gsw-u-sd-chzh", "target_context": "CTX-CH-ZH-GSW-2026"}
TRADITIONS = tuple(json.loads((ROOT / "schema/record.schema.json").read_text(encoding="utf-8"))["$defs"]["receptionTradition"]["enum"])
SKIP = ("revision_log", "knowledge")


def _tracked():
    """Dateien unter data/, die Git erfasst hat (für sie wird ein revision_log geführt)."""
    try:
        out = subprocess.run(["git", "ls-files", "-z", "data/reflections", "data/receptions", "data/localizations"], cwd=ROOT,
                             capture_output=True, text=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return None
    return {ROOT / f for f in out.split("\0") if f}


TRACKED = _tracked()
TEXT = {"reflection": ("question_de", "note_de"), "reception": ("period_de", "text_de")}


def _module(book):
    spec = importlib.util.spec_from_file_location(f"wd_{book}", SRC / f"{book}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _write(path, rec):
    """Schreibt nur bei Änderung; geänderte und gestrichene Felder mit voriger Fassung ins revision_log."""
    if path.exists():
        old = json.loads(path.read_text(encoding="utf-8"))
        changed = {k: old.get(k) for k in sorted(set(rec) | set(old)) if k not in SKIP and old.get(k) != rec.get(k)
                   and not (k == "check" and k not in old)}  # erstmals eingetragener Prüfvermerk ist keine inhaltliche Revision
        log = old.get("revision_log", [])
        if changed and (TRACKED is None or path in TRACKED):
            date = os.environ.get("BIBLE_REVISION_DATE") or datetime.date.today().isoformat()
            reason = os.environ.get("BIBLE_REVISION_REASON", "Überarbeitet")
            if log and log[-1].get("date") == date and log[-1].get("change_de") == reason:
                # derselbe Lauf (Tag und Grund): ein Eintrag; die älteste Fassung eines Feldes bleibt
                prev = log[-1].get("previous", {})
                log = log[:-1] + [{**log[-1], "previous": {**changed, **prev}}]
            else:
                log = log + [{"date": date, "change_de": reason, "previous": changed}]
            rec["knowledge"] = {**rec["knowledge"], "asserted_at": old.get("knowledge", {}).get("asserted_at", rec["knowledge"]["asserted_at"])}
        if log:
            rec["revision_log"] = log
    txt = json.dumps(rec, ensure_ascii=False, indent=2) + "\n"
    if not path.exists() or path.read_text(encoding="utf-8") != txt:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(txt, encoding="utf-8")
        return 1
    return 0


def _check(m, x):
    """Prüfvermerk eines Eintrags: eigener `check` oder der des Moduls (CHECK, CHECK_CORRECTED)."""
    if x.get("check"):
        return x["check"]
    c = getattr(m, "CHECK", None)
    if not c:
        return None
    return {"date": c["date"], "by": c["by"], "result": "corrected" if x["id"] in getattr(m, "CHECK_CORRECTED", ()) else "confirmed",
            "limits_de": c["limits_de"], **({"process": c["process"]} if c.get("process") else {})}


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
                chk = _check(m, x)
                rec.update({"process": proc, "authorship_de": x.get("authorship_de", author), **({"check": chk} if chk else {}),
                            "knowledge": {"asserted_at": date, "supersedes": None}})
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
