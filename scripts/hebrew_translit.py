#!/usr/bin/env python3
"""Lesehilfe: punktiertes Hebräisch in eine einfache, deutsch lesbare Umschrift.

Zweck: Aussprachehilfe für Leserinnen und Leser ohne Hebräischkenntnisse (wie die griechische Umschrift im
App), keine wissenschaftliche Transliteration. Die wissenschaftliche Umschrift von MACULA Hebrew bleibt
daneben in den Annotationen erhalten.

Regeln (vereinfacht, nach der heute üblichen Aussprache):
- Konsonanten deutsch: ב b/w, ג g, ד d, ה h, ו w, ז s, ח ch, ט t, י j, כ k/ch, ל l, מ m, נ n, ס s, ע ʿ, פ p/f,
  צ z, ק k, ר r, שׁ sch, שׂ s, ת t; א und ע im Wortinneren als ʾ bzw. ʿ, am Wortanfang nicht geschrieben.
- Begadkefat (ב כ פ) ohne Dagesch als w, ch, f; Dagesch forte verdoppelt den Konsonanten.
- Vokale: Patach/Qamez a, Segol/Zere e, Chireq i, Cholem o, Qubbuz/Schuruq u, Qamez chatuf o; Chatef-Vokale
  a/e/o; Schwa am Wortanfang, unter verdoppeltem Konsonanten und nach einem stillen Schwa als e, sonst stumm.
- Lesemütter (י nach i/e, ו als o/u, ה am Wortende ohne Mappiq, stummes א) werden nicht eigens geschrieben.
- Der Gottesname יהוה wird als «JHWH» wiedergegeben (in der jüdischen Lesung «Adonai»).
- Akzente (Teamim) und Meteg werden ignoriert; Maqqef wird zu «-».
Nur Standardbibliothek.
"""
import re
import sys
import unicodedata

ACCENTS = re.compile("[֑-ֽֿ֯׀׃ׅׄ׆]")
SHEVA, HATAF_E, HATAF_A, HATAF_O = "ְ", "ֱ", "ֲ", "ֳ"
HIRIQ, TSERE, SEGOL, PATAH, QAMATS, HOLAM, HOLAM_HASER, QUBUTS = "ִ", "ֵ", "ֶ", "ַ", "ָ", "ֹ", "ֺ", "ֻ"
DAGESH, SHIN_DOT, SIN_DOT, QAMATS_QATAN = "ּ", "ׁ", "ׂ", "ׇ"
VOWELS = {SHEVA: "", HATAF_E: "e", HATAF_A: "a", HATAF_O: "o", HIRIQ: "i", TSERE: "e", SEGOL: "e", PATAH: "a",
          QAMATS: "a", HOLAM: "o", HOLAM_HASER: "o", QUBUTS: "u", QAMATS_QATAN: "o"}
CONS = {"א": "ʾ", "ב": "b", "ג": "g", "ד": "d", "ה": "h", "ו": "w", "ז": "s", "ח": "ch", "ט": "t", "י": "j",
        "כ": "k", "ך": "k", "ל": "l", "מ": "m", "ם": "m", "נ": "n", "ן": "n", "ס": "s", "ע": "ʿ", "פ": "p", "ף": "p",
        "צ": "z", "ץ": "z", "ק": "k", "ר": "r", "ש": "sch", "ת": "t"}
SOFT = {"ב": "w", "כ": "ch", "ך": "ch", "פ": "f", "ף": "f"}
BGDKPT = set("בגדכךפףת")
GUTTURAL = set("אהחער")


def _letters(word):
    """Wort -> Liste (Buchstabe, Zeichenmenge)."""
    out = []
    for ch in word:
        if "א" <= ch <= "ת":
            out.append([ch, set()])
        elif out and ("ְ" <= ch <= "ׇ"):
            out[-1][1].add(ch)
    return out


def _cons(text):
    return re.sub("[^א-ת]", "", text)


