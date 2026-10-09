#!/usr/bin/env python3
"""Kanonische Bibelstellen: Parser, Prüfung und deutsche Anzeige.

Konvention siehe docs/BIBELSTELLEN.md. Gespeichert wird ausschliesslich die
kanonische Form (z. B. ``MRK.3.29`` oder ``MRK.3.22-MRK.3.30``); deutsche
Schreibweisen wie «Mk 3,29» sind reine Anzeige.

Nur Standardbibliothek. Aufruf zum Ausprobieren:
    python3 scripts/refs.py "Mk 3,22–30" "Mt 12:22-32" MRK.3.29
"""
import re
import sys

# (USFM-Code, deutsche Anzeige nach Loccumer Richtlinien, weitere Eingabe-Aliasse)
BOOKS = [
    ("GEN", "Gen", ["1Mose", "1 Mose", "Genesis"]),
    ("EXO", "Ex", ["2Mose", "2 Mose", "Exodus", "Exod"]),
    ("LEV", "Lev", ["3Mose", "3 Mose", "Levitikus", "Leviticus"]),
    ("NUM", "Num", ["4Mose", "4 Mose", "Numeri", "Numbers"]),
    ("DEU", "Dtn", ["5Mose", "5 Mose", "Deuteronomium", "Deut", "Deuteronomy"]),
    ("JOS", "Jos", ["Josua", "Joshua", "Josh"]),
    ("JDG", "Ri", ["Richter", "Judges", "Judg"]),
    ("RUT", "Rut", ["Ruth"]),
    ("1SA", "1 Sam", ["1Sam", "1 Samuel", "1Samuel"]),
    ("2SA", "2 Sam", ["2Sam", "2 Samuel", "2Samuel"]),
    ("1KI", "1 Kön", ["1Kön", "1 Koen", "1Koen", "1 Kings", "1Kgs"]),
    ("2KI", "2 Kön", ["2Kön", "2 Koen", "2Koen", "2 Kings", "2Kgs"]),
    ("1CH", "1 Chr", ["1Chr", "1 Chronik", "1 Chronicles"]),
    ("2CH", "2 Chr", ["2Chr", "2 Chronik", "2 Chronicles"]),
    ("EZR", "Esra", ["Esr", "Ezra"]),
    ("NEH", "Neh", ["Nehemia", "Nehemiah"]),
    ("EST", "Est", ["Ester", "Esther"]),
    ("JOB", "Ijob", ["Hiob", "Hi", "Job"]),
    ("PSA", "Ps", ["Psalm", "Psalmen", "Psalms", "Pss"]),
    ("PRO", "Spr", ["Sprüche", "Sprueche", "Proverbs", "Prov"]),
    ("ECC", "Koh", ["Kohelet", "Prediger", "Pred", "Ecclesiastes", "Eccl"]),
    ("SNG", "Hld", ["Hoheslied", "Song", "Song of Songs"]),
    ("ISA", "Jes", ["Jesaja", "Isaiah", "Isa"]),
    ("JER", "Jer", ["Jeremia", "Jeremiah"]),
    ("LAM", "Klgl", ["Klagelieder", "Lamentations", "Lam"]),
    ("EZK", "Ez", ["Ezechiel", "Hesekiel", "Hes", "Ezekiel", "Ezek"]),
    ("DAN", "Dan", ["Daniel"]),
    ("HOS", "Hos", ["Hosea"]),
    ("JOL", "Joel", []),
    ("AMO", "Am", ["Amos"]),
    ("OBA", "Obd", ["Obadja", "Obadiah", "Obad"]),
    ("JON", "Jona", ["Jonah"]),
    ("MIC", "Mi", ["Micha", "Micah", "Mic"]),
    ("NAM", "Nah", ["Nahum"]),
    ("HAB", "Hab", ["Habakuk", "Habakkuk"]),
    ("ZEP", "Zef", ["Zefanja", "Zephaniah", "Zeph"]),
    ("HAG", "Hag", ["Haggai"]),
    ("ZEC", "Sach", ["Sacharja", "Zechariah", "Zech"]),
    ("MAL", "Mal", ["Maleachi", "Malachi"]),
    ("TOB", "Tob", ["Tobit"]),
    ("JDT", "Jdt", ["Judit", "Judith"]),
    ("WIS", "Weish", ["Weisheit", "Wisdom", "Wis"]),
    ("SIR", "Sir", ["Jesus Sirach", "Sirach"]),
    ("BAR", "Bar", ["Baruch"]),
    ("1MA", "1 Makk", ["1Makk", "1 Maccabees", "1Macc"]),
    ("2MA", "2 Makk", ["2Makk", "2 Maccabees", "2Macc"]),
    ("MAT", "Mt", ["Matthäus", "Matthaeus", "Matthew", "Matt"]),
    ("MRK", "Mk", ["Markus", "Mark", "Mar"]),
    ("LUK", "Lk", ["Lukas", "Luke"]),
    ("JHN", "Joh", ["Johannes", "John", "Jn"]),
    ("ACT", "Apg", ["Apostelgeschichte", "Acts"]),
    ("ROM", "Röm", ["Roem", "Römer", "Romans", "Rom"]),
    ("1CO", "1 Kor", ["1Kor", "1 Korinther", "1 Corinthians", "1Cor"]),
    ("2CO", "2 Kor", ["2Kor", "2 Korinther", "2 Corinthians", "2Cor"]),
    ("GAL", "Gal", ["Galater", "Galatians"]),
    ("EPH", "Eph", ["Epheser", "Ephesians"]),
    ("PHP", "Phil", ["Philipper", "Philippians"]),
    ("COL", "Kol", ["Kolosser", "Colossians", "Col"]),
    ("1TH", "1 Thess", ["1Thess", "1 Thessalonicher", "1 Thessalonians"]),
    ("2TH", "2 Thess", ["2Thess", "2 Thessalonicher", "2 Thessalonians"]),
    ("1TI", "1 Tim", ["1Tim", "1 Timotheus", "1 Timothy"]),
    ("2TI", "2 Tim", ["2Tim", "2 Timotheus", "2 Timothy"]),
    ("TIT", "Tit", ["Titus"]),
    ("PHM", "Phlm", ["Philemon", "Phlm"]),
    ("HEB", "Hebr", ["Hebräer", "Hebraeer", "Hebrews", "Heb"]),
    ("JAS", "Jak", ["Jakobus", "James", "Jas"]),
    ("1PE", "1 Petr", ["1Petr", "1 Petrus", "1 Peter", "1Pet"]),
    ("2PE", "2 Petr", ["2Petr", "2 Petrus", "2 Peter", "2Pet"]),
    ("1JN", "1 Joh", ["1Joh", "1 John"]),
    ("2JN", "2 Joh", ["2Joh", "2 John"]),
    ("3JN", "3 Joh", ["3Joh", "3 John"]),
    ("JUD", "Jud", ["Judas", "Jude"]),
    ("REV", "Offb", ["Offenbarung", "Apk", "Revelation", "Rev"]),
]

