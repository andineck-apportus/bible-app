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
    """Vorbild: offene Schatztruhe (Spielsymbol) – gewölbter Deckel offen, Münzen, Edelstein, Schloss."""
    if v not in (1, 2):
        return None
    lid = (P("M4.4 13.4L4.6 6.4Q4.8 2.2 15 2.2Q25.2 2.2 25.4 6.4L25.6 13.4Z", WOOD, 1.1)
           + P("M6.4 13L6.6 7Q7 4.4 15 4.4Q23 4.4 23.4 7L23.6 13Z", "#5A3A1C", .7)
           + L("M8.6 3.2L8.8 12.8M21.4 3.2L21.2 12.8", 1.6, GOLD2))
    coins = "".join(f'<ellipse cx="{x}" cy="{y}" rx="2.3" ry="1.3" fill="{GOLD}" stroke="{INK}" stroke-width=".6"/>'
                    for x, y in [(7.6, 13.4), (11.2, 12.6), (18.8, 12.6), (22.4, 13.4), (9.4, 10.8), (20.6, 10.8), (15, 9.8)])
    gem = P("M13 10.2l2-2.4 2 2.4-2 2.6z", "#C0392B", .6) + L("M14.3 9.3l.7-.6", .4, "#F5B7B1")
    if v == 2:
        gem = P("M13 10.4l2-2.4 2 2.4-2 2.6z", "#2E86C1", .6) + L("M14.3 9.5l.7-.6", .4, "#D6EAF8")
    body = chest_body(3.4, 14, 26.6, 26) + P("M13.2 14h3.6v4.6q-1.8 1.4-3.6 0z", GOLD, .7) + C(15, 16.4, .7, INK, 0)
    return lid + coins + gem + P("M3 12.6Q15 11 27 12.6V14.4H3Z", GOLD, 1) + body


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
    """Vorbild: Truhe wie «Schatz», aber stumpf, rostig, löchrig, mit grosser Motte (Mt 6,19: Motte und Rost)."""
    rust = "#B5652B"
    if v == 1:  # geschlossene Truhe, Rostflecken, Mottenlöcher, grosse Motte obenauf
        t = (P("M4 14L4.2 10.6Q4.6 6.8 15 6.8Q25.4 6.8 25.8 10.6L26 14Z", "#8C7258", 1.1)
             + chest_body(3.4, 14, 26.6, 26, "#8C7258", "#8E8676")
             + P("M13.2 14h3.6v4.6q-1.8 1.4-3.6 0z", "#8E8676", .7)
             + F("M5.6 17.4q2 -1 3 .8 -.6 2 -2.4 1.6z", rust) + F("M20.8 21q2.4 -.8 3.4 1 -1 1.8 -3 1.2z", rust)
             + F("M18.4 9.2q2 -.6 2.8.6-.8 1.4-2.4 1z", rust) + F("M10 22.4q1.6-.6 2.4.6-.6 1.2-2 .8z", rust)
             + E(11.6, 18.8, .9, .7, INK, 0) + E(8.6, 11.2, .7, .55, INK, 0) + E(21.6, 17.2, .7, .55, INK, 0))
        return t + motte(19.4, 6.6, 1.05)
    if v == 2:  # offene Truhe, angelaufene Münzen, Rost, Motte am Deckel, Münze fällt durch ein Loch
        t = (P("M4.4 13.4L4.6 6.4Q4.8 2.2 15 2.2Q25.2 2.2 25.4 6.4L25.6 13.4Z", "#8C7258", 1.1)
             + P("M6.4 13L6.6 7Q7 4.4 15 4.4Q23 4.4 23.4 7L23.6 13Z", "#4E3A26", .7)
             + "".join(f'<ellipse cx="{x}" cy="{y}" rx="2.3" ry="1.3" fill="#A89A6A" stroke="{INK}" stroke-width=".6"/>'
                       for x, y in [(8, 13.2), (12.4, 12.4), (17.6, 12.4), (22, 13.2), (15, 10.8)])
             + P("M3 12.6Q15 11 27 12.6V14.4H3Z", "#8E8676", 1)
             + chest_body(3.4, 14, 26.6, 26, "#8C7258", "#8E8676")
             + F("M5.6 17.4q2 -1 3 .8 -.6 2 -2.4 1.6z", rust) + F("M20.8 21q2.4 -.8 3.4 1 -1 1.8 -3 1.2z", rust)
             + F("M11 21.6q1.6-.6 2.4.6-.6 1.2-2 .8z", rust) + E(17.4, 19, 1, .8, INK, 0))
        return t + motte(15, 5.6, .95)
    return None


def weg(v):
    """Vorbild: Verkehrspiktogramm Strasse in Perspektive + 👣, als gerahmtes Landschaftsbild (wie 🏞️)."""
    if v not in (1, 2):
        return None
    bot = "L29.2 16.6Q29.2 19.2 26.6 19.2H3.4Q.8 19.2 .8 16.6Z"
    s = '<rect x=".8" y=".8" width="28.4" height="18.4" rx="2.6" fill="#E9F1F2"/>'
    s += C(23.4, 4.6, 2, GOLD, .6) if v == 2 else ""
    s += P("M.8 8.6Q5 5.4 9.6 7.4Q14 4.6 19.4 7Q24.6 5 29.2 8.2" + bot, GREEN2, .6)
    s += P("M.8 10Q15 7.8 29.2 10" + bot, GREEN, .6)
    if v == 1:
        s += P("M8.6 19.2L14.3 8.4H15.7L21.4 19.2Z", SAND, .7)
        steps = [(13.4, 17.2, 1.15, 0), (16.6, 15, .95, 0), (14.2, 12.6, .75, 0), (15.8, 10.6, .55, 0)]
    else:
        s += P("M7 19.2Q11.4 15.4 17.2 13.6Q20.2 12.4 15.6 9.6L15.4 8.4L16.6 8.4Q22.6 11.4 20.6 14Q17.4 16.4 22.8 19.2Z", SAND, .7)
        steps = [(13, 17.4, 1.1, 30), (17, 15.2, .9, 60), (18.2, 12.4, .7, -20), (16.6, 10.2, .5, -30)]
    for x, y, sc, r in steps:
        s += G(F("M0 -1.5Q.9 -1.5 .9 -.2Q.9 1.3 0 1.5Q-.9 1.3 -.9 -.2Q-.9 -1.5 0 -1.5Z", "#7A5A36")
               + F("M-.45 -2.5a.45 .45 0 1 0 .01 0ZM.5 -2.4a.4 .4 0 1 0 .01 0Z", "#7A5A36"), f"translate({x} {y}) rotate({r}) scale({sc})")
    return s + '<rect x=".8" y=".8" width="28.4" height="18.4" rx="2.6" fill="none" stroke="#3B3226" stroke-width="1"/>'


