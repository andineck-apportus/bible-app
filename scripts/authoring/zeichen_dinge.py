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
    """Vorbild: offene Schatztruhe (Spielsymbol) im Wolkenbett mit Lichtstrahlen von oben – Schatz «im Himmel»."""
    if v not in (1, 2):
        return None
    lid = (P("M4.4 13.4L4.6 6.4Q4.8 2.2 15 2.2Q25.2 2.2 25.4 6.4L25.6 13.4Z", WOOD, 1.1)
           + P("M6.4 13L6.6 7Q7 4.4 15 4.4Q23 4.4 23.4 7L23.6 13Z", "#5A3A1C", .7))
    coins = "".join(f'<ellipse cx="{x}" cy="{y}" rx="2.6" ry="1.5" fill="{GOLD}" stroke="{INK}" stroke-width=".6"/>'
                    for x, y in [(9, 12.4), (15, 11.4), (21, 12.4), (12, 10), (18, 10)])
    body = chest_body(3.4, 14, 26.6, 25) + P("M13.2 14h3.6v4.6q-1.8 1.4-3.6 0z", GOLD, .7)
    chest = lid + coins + P("M3 12.6Q15 11 27 12.6V14.4H3Z", GOLD, 1) + body
    rays = L("M15 -1.4V-3.4M7.6 .2L6.2-1.4M22.4 .2L23.8-1.4", 1.2, GOLD2)
    if v == 1:
        cloud = P("M.8 27Q-.4 23.6 3 23Q3.4 20.6 6.4 21.2Q8 19.4 10.6 20.8Q13.4 19.2 15.6 21Q18.4 19.4 20.8 21.2Q23.6 19.8 25 21.8Q28.4 21.4 28.8 24Q30.8 25.4 29.2 27.4Z", "#FFFFFF", 1)
        return G(rays + chest, "translate(3.4 1.6) scale(.78)") + cloud
    return G(E(15, 13, 13, 9, "#FFF3C4", 0) + rays + chest, "translate(.6 3.2) scale(.96)")


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
    """Vorbild: geschlossene Truhe (wie «Schatz»), aber zerfressen: Löcher im Holz, rostbraune, abgeplatzte Beschläge,
    ein graubrauner Nachtfalter fliegt mit Flugspur davon (Mt 6,19); @2 dazu aufgebrochenes Schloss (Diebe)."""
    if v not in (1, 2):
        return None
    rust = "#9A4E26"
    t = P("M3.8 15L4 10.8Q4.4 6.4 15 6.4Q25.6 6.4 26 10.8L26.2 15Z", "#8C7258", 1.1)
    t += chest_body(3.4, 15, 26.6, 27, "#8C7258", rust)
    t += L("M4 15h22.6", 1.2)
    t += E(10, 21, 1.1, .9, INK, 0) + E(20, 23.4, .9, .7, INK, 0) + E(12.6, 10, .9, .7, INK, 0) + E(19.6, 9.4, .7, .6, INK, 0) + E(11.6, 24.6, .6, .5, INK, 0)
    if v == 1:
        t += P("M13.2 15h3.6v4.6q-1.8 1.4-3.6 0z", rust, .7)
    else:
        t += P("M15.6 16.6h3.6v4.6q-1.8 1.4-3.6 0z", rust, .7, ' transform="rotate(35 17.4 18)"')
    m = G(P("M0 0Q-3.6 -3.8 -6.8 -2.2Q-6.6 1.4 -3 2.2Q-1 2 0 .8Z", "#9E8E74", .7) + P("M0 0Q3.6 -3.8 6.8 -2.2Q6.6 1.4 3 2.2Q1 2 0 .8Z", "#B8A88E", .7)
          + E(0, .6, .9, 2.4, "#6F624E", .5) + L("M-.3 -1.6Q-1.2 -3.4 -2.4 -4M.3 -1.6Q1.2 -3.4 2.4 -4", .5), "translate(24 3.4) rotate(20) scale(.72)")
    trail = L("M14 6Q16.6 2.4 20.2 3.4", .55, "#8C8070", ' stroke-dasharray=".9 .8"')
    return t + trail + m


def weg(v):
    """Vorbild: Wanderweg-Piktogramm – Weg in Perspektive zwischen grünen Rändern, Fussabdrücke (Sohle + Ferse), am Ende ein
    Stadttor auf dem Horizont (Ziel)."""
    if v not in (1, 2):
        return None
    s = P("M1 19.6Q2 9.8 15 8.6Q28 9.8 29 19.6Z", GREEN, .9)  # Boden
    if v == 1:
        s += P("M7.4 19.6L13.8 9.2H16.2L22.6 19.6Z", SAND, .8)
    else:
        s += P("M5.4 19.6Q10 15.4 16 13.6Q19.4 12.4 14.6 9.4L16.4 9Q22.6 11.6 19.6 14.4Q15.6 16.8 18.8 19.6Z", SAND, .8)
    gate = (P("M11.4 9.2V3.2H18.6V9.2Z", "#D6CCB6", .8) + P("M10.8 3.4h8.4V1.8h-8.4z", "#B9AC92", .6)
            + P("M13.6 9.2V6.4Q15 5 16.4 6.4V9.2Z", "#5A4632", .5))
    s += gate

    def foot(x, y, sc, r):
        return G(F("M-.9 -1Q-.9 -2.6 0 -2.6Q.9 -2.6 .9 -1Q.9 .2 0 .4Q-.9 .2 -.9 -1Z", "#6A4A2A") + F("M-.7 1.1Q0 .7 .7 1.1V1.8Q0 2.4 -.7 1.8Z", "#6A4A2A"),
                 f"translate({x} {y}) rotate({r}) scale({sc})")
    steps = [(13.4, 17.4, 1.15, -8), (16.6, 15.2, 1, 8), (14.2, 12.8, .8, -6), (15.8, 10.8, .62, 6)] if v == 1 else \
        [(10.6, 17.6, 1.1, 50), (14.6, 15.2, .95, 65), (17.2, 13, .8, -30), (16, 10.8, .6, -50)]
    s += "".join(foot(*a) for a in steps)
    return s