def _word(word):
    cons_only = _cons(word)
    if cons_only == "יהוה":
        return "JHWH"
    if cons_only.endswith("יהוה"):  # Gottesname mit Vorsilbe (לַיהוָה)
        k = max(i for i, ch in enumerate(word) if ch == "י" and _cons(word[i:]) == "יהוה")
        return _word(word[:k]) + "-JHWH"
    if cons_only == "כל" and QAMATS in word:  # kol (Qamez chatuf vor Maqqef)
        return ("k" if DAGESH in word else "ch") + "ol"
    L = _letters(word)
    res, prev_vowel, prev_silent_sheva = [], False, False
    for i, (c, m) in enumerate(L):
        last = i == len(L) - 1
        vowel = next((VOWELS[x] for x in (SHEVA, HATAF_E, HATAF_A, HATAF_O, HIRIQ, TSERE, SEGOL, PATAH, QAMATS,
                                          HOLAM, HOLAM_HASER, QUBUTS, QAMATS_QATAN) if x in m and x != SHEVA), None)
        has_sheva = SHEVA in m
        # Lesemütter und Vokalbuchstaben
        if c == "ו" and DAGESH in m and vowel is None and not has_sheva:
            res.append("u"); prev_vowel = True; prev_silent_sheva = False; continue
        if c == "ו" and HOLAM in m and vowel == "o" and i > 0 and len(m) == 1:
            res.append("o"); prev_vowel = True; prev_silent_sheva = False; continue
        nxt = L[i + 1] if i + 1 < len(L) else None
        vav_vowel = nxt is not None and nxt[0] == "ו" and (HOLAM in nxt[1] or (DAGESH in nxt[1] and len(nxt[1]) == 1))
        if c == "י" and vowel is None and not has_sheva and DAGESH not in m and i > 0 and res and res[-1] in ("i", "e") and not last and not vav_vowel:
            continue
        if c == "י" and vowel is None and not has_sheva and nxt is not None and nxt[0] == "ו" and i + 1 == len(L) - 1 and not nxt[1] and res and res[-1] == "a":
            continue  # -ָיו = -aw
        if c == "י" and vowel is None and not has_sheva and last and res and res[-1] in ("i", "e"):
            continue
        if c == "ה" and last and DAGESH not in m and vowel is None and not has_sheva:
            continue
        if c == "א" and vowel is None and not has_sheva:
            continue
        # Konsonant
        if c == "ש":
            cons = "s" if SIN_DOT in m else "sch"
        elif c in SOFT and DAGESH not in m:
            cons = SOFT[c]
        else:
            cons = CONS[c]
        if c in ("א", "ע") and i == 0:
            cons = ""
        forte = DAGESH in m and i > 0 and prev_vowel and c not in GUTTURAL and not (c == "ה" and last)
        if forte and len(cons) == 1:
            cons = cons + cons
        # Patach furtivum am Wortende (ruach)
        if last and c in ("ח", "ע", "ה") and PATAH in m and not has_sheva and res and res[-1][-1:] not in ("a",):
            res.append("a" + cons); prev_vowel = True; continue
        res.append(cons)
        if PATAH in m and HIRIQ in m:  # Jeruschalajim (Ketiv/Qere perpetuum)
            res.append("aji"); prev_vowel = True; prev_silent_sheva = False; continue
        if vowel:
            res.append(vowel); prev_vowel = True; prev_silent_sheva = False
        elif has_sheva:
            vocal = i == 0 or forte or prev_silent_sheva
            if vocal:
                res.append("e"); prev_vowel = True; prev_silent_sheva = False
            else:
                prev_vowel = False; prev_silent_sheva = True
        else:
            prev_vowel = False; prev_silent_sheva = False
    out = "".join(res)
    return out


def translit(text):
    t = ACCENTS.sub("", unicodedata.normalize("NFD", text or ""))
    t = unicodedata.normalize("NFC", t)
    parts = re.split(r"(\s+|־)", t)
    return "".join("-" if p == "־" else (p if p.isspace() else _word(p)) for p in parts).replace("׃", "").strip()


if __name__ == "__main__":
    for a in sys.argv[1:]:
        print(a, "→", translit(a))
