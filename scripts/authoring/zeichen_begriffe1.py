#!/usr/bin/env python3
"""Bildzeichen «Begriffe, Teil 1» neu gezeichnet (docs/SYMBOLPROZESS.md, Runde 11, 2026-10-25).

Grund: Die Gestaltungskritik (Runde 11) bemängelte Doppelte (Licht = Stern, Tage = Sonne = Hitze, Wahrheit = vollbracht,
Sünde = unrein, Reich Gottes = Königsherrschaft), Gefühle als Klecks oder Tropfen statt Gesicht und Bedien-Symbole.
Jedes Zeichen hat hier sein eigenes Bild; je Zeichen mehrere Fassungen (…@1, …@2), die Fassung in WAHL wird übernommen.

    python3 scripts/authoring/zeichen_begriffe1.py --entwuerfe E.json [ID …]   # alle Fassungen als Entwürfe für zeichen_test.py
    python3 scripts/authoring/zeichen_begriffe1.py --schreiben                   # gewählte Fassungen → ueberarbeitet/begriffe1.json

Stil «Anime»: flache Flächen, Tinte #3B3226, Haut #E2AE80, Gold #E8B931; Gefühle als Emoji-Gesicht; keine IDs, Filter, Verläufe.
"""
import json
import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "scripts/authoring/bildsymbole_daten/ueberarbeitet/begriffe1.json"

INK, SKIN, GOLD = "#3B3226", "#E2AE80", "#E8B931"
EMO = "#F6D27A"        # Emoji-Gesicht (wie «freundlich»)
RED = "#C8352E"
BLUE_T, BLUE_TS = "#7CC0EE", "#3B6E9E"   # Träne, Tropfen


def f(x):
    return f"{x:.2f}".rstrip("0").rstrip(".")


def circ(cx, cy, r, fill, sw=1.4, stroke=INK, extra=""):
    return f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{extra}/>'


def path(d, fill="none", sw=1.4, stroke=INK, extra=""):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<path d="{d}" fill="{fill}"{st} stroke-linecap="round" stroke-linejoin="round"{extra}/>'


def dot(cx, cy, r=1.1, fill=INK):
    return f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{fill}"/>'


def sparkle(cx, cy, s, fill=GOLD, stroke="#B8891A", sw=.6):
    """Vierzackiges Funkeln."""
    k = s * .28
    d = (f"M{f(cx)} {f(cy - s)}Q{f(cx + k)} {f(cy - k)} {f(cx + s)} {f(cy)}Q{f(cx + k)} {f(cy + k)} {f(cx)} {f(cy + s)}"
         f"Q{f(cx - k)} {f(cy + k)} {f(cx - s)} {f(cy)}Q{f(cx - k)} {f(cy - k)} {f(cx)} {f(cy - s)}z")
    return path(d, fill, sw, stroke)


def drop(cx, top, h, fill=BLUE_T, stroke=BLUE_TS, sw=.8):
    w = h * .42
    d = f"M{f(cx)} {f(top)}Q{f(cx - w * 1.1)} {f(top + h * .55)} {f(cx - w)} {f(top + h * .7)}A{f(w)} {f(w)} 0 0 0 {f(cx + w)} {f(top + h * .7)}Q{f(cx + w * 1.1)} {f(top + h * .55)} {f(cx)} {f(top)}z"
    return path(d, fill, sw, stroke)


def rays(cx, cy, r1, r2, n, color=GOLD, sw=1.6, start=-90, span=360, alt=None):
    out = []
    for i in range(n):
        a = math.radians(start + (span * i / n if span == 360 else span * i / max(1, n - 1)))
        rr2 = r2 if not alt or i % 2 == 0 else alt
        out.append(f"M{f(cx + r1 * math.cos(a))} {f(cy + r1 * math.sin(a))}L{f(cx + rr2 * math.cos(a))} {f(cy + rr2 * math.sin(a))}")
    return path("".join(out), "none", sw, color)


def face(cx, cy, r, fill=EMO, sw=1.5):
    return circ(cx, cy, r, fill, sw)


def crown(cx, base, w, h, fill=GOLD, jewel=RED):
    """Krone: Band unten, drei Zacken mit Kugeln."""
    x0, x1 = cx - w / 2, cx + w / 2
    band = h * .3
    top = base - h
    d = (f"M{f(x0)} {f(base)}V{f(base - band)}L{f(x0 - w * .04)} {f(top + h * .18)}L{f(cx - w * .24)} {f(base - band - h * .22)}"
         f"L{f(cx)} {f(top)}L{f(cx + w * .24)} {f(base - band - h * .22)}L{f(x1 + w * .04)} {f(top + h * .18)}L{f(x1)} {f(base - band)}V{f(base)}z")
    s = path(d, fill, 1.3)
    s += path(f"M{f(x0)} {f(base - band)}H{f(x1)}", "none", 1.0)
    rb = w * .07
    for x, y in ((x0 - w * .04, top + h * .18), (cx, top), (x1 + w * .04, top + h * .18)):
        s += circ(x, y - rb * .6, rb, fill, 1.0)
    s += circ(cx, base - band / 2, rb * 1.05, jewel, .8)
    return s


