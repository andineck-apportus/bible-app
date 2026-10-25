#!/usr/bin/env python3
"""Neu gezeichnete Bildzeichen «Gegenstände und Orte» (docs/SYMBOLPROZESS.md, Runde 11, 2026-10-25).

Grund: Die Gestaltungskritik der Runde 11 liess diese Zeichen nicht bestehen (Landschaften als blasse Streifen ohne Kontur,
Doppelte See/Meer/Jordan und Feld/Kornfeld, griechischer statt herodianischer Tempel, Fäustlinge, abgeschnittene Formen).
Jedes Zeichen hat ein benanntes Vorbild (VORBILD) und bis zu drei Fassungen (@1, @2, @3).

    python3 scripts/authoring/zeichen_dinge.py entwuerfe E.json [FIG-…]     # alle Fassungen als Entwürfe für zeichen_test.py
    python3 scripts/authoring/zeichen_dinge.py schreiben FIG-…@n …          # gewählte Fassungen nach ueberarbeitet/dinge.json

Stil: flache Flächen, dunkle Kontur #3B3226 (aussen dicker), warme Farben, Gold #E8B931; keine IDs, Filter, Verläufe.
Seitenverhältnis wie die bisherige Zeichnung (Landschaftsbänder 186 × 70, Tempel 200 × 150).
"""
import json
import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import haende as H  # noqa: E402

INK, GOLD, GOLD2, SKIN = "#3B3226", "#E8B931", "#D9A441", "#E2AE80"
CREAM, PAPER, RED, DRED = "#F4F1EA", "#EFE3C8", "#A33A2E", "#6E1F18"
WATER, WATER2, WDARK, FOAM = "#5DA7DB", "#4A90C8", "#2E5478", "#DCEFFB"
GREEN, GREEN2, GREEN3, LEAF = "#9DB874", "#7FA05A", "#5E7F3E", "#6E8A52"
SAND, SAND2, ROCK, ROCK2 = "#E8CE96", "#D8B572", "#B9A07A", "#9C8462"
WOOD, WOOD2, STONE, STONE2 = "#9A6A3A", "#7A4F28", "#CFC4AE", "#A79A80"
SKY = "#E9F1F2"
OUT = pathlib.Path(__file__).resolve().parent / "bildsymbole_daten/ueberarbeitet/dinge.json"


def P(d, fill, sw=1.0, extra=""):
    return f'<path d="{d}" fill="{fill}" stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"{extra}/>'


def L(d, sw=.7, col=INK, extra=""):
    return f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{extra}/>'


def F(d, fill, extra=""):
    return f'<path d="{d}" fill="{fill}"{extra}/>'


def C(cx, cy, r, fill, sw=1.0, col=INK):
    return f'<circle cx="{cx:g}" cy="{cy:g}" r="{r:g}" fill="{fill}" stroke="{col}" stroke-width="{sw}"/>'


def E(cx, cy, rx, ry, fill, sw=1.0, extra=""):
    return f'<ellipse cx="{cx:g}" cy="{cy:g}" rx="{rx:g}" ry="{ry:g}" fill="{fill}" stroke="{INK}" stroke-width="{sw}"{extra}/>'


def G(inner, t=""):
    return f'<g transform="{t}">{inner}</g>' if t else inner


def sil(parts, fill, sw):
    """Mehrere Teile als eine Silhouette: Kontur nur aussen (wie haende.sil)."""
    ink = "".join(f'<path d="{p}"/>' for p in parts)
    return (f'<g fill="{INK}" stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round">{ink}</g>'
            f'<g fill="{fill}">{ink}</g>')


def f1(x):
    s = f"{x:.1f}"
    return s[:-2] if s.endswith(".0") else s


def bez(p0, p1, p2, p3, n=24):
    out = []
    for i in range(n + 1):
        t = i / n
        a, b, c, d = (1 - t) ** 3, 3 * t * (1 - t) ** 2, 3 * t * t * (1 - t), t ** 3
        out.append((a * p0[0] + b * p1[0] + c * p2[0] + d * p3[0], a * p0[1] + b * p1[1] + c * p2[1] + d * p3[1]))
    return out


def curve(segs, n=24):
    pts = []
    for s in segs:
        q = bez(*s, n=n)
        pts += q if not pts else q[1:]
    return pts