def tempel(v):
    """Vorbild: Modell des herodianischen Tempels (Israel-Museum): hoher weisser Kubus mit breiter Fassade, flaches Dach mit
    goldenen Spitzen, hohes Portal mit Vorhang, Plattform mit Stufen, Säulenhallen der Vorhöfe – kein Giebel."""
    if v not in (1, 2):
        return None
    sw = 2.4
    s = ""
    # Plattform und Stufen
    s += P("M6 128H194V140H6Z", STONE, sw) + P("M14 120H186V128H14Z", "#DDD3BE", sw * .8)
    s += P("M70 140H130L126 146H74Z", STONE2, sw * .7) if v == 1 else P("M76 128H124V140H76Z", "#DDD3BE", sw * .7) + L("M76 132H124M76 136H124", 1.2)
    # Vorhofmauern mit Säulenhalle
    for x0, x1 in [(14, 62), (138, 186)]:
        s += P(f"M{x0} 92H{x1}V120H{x0}Z", "#E6DCC6", sw * .8)
        s += P(f"M{x0 - 2} 88H{x1 + 2}V94H{x0 - 2}Z", STONE2, sw * .6)
        n = 4
        for i in range(n):
            ax = x0 + 4 + i * (x1 - x0 - 8) / n
            aw = (x1 - x0 - 8) / n - 3
            s += P(f"M{ax:.1f} 120V104Q{ax + aw / 2:.1f} 97 {ax + aw:.1f} 104V120Z", "#8C7A60", 1)
    # Hauptbau: Fassade breiter, dahinter schmaler Kubus
    s += P("M74 24H126V120H74Z", "#EDE6D6", sw * .8)  # Heiligtum dahinter (sichtbar über den Schultern)
    s += P("M52 40H148V120H52Z", "#F6F1E6", sw)  # Vorhalle/Fassade
    s += P("M50 34H150V42H50Z", GOLD2, sw * .7) + P("M72 18H128V26H72Z", GOLD2, sw * .7)
    spikes = "".join(f"M{x} 34l1.6-5 1.6 5Z" for x in range(53, 148, 7)) + "".join(f"M{x} 18l1.6-5 1.6 5Z" for x in range(74, 126, 7))
    s += P(spikes, GOLD, .9)
    # Portal mit goldenem Rahmen und Vorhang
    s += P("M82 120V58H118V120Z", GOLD, sw * .8)
    s += P("M88 120V64H112V120Z", "#7A2E3A", 1.4)
    s += L("M94 66V118M100 66V118M106 66V118", 1, "#A8495A")
    s += P("M84 54Q100 44 116 54Z", "#7FA05A", 1.2) + "".join(C(x, 53, 2.2, "#6B3A6E", .8) for x in (92, 100, 108))
    # Fenster/Gliederung
    s += L("M60 52V110M140 52V110", 1.4, "#CFC4AE")
    s += "".join(P(f"M{x} 62h6v10h-6z", "#B9AC92", 1) for x in (60, 134))
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
    """Vorbild: umgekippter Kelch (gleiche Form wie der volle), innen hell und leer, kein Henkel."""
    if v == 1:  # umgekippt auf der Seite, Öffnung nach rechts
        cup = (P("M6 9.2V11.6", "none", 1.4) + P("M2.4 13.4Q2.6 11.6 6 11.6Q9.4 11.6 9.6 13.4Z", GOLD2, .9)
               + P("M1.2 2.8Q1.4 8.8 6 9.4Q10.6 8.8 10.8 2.8Z", GOLD, 1) + L("M3.2 4Q3.4 7 5.2 8.2", .55, "#B8891A")
               + E(6, 2.8, 4.8, 1.9, "#FFF6DC", .9) + E(6, 3.3, 3.2, .9, "#F0E2BC", 0))
        return G(cup, "translate(6.6 8.4) rotate(80) scale(.88) translate(-6 -8)") + L("M.6 13.2H13.4", .8, "#8C7A60")
    if v == 2:  # aufrecht, von leicht oben: leeres helles Inneres
        return becher_form(empty=True) + E(6, 3.1, 3.4, .8, "#F0E2BC", 0)
    return None


def splitter(v):
    """Vorbild 👁 frontal; ein dunkler, gesplitterter Holzspan steckt schräg im Augenweiss, Träne (Mt 7,3)."""
    if v not in (1, 2):
        return None
    s = P("M2.4 9.4Q16 -1.6 29.6 9.4Q16 20.4 2.4 9.4Z", "#FFFFFF", 1.4)
    s += C(14.6, 9.4, 4.4, "#8A5A2E", .9) + C(14.6, 9.4, 2.1, INK, 0) + C(16, 8, 1, "#FFFFFF", 0)
    s += L("M2.4 9.4Q16 -1.6 29.6 9.4", 1.9)
    s += L("M5 1.4Q12 -1.4 19 .4", 1.6) if v == 2 else ""
    # Splitter: schmaler Holzspan, aussen ausgefranst, Spitze im Augenweiss
    s += P("M20.4 10.6L29.8 12.6L29 13.6L31 14.4L29.4 15.2L30.4 16.4L28.2 16Z", "#6B4423", .8) + L("M22.6 11.6l5.4 2", .4, "#A0703C")
    s += P("M8.4 13.8q1.3 1.9 1.3 2.7a1.3 1.3 0 0 1-2.6 0q0-.8 1.3-2.7z", "#7FC3EC", .6)
    return s