def cloud(x0, y1, w, h, fill="#FFFFFF", sw=1.3):
    """Wolke mit flachem Boden von x0 bis x0+w, Boden bei y1."""
    sx, sy = w / 26, h / 13
    pts = [(0, 13), (26, 13)]
    d = (f"M{f(x0 + 3 * sx)} {f(y1)}H{f(x0 + 23 * sx)}A{f(4 * sx)} {f(4 * sy)} 0 0 0 {f(x0 + 23.6 * sx)} {f(y1 - 7.8 * sy)}"
         f"A{f(6.2 * sx)} {f(6.2 * sy)} 0 0 0 {f(x0 + 12.4 * sx)} {f(y1 - 9.6 * sy)}A{f(4.6 * sx)} {f(4.6 * sy)} 0 0 0 {f(x0 + 4.6 * sx)} {f(y1 - 6.4 * sy)}"
         f"A{f(3.3 * sx)} {f(3.3 * sy)} 0 0 0 {f(x0 + 3 * sx)} {f(y1)}z")
    del pts
    return path(d, fill, sw)


def sun(cx, cy, r, core="#F2C76E", ray="#D9A441", n=8, rl=None, sw=1.6, edge="#D9A441"):
    rl = rl or r * .75
    return rays(cx, cy, r + 1.2, r + 1.2 + rl, n, ray, sw) + circ(cx, cy, r, core, 1.2, edge)


def qmark(x, y, s, color="#5E7FA8", sw=2.2):
    """Fragezeichen; (x, y) = oberer linker Punkt des Bogens, s = Breite."""
    d = f"M{f(x)} {f(y + s * .5)}Q{f(x)} {f(y - s * .05)} {f(x + s * .5)} {f(y - s * .05)}T{f(x + s)} {f(y + s * .5)}Q{f(x + s)} {f(y + s * .95)} {f(x + s * .5)} {f(y + s * 1.15)}V{f(y + s * 1.5)}"
    return path(d, "none", sw, color) + dot(x + s * .5, y + s * 2.05, sw * .62, color)


def piece(x, y, s, t, r_, b, l, fill, sw=1.1):
    """Puzzlestück: Quadrat mit Nasen (+1 aussen, -1 innen, 0 flach) oben, rechts, unten, links; im Uhrzeigersinn."""
    k = s * .17
    def side(ax, ay, bx, by, kind):
        if not kind:
            return f"L{f(bx)} {f(by)}"
        mx, my = (ax + bx) / 2, (ay + by) / 2
        ux, uy = (bx - ax) / s, (by - ay) / s
        p1 = (mx - ux * k, my - uy * k)
        p2 = (mx + ux * k, my + uy * k)
        sweep = 1 if kind > 0 else 0
        return f"L{f(p1[0])} {f(p1[1])}A{f(k * 1.15)} {f(k * 1.15)} 0 1 {sweep} {f(p2[0])} {f(p2[1])}L{f(bx)} {f(by)}"
    d = (f"M{f(x)} {f(y)}" + side(x, y, x + s, y, t) + side(x + s, y, x + s, y + s, r_)
         + side(x + s, y + s, x, y + s, b) + side(x, y + s, x, y, l) + "z")
    return path(d, fill, sw)


# ---------------------------------------------------------------- Gefühle (Emoji-Gesichter)

def freude(v):
    s = face(17, 19, 12)
    s += path("M10.6 16.2q2-3 4 0M19.4 16.2q2-3 4 0", "none", 1.6)                       # lachende Augen
    s += path("M10.4 20.6h13.2q-.4 7.6-6.6 7.6t-6.6-7.6z", "#7A2A22", 1.3)                # offener Mund
    s += path("M11 20.7h12q-.2 1.6-.6 2.2h-10.8q-.4-.6-.6-2.2z", "#FFFFFF", 0, None)
    s += path("M13.2 26.6q3.8-3.4 7.6 0q-1.6 1.6-3.8 1.6t-3.8-1.6z", "#E07A8A", 0, None)
    s += circ(8.6, 21.4, 1.8, "#F2A07A", 0, "none", ' opacity=".7"') + circ(25.4, 21.4, 1.8, "#F2A07A", 0, "none", ' opacity=".7"')
    if v == 1:
        s += sparkle(4, 6.6, 3.2) + sparkle(30.4, 5.4, 3.6) + sparkle(31.4, 15.6, 2.2) + sparkle(2.8, 15.2, 2)
    else:
        s += rays(17, 19, 14.6, 17.6, 7, GOLD, 1.8, -170, 160)
    return ("0 0 34 33" if v == 1 else "-1 0 36 33"), s


def trauer(v):
    s = face(16, 17, 13)
    if v == 1:
        s += path("M8.6 11.6L13.2 9.6M23.4 11.6L18.8 9.6", "none", 1.5)                    # Brauen innen hoch
        s += dot(11.6, 14.8, 1.3) + dot(20.4, 14.8, 1.3)
        s += path("M10.8 24.2q5.2-4.6 10.4 0", "none", 1.7)
        s += drop(21.2, 16.6, 8.2)
    else:
        s += path("M8.6 11L13.2 9.2M23.4 11L18.8 9.2", "none", 1.5)
        s += path("M9.6 14.6q2 1.8 4 0M18.4 14.6q2 1.8 4 0", "none", 1.6)                 # geschlossene, traurige Augen
        s += path("M11.6 24.4q4.4-3.6 8.8 0", "none", 1.7)
        s += drop(10.6, 16.6, 7.4) + drop(21.4, 16.6, 7.4)
    return "0 0 32 31", s