def tube(pts, wfun, cap_end=True):
    """Geschlossene Fläche entlang einer Mittellinie mit Breite wfun(t) (t 0..1); runde Kappe am Ende."""
    n = len(pts)
    lefts, rights = [], []
    for i, (x, y) in enumerate(pts):
        a = pts[max(0, i - 1)]
        b = pts[min(n - 1, i + 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]
        ln = math.hypot(dx, dy) or 1
        nx, ny = -dy / ln, dx / ln
        w = wfun(i / (n - 1)) / 2
        lefts.append((x + nx * w, y + ny * w))
        rights.append((x - nx * w, y - ny * w))
    d = "M" + " L".join(f"{f1(x)} {f1(y)}" for x, y in lefts)
    if cap_end:
        w = wfun(1) / 2
        d += f" A{f1(w)} {f1(w)} 0 0 1 {f1(rights[-1][0])} {f1(rights[-1][1])}"
    d += " L" + " L".join(f"{f1(x)} {f1(y)}" for x, y in reversed(rights))
    w0 = wfun(0) / 2
    if w0 > .05:
        d += f" A{f1(w0)} {f1(w0)} 0 0 1 {f1(lefts[0][0])} {f1(lefts[0][1])}"
    return d + "Z"


def poly(pts):
    return "M" + " L".join(f"{f1(x)} {f1(y)}" for x, y in pts)


# ------------------------------------------------------------------------------------------------ Gegenstände

def brief(v):
    """Vorbild ✉ mit rotem Wachssiegel (anders als die Schriftrolle mit zwei Stäben)."""
    if v == 1:  # Umschlag geschlossen, Lasche mit Siegel
        return (P("M1.5 3.2H22.5V16.2H1.5Z", PAPER, 1.1) + L("M1.8 16L9.6 9.6M22.2 16L14.4 9.6", .7)
                + P("M1.5 3.2L12 11.4L22.5 3.2Z", CREAM, 1.1)
                + C(12, 11, 2.6, RED, .7, DRED) + L("M10.9 10.4q1.1 1.4 2.2 0M12 9.6v2.6", .5, DRED))
    if v == 2:  # gefaltetes Blatt mit Schrift, Band und Siegel (antiker Brief)
        return (P("M3 1.4H18.6L21 3.8V16.6H3Z", CREAM, 1.1) + P("M18.6 1.4V3.8H21Z", PAPER, .8)
                + L("M5.6 4.8h10M5.6 7.2h12.4M5.6 9.6h12.4M5.6 12h7", .8, "#7A6E60")
                + L("M1.6 13.4H22.4", 1.8, INK) + L("M1.6 13.4H22.4", 1, "#B07A3A")
                + C(17, 13.4, 2.4, RED, .7, DRED) + L("M16 13q1 1.2 2 0", .5, DRED))
    return None


def chest_body(x0, y0, x1, y1, wood=WOOD, band=GOLD2, sw=1.1):
    w = x1 - x0
    return (P(f"M{x0} {y0}H{x1}V{y1}H{x0}Z", wood, sw)
            + L(f"M{x0 + .6} {y0 + (y1 - y0) * .5:.1f}H{x1 - .6}", .6, WOOD2)
            + P(f"M{x0 + w * .16:.1f} {y0}h2.4V{y1}h-2.4Z", band, .7) + P(f"M{x1 - w * .16 - 2.4:.1f} {y0}h2.4V{y1}h-2.4Z", band, .7))


def schatz(v):
    """Vorbild: offene Schatztruhe (Spielsymbol) mit Lichtschein von oben bzw. auf einer Wolke – Schatz «im Himmel»."""
    if v not in (1, 2):
        return None
    lid = (P("M4.4 13.4L4.6 6.4Q4.8 2.2 15 2.2Q25.2 2.2 25.4 6.4L25.6 13.4Z", WOOD, 1.1)
           + P("M6.4 13L6.6 7Q7 4.4 15 4.4Q23 4.4 23.4 7L23.6 13Z", "#5A3A1C", .7))
    coins = "".join(f'<ellipse cx="{x}" cy="{y}" rx="2.3" ry="1.3" fill="{GOLD}" stroke="{INK}" stroke-width=".6"/>'
                    for x, y in [(7.6, 13.4), (11.2, 12.6), (18.8, 12.6), (22.4, 13.4), (9.4, 10.8), (20.6, 10.8), (15, 9.8)])
    gem = P("M13 10.2l2-2.4 2 2.4-2 2.6z", "#C0392B", .6)
    body = chest_body(3.4, 14, 26.6, 24) + P("M13.2 14h3.6v4.6q-1.8 1.4-3.6 0z", GOLD, .7)
    chest = lid + coins + gem + P("M3 12.6Q15 11 27 12.6V14.4H3Z", GOLD, 1) + body
    if v == 1:  # auf einer Wolke
        cloud = P("M2 26.4Q.6 23 4 22.4Q4.6 19.6 8 20.4Q10 18.6 13 20Q16 18.4 19 20Q22 18.6 23.6 20.6Q27 20 27.4 22.6Q30 23.4 28.4 26.4Z", "#FFFFFF", 1)
        return G(chest, "translate(3 -1.2) scale(.8)") + cloud
    rays = L("M15 .2V-1.6M8 1.6L6.8.2M22 1.6L23.2.2M3.6 5L2 4.2M26.4 5L28 4.2", 1.1, GOLD2)
    glow = E(15, 9, 10, 4.6, "#FFF3C4", 0)
    return G(glow + chest, "translate(0 3) scale(1 .96)") + G(rays, "translate(0 1.8)")


def motte(cx, cy, s=1.0):
    """Motte von oben: breite, dreieckige graubraune Flügel, pelziger Leib, gefiederte Fühler (nicht Fliege, nicht Schleife)."""
    w = (P("M0 -1.6Q-4.4 -4.6 -8 -3.2Q-8.6 .6 -6.4 2.4Q-3 2.6 0 .6Z", "#B8A88E", .8)
         + P("M0 -1.6Q4.4 -4.6 8 -3.2Q8.6 .6 6.4 2.4Q3 2.6 0 .6Z", "#B8A88E", .8)
         + P("M0 .4Q-3.4 1.6 -5.4 4.6Q-2.6 5.6 0 2.6Z", "#9E8E74", .7) + P("M0 .4Q3.4 1.6 5.4 4.6Q2.6 5.6 0 2.6Z", "#9E8E74", .7)
         + L("M-6.2 -1.4q1.6 .6 2.6 2M6.2 -1.4q-1.6 .6 -2.6 2", .5, "#6F624E")
         + C(-4.6, -.8, .7, "#6F624E", 0) + C(4.6, -.8, .7, "#6F624E", 0)
         + E(0, .6, 1.1, 3.2, "#8A7A60", .7)
         + L("M-.4 -2.4Q-1.6 -4.8 -3.2 -5.6M.4 -2.4Q1.6 -4.8 3.2 -5.6", .6)
         + L("M-1.2 -3.8l-.8 .4M-2 -4.8l-.8 .2M1.2 -3.8l.8 .4M2 -4.8l.8 .2", .45))
    return G(w, f"translate({cx} {cy}) scale({s})")


def schatz_erde(v):
    """Vorbild: dieselbe Truhe wie «Schatz», aber stumpf und rostig: Beschläge rostbraun und zerfressen, Münzen angelaufen,
    eine Motte (kleiner Nachtfalter, graubraun) fliegt heraus, Löcher im Holz (Mt 6,19)."""
    if v not in (1, 2):
        return None
    rust, dull = "#A0522D", "#A99A64"
    lid = (P("M4.4 13.4L4.6 6.4Q4.8 2.2 15 2.2Q25.2 2.2 25.4 6.4L25.6 13.4Z", "#8C7258", 1.1)
           + P("M6.4 13L6.6 7Q7 4.4 15 4.4Q23 4.4 23.4 7L23.6 13Z", "#4E3A26", .7))
    coins = "".join(f'<ellipse cx="{x}" cy="{y}" rx="2.3" ry="1.3" fill="{dull}" stroke="{INK}" stroke-width=".6"/>'
                    for x, y in [(7.6, 13.4), (11.2, 12.6), (18.8, 12.6), (22.4, 13.4), (15, 10.8)])
    body = chest_body(3.4, 14, 26.6, 26, "#8C7258", rust) + P("M13.2 14h3.6v4.6q-1.8 1.4-3.6 0z", rust, .7)
    holes = E(10.2, 19.4, .9, .7, INK, 0) + E(20.4, 22, .8, .6, INK, 0) + E(11.4, 23.2, .6, .5, INK, 0) + E(19, 18, .6, .5, INK, 0)
    rust_marks = L("M5.4 14.2v3M24.6 14.2v2.4M9.8 2.8l.4 2M4 13.4h3", .9, rust)
    t = lid + coins + P("M3 12.6Q15 11 27 12.6V14.4H3Z", "#8E8676", 1) + body + holes + rust_marks
    m = motte(23.6, 4.4, .55) if v == 1 else motte(15, 3.6, .6)
    if v == 2:  # zusätzlich Dieb-Hand greift eine Münze? – nein: zweite Motte
        m += motte(25.4, 9, .4)
    return t + m + L("M19.6 7.6q-1.6 1-1.2 2.6", .5, "#8C8070", ' stroke-dasharray="1 .8"')


def weg(v):
    """Vorbild: Wegweiser-/Wanderweg-Piktogramm – geschwungener Weg mit Fussspuren führt zu einem Ziel (Stadttor) am Horizont."""
    if v not in (1, 2):
        return None
    s = P("M3 19.6Q7 15 13.4 13.4Q18.6 12 16 9.4Q14.6 8 17.6 6.8L19.6 6.8Q17.6 8.4 19.4 9.6Q22.6 12.4 17.4 14.8Q12.4 17 13 19.6Z", SAND, .8)
    gate = (P("M20.4 7V1.6H27.6V7Z", "#D6CCB6", .8) + P("M19.8 1.6h8.4V.4h-8.4z", "#B9AC92", .6)
            + P("M22.6 7V4.6Q24 3.2 25.4 4.6V7Z", "#5A4632", .5))
    s += gate if v == 1 else C(24, 3.6, 2.6, GOLD, .7) + L("M24 .2v-.8M27.4 3.6h.8M20.6 3.6h-.8", .6, GOLD2)
    s += L("M14.8 7.2H29.4", .7, "#8C7A60")

    def foot(x, y, sc, r):
        return G(F("M0 -1.6Q1 -1.6 1 -.1Q1 1.4 .2 1.7Q-.4 1.9 -.7 1.2L-1 -.2Q-1 -1.6 0 -1.6Z", "#5E4428")
                 + F("M-.7 -2.4a.5 .5 0 1 0 .01 0ZM.1 -2.7a.42 .42 0 1 0 .01 0ZM.8 -2.5a.36 .36 0 1 0 .01 0Z", "#5E4428"),
                 f"translate({x} {y}) rotate({r}) scale({sc})")
    s += foot(8.4, 17.6, 1.15, 55) + foot(10.4, 15.2, 1.05, 60) + foot(14.6, 14.2, .85, 70) + foot(16.4, 11.8, .7, -20) + foot(17.4, 9.4, .55, -40)
    return s


def tempel(v):
    """Vorbild: Modell des herodianischen Tempels (Israel-Museum): hoher weisser Kubus mit breiterer Fassade, flaches Dach
    mit Goldkante, hohes Portal mit Vorhang, Vorhofmauern, Plattform mit Stufen – kein Giebel, wenige grosse Formen."""
    if v not in (1, 2):
        return None
    sw = 3
    s = P("M8 126H192V142H8Z", STONE, sw)
    s += P("M66 142H134L130 148H70Z", STONE2, sw * .7)
    for x0, x1 in [(16, 60), (140, 184)]:  # Vorhofmauern mit Säulenhalle (wenige grosse Pfeiler)
        s += P(f"M{x0} 96H{x1}V126H{x0}Z", "#E6DCC6", sw * .8) + P(f"M{x0 - 3} 90H{x1 + 3}V98H{x0 - 3}Z", GOLD2, sw * .7)
        s += "".join(P(f"M{x} 126V108Q{x + 5} 102 {x + 10} 108V126Z", "#8C7A60", 1.6) for x in (x0 + 6, x0 + 26))
    if v == 1:
        s += P("M74 20H126V126H74Z", "#EDE6D6", sw * .8) + P("M70 14H130V22H70Z", GOLD, sw * .7)
    s += P("M50 40H150V126H50Z", "#F6F1E6", sw)
    s += P("M46 32H154V42H46Z", GOLD, sw * .8)
    s += P("M80 126V58H120V126Z", GOLD, sw * .8) + P("M87 126V65H113V126Z", "#7A2E3A", 1.8)
    s += L("M95 68V124M100 68V124M105 68V124", 1.4, "#A8495A")
    return s


def muenzen(v):
    """Vorbild 🪙 und Münzstapel (Kassen-Piktogramm): Stapel von der Seite, eine Münze von vorn mit Prägung."""
    def coin_stack(cx, ybot, n, rx=5.2, ry=1.6, h=1.6):
        out = ""
        for i in range(n):
            y = ybot - i * h
            out += P(f"M{cx - rx} {y - h}V{y}A{rx} {ry} 0 0 0 {cx + rx} {y}V{y - h}Z", GOLD2, .7)
            out += L(f"M{cx - rx + 1.2} {y + .5}v-1.2M{cx - rx + 2.6} {y + 1}v-1.2M{cx} {y + 1.3}v-1.2M{cx + rx - 2.6} {y + 1}v-1.2M{cx + rx - 1.2} {y + .5}v-1.2", .35, "#9A7420")
        y = ybot - n * h
        out += E(cx, y, rx, ry, GOLD, .7) + E(cx, y, rx * .6, ry * .55, "none", .4, ' stroke="#B8891A"').replace(f'stroke="{INK}" ', '')
        return out

    def face(cx, cy, r):
        return (C(cx, cy, r, GOLD, .8) + C(cx, cy, r * .78, "none", .45, "#B8891A")
                + P(f"M{cx - r * .3:.2f} {cy - r * .38:.2f}h{r * .6:.2f}l-{r * .1:.2f} {r * .38:.2f}q-{r * .2:.2f} {r * .18:.2f}-{r * .4:.2f} 0z"
                    f"M{cx - r * .05:.2f} {cy:.2f}v{r * .3:.2f}h-{r * .2:.2f}h{r * .5:.2f}", "#C99A22", .45))
    if v == 1:
        return coin_stack(8, 12.2, 5) + face(17.4, 8, 5.2)
    if v == 2:
        return coin_stack(6.4, 12.4, 3) + coin_stack(13.8, 12.6, 5) + face(19.8, 9.4, 3.8)
    return None


def schwein(v):
    """Vorbild 🐖: Seitenansicht, Schlappohr in der Silhouette, Beine in Körperfarbe, Ringelschwanz, Rüsselscheibe."""
    pink, pink2 = "#E6A4A0", "#C98480"

    def pig(t, col=pink, col2=pink2):
        parts = ["M6 9Q7 3.6 15 3.4Q24 3.2 27.4 6.4Q30.4 7.6 31 10.2Q31.4 13.4 28 14.6Q25 17.4 16 17.4Q7.4 17.4 6 13Z",
                 "M9 15h3.2v5h-3.2z", "M13 15.4h3v4.6h-3z", "M22 15.4h3.2v4.6H22z", "M25.6 14.4h3v5.4h-3z",
                 "M29.8 8.6h2.6q.8 1.6 0 3.6h-2.6z"]
        g = sil(parts, col, 1.8)
        g += P("M23 5.2Q26.6 4.4 27.6 6.6Q27.4 9.6 25 10.4Q23.4 8.2 23 5.2Z", col2, .8)  # Schlappohr nach vorn
        g += C(27.6, 9.2, .55, INK, 0) + E(31.3, 10.4, .3, .55, INK, 0)
        g += L("M6.4 9.4Q4 8.6 3.6 6.8Q3.4 5.4 4.8 5.8Q5.6 6.6 4.6 7.6", .8)
        g += L("M28.6 12.6q1.2.4 2-.4", .5)
        return G(g, t)
    if v == 1:
        return pig("")
    if v == 2:  # Herde: drei überlappende Schweine
        return (pig("translate(-1 -1.2) scale(.62)", "#D59490", "#B87470") + pig("translate(13 -.4) scale(.62)", "#D59490", "#B87470")
                + pig("translate(3.4 6.6) scale(.7)"))
    return None


def becher_form(fill_top=None, empty=False):
    """Kelch 12 × 14: Schale, Stiel, Fuss (Vorbild 🍷 / Abendmahlskelch)."""
    s = P("M6 9.2V11.6", "none", 1.4) + L("M6 9.2V11.6", .6, GOLD2)
    s += P("M2.4 13.4Q2.6 11.6 6 11.6Q9.4 11.6 9.6 13.4Z", GOLD2, .9)
    s += P("M1.2 2.8Q1.4 8.8 6 9.4Q10.6 8.8 10.8 2.8Z", GOLD, 1)
    s += L("M8.8 4Q8.6 7 6.8 8.2", .55, "#B8891A")
    if empty:
        s += E(6, 2.8, 4.8, 1.5, "#FFF6DC", .9)
    else:
        s += E(6, 2.8, 4.8, 1.5, fill_top or "#8E1F2A", .9) + L("M3.4 2.6q1.4-.6 3-.5", .45, "#D46A72")
    return s


def becher_voll(v):
    if v == 1:
        return becher_form()
    if v == 2:  # Wein bis zum Rand, ein Tropfen läuft über
        return becher_form() + P("M9.8 3.4q.9 1 .9 2 0 .8-.8.8-.7 0-.7-.8 0-1 .6-2z", "#8E1F2A", .5)
    return None


def becher_leer(v):
    """Vorbild: Kelch wie beim vollen Becher, geneigt, sodass man hineinsieht: innen nur blankes Gold und der Boden, kein
    Inhalt (keine helle oder dunkle Fläche, die als Flüssigkeit gelesen wird)."""
    if v not in (1, 2):
        return None
    cup = (P("M6 9.2V11.6", "none", 1.4) + L("M6 9.2V11.6", .6, GOLD2)
           + P("M2.4 13.4Q2.6 11.6 6 11.6Q9.4 11.6 9.6 13.4Z", GOLD2, .9)
           + P("M1.2 2.8Q1.4 8.8 6 9.4Q10.6 8.8 10.8 2.8Z", GOLD, 1)
           + E(6, 2.8, 4.8, 2.2, GOLD2, .9)  # Innenwand
           + F("M1.6 3.2Q6 6.6 10.4 3.2Q10 4.4 6 5Q2 4.4 1.6 3.2Z", "#B8891A")  # Schatten der Innenwand
           + E(6, 3.9, 1.6, .55, "#C99A22", .4)  # Boden der Schale
           + L("M2.4 2.1Q4 1.2 6 1.1", .45, "#FFF1B8"))
    if v == 1:  # geneigt, Öffnung zum Betrachter, auf dem Fuss stehend gekippt
        return G(cup, "translate(6.8 8) rotate(-22) scale(.9) translate(-6 -8)")
    return cup


def splitter(v):
    """Vorbild 👁 frontal; ein feiner dunkler Holzsplitter steckt im Augenweiss (ganz innerhalb der Kontur), keine Träne."""
    if v not in (1, 2):
        return None
    s = P("M2.4 9.4Q16 -1.6 29.6 9.4Q16 20.4 2.4 9.4Z", "#FFFFFF", 1.4)
    s += C(14, 9.4, 4.4, "#8A5A2E", .9) + C(14, 9.4, 2.1, INK, 0) + C(15.4, 8, 1, "#FFFFFF", 0)
    s += L("M2.4 9.4Q16 -1.6 29.6 9.4", 1.9)
    s += L("M5 1.4Q12 -1.4 19 .4", 1.6) if v == 2 else ""
    s += P("M19.8 7.8L26.6 11.4L25.4 12.8Z", "#5A3818", .7)  # Splitter, schmal
    if v == 1:
            return s


def salz(v):
    """Vorbild 🧂 bzw. Salzgefäss: Gefäss mit Löchern, aus dem weisse Körner rieseln; Häufchen grober Körner (keine Würfel)."""
    if v == 1:
        s = P("M6 4.6Q6 2 10 2Q14 2 14 4.6V6H6Z", "#C9CED2", .9)  # Deckel
        s += C(8.6, 3.6, .45, INK, 0) + C(10, 3.1, .45, INK, 0) + C(11.4, 3.6, .45, INK, 0)
        s += P("M5.6 6H14.4L15.6 14.4Q10 15.6 4.4 14.4Z", "#F4F1EA", 1)
        s += L("M7.6 8.6V12.4", .8, "#D9D2C4")
        s += "".join(f'<rect x="{x}" y="{y}" width=".9" height=".9" fill="#FFFFFF" stroke="{INK}" stroke-width=".3" transform="rotate(25 {x} {y})"/>'
                     for x, y in [(16.4, 2.4), (17.6, 4.4), (16.2, 6.2), (18.4, 7.4)])
        return G(s, "rotate(-14 10 9)")
    if v == 2:  # Häufchen grober weisser Körner in Tonschale, einzelne Körner glitzern
        heap = P("M3.6 9Q5 3.4 10 3Q15 3.4 16.4 9Z", "#FFFFFF", .9)
        heap += "".join(f'<path d="M{x} {y}l.8-.6.8.6-.8.6z" fill="#C9DCEB"/>' for x, y in [(7, 7), (9.6, 5.4), (12, 7.4), (10.4, 8), (8, 4.8), (13.4, 6)])
        b = P("M1.6 8.6H18.4Q17.8 14.6 10 14.8Q2.2 14.6 1.6 8.6Z", "#B5714A", 1) + L("M4.4 11.4Q10 13 15.6 11.4", .5, "#8A4F30")
        sp = L("M15.6 2.2l.8 1.4M17.2 3.2l-1.6.4M3.4 3.4l.6 1.2M4.6 4l-1.4.2", .5, "#7FA7C6")
        return heap + b + sp
    return None


def synagoge(v):
    """Vorbild: Synagoge von Kafarnaum (Steinbau, Giebelfront mit Bogenfenster; im Fries ein Davidstern) bzw. 🕍; das
    Erkennungszeichen gross: Torarolle (@1) oder Davidstern (@2) im Giebel."""
    if v not in (1, 2):
        return None
    s = P("M8 26H82V58H8Z", "#E4D9C2", 1.8) + P("M4 58H86V62H4Z", STONE2, 1.4)
    s += P("M4 27L45 3L86 27Z", "#D6CCB6", 1.8)
    s += P("M36 58V42Q45 34 54 42V58Z", "#5A4632", 1.4)
    s += P("M15 34h9v14h-9zM66 34h9v14h-9z", "#8C7A60", 1.2)
    if v == 1:
        t = (P("M-7 -5H7V5H-7Z", CREAM, 1) + L("M-4.6 -2h9.2M-4.6 .6h9.2", .8, "#7A6E60")
             + P("M-10.4 -7.6h3.4V7.6h-3.4Z", WOOD, 1) + P("M7 -7.6h3.4V7.6H7Z", WOOD, 1))
        s += G(t, "translate(45 17.4) scale(.82)")
    else:
        s += P("M45 9.6L50.4 19H39.6Z", "none", 1.6, ' stroke="#2E5478"').replace(f'stroke="{INK}" ', "")
        s += P("M45 22.2L39.6 12.8H50.4Z", "none", 1.6, ' stroke="#2E5478"').replace(f'stroke="{INK}" ', "")
    return s


def vogel(v):
    """Vorbild: fliegender Vogel als eine Silhouette (Piktogramm «Vogelschutz», Emoji 🐦 im Flug): Flügel hoch, Leib, Schwanz."""
    def bird(t, col="#8A6A4A"):
        parts = ["M3 10.4Q7 8.4 12 8.8Q16.6 8.8 19 7.4Q20.8 6.4 22 7.4L23.6 8L22 8.8Q20.2 11 15.6 11.8Q10.6 12.4 7 11.6L2 13.2Q2 11.6 3 10.4Z",
                 "M9.6 9.4Q8.2 4.6 4.6 1.8Q10 2.2 13.6 5.2Q15.2 6.8 15.4 9Z",
                 "M12.6 9.2Q14.4 4.4 18.4 2.2Q18.6 6.4 16.6 9.4Z"]
        g = sil(parts, col, 1.6) + C(20.6, 7.8, .5, INK, 0) + P("M23.6 8L22 7.4L22.1 8.7Z", GOLD2, .4)
        return G(g, t)
    if v == 1:
        return bird("")
    if v == 2:
        return bird("translate(13 0) scale(.46)") + bird("translate(1 1) scale(.5)") + bird("translate(4.6 5.4) scale(.66)")
    return None


def samen(v):
    """Vorbild: Sämann-Geste (haende.hand_gebend, wie 🫳) bzw. Saatkorn mit Keim."""
    if v == 1:
        hand = H.place(H.hand_gebend(), 2.6, 4.2, 10, .74)
        seeds = "".join(G(P("M0 -1.3Q.95 -.2 0 1.3Q-.95 -.2 0 -1.3Z", GOLD2, .45), f"translate({x} {y}) rotate({r})")
                        for x, y, r in [(16.4, 11, 20), (18.6, 12.6, -15), (14.8, 13.2, 30), (17.2, 15, 0), (19.8, 15.4, 25)])
        soil = P("M1 21.4Q2 17.4 12 17.2Q22 17.4 23 21.4Z", "#8B5E3C", .9) + L("M4 19.6q3-1 6-.4M13 19.4q3-.6 6 .2", .5, "#6A4428")
        return soil + hand + seeds
    if v == 2:  # drei grosse Saatkörner, eines keimt, über der Erde
        def korn(x, y, r):
            return G(P("M0 -3.4Q2.6 -2.6 2.4 .6Q2 3.4 0 3.6Q-2 3.4 -2.4 .6Q-2.6 -2.6 0 -3.4Z", "#D9A441", .8)
                     + L("M0 -2.6Q.6 0 0 2.8", .5, "#9A7420"), f"translate({x} {y}) rotate({r})")
        soil = P("M1 21.4Q2 16.4 12 16.2Q22 16.4 23 21.4Z", "#8B5E3C", .9)
        return (soil + korn(5.6, 13.4, -20) + korn(18.4, 13.2, 25)
                + L("M12 15V8.4", .9, LEAF) + P("M12 10Q9 7.4 8.2 9.6Q10 11.4 12 10Z", "#8DB25A", .6)
                + P("M12 8.6Q15 5.8 16 8Q14.2 10 12 8.6Z", "#8DB25A", .6) + korn(12, 16.2, 90).replace("rotate(90)", "rotate(90) scale(.9)"))
    return None


def fessel(v):
    """Vorbild: gefesselte Hände eines Gefangenen – Fäuste hängen nach unten, Handgelenke gekreuzt, Strick gewickelt,
    das Ende führt weg (abgeführt)."""
    if v not in (1, 2):
        return None

    def arm(t):
        return G(P("M-2.6 0H2.6V-9H-2.6Z", H.SKIN, 1) + P("M-3.4 -8H3.4V-19H-3.4Z", H.SLEEVE, 1), t)
    s = arm("translate(11 20) rotate(30)") + arm("translate(19 20) rotate(-30)")
    s += H.place(H.hand_faust(cuff_on=False), 19, 20, 60, .62) + H.place(H.hand_faust(cuff_on=False), 11, 20, -60, .62, True)
    rope, rope2 = "#C8A36A", "#8C6A38"
    for dy in (0, 2.6):
        s += P(f"M10.2 {11.4 + dy}Q15 {9.6 + dy} 19.8 {11.4 + dy}L19.8 {13.4 + dy}Q15 {11.6 + dy} 10.2 {13.4 + dy}Z", rope, .7)
        s += L(f"M12.6 {10.8 + dy}l.8 2M15 {10.5 + dy}v2M17.4 {10.8 + dy}l-.8 2", .45, rope2)
    d = "M19.6 13Q24 12 26 8Q27.4 5 29 4.4" if v == 1 else "M19.6 13Q25 14 27.4 18Q28.6 20 29 22"
    s += P(d, "none", 2.2) + L(d, 1.2, rope)
    return s


def matte(v):
    """Vorbild: Schlafmatte/Bettrolle in Aufsicht mit Kissen (Liegeplatz des Kranken), leicht perspektivisch, Rand gesäumt."""
    straw, straw2 = "#E3C27A", "#C9A35A"
    if v not in (1, 2):
        return None
    s = P("M2 4.4L27 2.6L30.6 9.6L3.4 11.2Z", straw, 1)
    s += L("M3.6 5.8L27.6 4M4.2 8.2L29.2 6.6", .5, straw2) + L("M8 4.1L9 10.9M13 3.7L14 10.6M18 3.4L19.2 10.3M23 3L24.4 10", .5, straw2)
    s += P("M3.4 5.2L9 4.8L9.6 10.4L4.2 10.8Z", "#F4F1EA", .8) + L("M4.6 7.6q2 .4 4 0", .5, "#C9BFAA") if v == 1 else ""
    if v == 2:  # mit Kissen und zurückgeschlagener Decke
        s += P("M3.4 5.2L9 4.8L9.6 10.4L4.2 10.8Z", "#F4F1EA", .8)
        s += P("M17 3.5L27 2.6L30.6 9.6L18.4 10.4Z", "#B5714A", .9) + L("M17.6 6.4L29 5.6", .6, "#8A4F30")
    return s


def sandale(v):
    """Vorbild 👡 von der Seite: Ledersohle mit Ferse und Zehenteil, Riemen über dem Rist und um die Ferse; ein Riemen gelöst
    (Joh 1,27: den Riemen lösen)."""
    sole_c, strap = "#B9783F", "#5E3518"
    if v == 1:  # Seitenansicht, Fersenriemen offen, hängendes Riemenende
        s = P("M2 15.6Q2 13.2 4.6 13.2H28Q32.6 13.4 32.6 15.4Q32.6 17.4 29 17.4H4.4Q2 17.4 2 15.6Z", sole_c, 1.1)
        s += L("M3.4 15.2H30.6", .5, "#E2B27A")
        s += P("M14 13.4Q17 4.4 22 6.6Q25 8.4 26.4 13.4H24.2Q22.8 9.6 21 9Q17.6 8.4 16.4 13.4Z", strap, .7)
        s += P("M18.4 12.8Q19.6 6.6 22.6 7.6", "none", 0) + P("M9.6 13.4Q9.4 7.6 14.6 7.4L15.4 9.4Q11.6 9.6 11.8 13.4Z", strap, .7)
        s += P("M4.6 13.2Q3.6 7.2 7.4 6L8.2 7.8Q5.6 8.8 6.6 13.2Z", strap, .7)  # Fersenriemen
        s += P("M7.8 6.8Q11 5.8 12.4 3.4Q13.6 2 14.4 3.2Q13.4 6.6 8.6 8.6Z", strap, .6)  # gelöstes Ende
        return s
    if v == 2:  # Paar in Aufsicht, ganz im Bild
        def one(t):
            g = P("M5 1C8.2 1 9.4 3.4 9.4 6C9.4 8.6 8 10 7.8 12.2C7.6 14.4 8.4 15.6 8.2 17.2A3.2 3.2 0 0 1 1.8 17.2C1.6 15.6 2.4 14.4 2.2 12.2C2 10 .6 8.6 .6 6C.6 3.4 1.8 1 5 1Z", sole_c, 1)
            g += P("M5 2.4C7.4 2.4 8 4.2 8 6C8 8 6.8 9.6 6.6 12C6.4 14 7 15.4 6.8 16.8A1.8 1.8 0 0 1 3.2 16.8C3 15.4 3.6 14 3.4 12C3.2 9.6 2 8 2 6C2 4.2 2.6 2.4 5 2.4Z", "#E2B27A", .4)
            g += P("M-.2 5.6Q5 7 10.2 5.6L10.2 8Q5 9.4 -.2 8Z", strap, .7) + P("M1 10.8Q5 12 9 10.8L8.8 13Q5 14.2 1.2 13Z", strap, .7)
            return G(g, t)
        return one("translate(6.6 .2) scale(.94)") + one("translate(18 .2) scale(.94)")
    return None


def leinenbinden(v):
    """Vorbild: Verbandsrolle (Piktogramm Erste Hilfe) + leeres Grab (Joh 20,5-7): aufgerollte Leinenbinden mit Spirale und
    lose liegendem Band, daneben gefaltetes Tuch, auf einer Steinbank; dahinter die dunkle Grabkammer."""
    if v not in (1, 2):
        return None
    linen, sh = "#FBF8EF", "#B9C3C8"
    s = P("M2 30V12Q2 3 18 3H42Q58 3 58 12V30Z", "#8C8070", 1.3) + P("M8 30V15Q8 8 18 8H42Q52 8 52 15V30Z", "#3E3428", 1)
    s += P("M2 22L5 19H55L58 22Z", "#D6CCB6", 1.1) + P("M2 22H58V31H2Z", STONE, 1.2)

    def roll(x, y, r, ln):
        return (P(f"M{x} {y - r}H{x + ln}A{r * .55:g} {r} 0 0 1 {x + ln} {y + r}H{x}Z", linen, .9)
                + E(x, y, r * .55, r, linen, .9) + L(f"M{x} {y - r * .45:g}A{r * .25:g} {r * .45:g} 0 1 0 {x + .01} {y - r * .45:g}", .5, sh))
    if v == 1:
        s += L("M14 20.4Q20 22.4 26 19.8Q30 18.4 36 20.2", 3, INK) + L("M14 20.4Q20 22.4 26 19.8Q30 18.4 36 20.2", 1.6, linen)
        s += roll(8, 16.4, 3.6, 6) + roll(20, 15.6, 3, 5)
        s += P("M40 20.4L42 15.2H52L50 20.4Z", linen, .9) + L("M41.2 18H51M47 15.4L45 20.4", .5, sh)
    else:
        s += roll(7, 16.2, 3.6, 7) + roll(20, 16.2, 3.6, 7) + roll(33, 16.2, 3.6, 7)
        s += P("M44 20.4L45.6 15.6H54L52.4 20.4Z", linen, .9) + L("M45 18H53.2", .5, sh)
    return s


def perle(v):
    """Vorbild: Perlenkette (Schmuck-Piktogramm) – geschlossener Ring grosser, schimmernder Perlen, eine Perle grösser."""
    pearl, ps = "#FBF7F2", "#D2C2D6"

    def pe(x, y, r):
        return (C(x, y, r, "#F1E9E2", .55, "#5E5060") + F(f"M{x - r * .15:.2f} {y + r * .98:.2f}A{r} {r} 0 0 0 {x + r * .98:.2f} {y + r * .15:.2f}A{r * 1.25:.2f} {r * 1.25:.2f} 0 0 1 {x - r * .15:.2f} {y + r * .98:.2f}Z", ps)
                + C(x - r * .35, y - r * .35, r * .3, "#FFFFFF", 0))
    if v not in (1, 2):
        return None
    n = 12 if v == 1 else 10
    rx, ry, cx, cy = (11, 6.2, 15, 8.6)
    s = E(cx, cy, rx, ry, "none", .8, ' stroke-dasharray="0"')
    pts = [(cx + rx * math.cos(2 * math.pi * i / n + math.pi / 2), cy + ry * math.sin(2 * math.pi * i / n + math.pi / 2)) for i in range(n)]
    pts.sort(key=lambda p: p[1])
    for i, (x, y) in enumerate(pts):
        s += pe(round(x, 1), round(y, 1), 2.3 if v == 1 else 2.6)
    if v == 2:
        s += pe(15, 8.6, 3)
    return s


def schlange(v):
    """Vorbild 🐍: vollständige S-Kurve, Schwanz spitz, Kopf erhoben, gespaltene Zunge, Rautenmuster; nichts abgeschnitten."""
    if v not in (1, 2):
        return None
    green, belly = "#7A9A3A", "#C9D48A"
    if v == 1:
        pts = curve([((1.6, 12.4), (3.6, 15.6), (8, 15.4), (10.4, 12.6)), ((10.4, 12.6), (12.8, 9.6), (15.4, 9.4), (17.4, 11.8)),
                     ((17.4, 11.8), (19.6, 14.6), (23.6, 14.2), (23.4, 9.4)), ((23.4, 9.4), (23.2, 7), (22.6, 6), (22.8, 5.2))], 16)
    else:
        pts = curve([((2, 13.6), (5, 15.4), (9.4, 14.6), (11.4, 11.4)), ((11.4, 11.4), (13.2, 8.4), (16.8, 8.2), (18.8, 11.4)),
                     ((18.8, 11.4), (20.4, 14), (24.8, 13.4), (24.2, 8.6)), ((24.2, 8.6), (24, 6.4), (23.2, 5.6), (23.6, 4.8))], 16)
    body = tube(pts, lambda t: .2 + 3.0 * min(1, t * 1.6) if t < .9 else 3.2, cap_end=False)
    s = P(body, green, .9)
    # Rautenmuster entlang der Mitte
    for i in range(10, len(pts) - 8, 5):
        x, y = pts[i]
        a, b = pts[i - 1], pts[i + 1]
        ang = math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))
        s += G(F("M-1 0L0 -.7L1 0L0 .7Z", "#4E6A22"), f"translate({f1(x)} {f1(y)}) rotate({ang:.0f})")
    hx, hy = pts[-1]
    s += G(P("M-2.4 1.4Q-2.8 -1.6 0 -2.2Q3.6 -2.4 4.6 -.4Q4.8 1.2 2.4 1.8Q-.6 2.6 -2.4 1.4Z", green, .9)
           + C(1.6, -.8, .55, INK, 0) + L("M4.6 .2L6.6 .4M6.6 .4l.8-.7M6.6 .4l.8.6", .5, RED), f"translate({hx + .6:.1f} {hy - .2:.1f})")
    return s