def tempel(v):
    """Vorbild: Modell des herodianischen Tempels (Israel-Museum) auf dem Tempelberg: hoher weisser Bau mit Goldkante und
    Vorhang-Portal auf einer mächtigen Quadermauer-Plattform (wie die Westmauer); @2 mit Brandopferaltar und Rauch."""
    if v not in (1, 2):
        return None
    sw = 3
    s = P("M4 98H196V148H4Z", "#D8C9A6", sw)  # Plattform aus grossen Quadern
    for y in (108, 118, 128, 138):
        s += L(f"M6 {y}H194", 1.4, "#A8956E")
    for i, y in enumerate((98, 108, 118, 128, 138)):
        off = 0 if i % 2 else 14
        s += "".join(L(f"M{x} {y}v10", 1.4, "#A8956E") for x in range(18 + off, 194, 28))
    for x0, x1 in [(14, 58), (142, 186)]:
        s += P(f"M{x0} 74H{x1}V98H{x0}Z", "#E6DCC6", sw * .8) + P(f"M{x0 - 3} 68H{x1 + 3}V76H{x0 - 3}Z", GOLD2, sw * .7)
    s += P("M74 6H126V98H74Z", "#EDE6D6", sw * .8) + P("M70 2H130V9H70Z", GOLD, sw * .6)
    s += P("M52 26H148V98H52Z", "#F6F1E6", sw) + P("M48 18H152V28H48Z", GOLD, sw * .8)
    s += P("M80 98V40H120V98Z", GOLD, sw * .8) + P("M87 98V47H113V98Z", "#7A2E3A", 1.8)
    s += L("M95 50V96M100 50V96M105 50V96", 1.4, "#A8495A")
    if v == 2:
        s += P("M22 74V62H44V74Z", STONE2, 2) + P("M26 62Q28 56 33 58Q36 52 40 58Z", "#E8862A", 1.4)
        s += P("M32 54Q26 44 34 36Q42 28 34 18Q46 26 40 38Q36 46 38 54Z", "#C9C3B8", 1.4)
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
    """Vorbild: Kelch wie beim vollen Becher, aber ausgegossen: gekippt, nur ein letzter Tropfen fällt (@1), bzw. umgedreht
    abgestellt (@2: ausgetrunken)."""
    if v not in (1, 2):
        return None
    cup = (P("M6 9.2V11.6", "none", 1.4) + L("M6 9.2V11.6", .6, GOLD2)
           + P("M2.4 13.4Q2.6 11.6 6 11.6Q9.4 11.6 9.6 13.4Z", GOLD2, .9)
           + P("M1.2 2.8Q1.4 8.8 6 9.4Q10.6 8.8 10.8 2.8Z", GOLD, 1) + L("M8.8 4Q8.6 7 6.8 8.2", .55, "#B8891A"))
    drop = P("M0 -1.4Q1 0 1 .6A1 1 0 0 1 -1 .6Q-1 0 0 -1.4Z", "#8E1F2A", .45)
    if v == 1:
        rim = E(6, 2.8, 4.8, 1.5, "#B8891A", .9)
        return G(cup + rim, "translate(8.4 5.6) rotate(-128) scale(.82) translate(-6 -8)") + G(drop, "translate(3 11.6)")
    rim = E(6, 2.8, 4.8, 1.5, GOLD2, .9)
    return G(cup + rim, "translate(6 7.6) rotate(180) translate(-6 -8)") + L("M.6 13.6H11.4", .8, "#8C7A60")


def splitter(v):
    """Vorbild 👁 frontal; ein Holzsplitter (helles Holz, dunkle Kontur, ausgefranstes Ende) steckt schräg im Augenweiss;
    @2 dazu der Zeigefinger (haende.hand_zeigend), der darauf weist (Mt 7,4: «lass mich den Splitter herausziehen»)."""
    if v not in (1, 2):
        return None
    eye = P("M2.4 9.4Q16 -1.6 29.6 9.4Q16 20.4 2.4 9.4Z", "#FFFFFF", 1.4)
    eye += C(13.4, 9.4, 4.2, "#8A5A2E", .9) + C(13.4, 9.4, 2, INK, 0) + C(14.8, 8, .9, "#FFFFFF", 0)
    eye += L("M2.4 9.4Q16 -1.6 29.6 9.4", 1.9)
    sp = P("M19.6 9.6L25.4 6.2L25.8 7.2L26.8 6.6L26.4 8L27.4 8.2L26.2 8.8Z", "#C99A5A", .6) + L("M21 9L25.4 7.2", .35, "#8A5A2E")
    if v == 1:
        return eye + sp
    return G(eye + sp, "translate(0 1) scale(.86)") + H.place(H.hand_zeigend(), 30.6, 15.6, 200, .42)


def salz(v):
    """Vorbild 🧂: Salzgefäss mit Löchern, aus dem weisse Körner rieseln (eindeutig «Salz»); @2 würzt ein Brot."""
    if v not in (1, 2):
        return None
    s = P("M6 4.6Q6 2 10 2Q14 2 14 4.6V6H6Z", "#C9CED2", .9)
    s += C(8.6, 3.6, .45, INK, 0) + C(10, 3.1, .45, INK, 0) + C(11.4, 3.6, .45, INK, 0)
    s += P("M5.6 6H14.4L15.6 14.4Q10 15.6 4.4 14.4Z", "#F4F1EA", 1) + L("M7.6 8.6V12.4", .8, "#D9D2C4")
    grains = "".join(f'<rect x="{x}" y="{y}" width="1" height="1" fill="#FFFFFF" stroke="{INK}" stroke-width=".35" transform="rotate(20 {x} {y})"/>'
                     for x, y in [(16.6, 2.2), (17.8, 4.2), (16.2, 5.6), (18.6, 6.6), (17.2, 8)])
    if v == 1:
        return G(s + grains, "rotate(-14 10 9)")
    return G(s + grains, "translate(-1 -1) scale(.8) rotate(-30 10 9)") + P("M10 15Q10 11 15 10.8Q19.6 11 19.6 15Z", "#D9A05A", .8) \
        + L("M13 12.6l1 1.4M16 12.2l1 1.6", .5, "#9A6A30")


