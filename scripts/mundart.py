#!/usr/bin/env python3
"""Prüft Züridüütsch-Texte gegen die Regeln in docs/ZUERIDUEUETSCH.md.

Maschinell prüfbar sind Sonderzeichen der Dieth-Schreibung (è, ò, ù, ì; Umschriften wie ā oder ô bleiben erlaubt), die Wortliste (abgelöste Form -> gültige Form) und einige Muster (hochdeutsches
Präteritum, «um z», Apostroph, Genitiv). Wortwahl und Satzbau prüft eine getrennte Instanz gegen das Dokument.

  python3 scripts/mundart.py            Übersicht je Buch und Regel
  python3 scripts/mundart.py JHN        Einzelfunde eines Buchs (Bibeltext und Lokalisierungen)
  python3 scripts/mundart.py --text "…" einen Text prüfen

Als Modul: pruefe(text) -> Liste (gefunden, Regel, Vorschlag).
"""
import glob
import json
import os
import re
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Abgelöste Form -> gültige Form, je mit Regel (Abschnitt in docs/ZUERIDUEUETSCH.md). Kleinschreibung; Gross am
# Satzanfang wird mitgeprüft.
WORTLISTE = {
    # 1.3 Dehnungs-h wie im Hochdeutschen
    "fäält": ("fehlt", "1.3"), "fääle": ("fehle", "1.3"), "jaar": ("jahr", "1.3"), "jaare": ("jahre", "1.3"),
    "oore": ("ohre", "1.3"), "oor": ("ohr", "1.3"), "loon": ("lohn", "1.3"), "söön": ("söhn", "1.3"),
    "soon": ("sohn", "1.3"), "ooni": ("ohni", "1.3"), "gsee": ("gseh", "1.3"), "gschee": ("gscheh", "1.3"),
    "leere": ("lehre", "1.3"), "leert": ("lehrt", "1.3"), "gleert": ("glehrt", "1.3"), "leerer": ("lehrer", "1.3"),
    "gläämt": ("glähmt", "1.3"), "gläämte": ("glähmte", "1.3"), "faare": ("fahre", "1.3"), "faart": ("fahrt", "1.3"),
    "gfaare": ("gfahre", "1.3"), "waar": ("wahr", "1.3"), "waarhäit": ("wahrheit", "1.3"), "zie": ("zieh", "1.3"),
    "ziend": ("ziehnd", "1.3"),
    # 1.4 ei statt äi
    "gsäit": ("gseit", "1.4"), "säit": ("seit", "1.4"), "zwäi": ("zwei", "1.4"), "gäischt": ("geischt", "1.4"),
    "häilig": ("heilig", "1.4"), "häilige": ("heilige", "1.4"), "käi": ("kei", "1.4"), "äis": ("eis", "1.4"),
    # 1.5 ie nur Zwielaut
    "wieder": ("wider", "1.5"), "viel": ("vil", "1.5"), "vieli": ("vili", "1.5"), "spiele": ("spile", "1.5"),
    # 1.10 Partizip ohne gg-/gch-
    "ggää": ("gää", "1.10"), "ggange": ("gange", "1.10"), "ggässe": ("gässe", "1.10"), "gchauft": ("kauft", "1.10"),
    "praacht": ("bracht", "1.10"), "ggäh": ("gää", "1.10"),
    # Entscheid Mänsch
    "mäntsch": ("mänsch", "Entscheid"), "mäntsche": ("mänsche", "Entscheid"),
    # 2 Formen
    "üs": ("öis", "2"), "üse": ("öise", "2"), "üsi": ("öisi", "2"), "üses": ("öises", "2"), "üsere": ("öisere", "2"),
    "üsem": ("öisem", "2"), "sie": ("si", "2"), "ihr": ("ir / ire", "2"), "nüt": ("nüüt", "2"), "öpis": ("öppis", "2"),
    "gsi": ("gsii", "2"),
    "eu": ("öi", "2"), "euch": ("öi", "2"), "eue": ("öie", "2"), "eui": ("öii", "2"), "wer": ("wär", "2"),
    "demit": ("damit", "2"), "tämpel": ("tempel", "3"), "ärde": ("erde", "1.6"), "drüü": ("drü", "2"),
    "brocht": ("bracht", "1.10"), "gha": ("ghaa", "2"), "brüedere": ("brüeder", "3"),
    # 3 Wortwahl: falsche Vermundartlichung
    "gfüel": ("gfühl", "3"), "stuefe": ("stufe", "3"),
    # Präteritum (2 Verb)
    "war": ("isch … gsii", "2 Präteritum"), "waren": ("sind … gsii", "2 Präteritum"),
    "hatte": ("hät … ghaa", "2 Präteritum"), "hatten": ("händ … ghaa", "2 Präteritum"),
    "kam": ("isch … choo", "2 Präteritum"), "kamen": ("sind … choo", "2 Präteritum"),
    "sagte": ("hät … gseit", "2 Präteritum"), "sagten": ("händ … gseit", "2 Präteritum"),
    "ging": ("isch … gange", "2 Präteritum"), "gingen": ("sind … gange", "2 Präteritum"),
    "sprach": ("hät … gseit", "2 Präteritum"), "wurde": ("isch … worde", "2 Präteritum"),
    "wurden": ("sind … worde", "2 Präteritum"),
}