def wurm(v):
    """Vorbild: Regenwurm-Piktogramm – schlanker rosa Leib mit Ringen, rundes Ende, ohne Auge, ragt aus einem Erdloch."""
    if v not in (1, 2):
        return None
    d = "M7.4 10.6Q6.4 5 10 3.2Q13.4 1.8 15 4.6Q16.4 7 19.6 6" if v == 1 else "M7.4 10.6Q6.8 6 9.6 4.4Q12.4 3 14 5.4Q15.6 7.6 18.4 6.4Q20.4 5.4 20.8 3.6"
    s = P("M.8 11.6Q2 8.8 12 8.6Q22 8.8 23.2 11.6Z", "#8B5E3C", .9) + E(7.4, 9.9, 2.8, .9, "#4E3420", .6)
    s += worm_line(d, 1.9, "#D98A86", .7)
    rings = [(7.2, 7.4, 0), (8, 5.4, 30), (9.6, 3.9, 70), (12, 3, 95), (14.2, 3.8, 140), (15.6, 5.8, 150), (17.6, 6.2, 85)] if v == 1 else \
        [(7.1, 7.6, 5), (8.2, 5.4, 45), (10.4, 4.1, 80), (12.6, 4.2, 120), (14.2, 5.8, 140), (16.4, 7, 95), (18.8, 6.1, 60)]
    for x, y, r in rings:
        s += G(L("M-1 0H1", .45, "#A85E5A"), f"translate({x} {y}) rotate({r})")
    s += G(F("M-1.2 -.8H1.4V.8H-1.2Z", "#C46E6A"), "translate(11 3.1) rotate(5)") if v == 1 else ""
    s += P("M4.2 10.4Q7.4 11.4 10.6 10.4Q10.2 11.6 7.4 11.8Q4.6 11.6 4.2 10.4Z", "#8B5E3C", .6)
    return s