def salz(v):
    """Vorbild: Salzkristalle als Würfel (Halit) – kantig statt körnig, damit nicht Reis oder Zucker; dazu Holzlöffel."""
    def cube(x, y, s):
        return G(P("M0 -2L2 -1V1.4L0 2.4L-2 1.4V-1Z", "#FFFFFF", .55) + P("M0 -2L2 -1L0 0L-2 -1Z", "#F2F8FC", .45)
                 + P("M0 0L2 -1V1.4L0 2.4Z", "#C9DCEB", .45), f"translate({x} {y}) scale({s})")
    if v == 1:  # Holzlöffel mit Kristallhaufen, grosse Kristalle daneben
        sp = P("M1.6 5.6L9.4 9.4", "none", 2.4) + L("M1.6 5.6L9.4 9.4", 1.2, WOOD)
        sp += P("M8.4 9.6Q9.4 6.6 13.6 7Q18.4 7.6 18.2 10.6Q17.6 13.4 13 13Q8.6 12.6 8.4 9.6Z", WOOD, 1)
        heap = "".join(cube(x, y, s) for x, y, s in [(11.6, 8.8, .9), (14, 8.2, .95), (16.2, 9.2, .85), (12.8, 6.4, .85), (15.2, 6.2, .8), (14, 4.4, .75)])
        big = cube(5.2, 12.6, 1.25) + cube(8.6, 14, 1)
        return sp + heap + big
    if v == 2:  # Schälchen mit Salzwürfeln, ein grosser Kristall vorn
        b = P("M2 8.6H18Q17.4 14.6 10 14.8Q2.6 14.6 2 8.6Z", "#B5714A", 1)
        heap = "".join(cube(x, y, s) for x, y, s in [(6, 7.6, .9), (8.6, 7, 1), (11.4, 7, 1), (14, 7.6, .9), (7.4, 4.8, .9), (10, 4.2, 1), (12.6, 4.8, .9), (10, 1.9, .8)])
        return heap + b + L("M4.4 11.4Q10 13 15.6 11.4", .5, "#8A4F30")
    return None


def synagoge(v):
    """Vorbild: Toraschrein / Tora auf dem Lesepult (Bima); Synagoge von Kafarnaum (Steinbau mit Bogenfenster)."""
    def tora(cx, cy, s):
        t = (P("M-7 -6H7V6H-7Z", CREAM, 1) + L("M-4.6 -3h9.2M-4.6 -.4h9.2M-4.6 2.2h6", .7, "#7A6E60")
             + P("M-10.2 -8.6h3.2V8.6h-3.2Z", WOOD, 1) + P("M7 -8.6h3.2V8.6H7Z", WOOD, 1)
             + P("M-9.2 -11h1.2V-8.6h-1.2ZM8 -11h1.2V-8.6H8ZM-9.2 8.6h1.2V11h-1.2ZM8 8.6h1.2V11H8Z", GOLD, .7))
        return G(t, f"translate({cx} {cy}) scale({s})")
    if v == 1:  # Bau mit grosser Torarolle als Emblem über dem Tor
        s = P("M8 22H82V58H8Z", "#E4D9C2", 1.8) + P("M4 58H86V62H4Z", STONE2, 1.4)
        s += P("M4 16H86V23H4Z", "#B9AC92", 1.6)
        s += P("M36 58V40Q45 31 54 40V58Z", "#5A4632", 1.4)
        s += P("M15 30h9v12h-9zM66 30h9v12h-9z", "#8C7A60", 1.2)
        s += P("M28 3H62V17H28Z", "#F3E7C6", 1.6) + tora(45, 10.2, .58)
        return s
    if v == 2:  # Innen: Tora auf dem Lesepult, Bänke beidseits, Bogen dahinter
        s = P("M4 60V22Q45 -2 86 22V60Z", "#E9DEC7", 1.8)
        s += P("M30 60V30Q45 20 60 30V60Z", "#D2C3A2", 1.2)
        s += P("M4 60H86V63H4Z", STONE2, 1.2)
        for x0, sg in ((6, 1), (84, -1)):  # Bänke
            s += P(f"M{x0} 48h{sg * 18}v4h{-sg * 18}z M{x0} 54h{sg * 22}v4h{-sg * 22}z", WOOD, 1.1)
        s += P("M38 60L41 44H49L52 60Z", WOOD, 1.3) + P("M33 40H57L54 45H36Z", WOOD2, 1.2)
        s += tora(45, 30, .95)
        return s
    return None


def vogel(v):
    """Vorbild: fliegende Schwalbe/Spatz im Piktogramm – Flügel aus dem Leib heraus, eine Silhouette."""
    def bird(t, col="#8A6A4A", col2="#6E5236"):
        parts = ["M4.6 9.2Q8 7.4 12.4 8Q16.4 8.2 18.6 6.6Q20.6 5.6 21.8 6.8L23.4 7.4L21.8 8.2Q20.4 10.6 16 11.4Q11 12.2 7 10.8L2 12.4Q2.6 10.6 4.6 9.2Z",
                 "M10 8.6Q8.6 4 5.6 1.6Q9.8 1.8 13.6 4.6Q15.4 6 15.6 8.2Z"]
        g = sil(parts, col, 1.4)
        g += P("M11.6 10.4Q13 5.2 17.2 2.6Q18.4 6.8 16 10.6Z", col2, .8)
        g += F("M12.4 10.6Q16 10.6 19.4 9", "#F0E0C4") + C(20.4, 7.2, .5, INK, 0)
        g += P("M23.4 7.4L21.8 6.8L22 8.1Z", GOLD2, .4)
        return G(g, t)
    if v == 1:
        return bird("")
    if v == 2:  # drei Vögel am Himmel
        return bird("translate(1 .5) scale(.5)") + bird("translate(13.4 0) scale(.42)") + bird("translate(4 5.6) scale(.68)")
    return None