def zorn(v):
    fill = "#EE7A54" if v == 1 else EMO
    s = face(14.6, 18, 12.6, fill)
    s += path("M7 12.2L12.6 14.6M22.2 12.2L16.6 14.6", "none", 2.0)                       # V-Brauen
    s += dot(10.8, 17.2, 1.3) + dot(18.4, 17.2, 1.3)
    if v == 1:
        s += path("M9.4 25.4q5.2-4.6 10.4 0", "none", 1.9)
    else:
        s += path("M8.6 22.2h12v4.2h-12z", "#FFFFFF", 1.2) + path("M11.6 22.2v4.2M14.6 22.2v4.2M17.6 22.2v4.2M8.6 24.3h12", "none", .7)
    s += path("M24.2 4.8Q26.2 5 26.2 2.8M30.8 4.8Q28.8 5 28.8 2.8M24.2 8.6Q26.2 8.4 26.2 10.6M30.8 8.6Q28.8 8.4 28.8 10.6",
              "none", 1.8, RED)                                                           # 💢
    return "0 0 32 32", s


def luege(v):
    if v == 1:
        s = face(13, 17, 12)
        s += path("M6.2 11.6L10.4 10.6M15 10.4L19.2 11.4", "none", 1.4)
        s += dot(10.2, 14.6, 1.2) + dot(17.2, 14.6, 1.2)                                  # Blick zur Seite
        s += path("M8.4 22.6q3.6 1.6 7.6-1", "none", 1.6)                                 # schiefes Lächeln
        s += path("M14 16.4H29.4a1.7 1.7 0 0 1 0 3.4H14", EMO, 1.3)                       # lange Nase 🤥
        s += path("M14.2 16.5V19.7", "none", 2.2, EMO)
        return "0 0 33 30", s
    # Sprechblase mit gespaltener Zunge
    s = path("M3 5.4Q3 2.6 6 2.6H27Q30 2.6 30 5.4V18Q30 20.8 27 20.8H12L6.6 26.4L7.6 20.8H6Q3 20.8 3 18z", "#FFFFFF", 1.4)
    s += path("M8.4 11.6H17.6L25 7.6M17.6 11.6L25.6 15", "none", 2.6, "#B8312F")
    s += path("M8.4 11.6H17.6L25 7.6M17.6 11.6L25.6 15", "none", 1.2, "#E2626A")
    return "0 0 33 28", s


def unglaube(v):
    s = face(14.4, 17.6, 12.4)
    s += path("M7.4 10.8Q9.6 7.2 13 9.4", "none", 1.7)                                   # hochgezogene Braue
    s += path("M16.6 12.4L21.8 13.2", "none", 1.7)                                       # gesenkte Braue
    s += dot(10.4, 14.6, 1.35) + dot(19.2, 16, 1.35)
    s += path("M9.6 23.2Q13 22 19.4 22.8", "none", 1.7)
    if v == 1:
        return "0 0 30 31", s
    s += qmark(27, 3.2, 4.6, "#5E7FA8", 2.0)
    return "0 0 34 31", s


def hass(v):
    def head(cx, look, shirt, hair):
        o = path(f"M{f(cx - 7.6)} 31Q{f(cx - 7.2)} 23 {f(cx)} 23T{f(cx + 7.6)} 31z", shirt, 1.2)
        o += circ(cx, 15, 6.8, SKIN, 1.3)
        o += path(f"M{f(cx - 6.8)} 14.2q0-7 6.8-7t6.8 7q-1.8-3.2-6.8-3.4-5 .2-6.8 3.4z", hair, .8)
        ex = cx + look * 1.4
        o += path(f"M{f(ex - 4)} 12.6L{f(ex - .9)} 14.4M{f(ex + .9)} 14.4L{f(ex + 4)} 12.6", "none", 1.6)
        o += dot(ex - 2.3, 16.4, 1.05) + dot(ex + 2.3, 16.4, 1.05)
        o += path(f"M{f(ex - 2.2)} 20.2q2.2-1.5 4.4 0", "none", 1.3)
        return o
    if v == 1:
        s = head(7.8, 1, "#5E7FA8", "#3A2A1E") + head(32.2, -1, "#A0563A", "#7A4A22")
        s += path("M21.6 6L18 13.6H22L18.4 22", "none", 2.6, RED)
        return "0 0 40 32", s
    s = head(7.8, -1, "#5E7FA8", "#3A2A1E") + head(32.2, 1, "#A0563A", "#7A4A22")
    s += path("M21.6 6L18 13.6H22L18.4 22", "none", 2.6, RED)
    return "0 0 40 32", s


def herz(v):
    body = "#C3CEDB"
    if v == 1:
        s = path("M3 32Q3.4 19.4 16 19.4T29 32z", body, 1.3) + circ(16, 9.4, 6.6, body, 1.3)
        s += path("M16 30.4C11.2 27.6 9.6 25.2 9.6 23.2a3.2 3.2 0 0 1 6.4-1.2 3.2 3.2 0 0 1 6.4 1.2c0 2-1.6 4.4-6.4 7.2z", "#C2414E", 1.1)
        return "0 0 32 33", s
    # Profil nach rechts, Herz in der Brust
    s = path("M5 32Q5 21 13 19.6L14.4 16.6Q9.4 15.4 9.4 9.6Q9.4 3 16 3Q22.4 3 22.6 9Q23.6 10.6 24.6 12.2Q23.6 12.8 22.8 13Q22.6 16.4 19.6 16.8L19.2 19.4Q27.6 20.6 28 32z",
             body, 1.3)
    s += path("M18 30C13.6 27.4 12.2 25.2 12.2 23.4a2.9 2.9 0 0 1 5.8-1.1 2.9 2.9 0 0 1 5.8 1.1c0 1.8-1.4 4-5.8 6.6z", "#C2414E", 1.1)
    return "0 0 32 33", s