def grab_zu(v):
    """Vorbild: Felsengrab im Hang (wie FIG-ORT-GRAB), Rollstein ganz vor der Öffnung; Siegel: Schnur vom Fels über den Stein
    mit rotem Siegelklumpen an der Fuge (Mt 27,66)."""
    if v not in (1, 2):
        return None
    s = P("M1 40Q3 18 14 10Q26 2 40 4Q54 6 60 18Q63 28 63 40Z", "#A79A80", 1.6)
    s += P("M14 10Q26 2 40 4Q54 6 60 18Q56 12 46 9Q32 6 20 10Z", "#8FA672", 1)  # Grasnarbe
    s += L("M48 16q5 3 7 9M8 26q1-5 4-8", .8, "#8C8070")
    s += P("M15 40V28Q15 18 27 18Q39 18 39 28V40Z", "#3B3226", 1)
    s += C(28, 27.4, 12.6, "#C9BFAA", 1.6) + L("M20 21q7-4 14 1M19 31q3 4 8 5", .8, "#8C8070")
    if v == 1:
        s += L("M8 22Q20 24 40 26Q46 26.6 48 22", 1.2, RED) + C(40.6, 26, 2.6, RED, .7, DRED) + C(8, 22, 1.8, RED, .6, DRED)
    else:
        s += L("M10 27.4H46", 1.2, RED) + C(10, 27.4, 2, RED, .6, DRED) + C(40.6, 27.4, 2.6, RED, .7, DRED) + C(46, 27.4, 2, RED, .6, DRED)
    s += L("M1 40.6H63", 1.4, "#8C7A60")
    return s