def samen(v):
    """Vorbild: Sämann-Geste – Hand von oben (haende.hand_gebend, wie 🫳) lässt Körner auf die Erde fallen."""
    if v not in (1, 2):
        return None
    hand = H.place(H.hand_gebend(), 3.4, 4.6, 8, .66)
    seeds = "".join(G(P("M0 -1.2Q.85 -.2 0 1.2Q-.85 -.2 0 -1.2Z", GOLD2, .4), f"translate({x} {y}) rotate({r})")
                    for x, y, r in [(14.4, 10.6, 20), (16.8, 11.6, -15), (12.8, 12.6, 30), (15.2, 13.8, 0), (17.8, 14.2, 25), (13, 15.4, -20)])
    soil = P("M1 21.4Q2 17.4 12 17.2Q22 17.4 23 21.4Z", "#8B5E3C", .9) + L("M4 19.6q3-1 6-.4M13 19.4q3-.6 6 .2", .5, "#6A4428")
    if v == 2:
        soil += L("M5.4 18v-2M5.4 16.6q-1.4-.6-1.8-1.8M5.4 16.4q1.2-.9 2.2-.9M9 18.2v-1.6M9 17q1-.8 1.8-.8", .7, LEAF)
    return soil + hand + seeds


def fessel(v):
    """Vorbild: gefesselte Hände (Piktogramm «verhaftet») – zwei Fäuste (haende.hand_faust), Handgelenke gekreuzt, Strick."""
    if v not in (1, 2):
        return None

    def arm(t):
        return G(P("M-2.6 0H2.6V10H-2.6Z", H.SKIN, 1) + P("M-3.4 9H3.4V20H-3.4Z", H.SLEEVE, 1), t)
    s = arm("translate(11 10) rotate(-30)") + arm("translate(19 10) rotate(30)")
    s += H.place(H.hand_faust(cuff_on=False), 19, 10, -60, .62) + H.place(H.hand_faust(cuff_on=False), 11, 10, 60, .62, True)
    rope, rope2 = "#C8A36A", "#8C6A38"
    for dy in (0, 2.6):
        s += P(f"M10.2 {14.4 + dy}Q15 {12.6 + dy} 19.8 {14.4 + dy}L19.8 {16.4 + dy}Q15 {14.6 + dy} 10.2 {16.4 + dy}Z", rope, .7)
        s += L(f"M12.6 {13.8 + dy}l.8 2M15 {13.5 + dy}v2M17.4 {13.8 + dy}l-.8 2", .45, rope2)
    if v == 1:
        s += P("M15 18.8Q16.6 22 14.6 25.4Q13.8 27.4 15.8 28.6", "none", 2.2) + L("M15 18.8Q16.6 22 14.6 25.4Q13.8 27.4 15.8 28.6", 1.2, rope)
    else:
        s += C(15, 19.4, 1.6, rope, .7)
        for d in ("M14.2 20.6Q12.4 24.6 13.4 28", "M15.8 20.6Q17.6 24.6 16.6 28"):
            s += P(d, "none", 2.2) + L(d, 1.2, rope)
    return s


def matte(v):
    """Vorbild: Schilf-/Strohmatte ausgebreitet in leichter Aufsicht, ein Ende eingerollt (Rolle von der Seite)."""
    straw, straw2 = "#E3C27A", "#C9A35A"
    if v == 1:
        s = P("M2.4 4.6L20 3.2L22.6 10.6L3.6 11.4Z", straw, 1)
        s += L("M5.4 4.4L6.6 11.2M8.6 4.1L9.8 11.1M11.8 3.9L13 10.9M15 3.6L16.2 10.8M18 3.4L19.4 10.7", .5, straw2)
        s += L("M2.9 6.8L20.8 5.6M3.2 9.1L21.7 8.2", .5, straw2)
        s += L("M2.4 5.6l-1.6-.4M2.6 7.4l-1.8 0M2.8 9.2l-1.8.2M3.2 10.8l-1.6.6", .6, straw2)
        s += P("M19.4 3.2Q24 1.2 28.6 2.4Q31.6 3.2 31.4 6.6Q31.4 10.4 28 10.8L22.6 10.6Z", straw, 1)
        s += P("M27.6 2.6Q31.4 3 31.4 6.6Q31.4 10.4 28 10.8Q24.6 10.6 24.6 6.6Q24.8 2.8 27.6 2.6Z", straw2, .9)
        s += L("M28 4.6Q29.6 4.8 29.6 6.6Q29.4 8.6 28 8.6Q26.6 8.4 26.8 6.6Q27 5.4 28.2 5.6Q28.8 6.2 28.2 7", .55)
        return s
    if v == 2:  # zusammengerollte Matte mit Schnur, darauf geflochtenes Muster (wird getragen)
        s = P("M3 3.6H27Q30.2 3.6 30.2 6.6Q30.2 9.6 27 9.6H3Z", straw, 1)
        s += L("M7 3.8v5.6M11 3.8v5.6M15 3.8v5.6M19 3.8v5.6M23 3.8v5.6", .5, straw2)
        s += E(3, 6.6, 2.2, 3, straw2, 1) + L("M3 4.8Q4.2 5.2 4 6.8Q3.6 8.2 2.6 7.8Q1.8 7 2.6 6.2", .5)
        s += P("M9 3.2h2v6.8H9zM21 3.2h2v6.8h-2z", "#8C6A38", .7)
        return s
    return None