CODES = {code for code, _, _ in BOOKS}
DISPLAY_DE = {code: de for code, de, _ in BOOKS}

def _norm(name):
    return re.sub(r"[\s.]", "", name).casefold()

ALIASES = {}
for _code, _de, _more in BOOKS:
    for _name in [_code, _de, *_more]:
        ALIASES[_norm(_name)] = _code

# Kanonische Formen
_POINT = r"(?P<{p}b>[1-3]?[A-Z]{{2,3}})(?:\.(?P<{p}c>[1-9]\d*)(?:\.(?P<{p}v>[1-9]\d*))?)?"
POINT_RE = re.compile(r"^" + _POINT.format(p="") + r"$")
RANGE_RE = re.compile(r"^" + _POINT.format(p="s") + "-" + _POINT.format(p="e") + r"$")


class RefError(ValueError):
    pass


def _point(m, p=""):
    b, c, v = m.group(p + "b"), m.group(p + "c"), m.group(p + "v")
    if b not in CODES:
        raise RefError(f"unbekannter Buchcode {b!r}")
    return (b, int(c) if c else None, int(v) if v else None)


def parse(ref):
    """Kanonische Stelle -> (start, end); start/end = (buch, kapitel|None, vers|None).
    Wirft RefError bei nicht kanonischer oder ungültiger Form."""
    if not isinstance(ref, str):
        raise RefError(f"Stelle muss Text sein: {ref!r}")
    m = POINT_RE.match(ref)
    if m:
        p = _point(m)
        return p, p
    m = RANGE_RE.match(ref)
    if not m:
        raise RefError(f"keine kanonische Stelle: {ref!r}")
    s, e = _point(m, "s"), _point(m, "e")
    if s[0] != e[0]:
        raise RefError(f"Bereich über Buchgrenzen nicht erlaubt: {ref!r}")
    if (s[1] is None) != (e[1] is None) or (s[2] is None) != (e[2] is None):
        raise RefError(f"Bereichsenden mit unterschiedlicher Genauigkeit: {ref!r}")
    if (s[1] or 0, s[2] or 0) >= (e[1] or 0, e[2] or 0):
        raise RefError(f"Bereichsende liegt nicht nach dem Anfang: {ref!r}")
    return s, e