def synagoge3():
    """Runde 16 (Entscheid Andi Neck 2026-10-26: kein Davidstern – anachronistisch, erinnert an die heutige Staatsflagge):
    Steinbau mit Giebel und Säulenfront wie die Synagogen in Galiläa (Kafarnaum, Gamla), grosse offene Torarolle im Giebel."""
    s = P("M4 57H86V62H4Z", STONE2, 1.4)
    s += P("M9 26H81V57H9Z", "#E4D9C2", 1.8)
    s += P("M5 27L45 4.6L85 27Z", "#D6CCB6", 1.8)
    for x in (14, 26, 58, 70):
        s += P(f"M{x} 31h6v26h-6z", "#F2EBDC", 1.1) + P(f"M{x - 1.6} 28h9.2v3h-9.2z", STONE, 1)
    s += P("M37 57V42Q45 34 53 42V57Z", "#5A4632", 1.4)
    t = (P("M-7 -5H7V5H-7Z", CREAM, 1) + L("M-4.6 -2.2h9.2M-4.6 0h9.2M-4.6 2.2h9.2", .7, "#7A6E60")
         + P("M-10.6 -7.4h3.6V7.4h-3.6Z", WOOD, 1) + P("M7 -7.4h3.6V7.4H7Z", WOOD, 1)
         + P("M-9.6 -9.4h1.6v2h-1.6zM8 -9.4h1.6v2H8zM-9.6 7.4h1.6v2h-1.6zM8 7.4h1.6v2H8z", WOOD2, .6))
    return s + G(t, "translate(45 19) scale(.9)")


def _rolle_offen(cx, cy, k=1.0):
    """Offene Torarolle: zwei Holzstäbe mit Griffen, dazwischen das Blatt mit Schriftzeilen."""
    t = (P("M-11 -6.4H11V6.4H-11Z", CREAM, 1) + L("M-8 -3.2h6M-8 0h6M-8 3.2h6M2 -3.2h6M2 0h6M2 3.2h6", .8, "#7A6E60")
         + P("M-15.4 -8.4h4.4V8.4h-4.4Z", WOOD, 1) + P("M11 -8.4h4.4V8.4H11Z", WOOD, 1)
         + P("M-14.2 -11h2v2.6h-2zM12.2 -11h2v2.6h-2zM-14.2 8.4h2v2.6h-2zM12.2 8.4h2v2.6h-2z", WOOD2, .6))
    return G(t, f"translate({cx} {cy}) scale({k})")


def synagoge4():
    """Runde 16, @4: schlichtes Versammlungshaus aus Stein (Flachdach wie in Galiläa, kein Säulentempel), über der Tür gross die
    offene Torarolle: das Haus, in dem die Schrift gelesen wird."""
    s = P("M4 58H86V62H4Z", STONE2, 1.4)
    s += P("M12 16H78V58H12Z", "#D9CCB0", 1.8) + P("M8 11H82V17H8Z", "#B9A88A", 1.6)
    s += L("M12 30H78M12 44H78M30 16V30M58 16V30M22 30V44M45 30V44M68 30V44M34 44V58M56 44V58", .6, "#A8987A")
    s += P("M38 58V45Q45 39 52 45V58Z", "#5A4632", 1.4)
    s += P("M16 46h7v7h-7zM67 46h7v7h-7z", "#6E5A44", 1)
    return s + P("M24 20H66V40H24Z", "#E9DDC4", 0) + _rolle_offen(45, 30, 1.25)


def synagoge5():
    """Runde 16, @5: Blick ins Versammlungshaus – ein Mann liest am Lesepult aus der offenen Rolle, davor sitzen Zuhörer."""
    s = P("M6 24L45 4L84 24V60H6Z", "#B9A88A", 1.8) + P("M12 26H78V60H12Z", "#F2E8D2", 1)
    s += P("M41 38h8v12h-8z", WOOD, 1)  # Lesepult
    s += P("M37 56Q37 40 45 38Q53 40 53 56Z", "#5E7FA0", 1) + C(45, 32, 5, SKIN, 1)  # Leser
    s += _rolle_offen(45, 40, .62)
    for x in (22, 34, 56, 68):  # Zuhörer (Köpfe und Schultern)
        s += P(f"M{x - 6} 60Q{x - 6} 52 {x} 51Q{x + 6} 52 {x + 6} 60Z", "#9C7B55", 1) + C(x, 47, 4, SKIN, .9)
    return s


def ausschluss():
    """Runde 16: Ausschluss aus der Synagoge ([[JHN.9.22]]) – die neue Synagoge (@4, ohne Davidstern) mit rotem Verbotszeichen."""
    return (synagoge4() + C(72, 48, 13, "#D32F2F", 1.4)
            + f'<rect x="63.4" y="45.4" width="17.2" height="5.2" rx="1" fill="#FFFFFF"/>')