MUSTER = [
    (re.compile(r"[èòùì]"), "Sonderzeichen", "1.1", "nur ä, ö, ü"),
    (re.compile(r"\bum z\b", re.I), "um z", "2 Infinitiv", "zum / damit"),
    (re.compile(r"[A-Za-zäöü]['’][A-Za-zäöü]|(?<![A-Za-zäöü])['’]s\b|\b[sdz]['’]"), "Apostroph", "1.11", "ohne Apostroph"),
    (re.compile(r"\bdes\b"), "Genitiv «des»", "2 Genitiv", "vo + Dativ"),
]

_WORT = re.compile(r"[A-Za-zÄÖÜäöüÀ-ÿ]+")


def pruefe(text):
    """Funde in einem Mundart-Text: Liste (gefunden, Regel, Vorschlag)."""
    funde = []
    for w in _WORT.findall(text or ""):
        k = w.lower()
        if k in WORTLISTE:
            neu, regel = WORTLISTE[k]
            if regel == "2 Präteritum" and w[0].isupper():
                continue  # «Sprach», «War» als Nomen; Präteritum am Satzanfang fängt die getrennte Prüfung
            funde.append((w, regel, neu))
    for rx, was, regel, neu in MUSTER:
        for m in rx.finditer(text or ""):
            funde.append((m.group(0), regel, neu))
    return funde


_OHNE = {"id", "type", "status", "tags", "reference", "language", "subject", "subjects", "revision_log", "knowledge",
         "authorship_de", "check", "localizes", "target", "field", "fields_source"}


def _strings(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for k, v in o.items():
            if k not in _OHNE:
                yield from _strings(v)
    elif isinstance(o, list):
        for v in o:
            yield from _strings(v)


def _buch(name):
    m = re.search(r"-(\d?[A-Z]{2,3})-", name)
    return m.group(1) if m else "?"


def korpus():
    """(Buch, Art, Stelle, Text) für alle Züridüütsch-Texte."""
    for f in sorted(glob.glob(os.path.join(ROOT, "data/translations/*GSW*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        for ref, t in d.get("text_by_reference", {}).items():
            yield ref.split(".")[0], "Bibeltext", ref, t
    for f in sorted(glob.glob(os.path.join(ROOT, "data/localizations/gsw-u-sd-chzh/*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        name = os.path.basename(f)[:-5]
        for t in _strings(d.get("fields", d)):
            yield _buch(name), "Lokalisierung", name, t


def main(argv):
    if len(argv) > 1 and argv[1] == "--text":
        for f in pruefe(" ".join(argv[2:])):
            print(*f, sep="\t")
        return
    nur = argv[1] if len(argv) > 1 else None
    tab = defaultdict(Counter)
    for buch, art, wo, text in korpus():
        if nur and buch != nur:
            continue
        for gef, regel, neu in pruefe(text):
            tab[(buch, art)][regel] += 1
            if nur:
                print(f"{wo}\t{gef} -> {neu}\t[{regel}]")
    if not nur:
        regeln = sorted({r for c in tab.values() for r in c})
        print("Buch Art".ljust(24) + " ".join(r[:12].rjust(12) for r in regeln))
        for (buch, art), c in sorted(tab.items()):
            print(f"{buch} {art}".ljust(24) + " ".join(str(c[r]).rjust(12) for r in regeln))
        print("Summe".ljust(24) + " ".join(str(sum(c[r] for c in tab.values())).rjust(12) for r in regeln))


if __name__ == "__main__":
    main(sys.argv)