def sandale(v):
    """Vorbild 👡/🩴 in Aufsicht: Sohle in Fussform (Ferse schmal, Ballen breit), Querriemen, Fersenriemen."""
    sole_c, top_c, strap = "#B9783F", "#E2B27A", "#5E3518"
    if v == 1:  # eine Sandale waagrecht, Zehen rechts
        s = P("M6.8 6.4C10 6.4 12 7.4 15 7.3C19 7.1 21 4.4 26 4.4C30.6 4.4 32.9 7 32.9 10C32.9 13 30.6 15.6 26 15.6C21 15.6 19 12.9 15 12.7C12 12.6 10 13.6 6.8 13.6A3.6 3.6 0 0 1 6.8 6.4Z", sole_c, 1.3)
        s += P("M7 8C10 8 12.4 8.8 15 8.8C19 8.6 21.4 6 26 6C29.6 6 31.3 8 31.3 10C31.3 12 29.6 14 26 14C21.4 14 19 11.4 15 11.2C12.4 11.2 10 12 7 12A2 2 0 0 1 7 8Z", top_c, .5)
        s += P("M22 3.4Q23.6 10 22 16.6L25 16.6Q26.6 10 25 3.4Z", strap, .8)
        s += P("M14 5.6Q15.4 10 14 14.4L16.8 14.4Q18.2 10 16.8 5.6Z", strap, .8)
        s += P("M5.4 5.8Q1.4 10 5.4 14.2L6.8 13Q4.2 10 6.8 7Z", strap, .8)
        s += P("M6.4 6.6Q10.4 6.8 14.2 6.6L14.2 8.2Q10.4 8.4 6.6 8.2Z M6.4 13.4Q10.4 13.2 14.2 13.4L14.2 11.8Q10.4 11.6 6.6 11.8Z", strap, .6)
        return s
    if v == 2:  # Paar senkrecht, Zehen oben
        def one(t):
            g = P("M5 1C8.2 1 9.4 3.4 9.4 6C9.4 8.6 8 10 7.8 12.2C7.6 14.4 8.4 15.6 8.2 17.2A3.2 3.2 0 0 1 1.8 17.2C1.6 15.6 2.4 14.4 2.2 12.2C2 10 .6 8.6 .6 6C.6 3.4 1.8 1 5 1Z", sole_c, 1)
            g += P("M5 2.4C7.4 2.4 8 4.2 8 6C8 8 6.8 9.6 6.6 12C6.4 14 7 15.4 6.8 16.8A1.8 1.8 0 0 1 3.2 16.8C3 15.4 3.6 14 3.4 12C3.2 9.6 2 8 2 6C2 4.2 2.6 2.4 5 2.4Z", top_c, .4)
            g += P("M-.2 5.6Q5 7 10.2 5.6L10.2 8Q5 9.4 -.2 8Z", strap, .7) + P("M1 10.8Q5 12 9 10.8L8.8 13Q5 14.2 1.2 13Z", strap, .7)
            g += P("M1.4 15.2Q5 16.4 8.6 15.2L8.6 16.8Q5 18 1.4 16.8Z", strap, .6)
            return G(g, t)
        return one("translate(6 .4)") + one("translate(18 .4)")
    return None


def leinenbinden(v):
    """Vorbild: Darstellungen des leeren Grabes (Joh 20,5-7) – helle gewickelte Binden (leer, eingesunken) und gefaltetes
    Schweisstuch auf einer Steinbank vor rauer Felswand; kein Bogen (wirkte wie ein Backofen)."""
    if v not in (1, 2):
        return None
    linen, sh = "#FBF8EF", "#AEB8BE"
    s = P("M2 32V8L8 4L16 6L24 2L34 5L44 2L52 6L58 4V32Z", "#8C8070", 1.3)
    s += L("M10 9l3 4M40 8l-2 5M50 11l2 3M22 9l1 3", .7, "#6F6456")
    if v == 2:
        s += P("M47 24V15Q47 10 52.5 10Q58 10 58 15V24Z", "#3E3428", .9)
    s += P("M3 24L6 21H54L57 24Z", "#D6CCB6", 1.1) + P("M3 24H57V31H3Z", STONE, 1.2)
    # Binden: lang gewickelt, gross, in der Mitte eingesunken (leer)
    s += P("M5 22.6Q4.6 14.6 11 14.2Q20 14.6 25 17Q30 14.6 36 14.2Q42 14.6 41.4 22.6Z", linen, 1)
    s += L("M9.4 14.6l2.4 7.8M13.6 14.4l2.2 8M17.8 15l2 7.4M22 16.2l1.4 6.2M26.4 16.2l-.2 6.4M30.6 15l-.8 7.4M34.8 14.4l-1.4 8M38.6 14.8l-1.6 7.6", .7, sh)
    s += P("M43.4 22.6L45.4 16.8H55L53 22.6Z", linen, 1) + L("M44.6 19.6H54M50.2 17L48.2 22.6", .6, sh)
    return s