def rabe(v):
    """Runde 16 ([[LUK.12.24]]): Rabe als schwarzer Vogel mit kräftigem Schnabel; @1 sitzt auf einem Zweig, @2 fliegt."""
    if v == 1:
        s = L("M3 18.4H25", 1.6, WOOD2) + L("M18 18.4l3-2.4", 1, WOOD2)
        s += L("M13.2 13.6v4.4M16 13.4v4.6", .9, INK)
        s += P("M3.6 12.6Q5.6 7 12.6 6.4Q17.4 6 19.6 4.4Q22.2 2.6 24.4 3.8L27.6 5.4L24.6 6.6Q23.6 9.6 20 11.8Q16 14.2 10.8 14.2L3.6 16.4Q2.8 14.4 3.6 12.6Z", "#2A2622", .9)
        s += P("M7.6 10.4Q11.6 7.8 17.6 8.4Q15.4 12.4 9.4 12.8Z", "#4A4E58", .6)
        s += C(23.4, 4.8, .7, "#FFFFFF", 0) + L("M24.6 5.9L27.6 5.4", .5, "#5A5650")
        return s
    if v == 2:
        s = P("M2.4 12.2Q6.4 9.6 12 10Q16.6 10 19.2 8.6Q21.4 7.4 23 8.4L26.4 9.8L23.2 10.8Q21.4 13.4 16.4 14.2Q11 14.8 7 13.8L2 16Q1.6 14 2.4 12.2Z", "#2A2622", .9)
        s += P("M9 11Q7.4 5 3.4 1.6Q10 2 14.4 6Q16.4 8 16.4 10.6Z", "#3A3C44", .8)
        s += P("M12.6 10.6Q14.6 5 19.4 2.4Q19.6 7.4 17.4 10.8Z", "#2A2622", .8)
        s += C(21.8, 9.1, .6, "#FFFFFF", 0)
        return s
    return None


def synagoge(v):
    """Vorbild: Synagoge von Kafarnaum (Steinbau, Giebelfront mit Bogenfenster; im Fries ein Davidstern) bzw. 🕍; das
    Erkennungszeichen gross: Torarolle (@1) oder Davidstern (@2) im Giebel."""
    if v == 3:
        return synagoge3()
    if v == 4:
        return synagoge4()
    if v == 5:
        return synagoge5()
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
    """Vorbild: Sämann-Geste (haende.hand_gebend, wie 🫳) bzw. offene Hand voller Saatkörner (haende.hand_empfangend, wie 🫴)."""
    def korn(x, y, r, sc=1.0):
        return G(P("M0 -1.5Q1.1 -1.2 1.1 0Q1.1 1.3 0 1.5Q-1.1 1.3 -1.1 0Q-1.1 -1.2 0 -1.5Z", "#D9A441", .4) + L("M0 -1V1", .3, "#9A7420"),
                 f"translate({x} {y}) rotate({r}) scale({sc})")
    if v == 1:
        hand = H.place(H.hand_gebend(), 2.6, 4.2, 10, .74)
        seeds = "".join(korn(x, y, r) for x, y, r in [(16.4, 11, 20), (18.6, 12.8, -15), (14.8, 13.4, 30), (17.4, 15, 0)])
        soil = P("M1 21.4Q2 17.4 12 17.2Q22 17.4 23 21.4Z", "#8B5E3C", .9) + L("M4 19.6q3-1 6-.4M13 19.4q3-.6 6 .2", .5, "#6A4428")
        return soil + hand + seeds
    if v == 2:
        hand = H.place(H.hand_empfangend(), 3.4, 14, -6, .92)
        heap = "".join(korn(x, y, r, 1.05) for x, y, r in [(9.4, 11.2, 20), (12, 11.6, -30), (14.6, 11.2, 10), (10.8, 9.2, -10), (13.4, 9.2, 40), (12.2, 7.2, 0)])
        fall = korn(19.4, 15, 30) + korn(21, 18.6, -20)
        return hand + heap + fall
    return None


def fessel(v):
    """Vorbild: gefesselte Hände – zwei offene Hände (haende.hand_offen, wie ✋), Handgelenke übereinander gekreuzt, mehrfach
    mit Strick umwickelt (@1); bzw. Strick als Schlinge mit Knoten (@2, ohne Hände)."""
    if v == 1:
        s = H.place(H.hand_offen(cuff_on=True, lang=6), 12.6, 21.4, -24, .72) + H.place(H.hand_offen(cuff_on=True, lang=6), 17.4, 21.4, 24, .72, True)
        rope, rope2 = "#C8A36A", "#8C6A38"
        for dy in (0, 2.4):
            s += P(f"M9.4 {19.6 + dy}Q15 {17.8 + dy} 20.6 {19.6 + dy}L20.6 {21.6 + dy}Q15 {19.8 + dy} 9.4 {21.6 + dy}Z", rope, .7)
            s += L(f"M12 {19 + dy}l.8 2M15 {18.7 + dy}v2M18 {19 + dy}l-.8 2", .45, rope2)
        d = "M20.4 23Q25 24 26.6 27.6"
        return s + P(d, "none", 2.2) + L(d, 1.2, rope)
    if v == 2:
        rope, rope2 = "#C8A36A", "#8C6A38"
        d1 = "M15 4Q7 4 7 11Q7 18 15 18Q23 18 23 11Q23 6 18 4.6"
        s = P(d1, "none", 3.4) + L(d1, 2, rope)
        s += P("M15 18Q14 22 11 25Q9 27 10 28.6", "none", 3.4) + L("M15 18Q14 22 11 25Q9 27 10 28.6", 2, rope)
        s += P("M15 18Q17 22 19.6 24.6Q21.6 26.6 20.6 28.6", "none", 3.4) + L("M15 18Q17 22 19.6 24.6Q21.6 26.6 20.6 28.6", 2, rope)
        s += E(15, 18, 2.6, 2, rope, .8) + L("M13.4 17.2q1.6 1.6 3.2 0", .5, rope2)
        s += L("M9 8l1.2 1M8.2 13l1.4.4M21.2 13.4l-1.4.4", .5, rope2)
        return s
    return None