def frame_land(inner, sky=SKY, sw=2.2):
    """Landschaft als gerahmtes Bild (Vorbild 🏞️): Himmel, Inhalt, Rahmen mit Kontur; nichts abgeschnitten.
    Inhalt hält sich an die Rahmenkanten x 3–183, y 3–67 (unten mit BOT abschliessen)."""
    return (f'<rect x="3" y="3" width="180" height="64" rx="8" fill="{sky}"/>' + inner
            + f'<rect x="3" y="3" width="180" height="64" rx="8" fill="none" stroke="{INK}" stroke-width="{sw}"/>')


def see(v):
    """Vorbild: 🏞️ und Kinderbibel-Bild vom See Gennesaret – ovales Wasser ringsum von Ufer und Hügeln, Fischerboot.
    Unterschied: Meer = nur Wellen ohne Ufer; Jordan = schmaler, gewundener Fluss."""
    if v not in (1, 2):
        return None
    s = ground("M3 26Q20 12 40 18Q60 8 82 16Q104 6 126 15Q150 6 168 16Q178 20 183 24", GREEN2)
    s += ground("M3 34Q50 26 93 28Q136 26 183 34", GREEN)
    s += P("M14 46Q16 32 93 31Q170 32 172 46Q170 61 93 62Q16 61 14 46Z", WATER, 2)
    s += L("M34 40q6-4 12 0t12 0M124 42q6-4 12 0t12 0M50 54q6-4 12 0t12 0M120 55q5-3 10 0", 1.6, FOAM)
    boat = (P("M78 46H110L104 52H84Z", WOOD, 1.6) + L("M94 46V24", 1.8) + P("M95.4 25L109 42H95.4Z", CREAM, 1.4)
            + P("M92.6 27L83 42H92.6Z", PAPER, 1.2))
    s += boat if v == 1 else G(boat, "translate(-26 0)") + P("M118 48H140L136 52H122Z", WOOD, 1.4) + C(129, 44, 2.4, SKIN, 1) + L("M129 46.4v1.6", 1.2)
    s += L("M8 62q-1-7 1-12M12 62q1-6 3-10M174 62q1-7-1-12M178 62q0-6 3-10", 1.6, GREEN3)
    return frame_land(s)


