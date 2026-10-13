#!/usr/bin/env python3
"""Bibelstellen im Fliesstext: sprachneutrale Marken.

In erklärenden Texten (Befunde, Deutungen, Hintergrund, Zusammenfassungen, Lokalisierungen …) stehen
Bibelstellen als Marke mit kanonischer Stelle: ``[[MAT.6.34]]`` oder ``[[MRK.3.28-MRK.3.29]]``.
Die Anzeige («Mt 6,34», «Matt 6:34», «6,34» im selben Buch) erzeugt die App je Sprache; so muss keine
Übersetzung Stellen umschreiben, und jede Sprache kann sie verlinken. Konvention: docs/BIBELSTELLEN.md.

- ``mark(text, ctx)`` wandelt deutsche Schreibweisen in Marken um (für Migration und Autorenwerkzeuge);
  ``ctx`` ist der Buchcode für Stellen ohne Buch («vgl. 6,34»).
- ``marks(text)`` liefert alle Marken eines Texts, ``unmarked(text)`` Stellen, die noch nicht markiert sind.
- ``render(text, lang)`` erzeugt die Anzeige (de: «Mt 6,34», en: «Matt 6:34»).
Nur Standardbibliothek.
"""
import re
import sys

import refs

MARK_RE = re.compile(r"\[\[([1-3]?[A-Z]{2,3}(?:\.\d+){0,2}(?:-[1-3]?[A-Z]{2,3}(?:\.\d+){0,2})?)\]\]")

_NAMES = {}
for code, de, more in refs.BOOKS:
    for n in [de, *more]:
        _NAMES[re.sub(r"[\s.]", "", n).casefold()] = code
_ALT = "|".join(re.escape(n).replace(r"\ ", r"\s*") for n in sorted({n for _, de, more in refs.BOOKS for n in [de, *more]},
                                                                     key=len, reverse=True))
_LEFT = r"(^|[^A-Za-zÄÖÜäöüß0-9\[])"
REF_RE = re.compile(_LEFT + r"(" + _ALT + r")\.?\s+(\d+),(\d+)((?:[–-]\d+(?:,\d+)?)?)((?:\.\d+(?:[–-]\d+)?)*)"
                    r"((?:;\s*\d+,\d+(?:[–-]\d+)?)*)")
# Stellen ohne Buch: nach typischen Einleitungen (Hochdeutsch und Mundart), im Buch des Kontexts
REL_RE = re.compile(r"((?:^|[\s(])(?:\(|vgl\.\s|Vgl\.\s|in\s|In\s|i\s|I\s|siehe\s|lueg\s|a\s|an\s|us\s|aus\s|nach\s|zu\s|bis\s)|\()"
                    r"(\d+),(\d+)((?:[–-]\d+(?:,\d+)?)?)(?!\d|,\d)")
# weitere Stellen direkt nach einer Marke (gleiches Buch): «[[MAT.6.2-MAT.6.4]] und 6,6», «Jes 63,16; 64,7»
CHAIN_RE = re.compile(r"(\[\[([1-3]?[A-Z]{2,3})\.[^\]]*\]\](?:\s*[;,]\s*|\s+(?:und|and)\s+))(\d+),(\d+)((?:[–-]\d+(?:,\d+)?)?)(?!\d|,\d)")


# Ausserbiblische Werke: Stellenangaben dahinter sind keine Bibelstellen («Henochbuch (10,4)», «Didache 8,2»)
NON_BIBLICAL = ("Henoch", "Didache", "Origenes", "Josephus", "Justin", "Avot", "Mischna", "Gebet", "Gebät", "Altertümer", "Tryphon")


def _non_biblical(text, pos):
    return any(w in text[max(0, pos - 30):pos] for w in NON_BIBLICAL)


def _ref(code, c, v, tail):
    c, v = int(c), int(v)
    if not tail:
        return f"{code}.{c}.{v}"
    m = tail[1:].split(",")
    if len(m) == 2:
        return f"{code}.{c}.{v}-{code}.{int(m[0])}.{int(m[1])}"
    return f"{code}.{c}.{v}-{code}.{c}.{int(m[0])}"


def _mk(ref):
    refs.parse(ref)
    return f"[[{ref}]]"


def mark(text, ctx=None):
    """Deutsche Schreibweisen -> Marken. Gibt (neuer Text, [(alt, neu)]) zurück."""
    changes = []

    def absolute(m):
        pre, name, c, v, tail, dots, more = m.groups()
        code = _NAMES.get(re.sub(r"[\s.]", "", name).casefold())
        if not code:
            return m.group(0)
        out = _mk(_ref(code, c, v, tail))
        for d in re.finditer(r"\.(\d+)((?:[–-]\d+)?)", dots):
            out += "." + _mk(_ref(code, c, d.group(1), d.group(2)))
        for r in re.finditer(r"(;\s*)(\d+),(\d+)((?:[–-]\d+)?)", more):
            out += r.group(1) + _mk(_ref(code, r.group(2), r.group(3), r.group(4)))
        changes.append((m.group(0)[len(pre):], out))
        return pre + out

    text = REF_RE.sub(absolute, text)
    if ctx:
        def relative(m):
            if _non_biblical(m.string, m.start()):
                return m.group(0)
            out = _mk(_ref(ctx, *m.groups()[1:]))
            changes.append((m.group(0)[len(m.group(1)):], out))
            return m.group(1) + out
        text = REL_RE.sub(relative, text)
    while True:
        def chain(m):
            out = _mk(_ref(m.group(2), m.group(3), m.group(4), m.group(5)))
            changes.append((m.group(0)[len(m.group(1)):], out))
            return m.group(1) + out
        new = CHAIN_RE.sub(chain, text)
        if new == text:
            break
        text = new
    return text, changes


def marks(text):
    return MARK_RE.findall(text or "")


def unmarked(text):
    """Stellen in deutscher Schreibweise, die (noch) nicht markiert sind."""
    rest = MARK_RE.sub("", text or "")
    return [m.group(0).strip() for m in REF_RE.finditer(rest)]


SHORT = {"de": refs.DISPLAY_DE}


def render(text, lang="de", ctx=None):
    """Marken -> Anzeige. Im Kontextbuch ohne Buchname; Folgestellen im selben Buch/Kapitel verkürzt."""
    names = SHORT.get(lang, refs.DISPLAY_DE)
    sep = ":" if lang == "en" else ","
    out, last, prev_end = [], None, 0
    for m in MARK_RE.finditer(text or ""):
        (b, c1, v1), (_, c2, v2) = refs.parse(m.group(1))
        between = text[prev_end:m.start()]
        if last and last[0] == b and last[1] == c1 and between == ".":
            head = f"{v1}"
        elif (last and last[0] == b and re.fullmatch(r"\s*(;|,|und|and|oder)\s*", between)) or b == ctx:
            head = f"{c1}{sep}{v1}" if v1 else f"{c1}"
        else:
            head = f"{names[b]} {c1}" + (f"{sep}{v1}" if v1 else "")
        tail = "" if (c1, v1) == (c2, v2) else (f"–{v2}" if c1 == c2 else f"–{c2}{sep}{v2}")
        out.append(between + head + tail)
        last, prev_end = (b, c2), m.end()
    out.append((text or "")[prev_end:])
    return "".join(out)


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        t, ch = mark(arg, "MAT")
        print(t, "→", render(t, ctx="MAT"))