def matte(v):
    """Vorbild: Schlafmatte/Bettrolle von der Seite (wie ein flaches Polster mit Kissen und gefalteter Decke); @2 an vier
    Seilen herabgelassen (Mk 2,4)."""
    if v == 1:
        s = P("M1.6 8.6Q1.6 6.4 4 6.4H28Q30.4 6.4 30.4 8.6V9.2Q30.4 11 28 11H4Q1.6 11 1.6 9.2Z", "#E3C27A", 1)
        s += L("M3 8.8H29", .5, "#C9A35A") + L("M7 6.6v4.2M12 6.6v4.2M17 6.6v4.2M22 6.6v4.2", .4, "#C9A35A")
        s += P("M3 6.6Q3 3.4 6.4 3.6Q9.4 3.6 9.4 6.6Z", "#F4F1EA", .8)
        s += P("M19 6.6Q19.4 4.6 22 4.6H28.4Q30 4.6 30 6.6Z", "#B5714A", .8)
        return s
    if v == 2:
        s = L("M8 0.6L4 7.4M8 .6L12 7.4M24 .6L20 7.4M24 .6L28 7.4", .6, "#8C6A38")
        s += P("M2 8.6Q2 7.4 3.6 7.4H28.4Q30 7.4 30 8.6V9.6Q30 11 28.4 11H3.6Q2 11 2 9.6Z", "#E3C27A", .9)
        s += L("M3.4 9.2H28.6", .45, "#C9A35A") + P("M3.4 7.6Q3.4 5.6 6 5.8Q8.4 5.8 8.4 7.6Z", "#F4F1EA", .7)
        return s
    return None


def sandale(v):
    """Vorbild 👡 in Schrägaufsicht: Sohle in Fussform mit Zehenschlaufe und zwei Riemen, der Fersenriemen ist gelöst und hängt
    mit Schnalle seitlich heraus (Joh 1,27: den Riemen lösen)."""
    if v not in (1, 2):
        return None
    sole_c, top_c, strap = "#B9783F", "#E2B27A", "#5E3518"
    s = P("M6.8 6.4C10 6.4 12 7.4 15 7.3C19 7.1 21 4.4 26 4.4C30.6 4.4 32.9 7 32.9 10C32.9 13 30.6 15.6 26 15.6C21 15.6 19 12.9 15 12.7C12 12.6 10 13.6 6.8 13.6A3.6 3.6 0 0 1 6.8 6.4Z", sole_c, 1.3)
    s += P("M7 8C10 8 12.4 8.8 15 8.8C19 8.6 21.4 6 26 6C29.6 6 31.3 8 31.3 10C31.3 12 29.6 14 26 14C21.4 14 19 11.4 15 11.2C12.4 11.2 10 12 7 12A2 2 0 0 1 7 8Z", top_c, .5)
    s += P("M27.4 10L21 7.2V8.8ZM27.4 10L21 12.8V11.2Z", strap, .6) + C(27.4, 10, 1, strap, .6)  # Zehenschlaufe
    s += P("M17 6.4Q18.4 10 17 13.6L19.6 13.4Q21 10 19.6 6.6Z", strap, .8)  # Riststrap
    if v == 1:  # Fersenriemen offen, hängt heraus
        s += P("M8.6 6.6L10.6 6.4L11 3.2Q10.6 1.2 8.4 1.4L5.4 2Q4.4 2.4 4.8 3.4L8.4 3.2Z", strap, .7)
        s += P("M8.6 13.4L10.6 13.6L10.8 16.6Q10.4 18.6 8 18.4L3 18Q2.2 17.6 2.8 16.8L8.2 16.4Z", strap, .7) + P("M2.2 15.8h1.8v2.8H2.2Z", GOLD, .5)
    else:  # Fersenriemen geschlossen um die Ferse
        s += P("M10.6 6.6Q4 4.6 2.6 10Q4 15.4 10.6 13.4L10.6 11.8Q5.6 13 4.6 10Q5.6 7 10.6 8.2Z", strap, .7)
    return s


def leinenbinden(v):
    """Vorbild: Bild vom leeren Grab (Joh 20,5-7). @1: Felsengrab offen, Stein beiseite; in der dunklen Kammer leuchten
    die weissen, liegengelassenen Tücher. @2: Nahansicht: weisse Leinenbänder lose gefaltet und das zusammengelegte
    Schweisstuch auf der Steinbank."""
    if v not in (1, 2):
        return None
    linen, sh = "#FFFFFF", "#AEB8BE"
    s = ""
    if v == 1:  # Felswand mit dunkler Grabkammer dahinter
        s += P("M2 22V8Q2 3 10 3H50Q58 3 58 8V22Z", "#A79A80", 1.2) + P("M38 22V12Q38 7 46 7Q54 7 54 12V22Z", "#3B3226", .9)
    s += P("M3 22L6 19H54L57 22Z", "#D6CCB6", 1.1) + P("M3 22H57V31H3Z", STONE, 1.2)
    for y0 in (17.6, 13.8, 10):
        s += P(f"M7 {y0 + 2}Q8 {y0 - .6} 12 {y0}Q20 {y0 + 1.2} 26 {y0 - .4}Q32 {y0 - 1.4} 36 {y0 + .6}L36 {y0 + 3}Q30 {y0 + 1.4} 24 {y0 + 2.6}Q16 {y0 + 3.6} 7 {y0 + 3.6}Z", linen, .8)
    s += P("M41 20.6L43 14.8H53L51 20.6Z", linen, .9) + L("M42.2 17.6H52M47.6 15L45.8 20.6", .55, sh)
    return s