def meer_offen(v):
    """Vorbild 🌊 (Hokusai-Welle): grosse stilisierte Wellen mit Gischtkrone und Kontur, kein Ufer."""
    if v == 1:
        s = ""
        for x0, y0, sc, col in [(0, 14, 1.0, WATER2), (64, 8, 1.15, WATER), (130, 16, 1.0, WATER2)]:
            w = "M0 48Q2 24 22 14Q40 6 52 16Q58 22 52 28Q46 30 44 24Q42 18 36 20Q28 24 30 34Q34 46 50 48Q58 49 66 48V54H0Z"
            s += G(P(w, col, 2.2 / sc) + L("M44 24Q42 18 36 20", 1.6 / sc, FOAM) + L("M10 40Q14 28 24 22", 1.8 / sc, FOAM),
                   f"translate({x0} {y0}) scale({sc})")
        s += P("M2 58Q24 50 46 58Q70 66 93 58Q116 50 140 58Q162 66 184 58V64Q93 72 2 64Z", WDARK, 2)
        return s
    if v == 2:  # gerahmt: Wellenreihen mit Gischt bis zum Horizont
        s = ground("M3 22Q20 18 40 22T80 22T120 22T160 22T183 22", "#7FB3DD", 1.4)
        s += ground("M3 40Q14 24 30 30Q42 36 52 26Q64 14 78 28Q90 38 102 26Q116 12 130 28Q142 38 154 26Q168 14 183 30", WATER, 2)
        for x in (52, 102, 154):
            s += P(f"M{x - 6} 27Q{x} 16 {x + 10} 20Q{x + 5} 22 {x + 5} 26Q{x} 23 {x - 6} 27Z", FOAM, 1.4)
        s += ground("M3 52Q20 42 38 50Q56 58 74 48Q92 38 110 50Q128 60 146 50Q164 40 183 50", WATER2, 2)
        s += ground("M3 62Q24 56 44 62Q64 66 84 60Q104 54 124 60Q144 66 164 60Q176 56 183 60", WDARK, 1.8)
        return frame_land(s, "#DDE9EE")
    return None


def jordan(v):
    """Vorbild: Flusspiktogramm in Perspektive (🏞️) – breiter gewundener Fluss vom Vordergrund zum Horizont, Schilf;
    @2 mit Taube darüber (Taufe Jesu am Jordan)."""
    if v not in (1, 2):
        return None
    s = ground("M3 26Q24 14 46 20Q70 10 96 18Q124 8 150 18Q170 14 183 22", "#C9BC90")
    s += ground("M3 30Q50 22 93 25Q136 22 183 30", GREEN)
    s += P("M48 67Q62 52 98 47Q126 42 108 35Q92 30 102 25L112 24Q126 27 118 31Q136 38 146 43Q154 56 118 60Q100 63 114 67Z", WATER, 2)
    s += L("M70 61q8-4 16 0M106 51q6-3 12 0M112 32q3-2 6 0", 1.4, FOAM)
    for x, y in [(30, 56), (38, 62), (154, 52), (162, 58)]:
        s += L(f"M{x} {y}q-1-8 1-14M{x + 4} {y}q1-9-1-14M{x + 8} {y}q0-7 2-11", 1.6, GREEN3)
        s += E(x + 1, y - 14, 1.3, 3, "#8A6A3A", 0) + E(x + 3, y - 14, 1.3, 3, "#8A6A3A", 0)
    if v == 2:
        dove = (P("M-8 0Q-2 -2 4 -1Q7 -1 9 1Q7 3 2 3Q-4 3 -8 0Z", "#FFFFFF", 1.2)
                + P("M-2 -1Q-6 -8 -12 -9Q-6 -3 -3 1Z", "#FFFFFF", 1.2) + P("M2 -1Q4 -9 10 -11Q8 -4 4 0Z", "#FFFFFF", 1.2))
        s += G(dove, "translate(56 16)")
    return frame_land(s)


