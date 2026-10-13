#!/usr/bin/env python3
"""Autorenwerkzeug: Hintergrund damals je Buch (background_note mit scope «book»).

Aufruf: python3 scripts/authoring/hintergrund_buecher.py [modul …]
        (ohne Angabe alle Module in scripts/authoring/buecher/; Modulname z. B. «g01_tora»)

Jedes Modul in scripts/authoring/buecher/ definiert NOTES, eine Liste von dict:
    id          «BG-<BUCH>-BOOK-000n»
    book        Buchcode (GEN …)
    context     ein CTX-HIST-*-Kontext
    confidence  high | probable | possible
    topic, text, uncertain   Hochdeutsch; Bibelstellen als Marken [[GEN.1.1]]
    evidence_refs            kanonische Stellen (Liste, darf leer sein)
    sources                  ausserbiblische Quellen mit üblicher Zitierweise (Liste, darf leer sein)
    terms                    Ursprachwörter aus dem Text: T(lang, wort, bedeutung[, umschrift])
    gsw         {"topic", "text", "uncertain", "terms": [Bedeutungen in Mundart, gleiche Reihenfolge]}

Schreibt data/background/overview/BG-*-BOOK-*.json und data/localizations/gsw-u-sd-chzh/BG-*.json, nur bei
inhaltlicher Änderung (frühere Fassung im revision_log). Prüft Pflichtfelder, Marken und unmarkierte Stellen.
KI-Entwurf (Claude) vom 2026-10-13 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt.
"""
import importlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(HERE))
import prose_refs  # noqa: E402
import refs  # noqa: E402
from _lib import localize, write  # noqa: E402

D = ROOT / "data"
DATE = "2026-10-13"
LANG, LCODE, LCTX = "gsw-u-sd-chzh", "GSW-ZH", "CTX-CH-ZH-GSW-2026"
AUTH = "KI-Entwurf (Claude) vom 2026-10-13 auf Wunsch von Andi Neck; keine fachliche Prüfung erfolgt."
AUTH_GSW = "KI-Entwurf (Claude) vom 2026-10-13; aus dem Hochdeutschen in Züridüütsch gefasst; Mundart noch nicht muttersprachlich geprüft."
CONTEXTS = {"CTX-HIST-BIBLE-FORMATION", "CTX-HIST-ISRAEL-IRON-PERSIAN", "CTX-HIST-SECOND-TEMPLE", "CTX-HIST-EARLY-CHRISTIANITY"}
BOOKS = {b[0] for b in refs.BOOKS}
NEEDS_TRANSLIT = {"heb", "arc", "lat", "akk", "egy", "uga"}


def T(lang, word, de, translit=None):
    return {"lang": lang, "word": word, **({"translit": translit} if translit else {}), "de": de}


def check(n):
    rid = n["id"]
    m = re.fullmatch(r"BG-([0-9A-Z]{3})-BOOK-(\d{4})", rid)
    errs = []
    if not m or m.group(1) != n["book"] or n["book"] not in BOOKS:
        errs.append("ID/Buch passt nicht")
    if n["context"] not in CONTEXTS:
        errs.append(f"Kontext {n['context']}")
    if n["confidence"] not in ("high", "probable", "possible"):
        errs.append("confidence")
    for k in ("topic", "text", "uncertain"):
        if not n.get(k) or not n["gsw"].get(k):
            errs.append(f"{k} fehlt")
    for k in ("text", "uncertain"):
        for src in (n[k], n["gsw"][k]):
            for mk in prose_refs.marks(src):
                if not refs.is_canonical(mk):
                    errs.append(f"Marke {mk}")
            left = prose_refs.unmarked(src)
            if left:
                errs.append(f"unmarkierte Stellen {left}")
    if len(n["gsw"].get("terms", [])) != len(n.get("terms", [])):
        errs.append("Anzahl Fachwörter gsw")
    for t in n.get("terms", []):
        if t["lang"] in NEEDS_TRANSLIT and not t.get("translit"):
            errs.append(f"Umschrift fehlt: {t['word']}")
    for r in n.get("evidence_refs", []):
        if not refs.is_canonical(r):
            errs.append(f"Beleg {r}")
    if errs:
        raise SystemExit(f"{rid}: " + "; ".join(errs))


def run(mods):
    n_written = 0
    count = 0
    for name in mods:
        mod = importlib.import_module(f"buecher.{name}")
        for n in mod.NOTES:
            check(n)
            rid = n["id"]
            rec = {"id": rid, "type": "background_note", "status": "draft", "tags": ["TAG-HISTORICAL-BACKGROUND"],
                   "scope": "book", "context": n["context"], "reference": n["book"], "topic_de": n["topic"],
                   "text_de": n["text"], "confidence": n["confidence"], "uncertain_de": n["uncertain"],
                   "evidence_refs": n.get("evidence_refs", []),
                   **({"sources_de": n["sources"]} if n.get("sources") else {}),
                   **({"terms": n["terms"]} if n.get("terms") else {}),
                   "authorship_de": AUTH, "knowledge": {"asserted_at": DATE, "supersedes": None}}
            n_written += write(D / "background" / "overview" / f"{rid}.json", rec, "Hintergrund überarbeitet")
            g = n["gsw"]
            fields = {"topic_de": g["topic"], "text_de": g["text"], "uncertain_de": g["uncertain"],
                      **({"terms": g["terms"]} if n.get("terms") else {})}
            n_written += localize(rid, rec, fields, LANG, LCODE, LCTX, AUTH_GSW, DATE)
            count += 1
    print(f"PASS: {count} Hintergrundnotizen je Buch aus {len(mods)} Modulen; {n_written} Dateien geschrieben")


if __name__ == "__main__":
    mods = sys.argv[1:] or sorted(p.stem for p in (HERE / "buecher").glob("g*.py"))
    run(mods)