def perle(v):
    """Vorbild: Perlenkette mit grosser Anhänger-Perle und Glanzstern (Schmuck-Piktogramm, «kostbar»)."""
    if v not in (1, 2):
        return None

    def pe(x, y, r):
        return (C(x, y, r, "#F1E9E2", .6, "#5E5060") + F(f"M{x - r * .15:.2f} {y + r * .98:.2f}A{r} {r} 0 0 0 {x + r * .98:.2f} {y + r * .15:.2f}A{r * 1.25:.2f} {r * 1.25:.2f} 0 0 1 {x - r * .15:.2f} {y + r * .98:.2f}Z", "#D2C2D6")
                + C(x - r * .35, y - r * .35, r * .3, "#FFFFFF", 0))
    star = lambda x, y, r: P(f"M{x} {y - r}Q{x + r * .2} {y - r * .2} {x + r} {y}Q{x + r * .2} {y + r * .2} {x} {y + r}Q{x - r * .2} {y + r * .2} {x - r} {y}Q{x - r * .2} {y - r * .2} {x} {y - r}Z", GOLD, .5)
    s = L("M4 2.4Q3.4 11 15 11.4Q26.6 11 26 2.4", .8, "#9A8670")
    pts = [(4.4, 3.4), (5.2, 6.4), (7.2, 8.8), (10, 10.4), (20, 10.4), (22.8, 8.8), (24.8, 6.4), (25.6, 3.4)]
    s += "".join(pe(x, y, 1.7) for x, y in pts)
    if v == 1:
        s += L("M15 11.4V12.4", .8, "#9A8670") + pe(15, 14.2, 3.2) + star(20.6, 14.6, 2)
    else:
        s += pe(13, 11.4, 1.7) + pe(17, 11.4, 1.7) + star(15, 4.6, 2.6)
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
    """Vorbild: Regenwurm-Piktogramm – schlanker rosa Leib mit regelmässigen Ringen, rundes Ende, ohne Auge, aus einem Erdloch."""
    if v not in (1, 2):
        return None
    d = "M7.4 10.6Q6.4 5 10 3.2Q13.4 1.8 15 4.6Q16.4 7 19.6 6" if v == 1 else "M7.4 10.6Q6.8 6 9.6 4.4Q12.4 3 14 5.4Q15.6 7.6 18.4 6.4Q20.4 5.4 20.8 3.6"
    s = P("M2.6 11.6Q4 9.4 12 9.2Q20 9.4 21.4 11.6Z", "#8B5E3C", .9) + E(7.4, 10, 2.6, .8, "#4E3420", .6)
    s += worm_line(d, 1.9, "#D98A86", .7)
    s += f'<path d="{d}" fill="none" stroke="#B5706C" stroke-width="1.9" stroke-dasharray=".3 1.2" stroke-dashoffset="-.6"/>'
    s += P("M4.6 10.5Q7.4 11.3 10.2 10.5Q9.8 11.5 7.4 11.6Q5 11.5 4.6 10.5Z", "#8B5E3C", .5)
    return s


def grab_zu(v):
    """Vorbild: Felsengrab im Hang (wie FIG-ORT-GRAB), Rollstein ganz vor der Öffnung; an der Fuge zwischen Stein und Fels
    ein rotes Wachssiegel mit kurzer Schnur (Mt 27,66)."""
    if v not in (1, 2):
        return None
    s = P("M2 40Q3 22 12 12Q24 2 40 4Q54 6 60 18Q63 28 62 40Z", "#A79A80", 1.6)
    s += P("M12 12Q24 2 40 4Q54 6 60 18Q56 12 46 9Q32 6 20 11Z", "#8FA672", 1)
    s += L("M48 16q5 3 7 9", .8, "#8C8070")
    s += P("M15 40V28Q15 18 27 18Q39 18 39 28V40Z", "#3B3226", 1)
    s += C(28, 27.4, 12.6, "#C9BFAA", 1.6) + L("M20 21q7-4 14 1", .8, "#8C8070")
    if v == 1:
        s += L("M37 24.4L46 22.6", 1.1, RED) + P("M38.6 21.2Q42.6 20.4 43.4 23.6Q43 27 39.4 27Q36.6 26.2 37 23.6Q37.4 21.6 38.6 21.2Z", RED, .8) + L("M39 23.8q1.2 1.2 2.6 0", .5, DRED)
    else:
        s += L("M14 22L22 24M34 24L42 22", 1.1, RED)
        for x, y in [(15, 22), (41, 22)]:
            s += P(f"M{x - 2.2} {y}Q{x - 2.2} {y - 2.4} {x} {y - 2.4}Q{x + 2.4} {y - 2.4} {x + 2.4} {y}Q{x + 2.4} {y + 2.4} {x} {y + 2.4}Q{x - 2.2} {y + 2.4} {x - 2.2} {y}Z", RED, .8)
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
    """Vorbild: Jordantal – grünes Flussband mit Bäumen und Schilf mitten in kahlen Wüstenhügeln (so unterscheidet sich der
    Jordan von See und Meer); Fluss gewunden vom Vordergrund zum Horizont."""
    if v not in (1, 2):
        return None
    s = ground("M3 24Q20 12 40 18Q60 8 84 16Q110 6 136 15Q160 8 183 18", "#D9C18E")
    s += ground("M3 34Q50 26 93 28Q136 26 183 34", SAND)
    s += P("M30 67Q48 50 84 44Q110 38 100 30L108 28Q128 34 130 42Q136 54 150 67Z", "#8FB45E", 1.6)  # grünes Ufer
    s += P("M66 67Q74 54 100 48Q120 43 106 35Q98 31 104 29L108 28.6Q118 32 116 36Q132 44 124 54Q114 60 120 67Z", WATER, 1.8)
    s += L("M84 61q6-3 12 0M106 50q5-3 10 0", 1.4, FOAM)
    trees = [(46, 54), (58, 48), (134, 50), (144, 58)] if v == 1 else [(48, 54), (140, 54)]
    for x, y in trees:
        s += L(f"M{x} {y + 6}v-6", 1.6, "#7A5A36") + E(x, y - 2, 6, 4.4, GREEN3, 1.2)
    if v == 2:
        for x, y in [(56, 60), (130, 62)]:
            s += L(f"M{x} {y}q-1-8 1-13M{x + 4} {y}q1-9-1-13", 1.6, GREEN3) + E(x + 1, y - 13, 1.3, 3, "#8A6A3A", 0)
    return frame_land(s, "#EEF2EC")