def feld(v):
    """Vorbild: 🏞️ mit Ackerreihen – weites helles reifes Feld («weiss zur Ernte») mit Reihen in Perspektive bis zum
    Horizont, Baum am Rand. Unterschied zu Kornfeld: Landschaft aus der Ferne, keine grossen Ähren vorn."""
    if v not in (1, 2):
        return None
    s = ground("M3 22Q30 14 60 18Q100 10 140 17Q166 14 183 20", GREEN2)
    ripe = "#F3E4A8" if v == 1 else "#F3E4A8"
    s += ground("M3 27Q93 21 183 27", ripe)
    for xb in (-120, -60, -10, 34, 72, 93, 114, 152, 196, 246, 306):
        sx = 93 + (xb - 93) * .15
        ex, ey = xb, 67.0
        if xb < 3 or xb > 183:
            edge = 3 if xb < 3 else 183
            t = (edge - sx) / (xb - sx)
            ex, ey = edge, 25 + t * 42
        s += L(f"M{sx:.1f} 25L{ex:.1f} {ey:.1f}", 1.3, "#C9A35A")
    if v == 2:  # vorn ein gepflügter Streifen, darauf die Saat
        s += ground("M3 56Q93 50 183 56", "#A8794A")
        s += L("M30 60l-4 7M70 58l-2 9M116 58l2 9M156 60l4 7", 1.2, "#7A5230")
    s += L("M160 22v4", 1.6) + E(160, 17, 6, 5, LEAF, 1.2)
    return frame_land(s)


def ahre(x, y, h, lean=0, col=GOLD2, k=1.0):
    """Grosse Ähre: Halm, Körner paarweise (k = Korngrösse), Grannen."""
    g = L(f"M0 0Q{lean * .3:.1f} {-h * .5:.1f} {lean:.1f} {-h:.1f}", 1.8, "#9A7A30")
    for i in range(4):
        t = .5 + i * .14
        cx, cy = lean * t * t, -h * t
        g += G(P("M0 0Q-3.4 -1 -2.8 -5Q-.4 -3.6 0 0Z", col, 1 / k) + P("M0 0Q3.4 -1 2.8 -5Q.4 -3.6 0 0Z", col, 1 / k), f"translate({cx:.1f} {cy:.1f}) scale({k})")
    g += G(P("M0 0Q-1.5 -3.2 0 -6.4Q1.5 -3.2 0 0Z", col, 1 / k), f"translate({lean:.1f} {-h:.1f}) scale({k})")
    g += L(f"M{lean - 2.4 * k:.1f} {-h * .9:.1f}l-4 -6M{lean + 2.4 * k:.1f} {-h * .9:.1f}l4 -6M{lean:.1f} {-h - 6.4 * k:.1f}v-5", .9, "#9A7A30")
    return G(g, f"translate({x} {y})")