def is_canonical(ref):
    try:
        parse(ref)
        return True
    except RefError:
        return False


def _fmt(b, c, v):
    return b + (f".{c}" if c else "") + (f".{v}" if v else "")


def canonical(text, default_book=None):
    """Lockere Eingabe (deutsch/englisch/kanonisch) -> kanonische Form.
    Beispiele: «Mk 3,22–30», «Mark 3:29», «Mt 12:22-32», «3:22» (mit default_book)."""
    t = text.strip().replace("–", "-").replace("—", "-")
    if is_canonical(t):
        return t
    m = re.match(r"^(?:(?P<book>(?:[1-3]\s*)?[^\W\d_][^\d]*?)\s*)?"
                 r"(?P<c1>\d+)(?:[,:.](?P<v1>\d+))?"
                 r"(?:\s*-\s*(?:(?P<c2>\d+)[,:.])?(?P<v2>\d+))?$", t)
    if not m:
        raise RefError(f"Stelle nicht erkannt: {text!r}")
    if m.group("book"):
        code = ALIASES.get(_norm(m.group("book")))
        if not code:
            raise RefError(f"Buch nicht erkannt: {m.group('book')!r}")
    elif default_book in CODES:
        code = default_book
    else:
        raise RefError(f"Buch fehlt: {text!r}")
    c1, v1, c2, v2 = (int(x) if x else None for x in m.group("c1", "v1", "c2", "v2"))
    start = _fmt(code, c1, v1)
    if v2 is None:
        result = start
    elif v1 is None:  # «Ps 23-24» = Kapitelbereich
        if c2 is not None:
            raise RefError(f"Stelle nicht erkannt: {text!r}")
        result = f"{start}-{_fmt(code, v2, None)}"
    else:
        result = f"{start}-{_fmt(code, c2 or c1, v2)}"
    parse(result)
    return result


def display_de(ref):
    """Kanonische Stelle -> deutsche Anzeige, z. B. MRK.3.22-MRK.3.30 -> «Mk 3,22–30»."""
    (b, c1, v1), (_, c2, v2) = parse(ref)
    head = DISPLAY_DE[b]
    if c1 is None:
        return head
    one = f"{head} {c1}" + (f",{v1}" if v1 else "")
    if (c1, v1) == (c2, v2):
        return one
    if v1 is None:
        return f"{one}–{c2}"
    if c1 == c2:
        return f"{one}–{v2}"
    return f"{one}–{c2},{v2}"


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        try:
            ref = canonical(arg)
            print(f"{arg!r:28} -> {ref:24} ({display_de(ref)})")
        except RefError as exc:
            print(f"{arg!r:28} -> FEHLER: {exc}")