def perle(v):
    """Vorbild: Perlenkette (Schmuck-Piktogramm) – grosse, schimmernde Perlen an einer Schnur, Anhänger-Perle."""
    pearl, ps = "#FBF7F2", "#D9CCD9"

    def pe(x, y, r):
        return (C(x, y, r, pearl, .7) + F(f"M{x - r * .15:.2f} {y + r * .98:.2f}A{r} {r} 0 0 0 {x + r * .98:.2f} {y + r * .15:.2f}A{r * 1.25:.2f} {r * 1.25:.2f} 0 0 1 {x - r * .15:.2f} {y + r * .98:.2f}Z", ps)
                + C(x - r * .35, y - r * .35, r * .3, "#FFFFFF", 0))
    if v == 1:  # Kette im Bogen, grosse Perle als Anhänger
        s = L("M4.6 2.4Q15 1.4 25.4 2.4", .7, "#9A8670") + P("M13.6 1.2h2.8v2.2h-2.8z", GOLD, .6)
        pts = [(4.4, 4.6), (5, 8), (6.8, 11), (9.6, 13.2), (20.4, 13.2), (23.2, 11), (25, 8), (25.6, 4.6)]
        s += L("M4.4 3Q3.6 15 15 14.2Q26.4 15 25.6 3", .7, "#9A8670")
        s += "".join(pe(x, y, 2) for x, y in pts) + pe(15, 14.4, 3)
        return s
    if v == 2:  # offene Auster mit grosser Perle, daneben Perlenschnur
        s = P("M1.6 9Q2.4 2.6 9 2.2Q15.6 2.6 16.4 9Q12 7.6 9 7.6Q6 7.6 1.6 9Z", "#A99C8C", .8)
        s += P("M1.4 10Q9 7 16.6 10Q15.6 16.6 9 16.8Q2.4 16.6 1.4 10Z", "#A99C8C", .9) + P("M3.4 10.6Q9 8.6 14.6 10.6Q13.6 14.8 9 15Q4.4 14.8 3.4 10.6Z", "#EBDDE6", .5)
        s += pe(9, 11.8, 2.8)
        s += "".join(pe(x, y, 1.6) for x, y in [(19, 14.6), (21, 11.8), (23.4, 9.4), (26, 7.4), (28.2, 5)])
        return s
    return None


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
    """Vorbild: Regenwurm-Piktogramm – rosa Ringsegmente, rundes Ende, ohne Auge, ragt halb aus einem Erdloch."""
    if v not in (1, 2):
        return None
    pink = "#D98A86"
    if v == 1:
        pts = curve([((7, 11), (6, 5), (10, 1.6), (13.6, 3.4)), ((13.6, 3.4), (16.4, 4.8), (17.6, 6.8), (20.2, 6.2))], 20)
    else:
        pts = curve([((7, 11), (6.6, 6), (9, 3), (12.6, 4.6)), ((12.6, 4.6), (15.6, 6.2), (17.4, 3.2), (20, 2.4))], 20)
    s = P("M.8 11.6Q2 8.8 12 8.6Q22 8.8 23.2 11.6Z", "#8B5E3C", .9) + E(7.4, 9.8, 3, 1, "#4E3420", .6)
    s += P(tube(pts, lambda t: 2.8), pink, .8)
    for i in range(3, len(pts) - 2, 3):
        x, y = pts[i]
        a, b = pts[i - 1], pts[i + 1]
        ang = math.degrees(math.atan2(b[1] - a[1], b[0] - a[0])) + 90
        s += G(L("M0 -1.2V1.2", .45, "#A85E5A"), f"translate({f1(x)} {f1(y)}) rotate({ang:.0f})")
    s += P("M4 10.4Q7.4 11.4 10.8 10.4Q10.4 11.6 7.4 11.8Q4.4 11.6 4 10.4Z", "#8B5E3C", .6)  # Erdrand vor dem Wurm
    return s


def grab_zu(v):
    """Vorbild: Felsengrab wie «Grab» (FIG-ORT-GRAB), aber der Rollstein deckt die Öffnung ganz; rotes Siegelband (Mt 27,66)."""
    if v not in (1, 2):
        return None
    s = P("M3 42V22Q3 4 26 3Q50 3 58 18Q62 26 61 42Z", "#A79A80", 1.6)
    s += L("M44 10q5 3 7 9M10 16q2-5 6-7", .8, "#8C8070")
    s += P("M14 42V28Q14 18 26 18Q38 18 38 28V42Z", "#3B3226", 1)
    s += C(27, 29, 14, "#C9BFAA", 1.6) + L("M19 22q7-4 14 1M18 33q3 4 8 5", .8, "#8C8070")
    if v == 1:
        s += L("M8 24L46 33", 1.4, RED) + C(9, 24.4, 2.4, RED, .7, DRED) + C(45, 32.8, 2.4, RED, .7, DRED)
    else:
        s += L("M9 30H45", 1.4, RED) + C(27, 30, 3.2, RED, .8, DRED) + L("M25.6 29.4q1.4 1.6 2.8 0", .6, DRED) \
            + C(9, 30, 1.8, RED, .6, DRED) + C(45, 30, 1.8, RED, .6, DRED)
    s += L("M1 42.6H63", 1.4, "#8C7A60")
    return s


# ------------------------------------------------------------------------------------------------ Landschaften 186 × 70

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
    """Vorbild: Flusspiktogramm in Perspektive (🏞️) – gewunden vom Vordergrund zum Horizont, Schilf, Ufer mit Kontur."""
    if v not in (1, 2):
        return None
    s = ground("M3 26Q24 14 46 20Q70 10 96 18Q124 8 150 18Q170 14 183 22", "#C9BC90")
    s += ground("M3 30Q50 22 93 25Q136 22 183 30", GREEN)
    s += P("M58 67Q70 54 102 48Q130 42 110 35Q94 30 104 26L110 25Q122 27 116 31Q132 38 140 43Q148 54 112 59Q96 63 104 67Z", WATER, 2)
    s += L("M76 61q8-4 16 0M106 51q6-3 12 0M112 32q3-2 6 0", 1.4, FOAM)
    reeds = [(36, 54), (44, 60), (152, 52), (160, 58), (96, 40)] if v == 1 else [(38, 56), (150, 54), (132, 34)]
    for x, y in reeds:
        s += L(f"M{x} {y}q-1-8 1-14M{x + 4} {y}q1-9-1-14M{x + 8} {y}q0-7 2-11", 1.6, GREEN3)
        s += E(x + 1, y - 14, 1.3, 3, "#8A6A3A", 0) + E(x + 3, y - 14, 1.3, 3, "#8A6A3A", 0)
    if v == 2:
        s += E(70, 56, 5, 2.6, STONE, 1.2) + E(146, 47, 4, 2.2, STONE, 1.2)
    return frame_land(s)