# ---------------------------------------------------------------- Herrschaft

def reich_gottes(v):
    if v == 1:  # Krone auf grosser Wolke
        s = rays(18, 14, 10.4, 13.2, 5, GOLD, 1.8, -150, 120)
        s += cloud(1.6, 31, 32.8, 13.6)
        s += crown(18, 24.4, 14, 11)
        return "0 0 36 32", s
    # himmlische Stadt auf Wolke, Krone darüber
    s = crown(18, 10.6, 11, 8.4)
    s += cloud(1.6, 31.4, 32.8, 11)
    s += path("M9.6 23.6V17.4H12V15.6H14.4V17.4H21.6V15.6H24V17.4H26.4V23.6z", "#F2E3B8", 1.1)
    s += path("M16.2 23.6V20.4Q18 18.4 19.8 20.4V23.6z", "#C08A2A", .9)
    return "0 0 36 32", s


def koenigsherrschaft(v):
    if v == 1:  # Zepter mit Krone als Knauf
        s = rays(16, 9, 9.6, 12.6, 7, GOLD, 1.6, -170, 160)
        s += path("M16 15.6V31", "none", 4.4) + path("M16 15.6V31", "none", 2.6, "#C08A2A")
        s += circ(16, 22, 2.0, GOLD, 1.0) + circ(16, 30.6, 1.6, GOLD, 1.0)
        s += crown(16, 16.6, 13, 10.4)
        return "0 0 32 32", s
    # Krone links, Zepter senkrecht daneben
    s = rays(13, 16, 11.6, 14.4, 5, GOLD, 1.6, -160, 140)
    s += crown(13, 28.6, 17, 13)
    s += path("M28.4 9V31", "none", 4.0) + path("M28.4 9V31", "none", 2.2, "#C08A2A")
    s += circ(28.4, 6.6, 3.0, GOLD, 1.2) + sparkle(28.4, 6.6, 1.6, "#FFF6DC", "#C08A2A", .4)
    return "0 0 32 32", s


# ---------------------------------------------------------------- Licht, Zeichen, Zeit

def licht(v):
    s = circ(16, 16, 14, "#FBEBB0", 0, "none", ' opacity=".8"') + circ(16, 16, 9.4, "#F8DB7A", 0, "none")
    if v == 1:
        out = []
        for i in range(16):
            a = math.radians(i * 22.5 - 90)
            r2 = 15.6 if i % 2 == 0 else 11.6
            w = .18 if i % 2 == 0 else .16
            pa, pb = a - w, a + w
            out.append(f"M{f(16 + 5 * math.cos(pa))} {f(16 + 5 * math.sin(pa))}L{f(16 + r2 * math.cos(a))} {f(16 + r2 * math.sin(a))}"
                       f"L{f(16 + 5 * math.cos(pb))} {f(16 + 5 * math.sin(pb))}z")
        s += path("".join(out), GOLD, .6, "#D29A1E")
        s += circ(16, 16, 5.2, "#FFFDF2", 1.0, "#E8B931")
        return "0 0 32 32", s
    s += rays(16, 16, 6.4, 15.4, 12, GOLD, 1.3, -90, 360, alt=11.8)
    s += circ(16, 16, 5.4, "#FFFFFF", 1.2, GOLD) + circ(16, 16, 2.6, "#FFF7D6", 0, "none")
    return "0 0 32 32", s


def stern_zeichen(v):
    import haende as H
    if v == 1:  # zeigende Hand weist auf strahlendes Funkeln
        s = H.place(H.hand_zeigend(), 4.6, 22, -28, 1.0)
        s += rays(27, 8.4, 6.2, 8.6, 8, GOLD, 1.4)
        s += sparkle(27, 8.4, 6)
        return "0 0 36 32", s
    # offene Hand, darüber Funkeln mit Strahlen (Tat, die auf Herrlichkeit weist)
    s = H.place(H.hand_empfangend(), 5, 25.6, -8, 1.1)
    s += rays(17, 9.6, 6.4, 9.2, 8, GOLD, 1.5)
    s += sparkle(17, 9.6, 6.2)
    return "0 0 32 32", s


def tage(v):
    def sheet(x, y, top=True):
        o = path(f"M{f(x)} {f(y + 2)}Q{f(x)} {f(y)} {f(x + 2)} {f(y)}H{f(x + 18)}Q{f(x + 20)} {f(y)} {f(x + 20)} {f(y + 2)}V{f(y + 19)}Q{f(x + 20)} {f(y + 21)} {f(x + 18)} {f(y + 21)}H{f(x + 2)}Q{f(x)} {f(y + 21)} {f(x)} {f(y + 19)}z", "#FFFFFF", 1.3)
        o += path(f"M{f(x)} {f(y + 6)}V{f(y + 2)}Q{f(x)} {f(y)} {f(x + 2)} {f(y)}H{f(x + 18)}Q{f(x + 20)} {f(y)} {f(x + 20)} {f(y + 2)}V{f(y + 6)}z", RED, 1.3)
        return o
    if v == 1:  # drei gestapelte Kalenderblätter, vorn eine Sonne
        s = sheet(10.4, 2) + sheet(7.2, 5.4) + sheet(4, 8.8)
        s += sun(14, 21, 3.6, "#F2C76E", "#D9A441", 8, 2.2, 1.4, "#C9902E")
        return "0 0 32 32", s
    s = sheet(1.6, 6.4).replace("20", "20")
    s = path("M1.6 9Q1.6 6.6 4 6.6H28Q30.4 6.6 30.4 9V27.6Q30.4 30 28 30H4Q1.6 30 1.6 27.6z", "#FFFFFF", 1.4)
    s += path("M1.6 12.6V9Q1.6 6.6 4 6.6H28Q30.4 6.6 30.4 9V12.6z", RED, 1.4)
    s += path("M11.2 12.6V30M20.8 12.6V30", "none", 1.0, "#B9AE9C")
    for cx in (6.4, 16, 25.6):
        s += circ(cx, 21.4, 3.0, "#F2C76E", 1.1, "#C9902E") + rays(cx, 21.4, 3.9, 4.4, 8, "#D9A441", .9)
    s += path("M9 3.4V8.8M23 3.4V8.8", "none", 3.0) + path("M9 3.4V8.8M23 3.4V8.8", "none", 1.4, "#CFC6B6")
    return "0 0 32 32", s