def kornfeld(v):
    """Vorbild 🌾 (Ährenbündel) gross vor goldenem Feld bis zur Horizontlinie, gerahmt wie 🏞️."""
    if v not in (1, 2):
        return None
    s = ground("M3 24Q30 16 60 20Q100 12 140 19Q166 16 183 22", GREEN2)
    s += ground("M3 28Q93 22 183 28", "#F3E3A6")
    s += ground("M3 58Q93 52 183 58", "#E8CF80", 1.2)
    xs = [(56, -6), (74, -3), (93, 0), (112, 3), (130, 6)] if v == 1 else [(70, -6), (93, 0), (116, 6)]
    for i, (x, lean) in enumerate(xs):
        s += ahre(x, 66, 31 + (4 if i == len(xs) // 2 else 0), lean, "#E8B931" if i % 2 else "#D99A2B", 2.2 if v == 1 else 2.8)
    return frame_land(s)


def wueste(v):
    """Vorbild: Wüstenpiktogramm (🏜️) – Tafelberg/Felsen, Dünen mit Kontur, grosse Sonne, dürrer Dornbusch; kein Wasser."""
    if v not in (1, 2):
        return None
    s = C(150, 20, 10, GOLD, 1.8) + L("M150 5v3M150 32v3M135 20h3M162 20h3M139 9l2 2M159 29l2 2M161 9l-2 2M141 29l-2 2", 1.8, GOLD2)
    s += P("M22 36L32 16H60L70 36Z", ROCK, 1.8) + L("M40 20l-3 9M54 20l2 10", 1.2, ROCK2)
    s += ground("M3 40Q30 32 60 36Q90 30 120 36Q150 30 183 38", SAND)
    s += ground("M3 52Q40 40 80 48Q120 58 150 46Q170 40 183 48", SAND2)
    bush = L("M118 48v-12M118 42l-7-7M118 40l7-8M111 35l-2-3M125 32l2-3M118 38l1-7", 1.8, "#7A5A36")
    s += bush if v == 1 else bush + P("M54 56q3-6 8-6 6 0 8 6z", ROCK2, 1.4) + P("M150 60q2-4 6-4 4 0 6 4z", ROCK, 1.2)
    return frame_land(s, "#F3ECDA")


def land(v):
    """Vorbild: Kundschafter-Traube (4 Mo 13,23) – ein Weinstock wächst vorn aus dem Boden und trägt eine grosse Traube;
    dahinter sanfte grüne Hügel mit Ölbäumen und Feld («gutes Land»)."""
    if v not in (1, 2):
        return None
    s = ground("M3 24Q24 12 50 18Q76 8 102 16Q130 6 156 16Q172 12 183 18", GREEN2)
    s += ground("M3 34Q50 24 93 30Q136 24 183 32", GREEN)
    s += P("M100 46Q130 38 160 42Q176 44 183 42V52Q140 50 100 54Z", "#E3C26A", 1.4)
    for x, y, r in [(112, 34, 6), (136, 30, 7), (164, 32, 6)]:
        s += L(f"M{x} {y + r * .6}v{r * .9:.1f}", 2, "#7A5A36") + E(x, y, r, r * .66, "#7F9A5E", 1.4)
    # Weinstock mit Pfahl
    s += L("M44 67V14", 2.6, "#7A5A36") + L("M44 66Q40 50 46 40Q52 30 46 20", 4.4, INK) + L("M44 66Q40 50 46 40Q52 30 46 20", 2.6, "#8A6236")
    s += P("M46 22Q34 10 26 18Q34 28 46 24Z", LEAF, 1.4) + P("M46 20Q58 8 66 16Q58 26 46 22Z", LEAF, 1.4)
    grape = "#6B3A6E"
    t = ""
    for x, y in [(52, 26), (61, 26), (70, 26), (56.5, 33.5), (65.5, 33.5), (52, 41), (61, 41), (70, 41), (56.5, 48.5), (65.5, 48.5), (61, 56)]:
        t += C(x, y, 4.8, grape, 1.2) + C(x - 1.4, y - 1.6, 1.2, "#A77AAA", 0)
    s += L("M48 22Q56 20 61 22", 1.8, "#6A4428") + (t if v == 1 else G(t, "translate(-2 0)"))
    return frame_land(s)


def ground(top, fill, sw=1.6):
    """Bodenfläche: obere Kante «top» (von x 3 bis x 183, beginnt mit M3 …), unten im Rahmen geschlossen."""
    return P(top + "L183 59Q183 67 175 67H11Q3 67 3 59Z", fill, sw)


def worm_line(d, w, fill, ow=.8):
    """Runder Körper als dicker Strich mit runden Enden: Tinte darunter, Farbe darüber (Kontur nur aussen)."""
    return (f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{w + 2 * ow:g}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{fill}" stroke-width="{w:g}" stroke-linecap="round" stroke-linejoin="round"/>')


SPEC = {  # Lexikon-ID: (Funktion, viewBox, Bedeutung kurz, gezeichnet je Fassung)
    "FIG-OBJ-BRIEF": (brief, "0 0 24 18", "Brief (an eine Gemeinde oder Person)", {1: "geschlossener Briefumschlag mit rotem Wachssiegel", 2: "beschriebenes Blatt mit Band und rotem Siegel"}),
    "FIG-ZEICHEN-SCHATZ": (schatz, "0 0 30 28", "Schatz / Lohn bei Gott", {1: "offene Schatztruhe auf einer Wolke", 2: "offene Schatztruhe mit Lichtschein und Strahlen"}),
    "FIG-ZEICHEN-SCHATZ-ERDE": (schatz_erde, "0 0 30 28", "Schatz auf der Erde (vergänglich: Motte und Rost zerstören ihn)", {1: "rostige, löchrige Truhe mit angelaufenen Münzen, Motte fliegt heraus", 2: "rostige, löchrige Truhe mit zwei Motten"}),
    "FIG-ZEICHEN-WEG": (weg, "0 0 30 20", "Weg / hingehen zu einem Ziel", {1: "geschwungener Weg mit Fussspuren zu einem Stadttor am Horizont", 2: "geschwungener Weg mit Fussspuren zur Sonne am Horizont"}),
    "FIG-ORT-TEMPEL": (tempel, "0 0 200 150", "Tempel in Jerusalem", {1: "herodianischer Tempel: hoher weisser Bau mit Goldkante, Portal mit Vorhang, Vorhofmauern, Plattform", 2: "herodianischer Tempel ohne Aufbau: weisser Bau, Goldkante, Portal, Vorhofmauern"}),
    "FIG-OBJ-MUENZEN": (muenzen, "0 0 24 14", "Münzen, Geld", {1: "Münzstapel und eine Münze mit Prägung", 2: "zwei Münzstapel und eine Münze mit Prägung"}),
    "FIG-OBJ-SCHWEIN": (schwein, "0 0 34 22", "Schwein (Herde)", {1: "Schwein von der Seite", 2: "drei Schweine einer Herde"}),
    "FIG-OBJ-BECHER-VOLL": (becher_voll, "0 0 12 14", "voller Becher (Wein)", {1: "goldener Kelch mit Rotwein", 2: "goldener Kelch randvoll mit Rotwein, Tropfen läuft über"}),
    "FIG-OBJ-BECHER-LEER": (becher_leer, "0 0 14 14", "leerer Becher", {1: "goldener Kelch, geneigt: innen blankes Gold, kein Inhalt", 2: "goldener Kelch von schräg oben: innen blankes Gold, kein Inhalt"}),
    "FIG-ORT-SEE": (see, "0 0 186 70", "See (See von Galiläa)", {1: "ovaler See von Hügeln umgeben, Fischerboot mit Segel", 2: "ovaler See, Fischerboot und Fischer mit Netz"}),
    "FIG-ORT-FELD": (feld, "0 0 186 70", "Feld (Acker, Felder reif zur Ernte)", {1: "weites helles reifes Feld mit Reihen bis zum Horizont", 2: "reifes Feld, vorn gepflügter Streifen"}),
    "FIG-OBJ-SPLITTER": (splitter, "0 0 32 18", "Splitter (im Auge des Bruders)", {1: "Auge, feiner dunkler Holzsplitter im Augenweiss, gerötet", 2: "Auge mit Braue, feiner dunkler Holzsplitter im Augenweiss"}),
    "FIG-OBJ-SALZ": (salz, "0 0 20 16", "Salz", {1: "Salzstreuer, aus dem Körner rieseln", 2: "Häufchen weisser Salzkörner in Tonschale"}),
    "FIG-ORT-SYNAGOGE": (synagoge, "0 0 90 64", "Synagoge (Versammlungshaus)", {1: "Steinbau mit Giebel, grosse Torarolle im Giebel", 2: "Steinbau mit Giebel, Davidstern im Giebel"}),
    "FIG-ORT-JORDAN": (jordan, "0 0 186 70", "Jordan (Fluss)", {1: "breiter gewundener Fluss zum Horizont, Schilf", 2: "gewundener Fluss mit Schilf, weisse Taube darüber"}),
    "FIG-OBJ-VOGEL": (vogel, "0 0 24 16", "Vogel (Vögel des Himmels)", {1: "fliegender Vogel", 2: "drei fliegende Vögel"}),
    "FIG-OBJ-SAMEN": (samen, "0 0 24 22", "Samen / Saat (säen)", {1: "Hand von oben streut Körner auf Erde", 2: "drei grosse Saatkörner, eines keimt"}),
    "FIG-OBJ-FESSEL": (fessel, "0 0 30 30", "Fessel (Strick, gebunden)", {1: "gekreuzte Handgelenke, Fäuste hängen nach unten, Strick gewickelt, Ende führt weg", 2: "gekreuzte Handgelenke, Fäuste nach unten, Strick mit hängendem Ende"}),
    "FIG-OBJ-MATTE": (matte, "0 0 32 12", "Liegematte (eines Kranken)", {1: "ausgebreitete Strohmatte mit Kissen", 2: "ausgebreitete Strohmatte mit Kissen und Decke"}),
    "FIG-OBJ-SANDALE": (sandale, "0 0 34 20", "Sandale (Riemen lösen)", {1: "Sandale von der Seite, Fersenriemen gelöst", 2: "Paar Sandalen von oben"}),
    "FIG-ORT-LAND": (land, "0 0 186 70", "Land (verheissenes Land)", {1: "Weinstock mit grosser Traube vor grünen Hügeln mit Ölbäumen und Feld", 2: "Weinstock mit grosser Traube vor grünen Hügeln"}),
    "FIG-ORT-MEER-OFFEN": (meer_offen, "0 0 186 70", "offenes Meer mit Wellen (Sturm)", {1: "drei grosse brechende Wellen", 2: "Wellenreihen mit Gischt"}),
    "FIG-ORT-WUESTE": (wueste, "0 0 186 70", "Wüste", {1: "Felsen, Sanddünen, Sonne, dürrer Busch", 2: "Felsen, Dünen, Sonne, Busch, Steine"}),
    "FIG-ORT-GRAB-VERSCHLOSSEN": (grab_zu, "0 0 64 44", "Grab (verschlossen, versiegelt)", {1: "Felsengrab im Hang, Rollstein vor der Öffnung, Siegelschnur mit rotem Siegel", 2: "Felsengrab, Rollstein, waagrechte Siegelschnur mit Siegeln"}),
    "FIG-OBJ-LEINENBINDEN": (leinenbinden, "0 0 60 34", "Leinenbinden und Schweisstuch im leeren Grab", {1: "aufgerollte Leinenbinden, loses Band und gefaltetes Tuch auf Steinbank vor dunkler Grabkammer", 2: "drei aufgerollte Leinenbinden und gefaltetes Tuch auf Steinbank vor Grabkammer"}),
    "FIG-OBJ-PERLE": (perle, "0 0 30 18", "Perlen (kostbar)", {1: "Perlenkette als geschlossener Ring", 2: "Perlenkette als Ring mit grosser Perle in der Mitte"}),
    "FIG-OBJ-SCHLANGE": (schlange, "0 0 30 16", "Schlange", {1: "Schlange in S-Kurve mit Zunge", 2: "Schlange in S-Kurve mit Zunge"}),
    "FIG-OBJ-WURM": (wurm, "0 0 24 12", "Wurm", {1: "schlanker Regenwurm ragt aus Erdloch", 2: "schlanker Regenwurm ragt aus Erdloch"}),
    "FIG-ORT-KORNFELD": (kornfeld, "0 0 186 70", "Kornfeld (reifes Getreide)", {1: "fünf grosse goldene Ähren vor goldenem Feld", 2: "drei grosse Ähren vor goldenem Feld"}),
}


def variants(fid):
    fn, vb, bed, gez = SPEC[fid]
    out = {}
    for n in (1, 2, 3):
        svg = fn(n)
        if svg:
            out[n] = {"vb": vb, "svg": svg, "bedeutung": bed, "gezeichnet": gez.get(n, "")}
    return out


def main():
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    if a[0] == "entwuerfe":
        ids = a[2:] or list(SPEC)
        res = {}
        for fid in ids:
            want = None
            if "@" in fid:
                fid, want = fid.split("@")
            for n, e in variants(fid).items():
                if want is None or str(n) == want:
                    res[f"{fid}@{n}"] = e
        pathlib.Path(a[1]).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"PASS: {len(res)} Entwürfe → {a[1]}")
    elif a[0] == "schreiben":
        cur = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
        for k in a[1:]:
            fid, n = k.split("@")
            e = variants(fid)[int(n)]
            cur[fid] = {"vb": e["vb"], "svg": e["svg"]}
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(cur, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"PASS: {len(cur)} Zeichen in {OUT}")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