def feld(v):
    """Vorbild: Ackerpiktogramm (🏞️ mit Furchen) – gepflügte Furchen in Perspektive, dahinter reifes helles Korn
    («weiss zur Ernte»). Unterschied zu Kornfeld: Landschaft mit Furchen statt grosser Ähren vorn."""
    if v not in (1, 2):
        return None
    s = ground("M3 22Q30 14 60 18Q100 10 140 17Q166 14 183 20", GREEN2)
    s += ground("M3 26Q93 20 183 26", "#F1DFA0")
    s += L("M14 29l1-4M24 28l1-5M34 27l1-5M44 27l1-5M54 26l1-5M64 26l1-5M74 25l1-5M84 25l1-5M94 25l1-5M104 25l1-5M114 25l1-5M124 26l1-5M134 26l1-5M144 27l1-5M154 27l1-5M164 28l1-5M174 29l1-4", 1, "#C9A35A")
    s += ground("M3 34Q93 28 183 34", "#A8794A")
    for xb in (-120, -50, 10, 52, 93, 134, 176, 236, 306):  # Furchen zum Fluchtpunkt, an den Rahmenkanten enden
        sx = 93 + (xb - 93) * .15
        ex, ey = xb, 67.0
        if xb < 3 or xb > 183:
            edge = 3 if xb < 3 else 183
            t = (edge - sx) / (xb - sx)
            ex, ey = edge, 32 + t * 35
        s += L(f"M{sx:.1f} 32L{ex:.1f} {ey:.1f}", 1.4, "#7A5230")
    if v == 2:
        s += "".join(L(f"M{x} {y}v-4M{x} {y - 2}q-2-1-3-3M{x} {y - 2}q2-1 3-3", 1.2, LEAF) for x, y in [(60, 52), (93, 58), (126, 52), (76, 42), (110, 42)])
    s += L("M150 20v3", 1.4) + E(150, 16, 5, 4, LEAF, 1.2)
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
    """Vorbild 🌾 (Ährenbündel) vor goldenem Feld bis zur Horizontlinie, gerahmt wie 🏞️."""
    if v not in (1, 2):
        return None
    s = ground("M3 24Q30 16 60 20Q100 12 140 19Q166 16 183 22", GREEN2)
    s += ground("M3 28Q93 22 183 28", "#F3E3A6")
    s += L("M12 40q10-4 20 0t20 0 20 0 20 0 20 0 20 0 20 0 20 0M12 54q10-4 20 0t20 0 20 0 20 0 20 0 20 0 20 0 20 0", 1.2, "#C99A32")
    xs = [(52, -6), (72, -3), (93, 0), (114, 3), (134, 6)] if v == 1 else [(66, -6), (93, 0), (120, 6)]
    for i, (x, lean) in enumerate(xs):
        s += ahre(x, 66, 31 + (4 if i == len(xs) // 2 else 0), lean, "#E8B931" if i % 2 else "#D99A2B", 2.0 if v == 1 else 2.6)
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
    """Vorbild: Kundschafter-Traube (4 Mo 13,23; Emblem «Land, wo Milch und Honig fliesst») – grosse Traube vorn, sanfte Hügel."""
    if v not in (1, 2):
        return None
    s = ground("M3 24Q24 12 50 18Q76 8 102 16Q130 6 156 16Q172 12 183 18", GREEN2)
    s += ground("M3 34Q50 24 93 30Q136 24 183 32", GREEN)
    s += ground("M3 50Q60 42 110 48Q150 52 183 46", "#B9C97E")
    for x, y, r in ([(120, 34, 8), (150, 30, 9)] if v == 1 else [(112, 36, 7), (138, 32, 8), (164, 34, 7)]):
        s += L(f"M{x} {y + r * .6}v{r * .9:.1f}", 2, "#7A5A36") + E(x, y, r, r * .66, "#7F9A5E", 1.4)
    grape = "#6B3A6E"
    t = L("M40 8Q42 3 48 1", 2, "#6A4428") + P("M42 10Q30 2 24 10Q30 16 42 12Z", LEAF, 1.4)
    for x, y in [(36, 15), (46, 15), (56, 15), (31, 24), (41, 24), (51, 24), (61, 24), (36, 33), (46, 33), (56, 33), (41, 42), (51, 42), (46, 51)]:
        t += C(x, y, 5.4, grape, 1.3) + C(x - 1.6, y - 1.8, 1.4, "#A77AAA", 0)
    s += G(t, "translate(10 6) scale(.98)" if v == 1 else "translate(20 6) scale(.98)")
    return frame_land(s)


def ground(top, fill, sw=1.6):
    """Bodenfläche: obere Kante «top» (von x 3 bis x 183, beginnt mit M3 …), unten im Rahmen geschlossen."""
    return P(top + "L183 59Q183 67 175 67H11Q3 67 3 59Z", fill, sw)


SPEC = {  # Lexikon-ID: (Funktion, viewBox, Bedeutung kurz, gezeichnet je Fassung)
    "FIG-OBJ-BRIEF": (brief, "0 0 24 18", "Brief (an eine Gemeinde oder Person)", {1: "geschlossener Briefumschlag mit rotem Wachssiegel", 2: "beschriebenes Blatt mit Band und rotem Siegel"}),
    "FIG-ZEICHEN-SCHATZ": (schatz, "0 0 30 28", "Schatz / Lohn bei Gott", {1: "offene Schatztruhe mit Goldmünzen, rotem Edelstein, Schloss", 2: "offene Schatztruhe mit Goldmünzen, blauem Edelstein, Schloss"}),
    "FIG-ZEICHEN-SCHATZ-ERDE": (schatz_erde, "0 0 30 28", "Schatz auf der Erde (vergänglich: Motte und Rost zerstören ihn)", {1: "rostige, löchrige Truhe mit grosser Motte", 2: "offene rostige Truhe mit angelaufenen Münzen und Motte"}),
    "FIG-ZEICHEN-WEG": (weg, "0 0 30 20", "Weg / hingehen zu einem Ziel", {1: "Weg in Perspektive zum Horizont mit Fussspuren", 2: "geschwungener Weg zum Horizont mit Fussspuren und Sonne"}),
    "FIG-ORT-TEMPEL": (tempel, "0 0 200 150", "Tempel in Jerusalem", {1: "herodianischer Tempel: hoher Kubus, flaches Dach mit Goldspitzen, Portal mit Vorhang, Säulenhallen, Plattform", 2: "dasselbe mit breiter Treppe"}),
    "FIG-OBJ-MUENZEN": (muenzen, "0 0 24 14", "Münzen, Geld", {1: "Münzstapel und eine Münze mit Prägung", 2: "zwei Münzstapel und eine Münze mit Prägung"}),
    "FIG-OBJ-SCHWEIN": (schwein, "0 0 34 22", "Schwein (Herde)", {1: "Schwein von der Seite", 2: "drei Schweine einer Herde"}),
    "FIG-OBJ-BECHER-VOLL": (becher_voll, "0 0 12 14", "voller Becher (Wein)", {1: "goldener Kelch mit Rotwein", 2: "goldener Kelch randvoll mit Rotwein, Tropfen läuft über"}),
    "FIG-OBJ-BECHER-LEER": (becher_leer, "0 0 14 14", "leerer Becher", {1: "umgekippter goldener Kelch, innen leer", 2: "goldener Kelch, innen leer und hell"}),
    "FIG-ORT-SEE": (see, "0 0 186 70", "See (See von Galiläa)", {1: "ovaler See von Hügeln umgeben, Fischerboot mit Segel", 2: "ovaler See, Fischerboot und Fischer mit Netz"}),
    "FIG-ORT-FELD": (feld, "0 0 186 70", "Feld (Acker, Felder reif zur Ernte)", {1: "gepflügter Acker mit Furchen bis zum Horizont, dahinter helles reifes Korn", 2: "Acker mit Furchen und Keimlingen, dahinter reifes Korn"}),
    "FIG-OBJ-SPLITTER": (splitter, "0 0 32 18", "Splitter (im Auge des Bruders)", {1: "Auge mit Wimpern, Holzsplitter steckt darin, Träne", 2: "Auge mit Braue, Holzsplitter steckt darin, Träne"}),
    "FIG-OBJ-SALZ": (salz, "0 0 20 16", "Salz", {1: "Holzlöffel mit würfelförmigen Salzkristallen", 2: "Schale mit würfelförmigen Salzkristallen"}),
    "FIG-ORT-SYNAGOGE": (synagoge, "0 0 90 64", "Synagoge (Versammlungshaus)", {1: "Steinbau mit grosser Torarolle über dem Eingang", 2: "Innenraum: Torarolle auf Lesepult, Bänke beidseits"}),
    "FIG-ORT-JORDAN": (jordan, "0 0 186 70", "Jordan (Fluss)", {1: "gewundener Fluss zum Horizont, Schilf am Ufer", 2: "gewundener Fluss, Schilf, Steine am Ufer"}),
    "FIG-OBJ-VOGEL": (vogel, "0 0 24 16", "Vogel (Vögel des Himmels)", {1: "fliegender Vogel (Spatz/Schwalbe)", 2: "drei fliegende Vögel"}),
    "FIG-OBJ-SAMEN": (samen, "0 0 24 22", "Samen / Saat (säen)", {1: "Hand streut Körner auf Erde", 2: "Hand streut Körner auf Erde mit Keimlingen"}),
    "FIG-OBJ-FESSEL": (fessel, "0 0 30 30", "Fessel (Strick, gebunden)", {1: "zwei Fäuste, Handgelenke mit Strick gebunden", 2: "zwei Fäuste, Handgelenke mit Strick und Knoten gebunden"}),
    "FIG-OBJ-MATTE": (matte, "0 0 32 12", "Liegematte (eines Kranken)", {1: "ausgebreitete Strohmatte, ein Ende eingerollt", 2: "zusammengerollte Matte mit Schnüren"}),
    "FIG-OBJ-SANDALE": (sandale, "0 0 34 20", "Sandale (Riemen lösen)", {1: "Sandale von oben mit Querriemen und Fersenriemen", 2: "Sandale von oben mit Zehenriemen"}),
    "FIG-ORT-LAND": (land, "0 0 186 70", "Land (verheissenes Land)", {1: "grosse Weintraube vor sanften grünen Hügeln mit Ölbäumen", 2: "grosse Weintraube vor grünen Hügeln mit drei Ölbäumen"}),
    "FIG-ORT-MEER-OFFEN": (meer_offen, "0 0 186 70", "offenes Meer mit Wellen (Sturm)", {1: "drei grosse brechende Wellen", 2: "Wellenreihen mit Gischt"}),
    "FIG-ORT-WUESTE": (wueste, "0 0 186 70", "Wüste", {1: "Felsen, Sanddünen, Sonne, dürrer Busch", 2: "Felsen, Dünen, Sonne, Busch, Steine"}),
    "FIG-ORT-GRAB-VERSCHLOSSEN": (grab_zu, "0 0 64 44", "Grab (verschlossen, versiegelt)", {1: "Felsengrab, runder Stein verschliesst, rotes Siegelband", 2: "Felsengrab, Stein mit Siegelband und Siegel"}),
    "FIG-OBJ-LEINENBINDEN": (leinenbinden, "0 0 60 34", "Leinenbinden und Schweisstuch im leeren Grab", {1: "gewickelte Binden und gefaltetes Tuch auf Steinbank im Grab", 2: "aufgerollte Binden und gefaltetes Tuch auf Steinbank im Grab"}),
    "FIG-OBJ-PERLE": (perle, "0 0 30 18", "Perlen (kostbar)", {1: "Perlenkette", 2: "Muschel mit Perle und Perlenschnur"}),
    "FIG-OBJ-SCHLANGE": (schlange, "0 0 30 16", "Schlange", {1: "Schlange in S-Kurve mit Zunge", 2: "Schlange in S-Kurve mit Zunge"}),
    "FIG-OBJ-WURM": (wurm, "0 0 24 12", "Wurm", {1: "Regenwurm ragt aus der Erde", 2: "Regenwurm ragt aus der Erde"}),
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