def hitze(v):
    if v == 1:  # Sonne und schwitzendes Gesicht, getrennt
        s = rays(8.6, 8.6, 5.8, 8.6, 8, "#E8622C", 1.9) + circ(8.6, 8.6, 4.8, "#F59A3C", 1.2, "#D0541E")
        s += face(21.8, 21, 10, "#F28A6A")
        s += path("M16.4 18.4q1.6-1.4 3.2 0M24 18.4q1.6-1.4 3.2 0", "none", 1.4)
        s += path("M18.4 24.8q3.4-2 6.8 0", "none", 1.5)
        s += drop(27.6, 12.4, 4.6) + drop(15.2, 14.6, 4)
        return "0 0 34 32", s
    # Thermometer hoch und Sonne
    s = rays(10, 10, 6.2, 9.4, 8, "#E8622C", 2.0) + circ(10, 10, 5.2, "#F59A3C", 1.2, "#D0541E")
    s += path("M22.6 4.6a3 3 0 0 1 6 0V20.6a5 5 0 1 1-6 0z", "#FFFFFF", 1.4)
    s += path("M25.6 8V23", "none", 2.4, RED) + circ(25.6, 24.6, 3.2, RED, 0, "none")
    s += path("M28.6 7.4h1.6M28.6 11h1.6M28.6 14.6h1.6", "none", .9)
    return "0 0 32 32", s


# ---------------------------------------------------------------- Wahrheit, vollbracht, Tod

def wahrheit(v):
    if v == 1:
        s = path("M3 6Q3 2.8 6.4 2.8H26.6Q30 2.8 30 6V18.6Q30 21.8 26.6 21.8H12.6L6.6 27.6L7.6 21.8H6.4Q3 21.8 3 18.6z", "#FFF6DC", 1.4, "#C08A2A")
        s += path("M9.4 12.6L14.4 17.2L23.6 7.4", "none", 4.0, "#2F8A3E")
        return "0 0 33 29", s
    # aus einem Mund (Profil) kommt ein Wort mit Haken
    s = path("M2 31V22Q1 19 3.2 17.6L2.4 15.4Q3 14 4.4 13.6Q4 11.4 4.6 9.4Q5.6 4 11 4Q12.6 4 13 4.6V31z", SKIN, 1.3)
    s += path("M4.4 4.6Q8 1.4 12.6 3V12Q9.6 9.6 7.6 9.8z", "#3A2A1E", .8)
    s += path("M16 6Q16 3.6 18.4 3.6H29.6Q32 3.6 32 6V15Q32 17.4 29.6 17.4H20L15.4 21.4L16.6 17.2Q16 16.6 16 15z", "#FFF6DC", 1.3, "#C08A2A")
    s += path("M19.6 10.6L22.8 13.6L28.6 7.4", "none", 2.8, "#2F8A3E")
    return "0 0 33 32", s


def vollbracht(v):
    stone, gold = "#C9BFAA", GOLD
    if v == 1:  # ganz entrollte Schriftrolle mit Siegel: abgeschlossen
        s = path("M6 4H26V27H6z", "#F4EAD2", 1.3)
        s += path("M4 2.4H8V6.4H4zM24 2.4H28V6.4H24z".replace("z", "z"), "none", 0, None)
        s += path("M3.4 4.4Q3.4 2 6 2H26Q28.6 2 28.6 4.4Q28.6 6.6 26 6.6H6Q3.4 6.6 3.4 4.4z", "#D9C29A", 1.3)
        s += path("M3.4 27.4Q3.4 25 6 25H26Q28.6 25 28.6 27.4Q28.6 29.6 26 29.6H6Q3.4 29.6 3.4 27.4z", "#D9C29A", 1.3)
        s += path("M9.4 10.4H22.6M9.4 14H22.6M9.4 17.6H16", "none", 1.1, "#8C8070")
        s += path("M19.4 21.4L18 27.2L20.4 26L22 28.2L22.6 22.4z", RED, .8) + circ(22, 20.4, 3.6, RED, 1.1)
        s += circ(22, 20.4, 2, "none", .7, "#F2A0A0")
        return "0 0 32 32", s
    # Fahne auf dem Gipfel: am Ziel
    s = path("M1 31L13 9.4L18 17L21.4 13L31 31z", "#A69580", 1.4)
    s += path("M13 9.4L10.6 13.8L13 13L15.2 14.4z", "#FFFFFF", .9)
    s += path("M13 9.6V1.6", "none", 1.4) + path("M13.4 2L21 4.4L13.4 6.8z", GOLD, 1.0)
    return "0 0 32 32", s


