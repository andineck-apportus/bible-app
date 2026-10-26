#!/usr/bin/env python3
"""Autorenwerkzeug: Bildstil «Symbol» – Darstellungen der Lexikon-Einträge und Bilder zu den Bildaufträgen.

Schichten (docs/BILDSPRACHE.md):
1. Bildlexikon (data/illustrations/lexicon/FIG-*.json, stilunabhängig): wer/was, Pflichtmerkmale.
2. Bildauftrag (data/illustrations/briefs/BRIEF-*.json, stilunabhängig): wer, was, wer zu wem, Reihenfolge.
3. Stil (hier «Symbol»): `renderings` ordnet jedem Lexikon-Eintrag ein Bauteil der SVG-Bibliothek zu
   (data/illustrations/symbol/_bibliothek.svg); die Bilder werden hier aus den Bauteilen zusammengesetzt und als SVG geschrieben.

Die Bildfelder folgen den Feldern des Bildauftrags (Nummer oben links). Personen ohne Gesicht; Gott nie als Mensch.
Jedes Bild ist Deutung (siehe interpretation_note_de im Auftrag). Prüfung auf Verständlichkeit: `check` im Bild-Datensatz.

Aufruf: python3 scripts/authoring/bilder_symbol.py
KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck; eigene Zeichnungen (CC0), keine fachliche Prüfung.
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _bubble import bubble_path  # noqa: E402
from _lib import D, localize, write  # noqa: E402

DATE = "2026-10-14"
AUTH = "KI-Entwurf (Claude) vom 2026-10-14 auf Wunsch von Andi Neck; eigene Zeichnung, keine fachliche Prüfung."
AUTH_GSW = "KI-Entwurf (Claude) vom 2026-10-14; Mundart noch nicht muttersprachlich geprüft."
LIC = "CC0 1.0 (eigene Zeichnung)"
OUT = D / "illustrations/symbol"

# Lexikon-Eintrag -> Bauteil der Bibliothek (nur, was dieser Stil schon zeichnet)
RENDER = {
    "FIG-JESUS": "ill-p-jesus", "FIG-MARIA-MUTTER-JESU": "ill-p-maria", "FIG-ROLLE-JUENGER": "ill-p-juenger",
    "FIG-ROLLE-BRAUT": "ill-p-braut", "FIG-ROLLE-BRAEUTIGAM": "ill-p-braeutigam", "FIG-ROLLE-GAST": "ill-p-gast",
    "FIG-GRUPPE-MENGE": "ill-p-menge", "FIG-ROLLE-DIENER": "ill-p-diener", "FIG-ROLLE-SPEISEMEISTER": "ill-p-meister",
    "FIG-ROLLE-HAENDLER": "ill-p-haendler", "FIG-OBJ-KRUG-WASSER": "ill-jar", "FIG-OBJ-KRUG-WEIN": "ill-jar-wein",
    "FIG-OBJ-KRUG-WEIN-LEER": "ill-jar-leer", "FIG-OBJ-BECHER-LEER": "ill-becher-leer", "FIG-OBJ-BECHER-VOLL": "ill-becher",
    "FIG-ORT-TEMPEL": "ill-tempel", "FIG-OBJ-TAUBE": "ill-taube-kaefig", "FIG-OBJ-PEITSCHE": "ill-peitsche",
    "FIG-OBJ-SCHAF": "ill-schaf", "FIG-OBJ-MUENZEN": "ill-muenzen", "FIG-OBJ-SCHRIFTROLLE": "ill-schriftrolle",
    "FIG-ZEICHEN-STERN": "ill-zeichen", "FIG-ZEICHEN-FEHLT": "ill-z-fehlt", "FIG-ZEICHEN-STUNDE": "ill-z-stunde",
    "FIG-ZEICHEN-HOEREN": "ill-z-hoeren", "FIG-ZEICHEN-GLAUBEN": "ill-z-glauben", "FIG-ZEICHEN-FREUDE": "ill-z-freude",
    "FIG-ZEICHEN-FRAGEN": "ill-z-frage", "FIG-ZEICHEN-BRINGEN": "ill-z-pfeil", "FIG-ZEICHEN-ABSTAND": "ill-z-abstand",
    "FIG-ZEICHEN-HOCHZEIT": "ill-z-hochzeit", "FIG-ZEICHEN-TAGE": "ill-sonne", "FIG-ZEICHEN-NIEDERREISSEN": "ill-tempel-riss",
    "FIG-ZEICHEN-LICHT": "ill-licht", "FIG-SYMBOL-ADLER": "ill-adler",
    "FIG-GOTT": "ill-gott", "FIG-HEILIGER-GEIST": "ill-geist", "FIG-MOSE": "ill-p-mose", "FIG-PAULUS": "ill-p-paulus",
    "FIG-ROLLE-PROPHET": "ill-p-prophet", "FIG-ROLLE-KOENIG": "ill-p-koenig", "FIG-ROLLE-SOLDAT": "ill-p-soldat",
    "FIG-OBJ-KREUZ": "ill-kreuz", "FIG-ORT-GRAB": "ill-grab", "FIG-ORT-JERUSALEM": "ill-jerusalem", "FIG-ORT-BERG": "ill-berg",
    "FIG-ORT-HAUS": "ill-haus", "FIG-ORT-WEG": "ill-weg", "FIG-OBJ-BOOT": "ill-boot", "FIG-OBJ-GESETZESTAFELN": "ill-tafeln",
    "FIG-ORT-MEER": "ill-meer", "FIG-ZEICHEN-SCHOEPFUNG": "ill-schoepfung", "FIG-OBJ-LEIER": "ill-leier",
    "FIG-ZEICHEN-HOFFNUNG": "ill-z-hoffnung", "FIG-ZEICHEN-UMKEHR": "ill-z-umkehr", "FIG-ZEICHEN-GERICHT": "ill-z-gericht",
    "FIG-ZEICHEN-NEUE-SCHOEPFUNG": "ill-neue-schoepfung", "FIG-ZEICHEN-EXIL": "ill-z-exil", "FIG-ZEICHEN-AUSBREITEN": "ill-z-ausbreiten",
    "FIG-OBJ-BRIEF": "ill-brief", "FIG-GRUPPE-GEMEINDE": "ill-gemeinde", "FIG-ZEICHEN-BETEN": "ill-z-beten", "FIG-ZEICHEN-TRAUER": "ill-z-trauer",
}
VB = {"ill-p": "0 0 30 64", "ill-jar": "0 0 30 56", "ill-jar-wein": "0 0 30 56", "ill-jar-leer": "0 0 40 56", "ill-becher": "0 0 12 14",
      "ill-becher-leer": "0 0 12 14", "ill-tempel": "0 0 200 150", "ill-tempel-riss": "0 0 200 150", "ill-taube-tier": "0 0 40 26",
      "ill-taube-kaefig": "0 0 40 40", "ill-peitsche": "0 0 22 26", "ill-schaf": "0 0 34 22", "ill-muenzen": "0 0 24 14",
      "ill-schriftrolle": "0 0 44 30", "ill-zeichen": "0 0 20 20", "ill-z-fehlt": "0 0 20 20", "ill-z-stunde": "0 0 16 22",
      "ill-z-hoeren": "0 0 26 22", "ill-z-glauben": "0 0 22 24", "ill-z-freude": "0 0 24 16", "ill-z-frage": "0 0 12 20",
      "ill-z-pfeil": "0 0 20 10", "ill-z-abstand": "0 0 8 60", "ill-z-hochzeit": "0 0 44 18", "ill-jesus-kopf": "0 0 24 24",
      "ill-sonne": "0 0 16 16", "ill-licht": "0 0 40 40", "ill-adler": "0 0 120 84", "ill-gott": "0 0 60 60", "ill-geist": "0 0 40 40",
      "ill-kreuz": "0 0 30 44", "ill-grab": "0 0 64 44", "ill-jerusalem": "0 0 80 56", "ill-berg": "0 0 80 50", "ill-haus": "0 0 40 36",
      "ill-weg": "0 0 80 30", "ill-boot": "0 0 50 40", "ill-tafeln": "0 0 30 28", "ill-meer": "0 0 90 50", "ill-schoepfung": "0 0 60 50",
      "ill-leier": "0 0 24 30", "ill-z-hoffnung": "0 0 24 24", "ill-z-umkehr": "0 0 24 18", "ill-z-gericht": "0 0 30 26",
      "ill-neue-schoepfung": "0 0 80 60", "ill-z-exil": "0 0 60 24", "ill-z-ausbreiten": "0 0 40 30", "ill-brief": "0 0 24 18",
      "ill-gemeinde": "0 0 60 44", "ill-z-beten": "0 0 22 24", "ill-z-trauer": "0 0 12 18"}

INK, PAPER, FLOOR, BUBBLE = "#3B3226", "#F4E7D3", "#E2CDA8", "#FFFFFF"


def use(sym, x, y, w, h, extra=""):
    return f'<use href="#{sym}" x="{x}" y="{y}" width="{w}" height="{h}"{extra}/>'


def fig(fid, x, y=58, w=28, h=60, extra=""):
    return use(RENDER[fid], x, y, w, h, extra)


def gesture(x1, y1, x2, y2):
    return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{INK}" stroke-width="2.2" stroke-linecap="round"/>'


def bubble(x, y, w, h, tx, ty, inner):
    """Sprechblase als eine Form mit eingebauter Spitze zur sprechenden Figur (tx, ty), siehe _bubble.py."""
    return f'<g><path d="{bubble_path(x, y, w, h, tx, ty, 8, 4.5)}" fill="{BUBBLE}" stroke="{INK}" stroke-width="1.2" stroke-linejoin="round"/>{inner}</g>'


def panel(n, px, py, body, w=186, h=140, num=True):
    clip = f"ill-cp-{n}-{px}-{py}"
    return (f'<g transform="translate({px} {py})"><clipPath id="{clip}"><rect width="{w}" height="{h}" rx="10"/></clipPath>'
            f'<g clip-path="url(#{clip})"><rect width="{w}" height="{h}" fill="{PAPER}"/><rect y="{h - 22}" width="{w}" height="22" fill="{FLOOR}"/>{body}</g>'
            + (f'<circle cx="13" cy="13" r="9" fill="#FFFDF6" stroke="{INK}"/><text x="13" y="17.5" text-anchor="middle" font-family="sans-serif" font-size="12" fill="{INK}">{n}</text>' if num else '') + '</g>')


# ---------- Johannes 2,1–12 (vier Felder) ----------
def hochzeit_tafel():
    seated = (use("ill-p-braut", 112, 36, 16, 34) + use("ill-p-braeutigam", 128, 36, 16, 34) + use("ill-p-gast", 144, 38, 15, 32)
              + use("ill-p-gast2", 159, 38, 15, 32))
    table = f'<rect x="104" y="62" width="76" height="6" fill="#FFFDF6" stroke="{INK}"/><path d="M106 68h72l-3 14h-66z" fill="#F2E6CC" stroke="{INK}"/>'
    return use("ill-z-hochzeit", 110, 20, 66, 22) + seated + table


def kana_1():
    b1 = bubble(8, 26, 62, 32, 40, 64, use("ill-jar-leer", 12, 28, 20, 28) + use("ill-becher-leer", 34, 35, 14, 17) + use("ill-z-fehlt", 50, 34, 16, 16))
    b2 = bubble(74, 20, 30, 28, 79, 58, use("ill-z-stunde", 82, 23, 15, 21))
    return hochzeit_tafel() + fig("FIG-MARIA-MUTTER-JESU", 26, 58) + gesture(48, 88, 58, 84) + fig("FIG-JESUS", 62, 56, 30, 64) + b1 + b2


def kana_2():
    b = bubble(14, 24, 100, 32, 46, 64, use("ill-jesus-kopf", 22, 28, 24, 24) + use("ill-z-pfeil", 50, 35, 20, 10) + use("ill-z-hoeren", 76, 27, 30, 25))
    return (fig("FIG-MARIA-MUTTER-JESU", 34, 58) + gesture(58, 88, 84, 84) + fig("FIG-ROLLE-DIENER", 108, 58)
            + fig("FIG-ROLLE-DIENER", 138, 62, 26, 56, ' opacity=".85"') + b)


def kana_3():
    jars = "".join(use("ill-jar", 50 + i * 16, 90, 15, 28) for i in range(6))
    pour = (f'<g transform="rotate(-75 150 76)">{use("ill-jar", 141, 62, 13, 24)}</g>'
            '<path d="M135 82q-4 3-4 10" fill="none" stroke="#4C9BD6" stroke-width="2.4" stroke-linecap="round"/>')
    b = bubble(12, 22, 86, 30, 25, 59, use("ill-jar", 20, 24, 14, 26) + use("ill-z-pfeil", 40, 32, 20, 10) + use("ill-p-meister", 66, 23, 13, 28))
    return fig("FIG-JESUS", 10, 56, 30, 64) + gesture(36, 88, 48, 96) + jars + fig("FIG-ROLLE-DIENER", 150, 58) + pour + b


def kana_4():
    b = bubble(24, 10, 64, 32, 54, 64, use("ill-becher", 31, 14, 20, 23) + use("ill-z-freude", 56, 20, 26, 17))
    hearts = use("ill-z-glauben", 147, 46, 16, 18) + use("ill-z-glauben", 167, 46, 16, 18)
    return (fig("FIG-ROLLE-DIENER", 2, 66, 22, 50) + use("ill-jar-wein", 22, 98, 11, 20) + fig("FIG-ROLLE-SPEISEMEISTER", 40, 58)
            + use("ill-becher", 62, 80, 11, 13) + gesture(66, 90, 78, 86) + use("ill-z-freude", 28, 60, 18, 11) + use("ill-z-freude", 64, 60, 18, 11) + b
            + fig("FIG-ROLLE-BRAEUTIGAM", 80, 58) + use("ill-zeichen", 118, 26, 16, 16) + fig("FIG-JESUS", 112, 56, 28, 62)
            + fig("FIG-ROLLE-JUENGER", 144, 68, 22, 50) + fig("FIG-ROLLE-JUENGER", 164, 68, 22, 50) + hearts)


def kana_kapitel():
    jars = "".join(use("ill-jar", 36 + i * 15, 92, 14, 26) for i in range(3))
    return (use("ill-z-hochzeit", 110, 26, 66, 22) + fig("FIG-ROLLE-BRAUT", 122, 56) + fig("FIG-ROLLE-BRAEUTIGAM", 150, 56)
            + fig("FIG-JESUS", 4, 56, 30, 64) + jars + use("ill-z-pfeil", 82, 100, 14, 8) + use("ill-jar-wein", 98, 88, 16, 30)
            + use("ill-zeichen", 96, 58, 20, 20))


# ---------- Johannes 2,13–22 (zwei Felder) ----------
def tempel_1():
    table = f'<g transform="rotate(-18 40 110)"><rect x="12" y="104" width="56" height="6" fill="#B07A3E" stroke="{INK}"/><path d="M18 104v-12M62 104v-12" stroke="{INK}" stroke-width="2.4"/></g>'
    coins = use("ill-muenzen", 10, 120, 22, 13) + use("ill-muenzen", 40, 124, 20, 12)
    b = bubble(84, 6, 66, 30, 92, 58, use("ill-tempel", 89, 10, 26, 20) + use("ill-muenzen", 116, 15, 16, 10) + use("ill-z-fehlt", 133, 13, 14, 14))
    return (use("ill-tempel", 0, 14, 80, 60) + table + coins + fig("FIG-ROLLE-HAENDLER", 2, 56, 26, 58) + fig("FIG-JESUS", 76, 56, 30, 64)
            + gesture(100, 86, 106, 72) + use("ill-peitsche", 104, 50, 18, 22) + use("ill-schaf", 130, 96, 36, 23)
            + use("ill-taube-kaefig", 152, 52, 28, 28) + b)


def tempel_2():
    crowd = (fig("FIG-GRUPPE-MENGE", 44, 70, 20, 44, ' opacity=".6"') + fig("FIG-GRUPPE-MENGE", 6, 58) + fig("FIG-GRUPPE-MENGE", 30, 64, 24, 52)
             + fig("FIG-GRUPPE-MENGE", 54, 62, 25, 54, ' opacity=".85"'))
    b1 = bubble(6, 24, 52, 30, 20, 64, use("ill-zeichen", 13, 29, 20, 20) + use("ill-z-frage", 38, 28, 12, 22))
    suns = "".join(use("ill-sonne", 113 + i * 8, 21, 7, 7) for i in range(3))
    b2 = bubble(62, 8, 120, 34, 150, 58, use("ill-p-menge", 64, 14, 8, 18) + use("ill-p-menge", 69, 11, 8, 18) + use("ill-p-menge", 74, 15, 8, 18) + use("ill-tempel-riss", 82, 15, 20, 18) + use("ill-z-pfeil", 102, 21, 10, 7) + suns
                + use("ill-z-pfeil", 138, 21, 10, 7) + use("ill-jesus-kopf", 149, 14, 13, 13) + use("ill-tempel", 163, 16, 17, 13))
    return crowd + fig("FIG-JESUS", 140, 56, 30, 64) + gesture(144, 88, 128, 84) + b1 + b2


def glaube_1():
    crowd = (fig("FIG-GRUPPE-MENGE", 70, 70, 20, 44, ' opacity=".55"') + fig("FIG-GRUPPE-MENGE", 18, 68, 22, 48, ' opacity=".7"')
             + "".join(fig("FIG-GRUPPE-MENGE", x, y, w, h) for x, y, w, h in ((4, 64, 25, 54), (34, 60, 27, 58), (60, 66, 24, 52), (86, 62, 26, 56))))
    stars = use("ill-zeichen", 18, 14, 16, 16) + use("ill-zeichen", 48, 6, 13, 13) + use("ill-zeichen", 76, 16, 15, 15)
    hearts = "".join(use("ill-z-glauben", x, y, 14, 16) for x, y in ((10, 44), (41, 40), (65, 46), (92, 42)))
    return (use("ill-tempel", 120, 16, 60, 45, ' opacity=".45"') + crowd + stars + hearts
            + use("ill-z-abstand", 116, 58, 8, 60) + fig("FIG-JESUS", 140, 56, 30, 64))


def kana_svg():
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 288">'
            + panel(1, 0, 0, kana_1()) + panel(2, 194, 0, kana_2()) + panel(3, 0, 148, kana_3()) + panel(4, 194, 148, kana_4()) + "</svg>")


def tempel_svg():
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 140">' + panel(1, 0, 0, tempel_1()) + panel(2, 194, 0, tempel_2()) + "</svg>"


def glaube_svg():
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 186 140">' + panel(1, 0, 0, glaube_1()) + "</svg>"


def kapitel_svg():
    pos = ((0, 0), (194, 0), (97, 148))  # höchstens zwei Spalten
    parts = [panel(i + 1, x, y, body) for i, (body, (x, y)) in enumerate(zip((kana_kapitel(), tempel_1(), glaube_1()), pos))]
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 288">' + "".join(parts) + "</svg>"


def buch_svg():
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 250"><rect width="380" height="250" fill="#1F2A44"/>'
            + use("ill-licht", 156, 6, 68, 68) + use("ill-adler", 84, 56, 212, 148)
            + use("ill-schriftrolle", 150, 202, 80, 40) + "</svg>")



# ---------- Obere Ebenen: Bibel, Testamente, Buchgruppen ----------
def fig_m(fid, x, y, w, h):
    """Figur gespiegelt (blickt nach rechts)."""
    return f'<g transform="translate({x + w} {y}) scale(-1 1)">{use(RENDER[fid], 0, 0, w, h)}</g>'


def menge(pos, extra=""):
    return "".join(fig("FIG-GRUPPE-MENGE", x, y, w, h, extra) for x, y, w, h in pos)


def f_schoepfung():
    b = bubble(78, 8, 38, 32, 68, 30, use("ill-licht", 85, 11, 24, 24))
    return use("ill-gott", 26, 6, 44, 44) + b + use("ill-schoepfung", 54, 42, 128, 107)


def f_meer():
    return (use("ill-meer", 0, 28, 186, 103) + fig("FIG-MOSE", 74, 54, 28, 60)
            + menge(((100, 64, 22, 48), (116, 66, 20, 44)), ' opacity=".9"'))


def f_berg(meer=False):
    sea = use("ill-meer", -4, 36, 56, 32, ' opacity=".9"') if meer else ""
    b = bubble(146, 6, 36, 30, 134, 20, use("ill-tafeln", 151, 9, 26, 24))
    return (use("ill-berg", 54, 26, 132, 82) + use("ill-gott", 100, 0, 36, 36) + b + sea + fig("FIG-MOSE", 56, 56, 30, 64) + use("ill-tafeln", 34, 76, 26, 24)
            + menge(((118, 66, 22, 50), (138, 64, 24, 54), (160, 66, 22, 50))))


def crack(x, y, sc=1.0):
    d = "M0 0l-4 8 5 5-4 8 4 6"
    return (f'<g transform="translate({x} {y}) scale({sc})"><path d="{d}" fill="none" stroke="#F6EBD9" stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/></g>')


def god_to(x, y, tx, ty, s=28):
    """Gott (Strahlenkranz) mit Handlungslinie zu einer Figur: spricht durch sie / sendet sie."""
    from bilder_auto import arrow_svg
    return use("ill-gott", x, y, s, s) + arrow_svg(x + s * .55, y + s, tx, ty, "act")


def f_exil():
    b = bubble(44, 30, 34, 28, 30, 62, use("ill-z-hoffnung", 49, 32, 24, 24))
    return (use("ill-jerusalem", 104, 14, 80, 56) + crack(150, 40) + crack(126, 48, .8) + fig_m("FIG-ROLLE-PROPHET", 8, 56, 30, 64) + god_to(26, 2, 22, 56) + b
            + menge(((80, 66, 22, 50), (100, 68, 20, 46))) + use("ill-z-trauer", 98, 72, 6, 9) + use("ill-z-trauer", 116, 74, 6, 9)
            + '<g transform="translate(184 76) scale(-1 1)">' + use("ill-z-exil", 0, 0, 60, 24) + "</g>")


def f_kreuz(jesus):
    left = fig("FIG-JESUS", 6, 56, 28, 62) if jesus else ""
    x0 = 40 if jesus else 22
    return left + use("ill-kreuz", x0, 58, 40, 59) + use("ill-grab", x0 + 50, 60, 87, 60)


def f_neu(gott=True, freude=False):
    out = use("ill-neue-schoepfung", 18, 34, 150, 112) + (use("ill-gott", 76, 0, 34, 34) if gott else "")
    if freude:
        out += menge(((2, 64, 22, 50), (162, 64, 22, 50))) + use("ill-z-freude", 0, 50, 26, 14) + use("ill-z-freude", 160, 50, 26, 14)
    return out


def f_stimmen():
    return (use("ill-schriftrolle", 6, 76, 46, 32) + use("ill-leier", 58, 66, 28, 36) + fig("FIG-ROLLE-PROPHET", 92, 56, 30, 64)
            + use("ill-brief", 130, 80, 48, 36))


def f_verkuendet(vier=False):
    rolls = "".join(use("ill-schriftrolle", 26 + i * 11, 10, 10, 8) for i in range(4)) if vier else ""
    b = bubble(70, 8, 110, 34, 146, 58, use("ill-gott", 76, 10, 30, 30) + use("ill-z-umkehr", 112, 16, 24, 18) + use("ill-z-glauben", 144, 12, 22, 24))
    return rolls + menge(((6, 62, 24, 54), (30, 60, 26, 56), (56, 64, 24, 52))) + fig("FIG-JESUS", 130, 56, 30, 64) + gesture(134, 88, 116, 86) + b


def f_nt_geist():
    return (use("ill-geist", 24, 6, 46, 46) + fig("FIG-ROLLE-JUENGER", 4, 62, 22, 50) + fig("FIG-ROLLE-JUENGER", 24, 60, 24, 54)
            + use("ill-z-ausbreiten", 52, 62, 40, 30) + use("ill-brief", 120, 28, 30, 22) + use("ill-gemeinde", 96, 60, 88, 64))


def f_nt_ende():
    return use("ill-gott", 26, 4, 40, 40) + use("ill-z-gericht", 8, 74, 44, 38) + use("ill-neue-schoepfung", 58, 32, 128, 96)


def f_koenig():
    return (use("ill-jerusalem", 70, 16, 110, 77) + fig("FIG-ROLLE-KOENIG", 24, 56, 30, 64)
            + menge(((118, 70, 20, 46), (136, 68, 22, 50), (156, 70, 20, 46))))


def f_zerstoert():
    return (use("ill-jerusalem", 8, 14, 90, 63) + crack(60, 40) + crack(32, 52, .8) + menge(((112, 64, 24, 52), (134, 66, 22, 50)))
            + use("ill-z-trauer", 131, 70, 6, 9) + use("ill-z-trauer", 152, 72, 6, 9) + use("ill-z-exil", 20, 80, 60, 24))


def f_gebet():
    b = bubble(28, 26, 50, 30, 44, 64, use("ill-z-trauer", 36, 31, 11, 19) + use("ill-z-freude", 52, 34, 22, 15))
    return (use("ill-gott", 130, 4, 44, 44) + fig("FIG-GRUPPE-MENGE", 30, 58, 28, 60) + use("ill-leier", 58, 76, 18, 23)
            + b)


def f_liebe():
    return (use("ill-z-hochzeit", 42, 14, 100, 40) + fig("FIG-ROLLE-BRAUT", 58, 56, 30, 64) + fig("FIG-ROLLE-BRAEUTIGAM", 96, 56, 30, 64)
            + use("ill-z-freude", 70, 40, 46, 20))


def f_weisheit():
    return (fig("FIG-GRUPPE-MENGE", 16, 58, 28, 60) + use("ill-schriftrolle", 40, 82, 36, 25) + use("ill-z-stunde", 96, 28, 26, 36)
            + use("ill-z-gericht", 134, 30, 46, 40))


def f_prophet(zwoelf=False):
    rolls = "".join(use("ill-schriftrolle", 120 + (i % 6) * 11, 6 + (i // 6) * 10, 10, 7) for i in range(12)) if zwoelf else ""
    b = bubble(42, 26, 68, 34, 30, 62, use("ill-z-gericht", 48, 30, 30, 26) + use("ill-z-umkehr", 82, 34, 24, 18))
    return rolls + fig_m("FIG-ROLLE-PROPHET", 8, 56, 30, 64) + menge(((110, 62, 24, 54), (134, 60, 26, 56), (160, 64, 24, 52))) + god_to(26, 2, 22, 56) + b


def f_aufbau():
    return (use("ill-gott", 72, 0, 36, 36) + use("ill-jerusalem", 50, 36, 84, 59) + use("ill-z-hoffnung", 14, 90, 28, 28)
            + menge(((140, 64, 22, 50), (160, 66, 22, 48))) + use("ill-z-freude", 140, 56, 26, 14) + use("ill-z-freude", 158, 58, 26, 14))


def f_pfingsten():
    return (use("ill-jerusalem", 96, 40, 88, 62) + use("ill-geist", 40, 2, 52, 52)
            + "".join(fig("FIG-ROLLE-JUENGER", x, y, w, h) for x, y, w, h in ((8, 62, 24, 52), (30, 58, 26, 58), (56, 62, 24, 52)))
            + "".join(use("ill-z-feuerzungen", x, y, 8, 11) for x, y in ((16, 50), (39, 45), (64, 50))))


def f_rom():
    return (use("ill-jerusalem", 2, 50, 48, 34) + use("ill-z-ausbreiten", 46, 40, 40, 30) + use("ill-rom", 92, 30, 90, 63)
            + fig("FIG-PAULUS", 98, 56, 30, 64) + fig("FIG-ROLLE-SOLDAT", 140, 56, 30, 64))


def path_dots(d):
    return f'<path d="{d}" fill="none" stroke="#8C8070" stroke-width="1.6" stroke-dasharray="3 4" stroke-linecap="round"/>'


def f_paulus():
    b = bubble(10, 24, 62, 32, 23, 62, use("ill-kreuz", 18, 27, 18, 26) + use("ill-z-glauben", 44, 29, 20, 22))
    return (fig("FIG-PAULUS", 8, 56, 30, 64) + path_dots("M40 84Q60 60 76 66") + use("ill-brief", 66, 54, 28, 21)
            + path_dots("M96 66Q106 70 112 76") + use("ill-gemeinde", 100, 52, 84, 62) + b)


def f_briefe():
    letters = "".join(use("ill-brief", 12, y, 30, 22) for y in (26, 56, 86))
    dots = "".join(path_dots(f"M46 {y + 11}Q70 {y + 11} 92 84") for y in (26, 56, 86))
    hearts = "".join(use("ill-z-glauben", x, y, 18, 20) for x, y in ((104, 36), (132, 30), (160, 36)))
    return letters + dots + use("ill-gemeinde", 94, 56, 90, 66) + hearts


def f_herrschaft():
    return (use("ill-gott", 62, 0, 62, 62) + fig("FIG-ROLLE-KOENIG", 18, 62, 26, 56) + fig("FIG-ROLLE-SOLDAT", 44, 62, 26, 56)
            + menge(((122, 66, 22, 50), (146, 64, 24, 54))) + use("ill-z-trauer", 140, 72, 6, 9) + use("ill-z-trauer", 166, 70, 6, 9))


def layout(bodies):
    n = len(bodies)
    if n == 1:
        return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 186 140">' + panel(1, 0, 0, bodies[0], num=False) + "</svg>"  # ein Feld: ohne Nummer
    if n == 2:
        return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 140">' + panel(1, 0, 0, bodies[0]) + panel(2, 194, 0, bodies[1]) + "</svg>"
    # höchstens zwei Spalten, alle Felder gleich gross (lesbar auf dem Handy); bei drei Feldern das dritte mittig darunter
    if n == 3:
        pos = ((0, 0), (194, 0), (97, 148))
        return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 288">'
                + "".join(panel(i + 1, x, y, b) for i, (b, (x, y)) in enumerate(zip(bodies, pos))) + "</svg>")
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 288">'
            + "".join(panel(i + 1, (i % 2) * 194, (i // 2) * 148, b) for i, b in enumerate(bodies)) + "</svg>")


UPPER_SVG = {
    "BIBLE": lambda: layout([f_berg(), f_kreuz(True), f_neu(), f_stimmen()]),
    "OT": lambda: layout([f_schoepfung(), f_meer(), f_berg(), f_exil()]),
    "NT": lambda: layout([f_verkuendet(), f_kreuz(False), f_nt_geist(), f_nt_ende()]),
    "GROUP-01": lambda: layout([f_schoepfung(), upper_auto("GROUP-01", 2), f_berg(meer=True)]),
    "GROUP-02": lambda: layout([upper_auto("GROUP-02", 1), f_koenig(), f_zerstoert(), upper_auto("GROUP-02", 4)]),
    "GROUP-03": lambda: layout([f_gebet(), f_liebe(), f_weisheit()]),
    "GROUP-04": lambda: layout([f_prophet(), f_exil()]),
    "GROUP-05": lambda: layout([f_prophet(zwoelf=True), f_aufbau()]),
    "GROUP-06": lambda: layout([f_verkuendet(vier=True), f_kreuz(False)]),
    "GROUP-07": lambda: layout([f_pfingsten(), f_rom()]),
    "GROUP-08": lambda: layout([f_paulus()]),
    "GROUP-09": lambda: layout([upper_auto("GROUP-09", 1)]),
    "GROUP-10": lambda: layout([f_herrschaft(), f_neu(freude=True)]),
}


GENERATED = {"ILL-SYM-JHN": buch_svg, "ILL-SYM-JHN-002-001-012": kana_svg, "ILL-SYM-JHN-002-013-022": tempel_svg,
             "ILL-SYM-JHN-002-023-025": glaube_svg, "ILL-SYM-JHN-002": kapitel_svg,
             **{f"ILL-SYM-{k}": v for k, v in UPPER_SVG.items()}}

# Bild -> (Bildauftrag, Bildbeschreibung DE, Bildbeschreibung GSW)
ILL = {
    "ILL-SYM-JHN": ("BRIEF-JHN", "Ein brauner Adler mit ausgebreiteten Flügeln und gelbem Hakenschnabel unter einem Licht mit Strahlen, darunter eine Schriftrolle.",
                    "En brune Adler mit uusbreitete Flügel und gälem Hakeschnabel under eme Liecht mit Strahle, drunder e Schriftrolle."),
    "ILL-SYM-JHN-002": ("BRIEF-JHN-002", "Drei Felder: 1 Hochzeit (Girlande, Braut und Bräutigam); Jesus, drei Wasserkrüge, ein Pfeil zu einem Weinkrug, darüber ein Stern (Zeichen). "
                        "2 Jesus treibt die Händler aus dem Tempel. 3 Die Menge glaubt wegen der Zeichen, eine gestrichelte Linie trennt sie von Jesus.",
                        "Drüü Fälder: 1 Hochziit (Girlande, Brut und Brüütigam); de Jesus, drüü Wasserchrüeg, en Pfiil zu eme Wiichrueg, drüber en Stern (Zeiche). "
                        "2 De Jesus tribt d Händler us em Tämpel. 3 D Mängi glaubt wäge de Zeiche, e gstrichleti Linie trännt si vom Jesus."),
    "ILL-SYM-JHN-002-001-012": ("BRIEF-JHN-002-001-012",
                                "Vier Felder: 1 Bei der Hochzeit zeigt Maria Jesus den leeren Weinkrug und den leeren Becher, Jesus antwortet mit der Sanduhr (noch nicht). 2 Maria sagt den Dienern: hört auf Jesus. "
                                "3 Jesus weist auf die sechs Krüge, ein Diener giesst Wasser ein; Sprechblase: Wasserkrug, Pfeil, Speisemeister. 4 Der Speisemeister freut sich, hält den Becher und spricht zum Bräutigam (Sprechblase: Becher und Funken – ausgezeichnet); "
                                "über Jesus ein Stern (Zeichen), über den Jüngern Herzen (sie glauben).",
                                "Vier Fälder: 1 A de Hochziit zeigt d Maria em Jesus de läär Wiichrueg und de läär Becher, de Jesus antwortet mit de Sanduhr (no nöd). 2 D Maria seit de Diener: losed uf de Jesus. "
                                "3 De Jesus zeigt uf di sächs Chrüeg, en Diener schüttet Wasser ii; Sprächblase: Wasserchrueg, Pfiil, Spiismeischter. 4 De Spiismeischter freut sich, hebt de Becher und redt mit em Brüütigam (Sprächblase: Becher und Funke – usgezeichnet); "
                                "über em Jesus en Stern (Zeiche), über de Jünger Härz (si glaubed)."),
    "ILL-SYM-JHN-002-013-022": ("BRIEF-JHN-002-013-022",
                                "Zwei Felder: 1 Jesus mit erhobener Geissel vor dem Tempel; umgestossener Tisch, Münzen, ein Händler weicht, ein Schaf, Tauben im Käfig; Sprechblase: Tempel, Münzen, durchgestrichen. "
                                "2 Die Menge fragt nach einem Zeichen (Stern, Fragezeichen); Jesus antwortet: Menge, Tempel mit Riss, drei Sonnen (drei Tage), Jesus, Tempel.",
                                "Zwei Fälder: 1 De Jesus mit ufghabener Geissle vor em Tämpel; umgheite Tisch, Münze, en Händler gaat ewäg, es Schaf, Tube im Chäfig; Sprächblase: Tämpel, Münze, durgstriche. "
                                "2 D Mängi fröget nach eme Zeiche (Stern, Fragezeiche); de Jesus antwortet: Mängi, Tämpel mit Riss, drüü Sunne (drüü Täg), Jesus, Tämpel."),
    "ILL-SYM-JHN-002-023-025": ("BRIEF-JHN-002-023-025", "Eine Menge unter goldenen Sternen (Zeichen), mit Herzen (sie glauben); eine gestrichelte Linie trennt sie von Jesus; im Hintergrund der Tempel.",
                                "E Mängi under goldige Stärn (Zeiche), mit Härz (si glaubed); e gstrichleti Linie trännt si vom Jesus; im Hindergrund de Tämpel."),
}
ILL.update({f"ILL-SYM-{k}": (f"BRIEF-{k}", a, g) for k, (a, g) in {'BIBLE': ('Vier Felder: 1 Über einem Berg der Strahlenkranz mit dem Gottesnamen; Mose mit den Tafeln, daneben das Volk. 2 Jesus, ein Kreuz und ein leeres Grab im Licht. 3 Eine Stadt im Licht mit Strom und Baum, darüber der Strahlenkranz. 4 Schriftrolle, Leier, ein Prophet und ein Brief.', 'Vier Fälder: 1 Über eme Bärg de Strahlechranz mit em Gottesname; de Mose mit de Tafle, dernäbe s Volk. 2 De Jesus, es Chrüz und es läärs Grab im Liecht. 3 E Stadt im Liecht mit Strom und Baum, drüber de Strahlechranz. 4 Schriftrolle, Leier, en Prophet und en Brief.'), 'OT': ('Vier Felder: 1 Der Strahlenkranz mit dem Gottesnamen spricht (Sprechblase: Licht); Erde mit Pflanze, Sonne, Mond und Sternen. 2 Mose und das Volk gehen durch das geteilte Meer. 3 Am Berg spricht der Strahlenkranz (Sprechblase: Tafeln); Mose mit den Tafeln, das Volk. 4 Jerusalem mit Rissen; Menschen mit Tränen auf dem Weg weg und gestrichelt zurück; ein Prophet spricht von Hoffnung (Spross aus dem Stumpf).', 'Vier Fälder: 1 De Strahlechranz mit em Gottesname redt (Sprächblase: Liecht); Erde mit Pflanze, Sunne, Mond und Stärn. 2 De Mose und s Volk gönd dur s teilte Meer. 3 Am Bärg redt de Strahlechranz (Sprächblase: Tafle); de Mose mit de Tafle, s Volk. 4 Jerusalem mit Riss; Mänsche mit Träne uf em Wäg ewäg und gstrichlet zrugg; en Prophet redt vo Hoffnig (Schoss us em Stumpe).'), 'NT': ('Vier Felder: 1 Jesus spricht zur Menge (Sprechblase: Gottesname, Umkehr-Pfeil, Herz). 2 Kreuz und leeres Grab. 3 Die Geist-Taube über zwei Jüngern; Pfeile breiten sich aus zu einer Gemeinde vor einem Haus, ein Brief. 4 Strahlenkranz, Waage und die leuchtende Stadt.', 'Vier Fälder: 1 De Jesus redt zur Mängi (Sprächblase: Gottesname, Umchehr-Pfiil, Härz). 2 Chrüz und läärs Grab. 3 D Geischt-Tube über zwei Jünger; Pfiil breited sich uus zu ere Gmeind vor eme Huus, en Brief. 4 Strahlechranz, Waag und di lüüchtend Stadt.'), 'GROUP-01': ('Zwei Felder: 1 Der Strahlenkranz spricht (Licht); Erde mit Pflanze, Sonne, Mond und Sternen. 2 Hinter dem Volk das geteilte Meer; am Berg spricht der Strahlenkranz (Sprechblase: Tafeln); Mose mit den Tafeln, das Volk.', 'Zwei Fälder: 1 De Strahlechranz redt (Liecht); Erde mit Pflanze, Sunne, Mond und Stärn. 2 Hinder em Volk s teilte Meer; am Bärg redt de Strahlechranz (Sprächblase: Tafle); de Mose mit de Tafle, s Volk.'), 'GROUP-02': ('Zwei Felder: 1 Ein König vor Jerusalem, daneben Menschen. 2 Jerusalem mit Rissen; Menschen mit Tränen; Weg mit Pfeil weg und gestrichelt zurück.', 'Zwei Fälder: 1 En Chünig vor Jerusalem, dernäbe Mänsche. 2 Jerusalem mit Riss; Mänsche mit Träne; Wäg mit Pfiil ewäg und gstrichlet zrugg.'), 'GROUP-03': ('Drei Felder: 1 Ein Mensch mit Leier spricht zum Strahlenkranz (Sprechblase: Träne und Freude). 2 Braut und Bräutigam unter einer Girlande, Freude. 3 Ein Mensch mit Schriftrolle, Sanduhr und Waage.', 'Drüü Fälder: 1 En Mänsch mit Leier redt zum Strahlechranz (Sprächblase: Träne und Fröid). 2 Brut und Brüütigam under ere Girlande, Fröid. 3 En Mänsch mit Schriftrolle, Sanduhr und Waag.'), 'GROUP-04': ('Zwei Felder: 1 Ein Prophet spricht zur Menge (Sprechblase: Gottesname, Waage, Umkehr-Pfeil). 2 Jerusalem mit Rissen, Menschen mit Tränen auf dem Weg weg und zurück; der Prophet spricht von Hoffnung (Spross).', 'Zwei Fälder: 1 En Prophet redt zur Mängi (Sprächblase: Gottesname, Waag, Umchehr-Pfiil). 2 Jerusalem mit Riss, Mänsche mit Träne uf em Wäg ewäg und zrugg; de Prophet redt vo Hoffnig (Schoss).'), 'GROUP-05': ('Zwei Felder: 1 Zwölf kleine Schriftrollen; ein Prophet spricht zur Menge (Gottesname, Waage, Umkehr-Pfeil). 2 Strahlenkranz über dem heilen Jerusalem, ein Spross, Menschen freuen sich.', 'Zwei Fälder: 1 Zwölf chlini Schriftrolle; en Prophet redt zur Mängi (Gottesname, Waag, Umchehr-Pfiil). 2 Strahlechranz über em ganze Jerusalem, en Schoss, Mänsche fröied sich.'), 'GROUP-06': ('Zwei Felder: 1 Vier kleine Schriftrollen; Jesus spricht zur Menge (Gottesname, Umkehr-Pfeil, Herz). 2 Kreuz und leeres Grab.', 'Zwei Fälder: 1 Vier chlini Schriftrolle; de Jesus redt zur Mängi (Gottesname, Umchehr-Pfiil, Härz). 2 Chrüz und läärs Grab.'), 'GROUP-07': ('Zwei Felder: 1 Die Geist-Taube kommt auf drei Jünger herab, dahinter Jerusalem. 2 Von Jerusalem gehen Pfeile aus zu einer Gemeinde; ein Schiff; Paulus mit einem Soldaten.', 'Zwei Fälder: 1 D Geischt-Tube chunnt uf drüü Jünger abe, dehinder Jerusalem. 2 Vo Jerusalem gönd Pfiil uus zu ere Gmeind; es Schiff; de Paulus mit eme Soldat.'), 'GROUP-08': ('Paulus spricht (Sprechblase: Kreuz und Herz); ein Brief fliegt zu einer Gemeinde vor einem Haus.', 'De Paulus redt (Sprächblase: Chrüz und Härz); en Brief flügt zu ere Gmeind vor eme Huus.'), 'GROUP-09': ('Drei Briefe gehen zu einer Gemeinde vor einem Haus; über der Gemeinde Herzen.', 'Drüü Brief gönd zu ere Gmeind vor eme Huus; über de Gmeind Härz.'), 'GROUP-10': ('Zwei Felder: 1 Oben gross der Strahlenkranz mit dem Gottesnamen; darunter ein König und ein Soldat, daneben Menschen mit Tränen. 2 Die leuchtende Stadt mit Strom und Baum, darüber der Strahlenkranz; Menschen freuen sich.', 'Zwei Fälder: 1 Obe gross de Strahlechranz mit em Gottesname; drunder en Chünig und en Soldat, dernäbe Mänsche mit Träne. 2 D lüüchtend Stadt mit Strom und Baum, drüber de Strahlechranz; Mänsche fröied sich.')}.items()})


# ---------------------------------------------------------------------------------------------------------------
# Automatisch gesetzte Bilder (bilder_auto.py) für alle übrigen Stellen; Figuren aus figuren.py, Bauteile aus bildsymbole.py
# ---------------------------------------------------------------------------------------------------------------
import bilder_auto as _auto  # noqa: E402
import bildsymbole as _bs  # noqa: E402
import figuren as _fg  # noqa: E402

_SYMS = _bs.all_symbols()
for _k, _v in _fg.symbol_render().items():
    RENDER.setdefault(_k, _v)
RENDER_X = {}  # nur zum Zeichnen (kein Lexikon-Eintrag), z. B. ruhiges Meer
for _k, _v in _SYMS.items():
    (RENDER_X if _k.startswith("_") else RENDER).setdefault(_k, _v["sym"])
    VB.setdefault(_v["sym"], _v["vb"])
EXTRA_META = {k: (v["place"], tuple(v["size"])) for k, v in _SYMS.items()}
AUTO_BEGIN, AUTO_END = "<!-- auto:begin -->", "<!-- auto:end -->"


def auto_library():
    """Bibliothek mit dem automatisch erzeugten Teil (Figuren, Attribute, neue Bauteile) zwischen den Marken."""
    lib = (OUT / "_bibliothek.svg").read_text(encoding="utf-8")
    auto = AUTO_BEGIN + _fg.symbol_library() + _bs.symbol_defs() + AUTO_END
    if AUTO_BEGIN in lib:
        a, rest = lib.split(AUTO_BEGIN, 1)
        lib = a + auto + rest.split(AUTO_END, 1)[1]
    else:
        lib = lib.replace("</defs></svg>", auto + "\n</defs></svg>")
    return lib


class SymComposer(_auto.Composer):
    def vb(self, fid):
        if fid == "FIG-GRUPPE-MENGE":
            return "0 0 50 64"
        sym = RENDER[fid]
        return VB.get(sym, VB["ill-p"] if sym.startswith("ill-p-") else "0 0 30 64")

    def head_r(self):
        return 8

    def icon_h(self):
        return 20

    def r_floor(self):
        return ""

    def r_band(self, t):
        w, h = self.m(t)[1]
        return use(RENDER.get(t) or RENDER_X[t], 0, 140 - h, w, h)

    def r_back(self, t, x, y, w, h):
        return use(RENDER[t], x, y, w, h, '' if t == "FIG-GRUPPE-GEMEINDE" else ' opacity=".8"')

    def r_sym(self, t, x, y, w, h, flip=False):
        if flip:
            return f'<g transform="translate({x + w:.1f} {y:.1f}) scale(-1 1)">{use(RENDER[t], 0, 0, w, h)}</g>'
        return use(RENDER.get(t) or RENDER_X[t], round(x, 1), round(y, 1), w, h)

    def r_icon(self, t, x, y, w, h):
        if t == "FIG-GRUPPE-MENGE":  # Mehrzahl: drei Figuren
            fw = w * .5
            return (use("ill-p-gast2", round(x, 1), round(y + h * .08, 1), round(fw, 1), round(h * .92, 1))
                    + use("ill-p-gast", round(x + w - fw, 1), round(y + h * .08, 1), round(fw, 1), round(h * .92, 1))
                    + use("ill-p-menge", round(x + (w - fw) / 2, 1), round(y, 1), round(fw, 1), round(h, 1)))
        return use(RENDER[t], round(x, 1), round(y, 1), round(w, 1), round(h, 1))

    def r_bubble(self, x, y, w, h, tx, ty, inner, attrs=""):
        return bubble(round(x, 1), round(y, 1), round(w, 1), round(h, 1), round(tx, 1), round(ty, 1), inner)

    def r_head_sign_native(self, t):
        return False

    def _size(self, n):
        return {1: 62, 2: 60, 3: 58, 4: 54, 5: 48}.get(n, 42)

    def r_person(self, s, n, look, arm, hold, p, out):
        fid, x = s["fid"], s["x"]
        st = p.get("stage") or {}
        pose = (st.get("pose") or {}).get(fid)
        h = self._size(n)
        w = h * 30 / 64
        y = _auto.FLOOR_Y - h
        sym = RENDER[fid]
        if any(_auto.meta(t, self.lex, EXTRA_META)[0] == "big" for t in p["objects"] + p["signs"]):
            h *= .8
            w = h * 30 / 64
            y = _auto.FLOOR_Y - h
        if fid == "FIG-GRUPPE-MENGE" and pose in (None, "sit", "away", "kneel"):
            if pose in ("sit", "kneel"):
                h *= .78 if pose == "sit" else .62
                w = h * 30 / 64
                y = _auto.FLOOR_Y - h
            sp = min(s["span"] * .3, w * .7)
            out.append(use("ill-p-gast2", round(x - sp - w * .4, 1), round(y + 4, 1), round(w * .85, 1), round(h * .92, 1))
                       + use("ill-p-gast", round(x + sp - w * .4, 1), round(y + 4, 1), round(w * .85, 1), round(h * .92, 1))
                       + use(sym, round(x - w / 2, 1), round(y, 1), round(w, 1), round(h, 1)))
            if hold and hold != "PRAY":
                ww, hh2 = self.m(hold)[1]
                out.append(use(RENDER[hold], round(x + (arm or 1) * w * .45 - ww / 2, 1), round(y + h * .45, 1), ww, hh2))
            wear = (st.get("wear") or {}).get(fid)
            if wear:
                out.append(self._sack(x - sp * .9, y + 4, w * .85, h * .92, wear) + self._sack(x + sp * .9, y + 4, w * .85, h * .92, wear) + self._sack(x, y, w, h, wear))
            if arm is not None:
                sx, sy = x + arm * w * .32, y + h * .42
                out.append(gesture(round(sx, 1), round(sy, 1), round(sx + arm * 11, 1), round(sy + 5, 1)))
            return (x, y + h * 14 / 64)
        if pose in ("lie", "sleep"):
            out.append(f'<g transform="rotate(-90 {x:.1f} {_auto.FLOOR_Y - 6})">{use(sym, round(x - w / 2, 1), round(_auto.FLOOR_Y - 6 - h / 2, 1), round(w, 1), h)}</g>')
            return (x - h * .35, _auto.FLOOR_Y - 8)
        if pose == "fall":
            out.append(f'<g transform="rotate(35 {x:.1f} {y + h / 2:.1f})">{use(sym, round(x - w / 2, 1), round(y, 1), round(w, 1), h)}</g>')
            return (x + 6, y + 14)
        if pose in ("sit", "kneel"):
            # Oberkörper in voller Grösse, Beine gefaltet (sitzen: nach vorn; knien: Unterschenkel am Boden) statt gestauchter Figur
            keep = 46 if pose == "sit" else 44
            k = h / 64
            hh = keep * k + (6 if pose == "sit" else 8) * k
            y = _auto.FLOOR_Y - hh
            robe = (_fg.FIGS.get(fid) or {}).get("robe", "#9C7A4C")
            d = arm or 1
            if pose == "sit":
                legs = f'<path d="M{x - w * .32:.1f} {y + keep * k - 2:.1f}h{w * .64 + d * 10:.1f}v{7 * k:.1f}h{-(w * .64 + d * 10):.1f}z" fill="{robe}" stroke="#3B3226" stroke-width="1"/>'
                if d < 0:
                    legs = f'<path d="M{x + w * .32:.1f} {y + keep * k - 2:.1f}h{-(w * .64 + 10):.1f}v{7 * k:.1f}h{w * .64 + 10:.1f}z" fill="{robe}" stroke="#3B3226" stroke-width="1"/>'
            else:
                legs = f'<path d="M{x - w * .34:.1f} {_auto.FLOOR_Y - 9 * k:.1f}q{w * .3:.1f} {-6 * k:.1f} {w * .7 + 6:.1f} 0v{9 * k:.1f}h{-(w * .7 + 6):.1f}z" fill="{robe}" stroke="#3B3226" stroke-width="1"/>'
            out.append(legs + f'<svg x="{x - w / 2:.1f}" y="{y:.1f}" width="{w:.1f}" height="{keep * k:.1f}" viewBox="0 0 30 {keep}" overflow="hidden">'
                       f'<use href="#{sym}" width="30" height="64"/></svg>')
            hy = y + h * 14 / 64
        else:
            out.append(use(sym, round(x - w / 2, 1), round(y, 1), round(w, 1), h))
            hy = y + h * 14 / 64
            # abgewandt: Figur bleibt mit Gesicht erkennbar wie in der Legende (früher Hinterkopf)
        wear = (st.get("wear") or {}).get(fid)
        if wear:
            out.append(self._sack(x, y, w, h, wear))
        if arm is not None:
            sx, sy = x + arm * w * .32, y + h * .42
            out.append(gesture(round(sx, 1), round(sy, 1), round(sx + arm * 11, 1), round(sy + 5, 1)))
        if hold == "PRAY":  # bei Gruppen sitzt die vordere Figur tiefer: Hände auf Brusthöhe, nicht vor dem Gesicht
            grp = s["group"] or fid.startswith("FIG-GRUPPE-")
            out.append(use("ill-z-beten", round(x - 6, 1), round(y + h * (.56 if grp else .34), 1), 12, 13))
            hold = None
        if hold == "FIG-OBJ-BRIEF" and (fid == "FIG-PAULUS" or (_fg.FIGS.get(fid) or {}).get("attr") == "brief"):
            hold = None  # trägt den Brief schon als Merkmal
        if hold == "FIG-OBJ-POSAUNE":  # Blasinstrument am Mund, Schalltrichter in Blickrichtung von der Figur weg
            dr = -1 if (look or 0) < 0 else 1
            out.append(f'<g transform="translate({x + dr * self.head_r() * .6:.1f} {hy + self.head_r() * .25:.1f}) scale({dr} 1)">'
                       + use(RENDER[hold], -1.2, -11.2, 22, 22) + '</g>')
            hold = None
        if hold:
            ww, hh2 = _auto.meta(hold, self.lex, EXTRA_META)[1]
            side = arm or 1
            out.append(use(RENDER[hold], round(x + side * w * .45 - ww / 2, 1), round(y + h * .45, 1), ww, hh2))
        return (x, hy)

    def _sack(self, x, y, w, h, wear="sack"):
        """Kleidung wechseln: «sack» (Sacktuch mit Asche), «binden» (Grabtücher) oder eine Farbe (#RRGGBB, z. B. Purpurmantel)."""
        k = h / 64
        g = f'<g transform="translate({x - w / 2:.1f} {y:.1f}) scale({w / 30:.3f} {k:.3f})">'
        if wear == "sack":
            return (g + '<path d="M5 62L8 26q7-7 14 0l3 36z" fill="#6A5E52" stroke="#3B3226" stroke-width="1.2"/>'
                    '<path d="M7 34h16M6 44h18M5.5 54h19" stroke="#4E453C" stroke-width=".9"/><g fill="#9A948C"><circle cx="11" cy="8" r="1"/><circle cx="17" cy="6.5" r=".9"/><circle cx="20" cy="9" r=".8"/></g></g>')
        if wear == "binden":
            return (g + '<path d="M5 62L8 26q7-7 14 0l3 36z" fill="#F4F1EA" stroke="#3B3226" stroke-width="1.2"/>'
                    '<path d="M7 30l16 4M6 38l18 4M6 46l18 4M5 54l20 4" stroke="#C9BFAA" stroke-width="1.2"/></g>')
        return g + f'<path d="M8 26q7-7 14 0l3 36H18L9 28z" fill="{wear}" stroke="#3B3226" stroke-width="1"/></g>'

    def r_inside(self, fid, cx, cy, w, p, out):
        st = p.get("stage") or {}
        pose = (st.get("pose") or {}).get(fid)
        h = 30 if w > 90 else 24
        ww = h * 30 / 64
        sym = RENDER[fid]
        if pose in ("lie", "sleep"):
            out.append(f'<g transform="rotate(-90 {cx:.1f} {cy:.1f})">{use(sym, round(cx - ww / 2, 1), round(cy - h / 2, 1), round(ww, 1), h)}</g>')
            return (cx - h * .3, cy)
        out.append(use(sym, round(cx - ww / 2, 1), round(cy - h / 2, 1), round(ww, 1), h))
        return (cx, cy - h / 2 + h * 14 / 64)


AUTO = [b["suffix"] for b in _auto.load_briefs()]


def upper_auto(key, n):
    """Ein Feld eines Auftrags der oberen Ebenen mit dem Zeichner setzen (neben handgezeichneten Feldern)."""
    brief = json.loads((D / "illustrations/briefs" / f"BRIEF-{key}.json").read_text(encoding="utf-8"))
    c = SymComposer(_auto.gather_lex(), EXTRA_META)
    c.uid = "s" + key.lower()
    return c.panel(brief["panels"][n - 1])


def auto_svg(suffix):
    lex = _auto.gather_lex()
    brief = json.loads((D / "illustrations/briefs" / f"BRIEF-{suffix}.json").read_text(encoding="utf-8"))
    c = SymComposer(lex, EXTRA_META)
    c.uid = "s" + suffix.lower()
    return layout([c.panel(p) for p in brief["panels"]])


for _b in _auto.load_briefs():
    GENERATED[f"ILL-SYM-{_b['suffix']}"] = (lambda s=_b["suffix"]: auto_svg(s))
    ILL[f"ILL-SYM-{_b['suffix']}"] = (f"BRIEF-{_b['suffix']}", _auto.alt_text(_b, "de"), _auto.alt_text(_b, "gsw"))


# Bildbeschreibungen nach der Überarbeitung der oberen Ebenen (2026-10-17)
_ALT2 = {'GROUP-01': ('Drei Felder: 1 Der Strahlenkranz spricht (Licht); Erde mit Pflanze, Sonne, Mond und Sternen. 2 Gott spricht zu Abraham (Sprechblase: Sternenhimmel über grünem Land). 3 Hinter dem Volk das geteilte Meer; am Berg spricht der Strahlenkranz (Tafeln); Mose mit den Tafeln, das Volk.', 'Drüü Fälder: 1 De Strahlechranz redt (Liecht); Erde mit Pflanze, Sunne, Mond und Stärn. 2 Gott redt zum Abraham (Sprächblase: Stärnehimmel über grüenem Land). 3 Hinder em Volk s teilte Meer; am Bärg redt de Strahlechranz (Tafle); de Mose mit de Tafle, s Volk.'), 'GROUP-02': ('Vier Felder: 1 Menschen ziehen in ein grünes Land mit Fluss. 2 Ein König vor Jerusalem, daneben Menschen. 3 Jerusalem mit Rissen; Menschen mit Tränen; ein Weg mit Pfeil weg und gestrichelt zurück. 4 Menschen freuen sich vor Jerusalem; Steine werden aufeinandergesetzt (Pfeil nach oben).', 'Vier Fälder: 1 Mänsche zieh i es grüens Land mit eme Fluss. 2 En Chünig vor Jerusalem, dernäbe Mänsche. 3 Jerusalem mit Riss; Mänsche mit Träne; en Wäg mit Pfiil ewäg und gstrichlet zrugg. 4 Mänsche fröied sich vor Jerusalem; Stei wärdet ufenand gsetzt (Pfiil ufe).'), 'GROUP-04': ('Zwei Felder: 1 Oben der Strahlenkranz, eine goldene Linie führt zum Propheten; er spricht zur Menge (Waage, Umkehr-Pfeil). 2 Strahlenkranz mit Linie zum Propheten; Jerusalem mit Rissen, Menschen mit Tränen auf dem Weg weg und zurück; der Prophet spricht von Hoffnung (Spross).', 'Zwei Fälder: 1 Obe de Strahlechranz, e goldigi Linie füert zum Prophet; er redt zur Mängi (Waag, Umchehr-Pfiil). 2 Strahlechranz mit Linie zum Prophet; Jerusalem mit Riss, Mänsche mit Träne uf em Wäg ewäg und zrugg; de Prophet redt vo Hoffnig (Schoss).'), 'GROUP-05': ('Zwei Felder: 1 Zwölf kleine Schriftrollen; der Strahlenkranz mit goldener Linie zum Propheten, der zur Menge spricht (Waage, Umkehr-Pfeil). 2 Strahlenkranz über dem heilen Jerusalem, ein Spross, Menschen freuen sich.', 'Zwei Fälder: 1 Zwölf chlini Schriftrolle; de Strahlechranz mit goldiger Linie zum Prophet, wo zur Mängi redt (Waag, Umchehr-Pfiil). 2 Strahlechranz über em ganze Jerusalem, en Schoss, Mänsche fröied sich.'), 'GROUP-07': ('Zwei Felder: 1 Die Geist-Taube über drei Jüngern mit Flammen über den Köpfen, dahinter Jerusalem. 2 Von Jerusalem gehen Pfeile aus nach Rom (Säulenhalle mit rotem Dach); davor Paulus mit Brief und ein Soldat.', 'Zwei Fälder: 1 D Geischt-Tube über drüü Jünger mit Flamme über de Chöpf, dehinder Jerusalem. 2 Vo Jerusalem gönd Pfiil uus uf Rom (Süülehalle mit rotem Dach); devor de Paulus mit Brief und en Soldat.'), 'GROUP-09': ('Ein Bote mit Brief spricht zu einer Gemeinde vor einem Haus (Sprechblase: Herz mit Strahlen, Anker, zwei Herzen, zwei Schriftrollen mit Haken und Kreuz).', 'En Bott mit Brief redt zu ere Gmeind vor eme Huus (Sprächblase: Härz mit Strahle, Anker, zwei Härz, zwei Schriftrolle mit Hake und Chrüz).')}
for _k, (_a, _g) in _ALT2.items():
    ILL[f"ILL-SYM-{_k}"] = (f"BRIEF-{_k}", _a, _g)
ILL["ILL-SYM-OT"] = ("BRIEF-OT", ILL["ILL-SYM-OT"][1] + ' Oben der Strahlenkranz mit Linie zum Propheten.', ILL["ILL-SYM-OT"][2] + ' Obe de Strahlechranz mit Linie zum Prophet.')


def run():
    lex = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in (D / "illustrations/lexicon").glob("FIG-*.json")}
    for k in RENDER:
        if k not in lex:
            raise SystemExit(f"{k} nicht im Bildlexikon")
    style = {"id": "ILLSTYLE-SYMBOL", "type": "illustration_style", "status": "draft", "tags": [],
             "key": "symbol", "labels": {"de": "Symbol", "en": "Symbol"},
             "description_de": "Flache, klare Symbolbilder. Personen ohne Gesicht, erkennbar an den Pflichtmerkmalen des Bildlexikons; "
                               "Sprechblasen mit Zeichen statt Wörtern; mehrere Schritte als nummerierte Bildfelder.",
             "library": "data/illustrations/symbol/_bibliothek.svg",
             "renderings": {k: {"symbol": v, "viewbox": VB.get(v, VB["ill-p"] if v.startswith("ill-p-") else "0 0 30 64")} for k, v in sorted(RENDER.items())},
             "license": LIC, "authorship_de": AUTH, "knowledge": {"asserted_at": DATE, "supersedes": None}}
    # Stil seit 2026-10-23 eingestellt (Andi Neck): Status bleibt «deprecated». Die Bibliothek bleibt Quelle der
    # Gegenstände und Zeichen des Stils Anime (bilder_anime.COPY); mit --bibliothek nur sie neu schreiben.
    sp = D / "illustrations/styles/ILLSTYLE-SYMBOL.json"
    if sp.exists():
        style["status"] = json.loads(sp.read_text(encoding="utf-8")).get("status", style["status"])
    lib = auto_library()
    n = 0
    if (OUT / "_bibliothek.svg").read_text(encoding="utf-8") != lib:
        (OUT / "_bibliothek.svg").write_text(lib, encoding="utf-8")
        n += 1
    if "--bibliothek" in sys.argv:
        print(f"PASS: Bibliothek Symbol (Quelle für Anime); {n} Datei geschrieben")
        return
    n += write(sp, style, "Darstellungen neu nach Bildlexikon (renderings statt eigener Figurenliste)")
    for rid, gen in GENERATED.items():
        svg = gen()
        f = OUT / f"{rid}.svg"
        if not f.exists() or f.read_text(encoding="utf-8").strip() != svg:
            f.write_text(svg + "\n", encoding="utf-8")
            n += 1
    for rid, (brief_id, alt, alt_g) in ILL.items():
        brief = json.loads((D / "illustrations/briefs" / f"{brief_id}.json").read_text(encoding="utf-8"))
        depicts = sorted({x for p in brief["panels"] for k in ("figures", "objects", "signs") for x in p[k]}
                         | {x for p in brief["panels"] for sp in p["speech"] for x in (sp["from"], sp["to"], *sp["icons"])})
        missing = [x for x in depicts if x not in RENDER]
        rec = {"id": rid, "type": "illustration", "status": "draft", "tags": brief.get("tags", []), "style": "ILLSTYLE-SYMBOL",
               "brief": brief_id, "level": brief["level"], **({"reference": brief["reference"]} if brief.get("reference") else {}), "target": brief["target"],
               "file": f"data/illustrations/symbol/{rid}.svg", "depicts": [x for x in depicts if x in RENDER],
               **({"not_rendered": missing} if missing else {}), "alt_de": alt, "license": LIC, "authorship_de": AUTH,
               "knowledge": {"asserted_at": DATE, "supersedes": None}}
        old = OUT / f"{rid}.json"
        if old.exists():
            o = json.loads(old.read_text(encoding="utf-8"))
            if "check" in o:
                rec["check"] = o["check"]
        n += write(old, rec, "Bild nach Bildauftrag neu gezeichnet bzw. neu verknüpft")
        n += localize(rid, rec, {"alt_de": alt_g}, "gsw-u-sd-chzh", "GSW-ZH", "CTX-CH-ZH-GSW-2026", AUTH_GSW, DATE)
    print(f"PASS: Bildstil Symbol – {len(RENDER)} Darstellungen, {len(ILL)} Bilder; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