def feld(v):
    """Vorbild: Feldflur von oben schräg (🏞️ mit Äckern): Felder in verschiedenen Farben (gepflügt braun, grün, reif hell)
    mit Furchen, getrennt durch Raine – «Feld» als Landschaft; Kornfeld zeigt dagegen grosse Ähren."""
    if v not in (1, 2):
        return None
    s = ground("M3 22Q30 14 60 18Q100 10 140 17Q166 14 183 20", GREEN2)
    s += ground("M3 26Q93 20 183 26", "#F3E4A8")
    s += P("M3 34L93 26L183 34V46H3Z", "#9DB874", 1.2)
    s += P("M93 26L183 34V58Q140 44 93 26Z", "#F3E4A8", 1.2)
    s += P("M3 46H183V59Q183 67 175 67H11Q3 67 3 59Z", "#A8794A", 1.4)
    s += L("M20 46l-8 21M50 46l-6 21M80 46l-2 21M110 46l2 21M140 46l6 21M170 46l8 21", 1.2, "#7A5230")
    s += L("M10 38l60-6M10 42l70-6", .9, "#7FA05A") + L("M110 34l60 14M100 30l78 20", .9, "#C9A35A")
    s += L("M93 26L3 46", 1.2)
    if v == 2:
        s += L("M150 22v3", 1.6) + E(150, 17, 6, 5, LEAF, 1.2) + L("M30 22v3", 1.6) + E(30, 18, 5, 4, LEAF, 1.2)
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
    """Vorbild 🌾: dichte Reihe grosser reifer Ähren über die ganze Breite vor dem Horizont (Nahansicht ins Kornfeld)."""
    if v not in (1, 2):
        return None
    s = ground("M3 30Q30 22 60 26Q100 18 140 25Q166 22 183 28", GREEN2)
    s += ground("M3 40Q93 34 183 40", "#F3E3A6")
    xs = range(16, 180, 14) if v == 1 else range(22, 176, 22)
    for i, x in enumerate(xs):
        lean = ((i * 7) % 5 - 2) * 1.5
        s += ahre(x, 67, 30 + (i % 2) * 4, lean, "#E8B931" if i % 2 else "#D99A2B", 1.9 if v == 1 else 2.4)
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
    """Vorbild: Blick vom Berg Nebo ins verheissene Land (5 Mo 34,1-4): vorn ein brauner Felsvorsprung, unten das grüne,
    fruchtbare Land mit Feldern und Fluss, Sonne geht auf; @2 dazu die Kundschafter-Traube vorn auf dem Fels."""
    if v not in (1, 2):
        return None
    s = C(150, 20, 9, GOLD, 1.6) + L("M150 6v3M136 20h3M161 20h3M140 10l2 2M160 10l-2 2", 1.6, GOLD2)
    s += ground("M3 26Q30 18 60 22Q100 14 140 22Q166 18 183 24", GREEN2)
    s += ground("M3 34Q93 28 183 34", GREEN)
    s += P("M70 40Q100 34 130 38L140 48Q100 46 76 50Z", "#E3C26A", 1.2) + P("M120 52Q150 46 180 50V58Q150 56 124 60Z", "#E3C26A", 1.2)
    s += P("M100 67Q110 54 128 46Q150 38 183 36V40Q156 42 136 50Q118 58 112 67Z", WATER, 1.4)
    s += P("M3 40Q20 36 34 44Q48 52 56 67H11Q3 67 3 59Z", "#9C7A52", 1.6) + L("M14 50l6 4M24 46l4 6", .9, "#7A5A36")
    if v == 2:
        t = L("M30 34Q32 30 36 29", 1.6, "#6A4428") + P("M32 36Q24 30 20 36Q24 40 32 38Z", LEAF, 1.2)
        for x, y in [(30, 40), (37, 40), (44, 40), (33.5, 46), (40.5, 46), (37, 52)]:
            t += C(x, y, 3.8, "#6B3A6E", 1.1) + C(x - 1.2, y - 1.3, 1, "#A77AAA", 0)
        s += t
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
    "FIG-ZEICHEN-SCHATZ": (schatz, "0 0 30 28", "Schatz / Lohn bei Gott", {1: "offene Schatztruhe mit Goldmünzen auf Wolke, Strahlen", 2: "offene Schatztruhe mit Goldmünzen im Lichtschein, Strahlen"}),
    "FIG-ZEICHEN-SCHATZ-ERDE": (schatz_erde, "0 0 30 28", "Schatz auf der Erde (vergänglich: Motte und Rost zerstören ihn)", {1: "geschlossene Truhe mit Löchern und Rost, Motte fliegt davon", 2: "zerfressene Truhe, Schloss aufgebrochen, Motte fliegt davon"}),
    "FIG-ZEICHEN-WEG": (weg, "0 0 30 20", "Weg / hingehen zu einem Ziel", {1: "Weg mit Fussabdrücken führt geradeaus zu einem Stadttor", 2: "geschwungener Weg mit Fussabdrücken zu einem Stadttor"}),
    "FIG-ORT-TEMPEL": (tempel, "0 0 200 150", "Tempel in Jerusalem", {1: "herodianischer Tempel auf Plattform aus grossen Quadern (Tempelberg), Goldkante, Vorhang-Portal", 2: "dasselbe mit Brandopferaltar und Rauch im Vorhof"}),
    "FIG-OBJ-MUENZEN": (muenzen, "0 0 24 14", "Münzen, Geld", {1: "Münzstapel und eine Münze mit Prägung", 2: "zwei Münzstapel und eine Münze mit Prägung"}),
    "FIG-OBJ-SCHWEIN": (schwein, "0 0 34 22", "Schwein (Herde)", {1: "Schwein von der Seite", 2: "drei Schweine einer Herde"}),
    "FIG-OBJ-BECHER-VOLL": (becher_voll, "0 0 12 14", "voller Becher (Wein)", {1: "goldener Kelch mit Rotwein", 2: "goldener Kelch randvoll mit Rotwein, Tropfen läuft über"}),
    "FIG-OBJ-BECHER-LEER": (becher_leer, "0 0 14 14", "leerer Becher", {1: "goldener Kelch ausgegossen, nur ein letzter Tropfen fällt", 2: "goldener Kelch umgedreht abgestellt"}),
    "FIG-ORT-SEE": (see, "0 0 186 70", "See (See von Galiläa)", {1: "ovaler See von Hügeln umgeben, Fischerboot mit Segel", 2: "ovaler See, Fischerboot und Fischer mit Netz"}),
    "FIG-ORT-FELD": (feld, "0 0 186 70", "Feld (Acker, Felder reif zur Ernte)", {1: "Feldflur: gepflügter, grüner und reifer Acker mit Furchen", 2: "Feldflur mit Furchen und Bäumen"}),
    "FIG-OBJ-SPLITTER": (splitter, "0 0 32 18", "Splitter (im Auge des Bruders)", {1: "Auge mit Holzsplitter im Augenweiss", 2: "Auge mit Holzsplitter, Zeigefinger weist darauf"}),
    "FIG-OBJ-SALZ": (salz, "0 0 20 16", "Salz", {1: "Salzstreuer, aus dem weisse Körner rieseln", 2: "Salzstreuer würzt ein Brot"}),
    "FIG-ORT-SYNAGOGE": (synagoge, "0 0 90 64", "Synagoge (Versammlungshaus)", {1: "Steinbau mit Giebel, grosse Torarolle im Giebel", 2: "Steinbau mit Giebel, Davidstern im Giebel", 3: "Steinbau mit Giebel und Säulenfront, grosse Torarolle im Giebel (Runde 16, ohne Davidstern)", 4: "schlichtes Steinhaus mit Flachdach, gross die offene Torarolle über der Tür", 5: "Blick ins Haus: Mann liest am Pult aus offener Rolle, Zuhörer sitzen davor"}),
    "FIG-ZEICHEN-AUSSCHLUSS": (lambda v: ausschluss() if v == 1 else None, "0 0 90 64", "aus der Synagoge ausgeschlossen", {1: "Synagoge (Steinhaus mit Torarolle) mit rotem Verbotszeichen"}),
    "FIG-OBJ-RABE": (rabe, "0 0 30 20", "Rabe", {1: "schwarzer Vogel mit kräftigem Schnabel auf einem Zweig", 2: "fliegender schwarzer Vogel"}),
    "FIG-ORT-JORDAN": (jordan, "0 0 186 70", "Jordan (Fluss)", {1: "grünes Flussband mit Bäumen, gewunden durch Wüstenhügel zum Horizont", 2: "Fluss mit grünem Ufer, Bäumen und Schilf in Wüstenhügeln"}),
    "FIG-OBJ-VOGEL": (vogel, "0 0 24 16", "Vogel (Vögel des Himmels)", {1: "fliegender Vogel", 2: "drei fliegende Vögel"}),
    "FIG-OBJ-SAMEN": (samen, "0 0 24 22", "Samen / Saat (säen)", {1: "Hand von oben streut Körner auf Erde", 2: "offene Hand voller Saatkörner, Körner fallen"}),
    "FIG-OBJ-FESSEL": (fessel, "0 0 30 30", "Fessel (Strick, gebunden)", {1: "zwei offene Hände, Handgelenke gekreuzt und mit Strick umwickelt", 2: "Strick als Schlinge mit Knoten"}),
    "FIG-OBJ-MATTE": (matte, "0 0 32 12", "Liegematte (eines Kranken)", {1: "flache Strohmatte von der Seite mit Kissen und Decke", 2: "Matte mit Kissen an vier Seilen herabgelassen"}),
    "FIG-OBJ-SANDALE": (sandale, "0 0 34 20", "Sandale (Riemen lösen)", {1: "Sandale von oben, Fersenriemen gelöst mit Schnalle", 2: "Sandale von oben mit Zehenschlaufe und Riemen"}),
    "FIG-ORT-LAND": (land, "0 0 186 70", "Land (verheissenes Land)", {1: "Blick vom Felsvorsprung auf grünes fruchtbares Land mit Feldern, Fluss und aufgehender Sonne", 2: "dasselbe mit grosser Traube vorn"}),
    "FIG-ORT-MEER-OFFEN": (meer_offen, "0 0 186 70", "offenes Meer mit Wellen (Sturm)", {1: "drei grosse brechende Wellen", 2: "Wellenreihen mit Gischt"}),
    "FIG-ORT-WUESTE": (wueste, "0 0 186 70", "Wüste", {1: "Felsen, Sanddünen, Sonne, dürrer Busch", 2: "Felsen, Dünen, Sonne, Busch, Steine"}),
    "FIG-ORT-GRAB-VERSCHLOSSEN": (grab_zu, "0 0 64 44", "Grab (verschlossen, versiegelt)", {1: "Felsengrab, Rollstein vor der Öffnung, rotes Wachssiegel an der Fuge", 2: "Felsengrab, Rollstein, zwei rote Siegel an den Fugen"}),
    "FIG-OBJ-LEINENBINDEN": (leinenbinden, "0 0 60 34", "Leinenbinden und Schweisstuch im leeren Grab", {1: "weisse Leinenbänder und gefaltetes Tuch auf Steinbank vor Felswand mit dunkler Grabkammer", 2: "weisse Leinenbänder und gefaltetes Tuch auf Steinbank"}),
    "FIG-OBJ-PERLE": (perle, "0 0 30 18", "Perlen (kostbar)", {1: "Perlenkette mit grosser Anhänger-Perle und Glanzstern", 2: "Perlenkette mit Glanzstern"}),
    "FIG-OBJ-SCHLANGE": (schlange, "0 0 30 16", "Schlange", {1: "Schlange in S-Kurve mit Zunge", 2: "Schlange in S-Kurve mit Zunge"}),
    "FIG-OBJ-WURM": (wurm, "0 0 24 12", "Wurm", {1: "schlanker rosa Regenwurm mit Ringen ragt aus Erdloch", 2: "schlanker rosa Regenwurm mit Ringen ragt aus Erdloch"}),
    "FIG-ORT-KORNFELD": (kornfeld, "0 0 186 70", "Kornfeld (reifes Getreide)", {1: "dichte Reihe grosser reifer Ähren vor dem Horizont", 2: "Reihe grosser reifer Ähren vor dem Horizont"}),
}


def variants(fid):
    fn, vb, bed, gez = SPEC[fid]
    out = {}
    for n in (1, 2, 3, 4, 5):
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