def tod(v):
    if v == 1:  # Felsgrab mit Rollstein
        s = path("M1 31L2.6 20L6.6 13.4L12.4 9L19.6 8.2L25.6 11L30 16.6L32 23.4L33 31z", "#A69580", 1.4)
        s += path("M7.8 31V22.2Q7.8 16.4 13.4 16.4T19 22.2V31z", "#2A221A", 1.0)
        s += circ(21.6, 24.6, 6.4, "#C9BFAA", 1.4)
        s += path("M17.8 22.6q3.6-2.6 7.4.4", "none", .8, "#8C8070")
        s += path("M24.6 13l2.4 2.2M5 20.6l2 .8M28.6 21.6l1.8-.4", "none", .9, "#6E6252")
        s += path("M0 31H34", "none", 1.4)
        return "0 0 34 32", s
    # Grabstein 🪦
    s = path("M2 31Q4 26.4 16 26.4T30 31z", "#8C6A44", 1.2)
    s += path("M8 27.6V9.6Q8 3 16 3T24 9.6V27.6z", "#B4AEA4", 1.4)
    s += path("M12.4 12.6H19.6M12.4 16.6H19.6M13.6 20.6H18.4", "none", 1.3, "#7A746A")
    return "0 0 32 32", s


# ---------------------------------------------------------------- rein / unrein / Sünde

ROBE = ("M11 3.4H21L29 9.4L26 14.2L23.4 12.6V30.6H8.6V12.6L6 14.2L3 9.4z")


def robe(fill):
    return path(ROBE, fill, 1.4) + path("M13 3.4L16 8.4L19 3.4", "none", 1.1)


def rein(v):
    s = robe("#FFFFFF")
    s += sparkle(28.4, 21, 3.8, "#9CCBEB", "#3B6E9E") + sparkle(3.6, 21.6, 3, "#9CCBEB", "#3B6E9E") + sparkle(27.6, 3.2, 2.8, GOLD)
    if v == 2:
        s = circ(16, 17, 15.4, "#E4F1FA", 0, "none") + s
    return "0 0 32 32", s


def unrein(v):
    s = robe("#D9D2C0")
    st = "#6A4A26"
    s += path("M10.6 15q2.4-2 4 .2 2.2-.8 1.8 2 1.2 2.2-1.4 2.6-1.4 2.2-3.2.2-2.6.2-2.2-2.2-1.4-1.8 1-2.8z", st, 0, None)
    s += path("M17.8 22q2.2-1.6 3.4.6 2 .2 1 2.2.6 2.2-2 2-1.6 1.2-2.6-.8-2-.8-.8-2.2-.8-1.4 1-1.8z", st, 0, None)
    s += path("M17.2 9.2q1.6-1 2.4.4 1.4.6.4 1.8-.4 1.4-2 1-1.6.2-1.6-1.2.2-1.6.8-2z", st, 0, None)
    s += circ(12, 26.4, 1.3, st, 0, "none") + circ(21.8, 14.8, 1, st, 0, "none")
    if v == 1:
        s += path("M26.4 18.6q-1.4 1.4 0 2.8t0 2.8M29.6 17.6q-1.4 1.4 0 2.8t0 2.8", "none", 1.3, "#7E8A54")
    return "0 0 32 32", s


def suende(v):
    def target(cx, cy, r):
        return (circ(cx, cy, r, "#FFFFFF", 1.5) + circ(cx, cy, r * .7, RED, 0, "none") + circ(cx, cy, r * .44, "#FFFFFF", 0, "none")
                + circ(cx, cy, r * .2, RED, 0, "none") + circ(cx, cy, r, "none", 1.5))
    def arrow(x0, y0, x1, y1, head=True):
        a = math.atan2(y1 - y0, x1 - x0)
        ux, uy = math.cos(a), math.sin(a)
        px, py = -uy, ux
        o = path(f"M{f(x0)} {f(y0)}L{f(x1)} {f(y1)}", "none", 4.2) + path(f"M{f(x0)} {f(y0)}L{f(x1)} {f(y1)}", "none", 2.4, "#A0703E")
        if head:
            hx, hy = x1 + ux * 4.4, y1 + uy * 4.4
            o += path(f"M{f(hx)} {f(hy)}L{f(x1 + px * 3)} {f(y1 + py * 3)}L{f(x1 - px * 3)} {f(y1 - py * 3)}z", "#9AA0A8", 1.2)
        for k in (0, 2.4):
            bx, by = x0 + ux * k, y0 + uy * k
            o += path(f"M{f(bx)} {f(by)}L{f(bx - ux * 3 + px * 2.8)} {f(by - uy * 3 + py * 2.8)}M{f(bx)} {f(by)}L{f(bx - ux * 3 - px * 2.8)} {f(by - uy * 3 - py * 2.8)}",
                      "none", 1.8, RED)
        return o
    if v == 1:  # Pfeil steckt neben der Scheibe
        s = target(12, 13.6, 10.4) + path("M9.4 23.6L7 30.6M14.6 23.6L17 30.6", "none", 1.8, "#8C6A44")
        s += path("M1 31H34", "none", 1.4)
        s += arrow(32.4, 13, 28.6, 26.4, head=False) + path("M25 31Q28.4 27.4 31.8 31z", "#8C6A44", 1.1)
        return "0 0 35 32", s
    s = target(13, 17.6, 11.4)
    s += arrow(4.4, 3.6, 29.6, 4.6)
    s += path("M24 9.4l3 .6M21 11.6l2.6.4", "none", 1.0, "#8A7A6A")
    return "0 0 35 31", s


# ---------------------------------------------------------------- fehlt, Sturm, Finsternis

def fehlt(v):
    clay = "#C9A27A"
    jug = (path("M6.6 4.4H15.4L14.2 8.4Q19.6 11.6 19.4 19.6Q19 26.8 15.2 29.4H6.8Q3 26.8 2.6 19.6Q2.4 11.6 7.8 8.4z", clay, 1.4)
           + path("M18.4 12.6Q23.6 12.6 23.2 17.6Q22.8 21.6 18.6 22.4", "none", 3.6) + path("M18.4 12.6Q23.6 12.6 23.2 17.6Q22.8 21.6 18.6 22.4", "none", 1.8, clay)
           + '<ellipse cx="11" cy="4.4" rx="5.2" ry="1.7" fill="#2A221A" stroke="#3B3226" stroke-width="1.2"/>')
    if v == 1:  # Krug ausgeschüttet, nur ein letzter Tropfen
        s = f'<g transform="translate(17.4 15.6) rotate(-125) translate(-12 -17)">{jug}</g>'
        s += drop(4.6, 26, 4.8)
        return "0 0 34 32", s
    # Krug liegt umgekippt, Öffnung zum Betrachter: innen leer
    s = path("M2 29.4H31", "none", 1.3)
    s += f'<g transform="translate(16 20) rotate(-90) translate(-11 -17)">{jug.replace("ry=\"1.7\"", "ry=\"1.7\"")}</g>'
    s += path("M3.6 27.6q1.4-1 2.8 0", "none", 1.0, "#3B6E9E")
    return "0 0 32 30", s


def sturm(v):
    boat = (path("M-7 0H7L4.8 3.8H-4.8z", "#9A6A3A", 1.2) + path("M0 0V-11", "none", 1.3)
            + path("M.6 -10.4L6.4 -1.4H.6z", "#F2EBDD", 1.0) + path("M-.6 -9.4L-5.4 -1.4H-.6z", "#F2EBDD", 1.0))
    if v == 1:  # dunkle Wolke, Wind, Boot zwischen hohen Wellen
        s = path("M2 12.6H24A4.4 4.4 0 0 0 23.4 4 6 6 0 0 0 12.4 3.6 4.4 4.4 0 0 0 4.8 7.4 3 3 0 0 0 2 12.6z", "#5A6272", 1.3)
        s += path("M26 6.4H33M27.6 10.6H34", "none", 1.6, "#8A8478")
        s += f'<g transform="translate(17 22.6) rotate(-16)">{boat}</g>'
        s += path("M1 31V25Q4.4 18.6 8.8 21Q6.4 22.6 7.4 25.4Q10 24.4 12.6 26.6Q17 24 21.4 26.6Q24.6 22 27 24.6Q25 19 30 18.6Q34 18.6 35 22V31z",
                  "#4C86C6", 1.3)
        s += path("M27.4 20.6Q29.4 19.4 31.6 20.4M3.6 23Q5 21.4 7 21.6", "none", 1.0, "#FFFFFF")
        return "0 0 36 32", s
    s = f'<g transform="translate(16 15.4) rotate(14)">{boat}</g>'
    s += path("M1 31V20.6Q5 13 11 16.4Q8.4 18 9.4 20.6Q12.6 19 15.2 21.2Q19.8 18.4 23.4 21.6Q22.4 14.8 28.4 14Q33.6 14 35 18.6V31z", "#4C86C6", 1.3)
    s += path("M24.4 17Q26.6 15.4 30 16.4M3 19.6Q5.4 16.6 8.6 17", "none", 1.0, "#FFFFFF")
    s += path("M1.6 3.4H13Q16 3.4 16 1.2M3 7.4H20Q23 7.4 23 9.6", "none", 1.6, "#8A8478")
    return "0 0 36 32", s


def finsternis(v):
    if v == 1:  # nur zwei Augen im Dunkeln
        s = path("M16 1.6C26 1.6 31 8 31 16S26 30.4 16 30.4 1 24 1 16 6 1.6 16 1.6z", "#1F2433", 1.4)
        s += '<ellipse cx="11.6" cy="15.4" rx="3" ry="3.8" fill="#FFFFFF"/><ellipse cx="20.4" cy="15.4" rx="3" ry="3.8" fill="#FFFFFF"/>'
        s += dot(12.4, 16.2, 1.5) + dot(21.2, 16.2, 1.5)
        return "0 0 32 32", s
    # erloschene Kerze mit Rauchfaden im Dunkeln
    s = path("M16 1.6C26 1.6 31 8 31 16S26 30.4 16 30.4 1 24 1 16 6 1.6 16 1.6z", "#1F2433", 1.4)
    s += path("M12.4 26.4V15.4H19.6V26.4z", "#D8D2C4", 1.0, "#F2EEE4") + path("M9.6 26.4H22.4", "none", 1.6, "#8A8E9A")
    s += path("M16 15.4V13.2", "none", 1.2, "#0E1118")
    s += path("M16 12.6Q14.2 10.6 16 8.6T15.6 4.2", "none", 1.4, "#9AA0B2")
    return "0 0 32 32", s


# ---------------------------------------------------------------- Liste

ZEICHEN = {
    "FIG-ZEICHEN-FREUDE": (freude, 2, "Freude, sich freuen", "lachendes Emoji-Gesicht mit offenem Mund, Funkeln bzw. Strahlen"),
    "FIG-ZEICHEN-TRAUER": (trauer, 2, "Trauer, traurig sein", "trauriges Emoji-Gesicht mit Träne (😢)"),
    "FIG-ZEICHEN-ZORN": (zorn, 2, "Zorn, zornig sein", "wütendes Gesicht mit V-Brauen und Zornzeichen 💢"),
    "FIG-ZEICHEN-LUEGE": (luege, 2, "Lüge, Lügner", "Gesicht mit langer Nase (🤥) bzw. Sprechblase mit gespaltener Zunge"),
    "FIG-ZEICHEN-UNGLAUBE": (unglaube, 2, "Unglaube, Zweifel", "skeptisches Gesicht mit hochgezogener Braue und Fragezeichen (🤨)"),
    "FIG-ZEICHEN-HASS": (hass, 2, "Hass, hassen, Feindschaft", "zwei Menschen mit bösem Blick, roter Blitz zwischen ihnen"),
    "FIG-ZEICHEN-HERZ": (herz, 2, "Herz (das Innere des Menschen)", "Oberkörper-Silhouette, rotes Herz leuchtet in der Brust"),
    "FIG-ZEICHEN-REICH-GOTTES": (reich_gottes, 2, "Reich Gottes / Himmelreich", "goldene Krone auf einer Wolke bzw. über einer Stadt, Strahlen"),
    "FIG-ZEICHEN-KOENIGSHERRSCHAFT": (koenigsherrschaft, 2, "Königsherrschaft (Gottes), Gott regiert", "Krone mit Zepter bzw. Thron mit Krone, Strahlen"),
    "FIG-ZEICHEN-LICHT": (licht, 2, "Licht, Herrlichkeit", "Strahlenkranz: heller Kern, lange und kurze Strahlen, Schein"),
    "FIG-ZEICHEN-STERN": (stern_zeichen, 2, "Zeichen (Tat, die auf Gottes Herrlichkeit hinweist)", "Wegweiser zeigt auf ein Funkeln bzw. Pfeil weist auf Funkeln"),
    "FIG-ZEICHEN-TAGE": (tage, 2, "Tage (eine Zahl von Tagen, z. B. in drei Tagen)", "Kalenderblatt mit Sonne bzw. drei Sonnen"),
    "FIG-ZEICHEN-HITZE": (hitze, 2, "Hitze, stechende Sonne", "stechende Sonne und schwitzendes Gesicht bzw. Hitzeflimmern über Boden"),
    "FIG-ZEICHEN-WAHRHEIT": (wahrheit, 2, "Wahrheit, wahr", "Sprechblase mit grünem Haken (wahres Wort)"),
    "FIG-ZEICHEN-VOLLBRACHT": (vollbracht, 2, "vollbracht, vollendet («Es ist vollbracht»)", "Puzzle, das letzte Stück wird eingesetzt"),
    "FIG-ZEICHEN-TOD": (tod, 2, "Tod, sterben", "Felsgrab mit Rollstein bzw. Grabstein"),
    "FIG-ZEICHEN-REIN": (rein, 2, "rein, rein werden", "weisses Gewand mit Funkeln bzw. Wassertropfen"),
    "FIG-ZEICHEN-UNREIN": (unrein, 2, "unrein", "fleckiges Gewand (Gegenstück zu rein)"),
    "FIG-ZEICHEN-SUENDE": (suende, 2, "Sünde (das Ziel verfehlen)", "Pfeil verfehlt die Zielscheibe"),
    "FIG-ZEICHEN-FEHLT": (fehlt, 2, "fehlt, leer, aufgebraucht", "leerer gekippter Krug bzw. leerer offener Krug"),
    "FIG-ZEICHEN-STURM": (sturm, 2, "Sturm (Seesturm)", "hohe Welle, kleines Boot, Windlinien"),
    "FIG-ZEICHEN-FINSTERNIS": (finsternis, 2, "Finsternis, Dunkelheit", "dunkle Fläche mit erloschener Lampe bzw. verfinsterter Sonne"),
}

# gewählte Fassung je Zeichen (nach Gestaltungskritik und Blindtest); fehlt ein Zeichen, bleibt die alte Zeichnung
WAHL = {}


def entwurf(k, v):
    fn, _, bed, gez = ZEICHEN[k]
    vb, svg = fn(v)
    return {"vb": vb, "svg": svg, "bedeutung": bed, "gezeichnet": gez}


def main():
    a = sys.argv[1:]
    if "--entwuerfe" in a:
        i = a.index("--entwuerfe")
        out = pathlib.Path(a[i + 1])
        ids = [x for x in a[:i] + a[i + 2:] if not x.startswith("--")]
        res = {}
        for k in ids or ZEICHEN:
            kk, _, vv = k.partition("@")
            vs = [int(vv)] if vv else range(1, ZEICHEN[kk][1] + 1)
            for v in vs:
                res[f"{kk}@{v}"] = entwurf(kk, v)
        out.write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"PASS: {len(res)} Entwürfe → {out}")
    elif "--schreiben" in a:
        res = {}
        for k, v in WAHL.items():
            e = entwurf(k, v)
            res[k] = {"vb": e["vb"], "svg": e["svg"]}
        OUT.write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"PASS: {len(res)} Zeichen → {OUT}")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
