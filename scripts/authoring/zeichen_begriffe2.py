#!/usr/bin/env python3
"""Bildzeichen «Begriffe, Teil 2» neu gezeichnet (docs/SYMBOLPROZESS.md, Runde 11, 2026-10-25).

Zeichen, die die Gestaltungskritik nicht bestanden haben (Böses, Dämon, Sorge, Frieden, Friede, Wille Gottes, satt, Kind,
bitter, Gebot, Hoffnung, töricht, nicht verstehen, nicht richten, Rang, Vollmacht, Mammon, Sabbat, Hochzeit, gerecht,
verborgen, Vergebung, Stammbaum, Löserecht). Je Zeichen mehrere Fassungen (…@1, …@2, …); die geprüfte Wahl steht in WAHL.

    python3 scripts/authoring/zeichen_begriffe2.py --entwuerfe E.json [ID …]   # alle (oder diese) Fassungen als Entwürfe
    python3 scripts/authoring/zeichen_begriffe2.py --schreiben                 # gewählte Fassungen nach ueberarbeitet/begriffe2.json

Stil «Anime»: flache Flächen, Tinte #3B3226, Haut #E2AE80, Gold #E8B931; Gefühle als Emoji-Gesicht; Verneinung als roter
Kreis mit Schrägstrich über dem Motiv; Hände nur aus haende.py.
"""
import json
import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import haende as H  # noqa: E402

INK, SKIN, GOLD = "#3B3226", "#E2AE80", "#E8B931"
YEL, RED, GREEN, LEAF = "#F6D27A", "#C8323C", "#4E8A3A", "#6E9A3E"
WHITE, STONE, WOOD, SKY = "#FFFDF6", "#C9BFAA", "#9A6A3A", "#5DA7DB"


def P(d, fill="none", stroke=INK, sw=1.4, extra=""):
    st = f' stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"' if stroke else ""
    return f'<path d="{d}" fill="{fill}"{st}{extra}/>'


def C(cx, cy, r, fill, stroke=INK, sw=1.4):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<circle cx="{cx:g}" cy="{cy:g}" r="{r:g}" fill="{fill}"{st}/>'


def E(cx, cy, rx, ry, fill, stroke=INK, sw=1.4):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<ellipse cx="{cx:g}" cy="{cy:g}" rx="{rx:g}" ry="{ry:g}" fill="{fill}"{st}/>'


def thick(d, fill, w=4.4, ow=1.2):
    """Linie als Band mit Aussenkontur (Tinte breiter darunter)."""
    return P(d, "none", INK, w + 2 * ow) + P(d, "none", fill, w)


def verbot(cx, cy, r, w=2.4):
    """Einheitliche Verneinung: roter Kreis mit Schrägstrich über dem Motiv."""
    a = r * .7071
    return (f'<circle cx="{cx:g}" cy="{cy:g}" r="{r:g}" fill="none" stroke="{RED}" stroke-width="{w}"/>'
            + P(f"M{cx - a:.2f} {cy + a:.2f}L{cx + a:.2f} {cy - a:.2f}", "none", RED, w))


def sparkle(cx, cy, r, fill=GOLD):
    k = r * .28
    return P(f"M{cx} {cy - r}Q{cx + k} {cy - k} {cx + r} {cy}Q{cx + k} {cy + k} {cx} {cy + r}Q{cx - k} {cy + k} {cx - r} {cy}"
             f"Q{cx - k} {cy - k} {cx} {cy - r}Z", fill, "#B8891A", .7)


def person(cx, foot, s=1.0, body="#6E8EAE", hair="#3A2A1E", mood="smile", tilt=0, beard=None):
    """Standardfigur (Kopf, Haarkappe, Rumpf als Trapez) wie in der Bibliothek; Höhe etwa 23·s."""
    hr = 5.2 * s
    hy = foot - 17.6 * s
    top = foot - 12 * s
    w1, w2 = 3 * s, 7.4 * s
    g = (P(f"M{cx - w1:.2f} {top:.2f}Q{cx - w1 - 1.8 * s:.2f} {top:.2f} {cx - w1 - 3 * s:.2f} {top + 4.8 * s:.2f}L{cx - w2:.2f} {foot:.2f}"
           f"H{cx + w2:.2f}L{cx + w1 + 3 * s:.2f} {top + 4.8 * s:.2f}Q{cx + w1 + 1.8 * s:.2f} {top:.2f} {cx + w1:.2f} {top:.2f}Z", body, INK, 1.2)
         + C(cx, hy, hr, SKIN, INK, 1.2)
         + P(f"M{cx - hr:.2f} {hy - .2 * s:.2f}q0-{hr:.2f} {hr:.2f}-{hr:.2f}t{hr:.2f} {hr:.2f}q-{hr:.2f}-{hr / 2:.2f}-{2 * hr:.2f} 0z", hair, INK, .8))
    if beard:
        g += P(f"M{cx - hr * .9:.2f} {hy + .6 * s:.2f}Q{cx - hr * .6:.2f} {hy + hr * 1.7:.2f} {cx:.2f} {hy + hr * 1.75:.2f}"
               f"Q{cx + hr * .6:.2f} {hy + hr * 1.7:.2f} {cx + hr * .9:.2f} {hy + .6 * s:.2f}Q{cx:.2f} {hy + hr * .9:.2f} {cx - hr * .9:.2f} {hy + .6 * s:.2f}Z",
               beard, INK, .8)
    ex, ey = 1.95 * s, hy + .2 * s
    if mood == "happy":  # geschlossene, lachende Augen
        g += P(f"M{cx - ex - .9 * s:.2f} {ey + .3 * s:.2f}q{.9 * s:.2f}-{1.1 * s:.2f} {1.8 * s:.2f} 0M{cx + ex - .9 * s:.2f} {ey + .3 * s:.2f}q{.9 * s:.2f}-{1.1 * s:.2f} {1.8 * s:.2f} 0", "none", INK, .7)
    else:
        g += C(cx - ex, ey, .55 * s, INK, None) + C(cx + ex, ey, .55 * s, INK, None)
    if not beard:
        g += P(f"M{cx - 1.8 * s:.2f} {hy + 2.3 * s:.2f}q{1.8 * s:.2f} {2 * s:.2f} {3.6 * s:.2f} 0", "none", INK, .7)
    if tilt:
        g = f'<g transform="rotate({tilt} {cx:.2f} {foot:.2f})">{g}</g>'
    return g


def emoji(cx, cy, r, fill=YEL):
    return C(cx, cy, r, fill, INK, 1.6)


def trochoid(cx, cy, a, b, r, k, n=260, phase=0.0):
    pts = []
    for i in range(n + 1):
        t = 2 * math.pi * i / n
        pts.append((cx + a * math.cos(t) + r * math.cos(k * t + phase), cy + b * math.sin(t) + r * math.sin(k * t + phase)))
    return "M" + " ".join(f"{x:.2f} {y:.2f}" for x, y in pts) + "Z"


def scribble(cx, cy, a, b, r, k, turns=2.0, n=420, seed=0.0):
    """Verknäuelte Linie (eine einzige Linie, mehrfach um ein Oval mit Schlaufen, unregelmässig)."""
    pts = []
    for i in range(n + 1):
        t = 2 * math.pi * turns * i / n
        aa = a * (1 + .18 * math.sin(1.7 * t + seed))
        bb = b * (1 + .22 * math.cos(1.3 * t + seed))
        rr = r * (1 + .3 * math.sin(2.3 * t + seed))
        pts.append((cx + aa * math.cos(t) + rr * math.cos(k * t), cy + bb * math.sin(t) + rr * math.sin(k * t)))
    return "M" + " ".join(f"{x:.2f} {y:.2f}" for x, y in pts)


def tear(cx, cy, s=1.0, fill="#9CCBEB", stroke="#3B6E9E"):
    return P(f"M{cx} {cy - 3.2 * s}q{-1.9 * s} {2.8 * s} {-1.9 * s} {4.1 * s}a{1.9 * s} {1.9 * s} 0 0 0 {3.8 * s} 0q0-{1.3 * s}-{1.9 * s}-{4.1 * s}z",
             fill, stroke, .8)


def scale_drawing(cx, top, w=13, pan="#D9A441", tilt=0.0, pw=6.0):
    """Waage mit Ständer, Balken und an Schnüren hängenden Schalen (tilt: Neigung des Balkens in Grad)."""
    t = math.radians(tilt)
    lx, ly = cx - w * math.cos(t), top + 3 - w * math.sin(t)
    rx, ry = cx + w * math.cos(t), top + 3 + w * math.sin(t)
    g = P(f"M{cx} {top + 2}V{top + 24}", "none", INK, 2.2) + P(f"M{cx - 7} {top + 25}h14", "none", INK, 2.6)
    g += P(f"M{lx:.2f} {ly:.2f}L{rx:.2f} {ry:.2f}", "none", INK, 2)
    for x, y in ((lx, ly), (rx, ry)):
        g += P(f"M{x:.2f} {y:.2f}L{x - pw * .77:.2f} {y + 9:.2f}M{x:.2f} {y:.2f}L{x + pw * .77:.2f} {y + 9:.2f}", "none", INK, .9)
        g += P(f"M{x - pw:.2f} {y + 9:.2f}h{2 * pw:.2f}q-1.4 {pw * .73:.2f}-{pw:.2f} {pw * .73:.2f}t-{pw:.2f}-{pw * .73:.2f}z", pan, INK, 1.2)
    g += C(cx, top + 2, 2.2, pan, INK, 1)
    return g


def gavel(x, y, s=1.0, rot=-35):
    """Richterhammer (Kopf und Stiel)."""
    g = (thick("M0 0L13 0", WOOD, 2.4, 1) + f'<rect x="10" y="-5.2" width="5.6" height="10.4" rx="1.2" fill="#8A5A30" stroke="{INK}" stroke-width="1.2"/>'
         + f'<rect x="9.2" y="-5.6" width="7.2" height="2" rx=".6" fill="{GOLD}" stroke="{INK}" stroke-width=".8"/>'
         + f'<rect x="9.2" y="3.6" width="7.2" height="2" rx=".6" fill="{GOLD}" stroke="{INK}" stroke-width=".8"/>')
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">{g}</g>'


def cloud(x, y, s=1.0, fill=WHITE, stroke=INK):
    d = "M4 14q-4 0-4-3.6 0-3.4 3.6-3.6Q4.4 2.6 9 3q2-3 6-3 4.6 0 6 4 4.4-.4 5 3.4 3.6.4 3.6 3.6T26 14z"
    return f'<g transform="translate({x} {y}) scale({s})">{P(d, fill, stroke, 1.4 / s)}</g>'


# ---------------------------------------------------------------- Zeichen
Z = {}


def zeichen(fid):
    def deco(fn):
        Z[fid] = fn
        return fn
    return deco


@zeichen("FIG-ZEICHEN-BOESES")
def boeses():
    """Vorbild: die Schlange (1 Mo 3, Offb 12,9) als schwarze, geringelte Schlange mit roten Augen – keine Gestalt, kein Klecks."""
    body, dark = "#2E2A33", "#4A4452"
    # @1 geringelt, Kopf erhoben
    coil = ("M4 27.4Q4 31 16 31T28 27.4Q28 24 18.6 23.6 9 23.6 9 26.4 9 28.4 16.6 28.4 24 28.2 23 25.2"
            "Q22 22.6 18 21.6 13.6 20 14.6 15.4 15.6 11 20.4 9.6")
    s1 = (thick(coil, dark, 4.2, 1.2)
          + P("M19 6.6Q22.8 4.4 26.6 6.4Q28.6 7.8 27 9.8Q24.8 12 20.4 12.2Q17.6 11.8 17.8 9.4Q18 7.6 19 6.6Z", body, INK, 1.2)
          + P("M27.4 8.4l2.6-.4M30 8l1.4-1.2M30 8l1.2 1.2", "none", RED, 1)
          + C(23.6, 7.6, 1.2, "#F04A2E", None) + C(23.9, 7.4, .4, "#FFE08A", None)
          + P("M8 29.6q4 1 8 1M12 26.4q3 .8 6 .8", "none", "#6A6276", .6))
    # @2 S-förmig aufgerichtet
    s2 = (thick("M6 30.4Q2 30.4 4.4 27.6 8 24.4 15 25.6 23 27 25.6 23 27.4 19.6 21.6 17.4 13 14.4 15.6 9.6 17.4 7 20.6 6.6", dark, 4.4, 1.2)
          + P("M19.6 3.6Q23.8 1.6 27.8 3.6Q29.8 5 28.2 7Q26 9.2 21.4 9.4Q18.4 9 18.6 6.4Q18.8 4.6 19.6 3.6Z", body, INK, 1.2)
          + P("M28.6 5.6l2.4-.4M31 5.2l1.2-1.1M31 5.2l1.1 1.1", "none", RED, 1)
          + C(24.6, 4.8, 1.2, "#F04A2E", None) + C(24.9, 4.6, .4, "#FFE08A", None))
    return {"@1": ("0 0 32 32", s1, "Schwarze, am Boden geringelte Schlange mit erhobenem Kopf, roten Augen und gespaltener Zunge"),
            "@2": ("0 0 33 32", s2, "Schwarze, S-förmig aufgerichtete Schlange mit roten Augen und gespaltener Zunge")}


@zeichen("FIG-ZEICHEN-DAEMON")
def daemon():
    """Vorbild: 👻, aber dunkel, eckig-zerrissen, mit leuchtenden Augen; ohne Hörner (Satan) und ohne Wirbel (unreiner Geist)."""
    f = "#3E3A4A"
    body = ("M7 30.6L6.4 15Q6 4 16 3.4 26 4 25.6 15L25 30.6 22.6 27.4 20.4 31 18 27.2 16 31 13.8 27.2 11.4 31 9.4 27.4Z")
    arms = "M7 15.4L1.4 12.6 4 17.4 1.6 19.8 7.2 20.4M25 15.4L30.6 12.6 28 17.4 30.4 19.8 24.8 20.4"
    eyes = (P("M10 12.6L14.4 14.4 13.8 16.2Q11 16.2 10 12.6Z", "#F2E35A", "#C9B21E", .6)
            + P("M22 12.6L17.6 14.4 18.2 16.2Q21 16.2 22 12.6Z", "#F2E35A", "#C9B21E", .6))
    mouth = P("M11.6 21.2L13.4 19.8 14.8 21.4 16 19.8 17.2 21.4 18.6 19.8 20.4 21.2 16 23.2Z", "#1E1A22", "#1E1A22", .6)
    s1 = P(arms, f, INK, 1.3) + P(body, f, INK, 1.3) + eyes + mouth
    s2 = (P(body, f, INK, 1.3) + eyes + mouth
          + P("M3.4 22q1.6-2 3.4-1M28.6 22q-1.6-2-3.4-1M2.6 9q2 .6 3.8 2.4M29.4 9q-2 .6-3.8 2.4", "none", "#6A6276", 1.2))
    return {"@1": ("0 0 32 32", s1, "Dunkle Geistgestalt wie ein schwarzes Gespenst, unten und an den Armen zerrissen, leuchtend gelbe schräge Augen, gezackter Mund"),
            "@2": ("0 0 32 32", s2, "Dunkle Geistgestalt wie ein schwarzes Gespenst mit zerrissenem Saum, leuchtend gelbe schräge Augen, Wehlinien")}


@zeichen("FIG-ZEICHEN-SORGE")
def sorge():
    """Vorbild: 😟/😰 mit Schweisstropfen und einem verknäuelten Kritzel (eine einzige Linie) über dem Kopf."""
    face = (emoji(16, 22, 9.4)
            + P("M10.4 18.4Q12.2 16.6 14 17.2M21.6 18.4Q19.8 16.6 18 17.2", "none", INK, 1.3)
            + E(12.6, 20.6, 1, 1.3, INK, None) + E(19.4, 20.6, 1, 1.3, INK, None)
            + P("M11.8 27.2Q13.4 25.2 16 25.6T20.4 27", "none", INK, 1.4)
            + tear(24.4, 18.6, .9))
    knot1 = P(scribble(16, 6.2, 5.4, 2.6, 2.2, -4.6, 2.3, seed=.4), "none", INK, 1.1)
    knot2 = P(scribble(16, 6.0, 6.2, 3.0, 1.8, 6.4, 2.6, seed=1.1), "none", INK, 1.1)
    return {"@1": ("0 0 32 32", face + knot1, "Gelbes besorgtes Emoji-Gesicht mit hochgezogenen Brauen und Schweisstropfen, darüber ein verknäuelter Kritzel aus einer Linie"),
            "@2": ("0 0 32 32", face + knot2, "Gelbes besorgtes Emoji-Gesicht mit Schweisstropfen, darüber ein dichter Knäuel-Kritzel")}


@zeichen("FIG-ZEICHEN-FRIEDEN")
def frieden():
    """Vorbild: 🫂 (zwei Menschen umarmen sich): Seite an Seite, die Köpfe zueinander, je eine Hand auf der fernen Schulter des
    anderen – Arme hinter dem Rücken, kein Balken über den Körpern."""
    def pair(hands=True, twig=False):
        g = person(9.8, 31, 1.08, "#6E8EAE", "#3A2A1E", "happy", 0) + person(22.2, 31, 1.08, "#B0704A", "#5A3A22", "happy", 0)
        if hands:  # Hände auf der fernen Schulter des anderen (Arm verdeckt hinter dem Rücken)
            g += P("M27.4 19.4q1.8-.4 2.4 1.2t-1.2 2.2q-1.6.2-2.2-1", SKIN, INK, 1)
            g += P("M4.6 19.4q-1.8-.4-2.4 1.2t1.2 2.2q1.6.2 2.2-1", SKIN, INK, 1)
        if twig:
            g += P("M10 3.4Q16 1 22 3.4", "none", "#5B7A2E", 1) + E(13, 2.2, 1.8, .8, LEAF, INK, .5) + E(19, 2.2, 1.8, .8, LEAF, INK, .5)
        return g
    # @2 Umarmung im Profil: zwei Rümpfe überlappen, vordere Arme als Teil der Silhouette um den Rücken
    # Profil: zwei Menschen lehnen sich aneinander (Λ), Köpfe berühren sich, je eine Hand auf dem Rücken des anderen
    a = (P("M2.6 31L5.8 20.4Q7.8 16.2 12.6 16.6L16.4 18.6 16 31Z", "#6E8EAE", INK, 1.2)
         + P("M29.4 31L26.2 20.4Q24.2 16.2 19.4 16.6L15.6 18.6 16 31Z", "#B0704A", INK, 1.2)
         + C(11.8, 10.8, 4.9, SKIN, INK, 1.2) + C(20.2, 10.8, 4.9, SKIN, INK, 1.2)
         + P("M6.9 10.6q0-4.9 4.9-4.9 3.6 0 4.6 2.6-1.8-.6-3.2.4-3.4-.6-6.3 1.9z", "#3A2A1E", INK, .8)
         + P("M25.1 10.6q0-4.9-4.9-4.9-3.6 0-4.6 2.6 1.8-.6 3.2.4 3.4-.6 6.3 1.9z", "#5A3A22", INK, .8)
         + P("M11.4 11.2q.9-1 1.8 0M18.8 11.2q.9-1 1.8 0", "none", INK, .7)
         + P("M11.6 13.6q1.1.9 2.2 0M18.2 13.6q1.1.9 2.2 0", "none", INK, .6)
         + P("M5.2 21.4q-1.4-1.6.2-2.6 1.6-.8 2.6.6.6 1.4-.6 2.4-1.4.6-2.2-.4z", SKIN, INK, .9)
         + P("M26.8 21.4q1.4-1.6-.2-2.6-1.6-.8-2.6.6-.6 1.4.6 2.4 1.4.6 2.2-.4z", SKIN, INK, .9))
    return {"@1": ("0 0 32 32", pair(), "Zwei Menschen Seite an Seite, Köpfe zueinander geneigt, lächelnd mit geschlossenen Augen, je eine Hand auf der Schulter des anderen"),
            "@2": ("0 0 32 32", a, "Zwei Menschen lehnen sich aneinander und umarmen sich, Köpfe berühren sich, je eine Hand auf dem Rücken des anderen")}


@zeichen("FIG-ZEICHEN-FRIEDE")
def friede():
    """Vorbild: 🕊 Taube mit Ölzweig im Schnabel (1 Mo 8,11), ganz im Bild."""
    def leaf(x, y, rot, l=2.0):
        return f'<ellipse cx="{x}" cy="{y}" rx="{l}" ry="{l * .42:.2f}" transform="rotate({rot} {x} {y})" fill="{LEAF}" stroke="{INK}" stroke-width=".5"/>'
    back = P("M14.4 15.4Q15.4 7.4 21.6 4.2Q21.2 8.6 24 10.6Q23 14.4 18.4 15.8Z", "#DCE3EA", INK, 1.1)
    tail = P("M8.4 19.4L2.2 16.4Q.8 18 2.4 19.6 .4 21 2 22.8 1 24.6 3 25.2L8.8 22.6Z", WHITE, INK, 1.2)
    body = P("M4.6 20.6Q7 15.8 12.6 15.6L20.4 15.2Q23.2 12.8 26 13.4Q28.2 14 28.6 15.6L26.8 16.4Q25.6 21.2 18.8 22.6Q11.6 23.8 4.6 20.6Z", WHITE, INK, 1.3)
    wing = (P("M11.2 16.6Q9.6 8.4 14.2 2.6Q15.4 7.4 19.2 8.4Q21.8 9.4 21 12.6Q19.8 15.8 14.8 17Z", WHITE, INK, 1.3)
            + P("M13.4 9.6q1.6 1.4 4.2 1.4M13.2 12.8q2 1 4.6.8", "none", "#9AA8B8", .8))
    head = C(25.2, 14.6, .75, INK, None) + P("M28.4 14.6l2.4 1-2.2 1z", "#E8A33A", INK, .6)
    dove = back + tail + body + wing + head
    twig = (P("M29.4 16.2Q30.6 19.4 29 23.4", "none", "#5B7A2E", 1.1)
            + leaf(31.2, 18, -30) + leaf(28.2, 20, 30) + leaf(30.8, 22, -20) + C(28.6, 24.2, .9, "#5B7A2E", INK, .4))
    twig2 = (P("M29.6 16.2Q31.2 17.6 31.6 20.4", "none", "#5B7A2E", 1.1)
             + leaf(30.4, 15, -10, 1.7) + leaf(32.2, 18, 50, 1.7) + leaf(30.4, 19.2, 70, 1.6))
    return {"@1": ("0 0 33 26", dove + twig, "Weisse fliegende Taube mit erhobenem Flügel, im Schnabel ein grüner Ölzweig mit Blättern und Olive"),
            "@2": ("0 0 33 26", dove + twig2, "Weisse fliegende Taube, im Schnabel ein kleiner grüner Ölzweig")}


@zeichen("FIG-ZEICHEN-WILLE-GOTTES")
def wille():
    """Vorbild: Gleichung «wie im Himmel, so auf Erden» (Mt 6,10): oben Wolke, unten Erdkugel, beide mit demselben goldenen
    Zeichen; dazwischen ein goldener Lichtstrahl (kein Pfeil)."""
    earth = (P("M2 32Q2 20.4 16 20.4T30 32Z", SKY, INK, 1.4)
             + P("M6 26.6Q9 23.4 13 24.6 14.4 27.4 10.6 28.4 7.8 29.4 6 26.6ZM19 23.2Q24 22.6 26.6 26 24.4 28 21.4 26.6 18.4 25.6 19 23.2Z", "#7BAE5A", INK, .8))
    beam = P("M13.6 12.4L11.4 21.6H20.6L18.4 12.4Z", "#FBE7A0", None) + P("M13.6 12.4L11.4 21.6M18.4 12.4L20.6 21.6", "none", GOLD, .8)
    s1 = beam + earth + cloud(1.4, .2, 1.0) + sparkle(16, 7.6, 3.2) + sparkle(16, 27.4, 3.2)
    # @2 waagrecht: Wolke = Erde
    eq = (cloud(.4, 4, .62) + sparkle(9.6, 8.4, 2.4)
          + P("M20.6 7.4h4.8M20.6 10.4h4.8", "none", INK, 1.6)
          + C(36, 9.2, 7.2, SKY, INK, 1.4)
          + P("M31 6.6q3-2 5 0 .4 2.6-2.6 3-2.6 0-2.4-3zM37.4 11.4q3-1.6 4.4.6-1 2.6-3.4 2.2-1.6-.8-1-2.8z", "#7BAE5A", INK, .7)
          + sparkle(36, 9.2, 2.4))
    s2 = P(eq.replace("<", "<", 1), "none", None) if False else eq
    return {"@1": ("0 0 32 32", s1, "Oben eine weisse Wolke mit goldenem Stern, unten die Erde (Kugelausschnitt) mit demselben goldenen Stern, goldenes Licht verbindet beide"),
            "@2": ("0 0 44 18", s2, "Wolke mit goldenem Stern, Gleichheitszeichen, Erdkugel mit goldenem Stern")}


@zeichen("FIG-ZEICHEN-SATT")
def satt():
    """Vorbild: 😋 (zufrieden nach dem Essen) mit leerem Teller und Krümeln; Fassung 2: rundliche Figur, Hände auf dem vollen Bauch."""
    face = (emoji(16, 13.4, 10.4)
            + P("M10.6 11.4q1.6-1.8 3.2 0M18.2 11.4q1.6-1.8 3.2 0", "none", INK, 1.4)
            + P("M10.4 15.6Q16 21.6 21.6 15.6", "none", INK, 1.5)
            + P("M18.4 17.4q1.6 2.6 3.2.6", "#E8707A", INK, 1)
            + C(9.2, 15, 1.4, "#F09A8A", None) + C(22.8, 15, 1.4, "#F09A8A", None))
    plate = (E(16, 28.2, 13, 3.4, WHITE, INK, 1.4) + E(16, 27.6, 8, 1.8, "#EFE6D2", "#B9AD94", .7)
             + C(12.6, 27.6, .6, "#C99A62", None) + C(18.6, 27.2, .5, "#C99A62", None) + C(15.4, 28.2, .45, "#C99A62", None))
    s1 = face + plate
    # @2 Figur mit vollem Bauch
    fig = (P("M7 31.4Q4.4 23 9 19.6 12 17.6 16 17.6T23 19.6Q27.6 23 25 31.4Z", "#6E8EAE", INK, 1.3)
           + C(16, 10.6, 6.2, SKIN, INK, 1.2) + P("M9.8 10.4q0-6.2 6.2-6.2t6.2 6.2q-6.2-3.1-12.4 0z", "#3A2A1E", INK, .8)
           + P("M12.4 10.8q1-1.2 2 0M17.6 10.8q1-1.2 2 0", "none", INK, .8) + P("M13.4 13.4q2.6 2.4 5.2 0", "none", INK, .8)
           + C(12, 12.8, .9, "#F09A8A", None) + C(20, 12.8, .9, "#F09A8A", None)
           + P("M10.6 24.4q2.4-1.8 4.4.2-1.6 2.6-4.2 1.6-1-.6-.2-1.8zM21.4 24.4q-2.4-1.8-4.4.2 1.6 2.6 4.2 1.6 1-.6.2-1.8z", SKIN, INK, .9)
           )
    return {"@1": ("0 0 32 32", s1, "Gelbes zufriedenes Emoji-Gesicht mit geschlossenen Augen, Lächeln und Zungenspitze (😋), davor ein leerer Teller mit Krümeln")}


@zeichen("FIG-ZEICHEN-KIND")
def kind():
    """Vorbild: Leitsystem «Familie» (👨‍👧): Erwachsener und Kind Hand in Hand, gleichwertige Silhouetten, Kind auf Hüfthöhe."""
    def fig(cx, foot, s, body, hair, arm_to):
        g = person(cx, foot, s, body, hair)
        return g
    adult = person(10, 31.4, 1.2, "#6E8EAE", "#3A2A1E")
    child = person(24.4, 31.4, .74, "#E8B931", "#5A3A22")
    arms = (thick("M15.2 19.6Q17 24.6 19.2 24.4", "#6E8EAE", 2.2, 1) + thick("M20.6 22.8Q20 24 19.4 24.4", "#E8B931", 1.6, .9)
            + C(19.2, 24.6, 1.4, SKIN, INK, .9))
    s1 = adult + child + arms
    # @2 Kind mit Zöpfen, Hände höher
    child2 = person(24.6, 31.4, .74, "#D9534F", "#5A3A22") + C(20.4, 17.6, 1.2, "#5A3A22", INK, .7) + C(28.8, 17.6, 1.2, "#5A3A22", INK, .7)
    arms2 = (thick("M15.2 19.6Q16.6 23.6 19.4 23.8", "#6E8EAE", 2.2, 1) + thick("M20.8 22.6Q20.2 23.6 19.6 23.8", "#D9534F", 1.6, .9)
             + C(19.4, 24, 1.4, SKIN, INK, .9))
    return {"@1": ("0 0 32 32", s1, "Erwachsener (blau) und kleines Kind (gelb) stehen nebeneinander und halten sich an der Hand; Kind reicht bis zur Hüfte"),
            "@2": ("0 0 32 32", adult + child2 + arms2, "Erwachsener und kleines Mädchen mit Zöpfen Hand in Hand; Kind reicht bis zur Hüfte")}


@zeichen("FIG-ZEICHEN-BITTER")
def bitter():
    """Vorbild: 😖/😝 – zugekniffene Augen, Zunge heraus nach dem Trinken; daneben ein Becher mit dunklem Trank und Bitterkraut."""
    face = (emoji(13.4, 15, 10.6)
            + P("M7 11.4l3.4 1.8-3.4 1.6M19.8 11.4l-3.4 1.8 3.4 1.6", "none", INK, 1.4)
            + P("M8.4 19.6Q10 18.2 11.4 19.6T14.4 19.6 17.4 19.6 18.6 19.4", "none", INK, 1.4)
            + P("M12 20.2Q12.2 25 14.6 25 16.6 24.8 16.4 20.2", "#E8707A", INK, 1.1) + P("M14.2 20.8v2.6", "none", "#B84A54", .6))
    cup = (P("M30.4 22.6q2.8-.2 2.6 2.8-.2 2.4-3 2.6", "none", INK, 1.2)
           + P("M22.4 20.6h8.4l-1.2 9.6q-.2 1.2-1.4 1.2h-3.2q-1.2 0-1.4-1.2z", STONE, INK, 1.2)
           + P("M22.6 22.2h8l.1-1.6h-8.4z", "#4E6A2E", INK, .6)
           + P("M24.4 21.2q-1.6-3.4 1-5.4 2 2.6-.4 5.4z", LEAF, INK, .7) + P("M24.4 21.2q.2-2.6 1-5.4", "none", "#3E5A22", .5)
           + P("M27.4 18.6q1-1.6 0-3M29.6 18.2q1-1.6 0-3", "none", "#8A9A6A", .8))
    s1 = face + cup
    face2 = (emoji(12.4, 14, 10.6)
             + P("M6 10.4l3.4 1.8-3.4 1.6M18.8 10.4l-3.4 1.8 3.4 1.6", "none", INK, 1.4)
             + P("M7.4 18.8Q9 17.4 10.4 18.8T13.4 18.8 16.4 18.8", "none", INK, 1.4)
             + P("M10.4 19.2Q10.6 23.8 13 23.8 15 23.6 14.8 19.2", "#E8707A", INK, 1.1)
             + P("M24.4 6.4q2 1.2 1 3M27 5q2.2 1.8 1 4.4M3 4.6q1-1.8 3-1.6", "none", INK, .9))
    return {"@1": ("0 0 32 32", s1, "Gelbes Emoji-Gesicht mit zugekniffenen Augen (> <), welligem Mund und herausgestreckter Zunge, daneben ein Becher mit dunkelgrünem Trank und Kräuterzweig"),
            "@2": ("0 0 32 32", face2 + cup, "Gelbes Gesicht verzieht sich nach dem Trinken (Augen > <, Zunge heraus, Schüttellinien), daneben Becher mit Bitterkraut")}


@zeichen("FIG-ZEICHEN-GEBOT")
def gebot():
    """Vorbild: die beiden Tafeln mit römischen Ziffern (I–X), das verbreitete Piktogramm für die Zehn Gebote; mit Strahlen
    (von Gott gegeben) – unterscheidet sich so vom Gegenstand «Gesetzestafeln» (Tafeln mit Zeilen)."""
    def tablet(x, nums):
        g = P(f"M{x} 31V12.4Q{x} 5 {x + 6.4} 5T{x + 12.8} 12.4V31Z", "#D8D0BE", INK, 1.5)
        for i, t in enumerate(nums):
            g += f'<text x="{x + 6.4}" y="{14.4 + i * 5.2}" font-family="Georgia,serif" font-size="4.4" font-weight="bold" text-anchor="middle" fill="#5B4630">{t}</text>'
        return g
    tabs = tablet(2.4, ["I", "II", "III"]) + tablet(16.8, ["IV", "V", "VI"])
    rays = P("M16 1.6V3.6M9 2.4l.9 1.6M23 2.4l-.9 1.6M4 5.2l1.4 1.2M28 5.2l-1.4 1.2", "none", GOLD, 1.6)
    return {"@1": ("0 0 32 32", tabs, "Zwei Steintafeln mit runden Oberkanten nebeneinander, darauf römische Ziffern I–VI"),
            "@2": ("0 0 32 32", rays + tabs, "Zwei Steintafeln mit runden Oberkanten und römischen Ziffern, darüber goldene Strahlen")}


@zeichen("FIG-ZEICHEN-HOFFNUNG")
def hoffnung():
    """Vorbild: Jes 11,1 – Baumstumpf mit Jahrringen auf der Schnittfläche, Rinde, gespreizten Wurzeln und einem Spross, der
    seitlich aus dem Stumpf treibt."""
    bark = "#8A5E36"
    stump = (P("M3 31.4Q6 29.6 7.6 27.6 8 22 8.4 16.4H23.6Q24 22 24.4 27.6 26 29.6 29 31.4Z", bark, INK, 1.4)
             + P("M8.4 31.2Q10 29.6 10.6 28M23.6 31.2Q22 29.6 21.4 28M16 31.2V28.4", "none", INK, .9)
             + P("M11.4 19.4v6M15 19.6v7M19.6 19.4v6.6", "none", "#5E3E22", .8)
             + E(16, 16.4, 7.6, 2.8, "#E3C08A", INK, 1.4)
             + E(16, 16.4, 4.8, 1.7, "none", "#B88A50", .7) + E(16, 16.4, 2.2, .8, "none", "#B88A50", .7))
    sprout = (P("M22.4 21.6Q27.2 19.4 26.6 11.6", "none", "#4E7A2A", 1.8)
              + P("M26.6 13.6Q22.6 12.8 22 9.2 26 9.4 26.6 13.6Z", "#7DB04A", INK, .9)
              + P("M26.8 11.8Q28 7.6 31.4 6.8 31.4 10.8 26.8 11.8Z", "#7DB04A", INK, .9))
    ground = P("M1 31.6H31", "none", "#8A7A5A", 1.2)
    return {"@1": ("0 0 32 32", ground + stump + sprout, "Abgesägter Baumstumpf mit Jahrringen auf der Schnittfläche, Rinde und gespreizten Wurzeln; seitlich treibt ein grüner Spross mit zwei Blättern"),
            "@2": ("0 0 32 32", ground + stump + sprout.replace("M22.4 21.6", "M21.8 24.4"), "Baumstumpf mit Jahrringen und Wurzeln, ein grüner Spross wächst aus seiner Seite")}


@zeichen("FIG-ZEICHEN-TOERICHT")
def toericht():
    """Vorbild: Mt 7,26f – das Haus auf dem Sand stürzt ein (Gegenstück zu «Haus auf Sand gebaut», das steht); Fassung 2: 🤪."""
    house = ('<g transform="rotate(16 20 26)">'
             + P("M9 26V13.4H25V26Z", "#E9DDBF", INK, 1.4) + P("M7.4 13.6L17 5.6 26.6 13.6Z", "#B5553A", INK, 1.3)
             + P("M15 26v-6h4v6z", "#8A6A3A", INK, 1) + P("M20.4 15.6h3v2.6h-3z", INK, None)
             + P("M12.6 14.4l1.6 3.4-1.4 2.2 1.2 3", "none", INK, 1) + "</g>")
    sand = (P("M0 32V28.4Q8 25.6 16 27.2T32 26.4V32Z", "#EBCB8A", "#B49A5A", 1.2)
            + P("M0 32V29.6Q4 28.2 8 29.6T16 29.6 24 29.6 32 29.4V32Z", SKY, "#3B6E9E", .9)
            + P("M3.6 6.4q2-2 4 0t4 0M2 10.4q2-2 4 0", "none", "#3B6E9E", 1.1)
            + P("M28.6 25.4l1.6-1.4M5.6 26.2l-1.2-1.6", "none", INK, .9) + P("M27.4 27.4l2 .2 .4-1.6-1.8-.4z", "#C9BFAA", INK, .6))
    s1 = sand + house
    zany = (emoji(16, 16, 13)
            + C(11, 12.4, 2.6, WHITE, INK, 1.1) + C(11.6, 12.8, 1.2, INK, None)
            + C(21.6, 11.4, 1.6, WHITE, INK, 1.1) + C(21.4, 11.2, .7, INK, None)
            + P("M8.8 19Q16 26.6 23.6 18.6", "#7A2E2A", INK, 1.4)
            + P("M17.2 22.6Q18.4 27.6 21.4 26.6 23 25.6 21.6 21.4", "#E8707A", INK, 1)
            + P("M7.6 8.4l3.6-1.6M19 7.2l4.4 1", "none", INK, 1.2))
    return {"@1": ("0 0 32 32", s1, "Ein Haus auf Sand am Wasser kippt schräg und reisst, Risse im Haus, Wellen"),
            "@2": ("0 0 32 32", zany, "Gelbes albernes Emoji-Gesicht (🤪), ein Auge gross, ein Auge klein, Zunge seitlich heraus")}


@zeichen("FIG-ZEICHEN-NICHT-VERSTEHEN")
def nicht_verstehen():
    """Vorbild: 😕 + ❓ – verwirrtes Emoji-Gesicht mit grossem Fragezeichen neben dem Kopf (Gegenstück: verstehen = Häkchen)."""
    def qmark(x, y, s, col="#D9534F"):
        d = "M-3.4 -3Q-3.4 -7.4 0 -7.4T3.4 -3.6Q3.4 -1.2 .8 .2 0 .8 0 2.6"
        return (f'<g transform="translate({x} {y}) scale({s})">' + P(d, "none", INK, 4.2) + P(d, "none", col, 2.4)
                + C(0, 6.2, 1.9, col, INK, 1) + "</g>")
    face = (emoji(13, 19, 11.2)
            + P("M6.6 14.6q2-1.6 4 -.6M15.4 14q2.4-.4 3.8 1.6", "none", INK, 1.3)
            + E(9.4, 17.4, 1, 1.4, INK, None) + E(16.8, 17.8, 1, 1.4, INK, None)
            + P("M8.6 25.2q2.4-1.6 4.4-.4t4.4-.8", "none", INK, 1.4))
    s1 = face + qmark(26, 8.6, 1.0)
    s2 = face + qmark(26, 8.6, 1.0) + qmark(19.6, 3.6, .55, "#E87A5A").replace('translate(19.6 3.6)', 'translate(19.4 5.2) rotate(-18)')
    return {"@1": ("0 0 32 32", s1, "Gelbes verwirrtes Emoji-Gesicht (eine Braue hoch, Mund schief), daneben oben ein grosses rotes Fragezeichen"),
            "@2": ("0 0 32 32", s2, "Gelbes verwirrtes Emoji-Gesicht mit schiefem Mund, daneben ein grosses und ein kleines Fragezeichen")}


@zeichen("FIG-ZEICHEN-NICHT-RICHTEN")
def nicht_richten():
    """Vorbild: Richterhammer (⚖/🔨 «urteilen») und Waage, darüber das einheitliche Verbotsschild (roter Kreis, Schrägstrich)."""
    block = P("M7 25.4h18v3.6H7z", "#8A5A30", INK, 1.2)
    s1 = block + gavel(9.6, 21.4, 1.05, -38) + P("M22.6 13.4l2.6-1.6M24 17l3-.2M21 10.4l1-2.6", "none", INK, 1.1) + verbot(16, 16, 14.2, 2.6)
    s2 = scale_drawing(16, 4.4, 7.4, pw=4.4) + verbot(16, 16, 14.2, 2.6)
    s3 = scale_drawing(13, 4, 6.2, pw=3.8) + gavel(16.4, 24.6, .72, -30) + verbot(16, 16, 14.6, 2.6)
    return {"@1": ("0 0 32 32", s1, "Richterhammer schlägt auf einen Holzblock, darüber roter Verbotskreis mit Schrägstrich"),
            "@2": ("0 0 32 32", s2, "Waage mit hängenden Schalen, darüber roter Verbotskreis mit Schrägstrich"),
            "@3": ("0 0 32 32", s3, "Waage und Richterhammer, darüber roter Verbotskreis mit Schrägstrich")}


@zeichen("FIG-ZEICHEN-RANG")
def rang():
    """Vorbild: Siegerpodest (🥇-Treppchen) mit einer Figur auf dem höchsten Platz; Fassung 2: Ehrenstuhl am Kopf der Tafel."""
    pod = (P("M1 31.6V23.4H10.6V31.6ZM21.4 31.6V25.8H31V31.6Z", "#C9BFAA", INK, 1.3)
           + P("M10.6 31.6V17.6H21.4V31.6Z", GOLD, INK, 1.4)
           + f'<text x="16" y="27.6" font-family="sans-serif" font-size="7" font-weight="bold" text-anchor="middle" fill="#7A5A12">1</text>')
    fig = person(16, 17.6, .7, "#B5553A", "#3A2A1E", "happy")
    crown = P("M12.6 4.4l1 -2.6 1.2 1.6 1.2-2.4 1.2 2.4 1.2-1.6 1 2.6z", GOLD, INK, .7)
    s1 = pod + fig + crown.replace("M12.6 4.4", "M12.6 5.4").replace("l1 -2.6", "l1 -2.6")
    # @2 Tafel mit Ehrenstuhl
    tab = (P("M2 21.4h22v2.4H2z", WOOD, INK, 1.2) + P("M4 23.8v7.6M22 23.8v7.6", "none", INK, 1.6)
           + P("M4 19.6h3.6v1.8H4zM10.4 19.6h3.6v1.8h-3.6zM16.8 19.6h3.6v1.8h-3.6z", STONE, INK, .7)
           + P("M24.8 31.4V20.4H30.4V31.4M24.8 25.4h5.6", "none", INK, 1.4)
           + P("M25 25.2V6.4Q27.6 3.6 30.2 6.4V25.2Z", GOLD, INK, 1.4) + sparkle(27.6, 10.6, 2))
    return {"@1": ("0 0 32 32", s1, "Siegerpodest mit drei Stufen, auf der höchsten goldenen Stufe (mit «1») steht eine Figur mit kleiner Krone"),
            "@2": ("0 0 32 32", tab, "Lange Tafel, am Tischende ein hoher goldener Ehrenstuhl mit Funkeln")}


@zeichen("FIG-ZEICHEN-VOLLMACHT")
def vollmacht():
    """Vorbild: Zepter als Herrschaftszeichen, zusammen mit einer gesiegelten Urkunde (Vollmacht = Recht zu handeln)."""
    scep = (thick("M8 30.6L22.4 8.6", GOLD, 2.6, 1.1)
            + C(23.8, 6.4, 4, GOLD, INK, 1.3) + P("M20.6 4.4l1.6-3 1.6 2 1.6-2 1.4 3", GOLD, INK, .9)
            + C(23.8, 6.4, 1.6, "#C8323C", INK, .7)
            + P("M18.6 13.4l3.4 2.2M17.4 15.4l3.4 2.2", "none", INK, 1.6)
            + P("M8.6 29.6l-1.6 2.2", "none", INK, 2.2))
    doc = (P("M2 10.6h12.4v15.6H2z", "#F4F1EA", INK, 1.2) + P("M4.4 14h7.6M4.4 17h7.6M4.4 20h5", "none", "#5B4630", 1)
           + C(11.4, 24.2, 2.6, "#C8323C", "#7A1E22", .8) + P("M10 26.4l-.8 3.2 2.2-1.4 2.2 1.4-.8-3.2", "#C8323C", "#7A1E22", .6))
    s1 = doc + scep
    # @2 Zepter allein, gross, mit Strahlen
    s2 = ('<g transform="translate(-2 1)">' + thick("M8 30.6L22.4 8.6", GOLD, 3, 1.1) + C(23.8, 6.4, 4.4, GOLD, INK, 1.3)
          + P("M20.4 4.2l1.6-3.2 1.8 2.2 1.8-2.2 1.6 3.2", GOLD, INK, .9) + C(23.8, 6.4, 1.8, "#C8323C", INK, .7)
          + P("M18.4 13.6l3.6 2.4M17.2 15.6l3.6 2.4", "none", INK, 1.6) + "</g>"
          + P("M29 4.4l2.6-1.2M29.6 9l2.8.4M27 13l2 1.8M15.6 3.6l-2.4-1.4", "none", GOLD, 1.5))
    return {"@1": ("0 0 32 32", s1, "Goldenes Zepter mit verziertem Kopf (Krönchen, roter Stein) schräg vor einer Urkunde mit rotem Siegel"),
            "@2": ("0 0 32 32", s2, "Grosses goldenes Zepter mit verziertem Kopf (Krönchen, roter Stein), Strahlen")}


@zeichen("FIG-ZEICHEN-MAMMON")
def mammon():
    """Vorbild: «Geld als Herr» – Geldsack mit grosser Krone auf einem Sockel, eine kleine Figur verneigt sich davor (Mt 6,24)."""
    ped = P("M14 31.6V25.4H31V31.6Z", STONE, INK, 1.3) + P("M13 25.4h19", "none", INK, 1.6)
    bag = (P("M18.4 13.6Q14.4 17.6 15 21.4 15.6 25.2 22.6 25.2 29.6 25.2 30.2 21.4 30.8 17.6 26.8 13.6Z", "#C9A15A", INK, 1.3)
           + P("M18.2 13.6Q22.6 15 27 13.6L25.6 11.4H19.6Z", "#A6803A", INK, 1)
           + C(22.6, 20.2, 3, GOLD, INK, 1) + C(22.6, 20.2, 1.7, "none", "#B8891A", .7)
           + P("M16.6 11.2L17.2 3.6 19.8 7 22.6 2.4 25.4 7 28 3.6 28.6 11.2Z", GOLD, INK, 1.1)
           + C(22.6, 8.4, .9, "#C8323C", None))
    bow = (P("M2.6 31.6Q2.6 26 5.6 24.6L10.6 22.6Q12.4 22.4 12.2 24.4L8.6 27 9.6 31.6Z", "#6E8EAE", INK, 1.2)
           + C(11.4, 20.4, 2.8, SKIN, INK, 1.1) + P("M8.8 19.8q.6-3 3.4-2.4 2 .6 2 2.6-2.6-1.8-5.4-.2z", "#3A2A1E", INK, .6))
    s1 = ped + bag + bow
    s2 = ped + bag + P("M3 31.6V24.4q2.6-3.8 8.4-1.8L12.4 31.6z", "#6E8EAE", INK, 1.2) + C(12.6, 21.6, 2.8, SKIN, INK, 1.1) + \
        P("M9.8 21.4q.2-3 2.8-3 2.8 0 3 2.4-2.8-1.4-5.8.6z", "#3A2A1E", INK, .6)
    return {"@1": ("0 0 32 32", s1, "Geldsack mit Goldmünze und grosser goldener Krone auf einem Steinsockel, davor verneigt sich eine kleine Figur tief"),
            "@2": ("0 0 32 32", s2, "Gekrönter Geldsack auf Sockel, davor kniet eine kleine Figur")}


@zeichen("FIG-ZEICHEN-SABBAT")
def sabbat():
    """Vorbild: Wochenstreifen (Kalender) mit sieben Feldern; das siebte gross, golden, mit zwei Sabbatkerzen."""
    cells = "".join(P(f"M{1 + i * 4.6} 14.4h3.8v6.4h-3.8z", "#D8D0BE", INK, .9) for i in range(6))
    seventh = P("M29 9.4h11v15.2H29z", GOLD, INK, 1.4)
    candles = ""
    for x in (32.4, 36.6):
        candles += (P(f"M{x - 1} 16h2v6.4h-2z", WHITE, INK, .8)
                    + P(f"M{x} 11.4q-1.4 1.8-1.2 3 .2 1.2 1.2 1.2t1.2-1.2q.2-1.2-1.2-3z", "#F08A2A", "#B8501A", .5))
    base = P("M30.6 22.4h7.8", "none", INK, 1.2)
    s1 = cells + seventh + candles + base
    # @2 Kalenderblatt mit sieben Spalten, letzte golden mit Kerzen darüber
    cal = (P("M1 8.6h30v20H1z", WHITE, INK, 1.4) + P("M1 8.6h30v4.2H1z", "#B5553A", INK, 1.4)
           + "".join(P(f"M{1.8 + i * 4.2} 14.4h3.4v12.6h-3.4z", "#E6DECB", None) for i in range(6))
           + P("M27 13.4h3.4v14.6H27z", GOLD, INK, .9))
    cand2 = ""
    for x in (26.6, 30.8):
        cand2 += P(f"M{x - .9} 2.8h1.8v5.8h-1.8z", WHITE, INK, .7) + P(f"M{x} -.8q-1.2 1.6-1 2.6.2 1 1 1t1-1q.2-1-1-2.6z", "#F08A2A", "#B8501A", .4)
    return {"@1": ("0 8 41 18", s1, "Streifen aus sechs kleinen grauen Feldern und einem grossen goldenen siebten Feld mit zwei brennenden Kerzen"),
            "@2": ("0 -2 32 32", cal + cand2, "Wochenkalender mit sieben Spalten, die letzte golden, darüber zwei brennende Kerzen")}


@zeichen("FIG-ZEICHEN-HOCHZEIT")
def hochzeit():
    """Vorbild: 🥂 (zwei Becher stossen an) mit Weinkrug (Kana, Joh 2); Fassung 2: Paar unter dem Hochzeitsbaldachin (💒/Chuppa)."""
    def goblet(rot, cx):
        g = (P("M-5 -9h10q0 7-5 8-5-1-5-8z", "#F2D78A", INK, 1.2) + P("M-4.6 -6.4h9.2q-.6 4.6-4.6 5.2-4-.6-4.6-5.2z", "#9A2A4A", None)
             + P("M0 -1v7M-3.6 6.4h7.2", "none", INK, 1.6))
        return f'<g transform="translate({cx} 20) rotate({rot})">{g}</g>'
    clink = goblet(18, 10.4) + goblet(-18, 21.6) + sparkle(16, 6.6, 3.4) + P("M10.6 4.6l-2-1.6M21.4 4.6l2-1.6M16 1.2v-1", "none", GOLD, 1.2)
    jar = (P("M27.4 31.6h6.4l.6-5q.4-2.4-1.4-3.4l.6-1.4h-4.6l.6 1.4q-1.8 1-1.4 3.4z", "#C98A5A", INK, 1)
           + P("M27.6 27h6.4", "none", "#8A5A30", .8))
    s1 = clink
    s3 = '<g transform="translate(-1 0)">' + clink + "</g>" + jar
    # @2 Paar unter Baldachin
    can = (P("M2 31.6V9M30 31.6V9", "none", WOOD, 2) + P("M.6 9.6Q16 1 31.4 9.6Q24 12.6 16 10.4 8 12.6 .6 9.6Z", WHITE, INK, 1.3)
           + C(8, 10.6, 1.4, "#E86A8A", INK, .5) + C(16, 10.4, 1.4, "#E86A8A", INK, .5) + C(24, 10.6, 1.4, "#E86A8A", INK, .5)
           + person(11, 31.6, .78, "#3E4E6E", "#3A2A1E", "happy") + person(21, 31.6, .78, WHITE, "#7A4A22", "happy")
           + P("M16.4 17.4q4.6-2.4 9.2 0l1.4 7.6h-12z", "#F4F1EA", INK, .7).replace("M16.4", "M16.4") )
    return {"@1": ("0 0 32 32", s1, "Zwei goldene Becher mit Rotwein stossen an, goldener Funke darüber"),
            "@2": ("0 0 32 32", can, "Brautpaar (Mann dunkel, Frau weiss) unter einem Baldachin mit Blumen"),
            "@3": ("0 0 35 32", s3, "Zwei Becher mit Wein stossen an, daneben ein Weinkrug")}


@zeichen("FIG-ZEICHEN-GERECHT")
def gerecht():
    """Vorbild: dieselbe Waage wie «Gericht», hier im Gleichgewicht mit hängenden Schalen, dazu ein grünes Häkchen in eigenem Kreis."""
    check = C(27.6, 26.6, 4.6, GREEN, INK, 1.2) + P("M25.2 26.6l1.8 1.8 3.2-3.6", "none", WHITE, 1.6)
    s1 = scale_drawing(15.4, 2.4, 9.6, pw=5.2) + check
    s2 = scale_drawing(16, 2.4, 11.6) + C(16, 13.6, 0, "none", None) + P("M11.4 8.2l2.2 2.2 4-4.6", "none", GREEN, 0)
    s2 = scale_drawing(16, 6.4, 9.6, pw=5.2) + C(16, 3.2, 3.4, GREEN, INK, 1.1) + P("M14.4 3.2l1.2 1.3 2.2-2.6", "none", WHITE, 1.3)
    return {"@1": ("0 0 32 32", s1, "Waage im Gleichgewicht mit an Schnüren hängenden goldenen Schalen, rechts unten ein grünes Häkchen im Kreis"),
            "@2": ("0 0 32 32", s2, "Waage im Gleichgewicht, oben auf dem Ständer ein grüner Kreis mit Häkchen")}


@zeichen("FIG-ZEICHEN-VERBORGEN")
def verborgen():
    """Vorbild: «geh in deine Kammer, schliess die Tür … dein Vater sieht ins Verborgene» (Mt 6,6): geschlossene Tür mit
    Schlüsselloch, darüber ein Auge."""
    door = (P("M7 31.6V14Q7 7.4 16 7.4T25 14V31.6Z", "#9A6A3A", INK, 1.5)
            + P("M11.4 31.6V14.6M16 31.6V8M20.6 31.6V14.6", "none", "#6E4A26", .9)
            + C(16, 21.4, 1.5, INK, None) + P("M15.2 21.6l-.6 3.4h2.8l-.6-3.4z", INK, None)
            + P("M4 31.6h24", "none", INK, 1.6))
    eye = (P("M8.6 3.8Q16 -2.6 23.4 3.8 16 10.2 8.6 3.8Z", WHITE, INK, 1.2) + C(16, 3.8, 2.4, "#5E7FA8", INK, .8) + C(16, 3.8, 1, INK, None))
    s1 = '<g transform="translate(0 2)">' + door + "</g>" + eye
    wall = P("M1 33.6V12H31V33.6Z", "#E9DDBF", INK, 1.4) + P("M1 12L16 2 31 12", "none", "none", 0)
    s2 = ('<g transform="translate(0 2)">' + P("M2 31.6V12.6H30V31.6Z", "#E9DDBF", INK, 1.4) + door + "</g>"
          + eye + P("M6 5.6l-2.2-.8M26 5.6l2.2-.8M8.2 0l-1.6-1.4M23.8 0l1.6-1.4", "none", GOLD, 1.2))
    return {"@1": ("0 -2 32 36", s1, "Geschlossene Holztür mit Schlüsselloch, darüber ein offenes Auge"),
            "@2": ("0 -2 32 36", s2, "Geschlossene Holztür mit Schlüsselloch in einer Wand, darüber ein Auge mit goldenen Strahlen")}


@zeichen("FIG-ZEICHEN-VERGEBUNG")
def vergebung():
    """Vorbild: «Wenn eure Sünde blutrot ist, soll sie schneeweiss werden» (Jes 1,18; 1 Joh 1,7.9): Wasser fällt auf ein Tuch,
    der dunkle Fleck verschwindet, die gewaschene Hälfte glänzt. Nicht der zerrissene Schuldschein (das ist «vergeben»)."""
    cloth = P("M3 14.4Q9 12.6 16 14.4T29 14.4L28 30.4Q22 28.8 16 30.4T4 30.4Z", WHITE, INK, 1.4)
    stain = P("M5.6 19.6Q6 16.6 9.4 17.2 12.6 16.4 13.2 19.4 15 21.4 13 24 11.6 27.2 8.6 26 5 26.4 5.2 23.4 4 21.6 5.6 19.6Z", "#5A2E3A", None)
    fade = P("M17 20.6Q19.6 18.6 21.6 20.4", "none", "#C9A6AE", 1, ' stroke-dasharray="1.4 1.6"')
    drops = tear(9, 5.6, .9) + tear(14.6, 3.6, .9) + tear(20.4, 6, .9) + tear(25.6, 4, .9)
    shine = sparkle(23.4, 22.4, 3.6) + sparkle(18.4, 26.4, 1.8)
    s1 = drops + cloth + stain + shine
    # @2 Kreuz mit Licht, darunter verblassender Fleck
    cross = P("M14 2h4v8h8v4h-8v18h-4V14H6v-4h8z", "#B07E44", INK, 1.4)
    s2 = (P("M16 12m-12 0a12 12 0 1 0 24 0a12 12 0 1 0-24 0", "#FBE7A0", None) + cross
          + P("M4.6 28.6Q6 25.6 9 26.4 11.6 25.6 11.6 28.2 11.6 30.8 8.4 30.6 4.4 31 4.6 28.6Z", "#5A2E3A", None)
          + P("M20.6 28.6Q22 26.4 24.6 27 27 26.4 27.4 28.4 27.4 30.6 24.4 30.4 20.4 30.8 20.6 28.6Z", "none", "#C9A6AE", .9, ' stroke-dasharray="1.2 1.4"')
          + sparkle(27, 22.4, 2.4))
    return {"@1": ("0 0 32 32", s1, "Wassertropfen fallen auf ein weisses Tuch: links noch ein dunkler Fleck, rechts ist es sauber und glänzt (goldenes Funkeln)"),
            "@2": ("0 0 32 32", s2, "Holzkreuz vor hellem Licht, unten links ein dunkler Fleck, rechts nur noch gestrichelt mit Funkeln")}


@zeichen("FIG-ZEICHEN-STAMMBAUM")
def stammbaum():
    """Vorbild: Stammbaum als Baum mit Köpfen in Medaillons (Generationenfolge von unten nach oben; Rut 4,18–22)."""
    def head(cx, cy, r, hair, beard=None):
        g = C(cx, cy, r + 1.4, "#F4ECD8", INK, 1.1) + C(cx, cy, r, SKIN, INK, .9)
        g += P(f"M{cx - r:.2f} {cy - .1:.2f}q0-{r:.2f} {r:.2f}-{r:.2f}t{r:.2f} {r:.2f}q-{r:.2f}-{r / 2:.2f}-{2 * r:.2f} 0z", hair, INK, .6)
        if beard:
            g += P(f"M{cx - r * .85:.2f} {cy + .4:.2f}Q{cx:.2f} {cy + r * 1.9:.2f} {cx + r * .85:.2f} {cy + .4:.2f}Q{cx:.2f} {cy + r * .8:.2f} {cx - r * .85:.2f} {cy + .4:.2f}Z", beard, INK, .5)
        g += C(cx - r * .38, cy + .1, .42, INK, None) + C(cx + r * .38, cy + .1, .42, INK, None)
        return g
    trunk = (P("M13.6 31.6Q15 24 15 18 13 13 7.6 10.6M15.6 21.4Q17.4 16 24.4 12.6M15.4 16Q16 9 16 5", "none", INK, 4.2)
             + P("M13.6 31.6Q15 24 15 18 13 13 7.6 10.6M15.6 21.4Q17.4 16 24.4 12.6M15.4 16Q16 9 16 5", "none", "#8A5E36", 2.4)
             + P("M10 31.6h12", "none", INK, 1.4)
             + E(11.2, 15.4, 1.8, .9, LEAF, INK, .5) + E(20.6, 19, 1.8, .9, LEAF, INK, .5) + E(19.4, 9.4, 1.6, .8, LEAF, INK, .5))
    s1 = trunk + head(16, 5.2, 3.6, "#3A2A1E") + head(7, 11.6, 3.6, "#8A8A8A", "#E6E2DA") + head(25, 13.2, 3.6, "#5A3A22", "#5A3A22")
    # @2 senkrechte Kette: Grossvater → Vater → Sohn
    chain = (P("M16 9.8V12.6M16 21V23.6", "none", INK, 1.6)
             + head(16, 5.4, 3.8, "#8A8A8A", "#E6E2DA") + head(16, 16.6, 3.8, "#5A3A22", "#5A3A22") + head(16, 27.4, 3.2, "#3A2A1E")
             + P("M7 5.4q-3 5.6 0 11.2M7 16.6q-3 5.4 0 10.8", "none", LEAF, 1.6) + P("M5.6 15.6l1.4 1-1.6.8M5.6 26.4l1.4 1-1.6.8", "none", LEAF, 1.2))
    return {"@1": ("0 0 32 32", s1, "Kleiner Baum mit braunem Stamm und drei Ästen, an den Astenden drei Köpfe in runden Medaillons (alter Mann mit weissem Bart, Mann mit Bart, junger Mann)"),
            "@2": ("0 0 32 32", chain, "Drei Köpfe senkrecht übereinander, mit Strichen verbunden: oben alter Mann mit weissem Bart, Mitte Mann mit Bart, unten junger Mann")}


@zeichen("FIG-ZEICHEN-LOESERECHT")
def loeserecht():
    """Vorbild: Rut 4,7 – zur Bestätigung eines Lösekaufs zog einer seine Sandale aus und gab sie dem anderen. Eine Hand gibt die
    Sandale von oben in eine offene Hand; dahinter der Acker mit Furchen und kleinem Haus (Land und Familie)."""
    field = (P("M2 21.4L8 14.6H30L34 21.4Z", "#B07E44", INK, 1.2)
             + P("M6 19.6L10 15.8M11 20L14 15.8M16.4 20.2L18 15.8M22 20.2L22 15.8M27.4 20.2L26 15.8M32 20L30 15.8", "none", "#7A5430", .9)
             + P("M24.4 14.6V9.6L27.6 6.8 30.8 9.6V14.6Z", "#E9DDBF", INK, 1) + P("M23.8 10l3.8-3.6 3.8 3.6", "none", "#B5553A", 1.4)
             + P("M26.8 14.6v-2.6h1.6v2.6z", "#8A6A3A", None))
    sandal = ('<g transform="translate(4.8 4.2) rotate(-6 17 9) scale(.7)">'
              + P("M2.4 13.4Q2.6 17 5.4 17.6H28Q32.8 17.2 33 14.4V12.6Q31 15 27 15H5.4Q2.6 15 2.4 12.6z", "#6E4A26", INK, 1.2)
              + P("M2.4 12.6Q1.6 9.4 5.6 9.4 12 10 18 9 26 7.6 31 9.6 34 11 33 12.6 31 15 27 15H5.4Q2.6 15 2.4 12.6z", "#B07E44", INK, 1.2)
              + thick("M14 13.2Q15.6 5.2 21 5.8 25.6 6.6 28.4 11.8", "#8A5E36", 1.4, .9)
              + thick("M4.6 13Q3.8 6.4 8.8 5.8 12.2 5.6 13.4 12.8", "#8A5E36", 1.4, .9) + "</g>")
    give = f'<g transform="translate(16 0) scale(.62)">{H.hand_gebend("#7E5A8E")}</g>'
    take = f'<g transform="translate(0 14.6) scale(.64)">{H.hand_empfangend("#5E7FA8")}</g>'
    s1 = '<g transform="translate(13.6 17.6) scale(.64)">' + field + "</g>" + take + sandal + give
    # @2 Sandale gross vor dem Acker, Rückkaufpfeil um Haus
    s2 = (field.replace("M2 21.4L8 14.6H30L34 21.4Z", "M2 21.4L8 14.6H30L34 21.4Z")
          + P("M20 4.4Q27.6 .4 33 6", "none", GOLD, 0)
          + '<g transform="translate(1 17) scale(.72)">'
          + P("M2.4 13.4Q2.6 17 5.4 17.6H28Q32.8 17.2 33 14.4V12.6Q31 15 27 15H5.4Q2.6 15 2.4 12.6z", "#6E4A26", INK, 1.2)
          + P("M2.4 12.6Q1.6 9.4 5.6 9.4 12 10 18 9 26 7.6 31 9.6 34 11 33 12.6 31 15 27 15H5.4Q2.6 15 2.4 12.6z", "#B07E44", INK, 1.2)
          + thick("M14 13.2Q15.6 5.2 21 5.8 25.6 6.6 28.4 11.8", "#8A5E36", 1.4, .9)
          + thick("M4.6 13Q3.8 6.4 8.8 5.8 12.2 5.6 13.4 12.8", "#8A5E36", 1.4, .9) + "</g>"
          + H.muenze(5, 9.6, 2.4) + H.muenze(10, 8, 2.4))
    arrow = (P("M30.6 10.6A13.4 9 0 1 0 31.6 22.4", "none", INK, 3.6) + P("M30.6 10.6A13.4 9 0 1 0 31.6 22.4", "none", GOLD, 2)
             + P("M27.2 22.2L33.4 21.4 32.4 27.4Z", GOLD, INK, 1))
    sandal3 = sandal.replace('translate(4.8 4.2) rotate(-6 17 9) scale(.7)', 'translate(1.4 22) scale(.5)')
    s3 = '<g transform="translate(1 4.4) scale(.86)">' + field + "</g>" + arrow + sandal3
    return {"@3": ("0 0 35 33", s3, "Gepflügter Acker mit kleinem Haus, von einem goldenen Rückkehr-Pfeil umfasst; vorn eine Sandale"),
            "@1": ("0 0 35 33", s1, "Eine Hand von oben reicht eine Sandale in eine offene Hand darunter; dahinter ein gepflügter Acker mit kleinem Haus"),
            "@2": ("0 0 35 33", s2, "Sandale vor einem gepflügten Acker mit kleinem Haus, daneben zwei Münzen")}


# ---------------------------------------------------------------- Runde 2 (nach der Gestaltungskritik der Fassungen @1–@3)
Z2 = {}


def runde2(fid):
    def deco(fn):
        Z2[fid] = fn
        return fn
    return deco


def kneel(x, g, body="#6E8EAE", hair="#3A2A1E", bow=False):
    """Kniende Figur im Profil, Blick nach rechts (x = Rücken, g = Boden); bow: tief verneigt."""
    if bow:  # 🙇 im Profil: Beine gefaltet am Boden, Rumpf schräg nach vorn, Arme zum Boden, Kopf tief
        return (thick(f"M{x + 1.4} {g - 1.8}H{x + 8.4}", body, 3.2, 1.1)
                + thick(f"M{x + 2} {g - 3.6}L{x + 9.6} {g - 8}", body, 4.8, 1.1)
                + thick(f"M{x + 9.4} {g - 7.4}L{x + 13.8} {g - 1.8}", body, 2.2, 1)
                + E(x + 14.8, g - 1.4, 1.5, .9, SKIN, INK, .8)
                + C(x + 13, g - 9.6, 2.9, SKIN, INK, 1.1)
                + P(f"M{x + 10.4} {g - 10.6}q1-2.8 3.6-2.2 2 .6 1.8 2.6-2.6-1.8-5.4-.4z", hair, INK, .6))
    b = P(f"M{x} {g}H{x + 10}Q{x + 10.6} {g - 3} {x + 7.6} {g - 3.6}L{x + 7.4} {g - 11.6}Q{x + 6.6} {g - 14} {x + 3.6} {g - 14}"
          f"Q{x + .2} {g - 14} {x - .4} {g - 10}Q{x - 1} {g - 3} {x} {g}Z", body, INK, 1.2)
    h = C(x + 4.6, g - 18, 3.4, SKIN, INK, 1.1) + P(f"M{x + 1.2} {g - 18.2}q0-3.4 3.4-3.4 3 0 3.4 2.4-2-1.2-3.4-.4-.6 1.6-3.4 1.4z", hair, INK, .6)
    return b + h


@runde2("FIG-ZEICHEN-BOESES")
def boeses2():
    body = "#2E2A33"
    aura = P("M15 2.4L18.4 5.6 22.6 1.4 24.4 6.4 30 5 28.6 10 32.4 13.4 27.4 15.6 29 20.6 23.6 19.8 22.4 25 18.8 21 14.6 24.6"
             " 14 19.4 9 20.6 11 15.6 6.4 12.8 11.6 10.4 9.6 5.4 14.4 7.2Z", "#7A2E3A", None)
    snake = (thick("M5.4 30.6Q1.6 30.4 4 27.8 7.6 24.6 14.6 25.8 22.4 27.2 24.8 23.4 26.2 20.2 21.2 18.4 14 16 16.2 11.8 17.8 9.6 20 9", "#4A4452", 3.8, 1.2)
             + P("M3 31.2Q1 31 2 29.6", "none", INK, 1.4)
             + P("M19.4 6.4Q23.4 4.2 27.4 6.2Q29.4 7.6 27.8 9.6Q25.6 11.8 21 12Q18 11.6 18.2 9Q18.4 7.2 19.4 6.4Z", body, INK, 1.2)
             + P("M22.2 6.6l3.8 1.4", "none", "#F04A2E", 1.2) + C(24.4, 8.4, 1, "#F04A2E", None)
             + P("M23 11.6l.4 1.6.6-1.6M25.4 11.2l.3 1.4.6-1.5", WHITE, INK, .4)
             + P("M28.2 8.2l2.4-.4M30.6 7.8l1.2-1.1M30.6 7.8l1.1 1.1", "none", RED, 1))
    snake2 = snake.replace(P("M22.2 6.6l3.8 1.4", "none", "#F04A2E", 1.2), P("M21.6 6.4l4.6 1.8", "none", INK, 1.4))
    return {"@4": ("0 0 33 32", aura + snake, "Schwarze aufgerichtete Schlange mit böse zusammengezogener roter Braue, rotem Auge, Giftzähnen und gespaltener Zunge vor einem dunkelroten Zackenschein"),
            "@5": ("0 0 33 32", snake2, "Schwarze aufgerichtete Schlange mit böse gesenkter Braue, rotem Auge, Giftzähnen und gespaltener Zunge")}


@runde2("FIG-ZEICHEN-SORGE")
def sorge2():
    def face(cx=16, cy=17.6, r=12):
        return (emoji(cx, cy, r)
                + P(f"M{cx - 7.6} {cy - 5}Q{cx - 5.4} {cy - 7.6} {cx - 2.6} {cy - 6.8}M{cx + 7.6} {cy - 5}Q{cx + 5.4} {cy - 7.6} {cx + 2.6} {cy - 6.8}", "none", INK, 1.4)
                + E(cx - 4, cy - 2, 1.1, 1.5, INK, None) + E(cx + 4, cy - 2, 1.1, 1.5, INK, None)
                + P(f"M{cx - 5} {cy + 6.6}Q{cx - 3} {cy + 3.6} {cx} {cy + 4.4}T{cx + 5} {cy + 6.2}", "none", INK, 1.5))
    # @4 😰: blaue Stirn (flach), Schweisstropfen am Rand
    cx, cy, r = 16, 17.6, 12
    blue = P(f"M{cx - 11.4} {cy - 3.6}A{r} {r} 0 0 1 {cx + 11.4} {cy - 3.6}Q{cx} {cy - 7.4} {cx - 11.4} {cy - 3.6}Z", "#9CC0E6", None)
    s4 = (emoji(cx, cy, r) + blue + C(cx, cy, r, "none", INK, 1.6)
          + P(f"M{cx - 7.6} {cy - 4}Q{cx - 5.4} {cy - 6.6} {cx - 2.6} {cy - 5.8}M{cx + 7.6} {cy - 4}Q{cx + 5.4} {cy - 6.6} {cx + 2.6} {cy - 5.8}", "none", INK, 1.4)
          + E(cx - 4, cy - 1, 1.1, 1.5, INK, None) + E(cx + 4, cy - 1, 1.1, 1.5, INK, None)
          + P(f"M{cx - 5} {cy + 7}Q{cx - 3} {cy + 4} {cx} {cy + 4.8}T{cx + 5} {cy + 6.6}", "none", INK, 1.5)
          + tear(cx + 12.6, cy - 4.6, 1.15))
    knot = P(scribble(16, 3.4, 4.2, 1.7, 1.3, -4.4, 1.6, seed=.8), "none", INK, .9)
    s5 = face(16, 19.4, 11.4) + knot + tear(28.4, 15.6, 1.1)
    return {"@4": ("0 0 32 32", s4, "Gelbes besorgtes Emoji-Gesicht (😰): Stirn blau, hochgezogene Brauen, zittriger Mund, Schweisstropfen an der Schläfe"),
            "@5": ("0 0 32 32", s5, "Gelbes besorgtes Emoji-Gesicht mit hochgezogenen Brauen und Schweisstropfen, darüber ein kleiner feiner Kritzel-Knäuel")}


@runde2("FIG-ZEICHEN-FRIEDEN")
def frieden2():
    """🫂 ohne Knubbelhände: eine gemeinsame Silhouette, Köpfe aneinander gelehnt; Fassung 5 mit Ölzweig darüber."""
    bodies = (P("M2.4 31.4L4.6 22Q6 17.6 10.4 17.4H16V31.4Z", "#6E8EAE", INK, 1.3)
              + P("M29.6 31.4L27.4 22Q26 17.6 21.6 17.4H16V31.4Z", "#B0704A", INK, 1.3)
              + P("M16 18.6V31", "none", INK, .7))
    arms = (P("M16 22.4Q22 21.8 26.6 19.4L27.6 22.6Q22 25.4 16 25.6Z", "#6E8EAE", None)
            + P("M16 22.4Q22 21.8 26.6 19.4M27.6 22.6Q22 25.4 16 25.6", "none", INK, .9))
    heads = (person(11.6, 31.4, 1.1, "#6E8EAE", "#3A2A1E", "happy", 9).split('<circle', 1)[0] and "")
    def head(cx, cy, hair, tilt):
        g = (C(cx, cy, 5.6, SKIN, INK, 1.2)
             + P(f"M{cx - 5.6} {cy - .2}q0-5.6 5.6-5.6t5.6 5.6q-5.6-2.8-11.2 0z", hair, INK, .8)
             + P(f"M{cx - 3.1} {cy + .6}q.9-1.1 1.8 0M{cx + 1.3} {cy + .6}q.9-1.1 1.8 0", "none", INK, .8)
             + P(f"M{cx - 1.6} {cy + 2.6}q1.6 1.6 3.2 0", "none", INK, .7)
             + C(cx - 3.4, cy + 2.2, .8, "#F09A8A", None) + C(cx + 3.4, cy + 2.2, .8, "#F09A8A", None))
        return f'<g transform="rotate({tilt} {cx} {cy + 5})">{g}</g>'
    hh = head(11.4, 11.4, "#3A2A1E", 14) + head(20.6, 11.4, "#5A3A22", -14)
    twig = (P("M10.6 3Q16 .6 21.4 3", "none", "#5B7A2E", 1) + E(12.8, 1.8, 1.8, .75, LEAF, INK, .5) + E(16.4, 1.2, 1.8, .75, LEAF, INK, .5)
            + E(19.8, 1.8, 1.8, .75, LEAF, INK, .5))
    s4 = bodies + hh
    return {"@4": ("0 0 32 32", s4, "Zwei Menschen ganz nah beieinander, Schultern aneinander, Köpfe zueinander geneigt, lächelnd mit geschlossenen Augen"),
            "@5": ("0 0 32 32", twig + bodies + hh, "Zwei Menschen ganz nah beieinander, Köpfe zueinander geneigt, lächelnd, darüber ein kleiner Ölzweig")}


@runde2("FIG-ZEICHEN-FRIEDE")
def friede2():
    def leaf(x, y, rot, l=2.3):
        return f'<ellipse cx="{x}" cy="{y}" rx="{l}" ry="{l * .42:.2f}" transform="rotate({rot} {x} {y})" fill="{LEAF}" stroke="{INK}" stroke-width=".55"/>'
    tail = P("M9.4 19.2Q3.4 16.2 1.4 18.4Q.2 21.2 1.4 24.2Q3.8 25.8 9.6 22.6Z", WHITE, INK, 1.3) + P("M3 21.2l5 .4M3.4 23.4l4.8-.8", "none", "#9AA8B8", .8)
    body = P("M6.4 21Q8.4 16 13.6 15.6L20.4 15.2Q23.2 12.8 26 13.4Q28.2 14 28.6 15.6L26.8 16.4Q25.6 21.2 18.8 22.6Q12 23.8 6.4 21Z", WHITE, INK, 1.4)
    wing = (P("M11.6 16.8Q10.4 8.4 15.4 2.4Q16.4 7.2 20 8.2Q22.6 9.2 21.8 12.6Q20.6 15.8 15.4 17.2Z", WHITE, INK, 1.4)
            + P("M14 9.8q1.6 1.4 4.2 1.4M13.8 13q2 1 4.6.8", "none", "#9AA8B8", .9))
    head = C(25.2, 14.6, .8, INK, None) + P("M28.4 14.6l2.4 1-2.2 1z", "#E8A33A", INK, .6)
    twig = (P("M29.4 16.2Q31 19.6 29.2 24.4", "none", "#5B7A2E", 1.3)
            + leaf(31.6, 18.2, -30) + leaf(28, 20.4, 30) + leaf(31.2, 22.6, -20) + C(28.8, 25.2, 1.1, "#5B7A2E", INK, .5))
    s4 = tail + body + wing + head + twig
    return {"@4": ("0 0 33 27", s4, "Weisse fliegende Taube mit erhobenem Flügel und rundem Schwanz, im Schnabel ein grüner Ölzweig mit drei Blättern und Olive")}


@runde2("FIG-ZEICHEN-WILLE-GOTTES")
def wille2():
    """Mt 6,10 «Dein Wille geschehe»: Fassung 4 – eine Schriftrolle (Gottes Weisung) entrollt sich aus der Wolke bis auf die Erde;
    Fassung 5 – ein Mensch kniet unter der Wolke im goldenen Licht (Hingabe an Gottes Willen)."""
    earth = (P("M2 32Q2 22.4 16 22.4T30 32Z", SKY, INK, 1.4)
             + P("M5.6 28.6Q8.6 25.4 12.6 26.4 13.6 28.8 10.4 29.6 7.4 30.6 5.6 28.6ZM19.6 25.2Q24 24.6 26.4 27.6 24.4 29.4 21.6 28.2 18.8 27.4 19.6 25.2Z", "#7BAE5A", INK, .8))
    scroll = (P("M11 8.8H21V22.6Q16 24.6 11 22.6Z", "#F4ECD8", INK, 1.2)
              + P("M13.2 12h5.6M13.2 14.6h5.6M13.2 17.2h5.6M13.2 19.8h3.6", "none", "#8A6A3A", .9)
              + E(16, 23.4, 5.6, 1.4, "#E3D3AE", INK, 1))
    s4 = earth + scroll + cloud(1.4, .6, 1.0) + sparkle(16, 7, 2.6)
    light = P("M10.6 11.6L4 29.4H28L21.4 11.6Z", "#FBE7A0", None)
    ground = P("M1 30.4H31", "none", "#8A7A5A", 1.4)
    s5 = light + ground + cloud(1.4, .4, 1.0) + sparkle(16, 7, 2.6) + kneel(10.6, 30.2, "#6E8EAE", "#3A2A1E", True)
    return {"@4": ("0 0 32 32", s4, "Aus einer weissen Wolke mit goldenem Stern entrollt sich eine beschriebene Schriftrolle bis hinunter auf die Erde"),
            "@5": ("0 0 32 32", s5, "Unter einer Wolke mit goldenem Stern kniet ein Mensch tief verneigt im goldenen Lichtkegel")}


@runde2("FIG-ZEICHEN-SATT")
def satt2():
    """😮‍💨 + leerer Teller mit abgelegtem Löffel: genug gegessen (nicht «lecker»)."""
    face = (emoji(13, 13, 10.6)
            + P("M7.6 11q1.6 1.4 3.2 0M15.2 11q1.6 1.4 3.2 0", "none", INK, 1.4)
            + C(13, 17.6, 1.6, "#7A2E2A", INK, 1)
            + C(7.4, 15.4, 2.6, "#F4B0A0", None) + C(18.6, 15.4, 2.6, "#F4B0A0", None)
            + P("M24.6 15.6q2.4-.6 3.6.8-1.2 1.6-3.2 1.2M25.4 18.6q2.6 0 4 1.6", "none", "#9AA8B8", 1.2))
    plate = (E(16, 28.4, 13.6, 3.2, WHITE, INK, 1.4) + E(16, 27.9, 8.6, 1.7, "#EFE6D2", "#B9AD94", .7)
             + C(12, 27.8, .7, "#C99A62", None) + C(18.6, 27.4, .6, "#C99A62", None)
             + thick("M21.6 26.6L29.6 23.8", "#B9B4A8", .9, .7) + E(20.4, 27, 1.8, 1.1, "#B9B4A8", INK, .8))
    s4 = face + plate
    face5 = (emoji(16, 12.6, 10.6)
             + P("M10.6 11.4q1.6-1.8 3.2 0M18.2 11.4q1.6-1.8 3.2 0", "none", INK, 1.4)
             + P("M12.4 16.4q3.6 2.6 7.2 0", "none", INK, 1.4)
             + C(9.4, 15.2, 2, "#F4B0A0", None) + C(22.6, 15.2, 2, "#F4B0A0", None))
    return {"@4": ("0 0 32 32", s4, "Gelbes Emoji-Gesicht mit geschlossenen Augen und runden Pausbacken, das ausatmet (😮‍💨, genug gegessen), darunter ein leerer Teller mit Krümeln und abgelegtem Löffel"),
            "@5": ("0 0 32 32", face5 + plate, "Gelbes zufriedenes Gesicht mit geschlossenen Augen und Pausbacken, darunter ein leerer Teller mit Krümeln und abgelegtem Löffel")}


@runde2("FIG-ZEICHEN-KIND")
def kind2():
    """Kind als Hauptmotiv: Kinderproportionen (grosser Kopf, kurzer Körper) neben den Beinen eines Erwachsenen (Grössenmass,
    angeschnitten); Fassung 5: zwei Kinder."""
    def child(cx, foot, body, hair, pig=False, s=1.0):
        hr = 5.6 * s
        hy = foot - 15.6 * s
        g = (P(f"M{cx - 2.4 * s} {foot - 9 * s}Q{cx - 5.4 * s} {foot - 8.6 * s} {cx - 5.8 * s} {foot - 1.6 * s}H{cx + 5.8 * s}Q{cx + 5.4 * s} {foot - 8.6 * s} {cx + 2.4 * s} {foot - 9 * s}Z", body, INK, 1.2)
             + P(f"M{cx - 2.2 * s} {foot - 1.8 * s}v{1.6 * s}M{cx + 2.2 * s} {foot - 1.8 * s}v{1.6 * s}", "none", INK, 2 * s))
        if pig:
            g += C(cx - hr - .6 * s, hy + .6 * s, 1.6 * s, hair, INK, .8) + C(cx + hr + .6 * s, hy + .6 * s, 1.6 * s, hair, INK, .8)
        g += (C(cx, hy, hr, SKIN, INK, 1.2)
              + P(f"M{cx - hr:.2f} {hy - .4 * s:.2f}q0-{hr:.2f} {hr:.2f}-{hr:.2f}t{hr:.2f} {hr:.2f}q-{hr * .7:.2f}-{hr * .9:.2f}-{hr:.2f}-{hr * .3:.2f}q-{hr * .3:.2f} {hr * .6:.2f}-{hr:.2f} {hr * .3:.2f}z", hair, INK, .8)
              + C(cx - 2.1 * s, hy + .8 * s, .75 * s, INK, None) + C(cx + 2.1 * s, hy + .8 * s, .75 * s, INK, None)
              + C(cx - 3.4 * s, hy + 2.6 * s, 1 * s, "#F09A8A", None) + C(cx + 3.4 * s, hy + 2.6 * s, 1 * s, "#F09A8A", None)
              + P(f"M{cx - 1.6 * s} {hy + 2.8 * s}q{1.6 * s} {1.8 * s} {3.2 * s} 0", "none", INK, .8))
        return g
    legs = (P("M2 4.4H11.6L12.2 30.4H8.4L7 12.6 5.8 30.4H2Z", "#6E8EAE", INK, 1.2)
            + P("M1.6 31.4h4.6v-1.4H1.6zM7.8 31.4h4.8v-1.4H7.8z", "#5A3A22", INK, .8))
    s4 = legs + child(21, 31.4, GOLD, "#5A3A22", False, 1.08)
    s5 = child(9.6, 31.4, GOLD, "#5A3A22", False, .98) + child(22.6, 31.4, "#D9534F", "#3A2A1E", True, .98)
    return {"@4": ("0 0 32 32", s4, "Kleines Kind mit grossem Kopf und rosigen Wangen steht neben den Beinen eines Erwachsenen (angeschnitten); das Kind reicht bis zur Hüfte"),
            "@5": ("0 0 32 32", s5, "Zwei kleine Kinder mit grossen Köpfen nebeneinander, ein Junge und ein Mädchen mit Zöpfen")}


@runde2("FIG-ZEICHEN-BITTER")
def bitter2():
    """Saures/bitteres Gesicht (zugekniffen, zusammengezogener Mund, Schüttellinien) neben einem freistehenden Becher mit
    Bitterkraut – ohne Zunge, damit es nicht «eklig» heisst."""
    face = (emoji(12.4, 14.4, 10.6)
            + P("M6.2 10.6l3.6 1.6-3.6 1.6M18.6 10.6l-3.6 1.6 3.6 1.6", "none", INK, 1.4)
            + P("M5.6 8q2-1.6 4-1M19.2 8q-2-1.6-4-1", "none", INK, 1.2)
            + P("M9.4 20.6q1.4-2 3-.6 1.6-1.4 3 .6-1.4 1.6-3 .4-1.6 1.2-3-.4z", "#B84A54", INK, 1)
            + P("M.8 9.4q-1 2.6 0 5M.8 16q-1 2.4 0 4.6", "none", INK, .9))
    cup = (P("M22.8 18.4h8.4l-1.2 10.6q-.2 1.4-1.6 1.4h-2.8q-1.4 0-1.6-1.4z", STONE, INK, 1.2)
           + P("M23 20.2h8l.2-1.8h-8.4z", "#4E6A2E", INK, .6)
           + P("M26 18.6Q25.4 13.6 27.6 11.4M25.8 15.4q-2.6-.6-3.2-2.8 2.6-.2 3.2 2.8zM26.6 13.2q.6-2.6 3.2-3-.2 2.6-3.2 3zM26.4 17q2.4-1.2 4 0-1.8 1.8-4 0z", LEAF, INK, .7))
    s4 = face + cup
    face5 = face.replace(P("M9.4 20.6q1.4-2 3-.6 1.6-1.4 3 .6-1.4 1.6-3 .4-1.6 1.2-3-.4z", "#B84A54", INK, 1),
                         P("M8.4 20.4Q10 18.8 11.4 20.4T14.4 20.4 16.6 20", "none", INK, 1.4))
    return {"@4": ("0 0 32 32", s4, "Gelbes Gesicht mit zugekniffenen Augen und sauer zusammengezogenem Mund, Schüttellinien; daneben ein Becher mit dunkelgrünem Trank und Bitterkraut"),
            "@5": ("0 0 32 32", face5 + cup, "Gelbes Gesicht mit zugekniffenen Augen und welligem Mund, Schüttellinien; daneben ein Becher mit Bitterkraut")}


@runde2("FIG-ZEICHEN-GERECHT")
def gerecht2():
    """Ein Mensch (gerecht = Eigenschaft eines Menschen): aufrechte Figur, auf der Brust die Waage im Gleichgewicht, grünes Häkchen."""
    fig = person(16, 31.6, 1.36, "#F4ECD8", "#3A2A1E")
    emb = ('<g transform="translate(16 20.2) scale(.34) translate(-16 -6)">' + scale_drawing(16, 0, 9.6, pw=5.2) + "</g>")
    check = C(27, 7, 4.2, GREEN, INK, 1.2) + P("M24.8 7l1.6 1.7 3-3.4", "none", WHITE, 1.6)
    return {"@4": ("0 0 32 32", fig + emb + check, "Aufrecht stehender Mensch, auf seiner Brust eine Waage im Gleichgewicht; oben rechts ein grünes Häkchen im Kreis")}


@runde2("FIG-ZEICHEN-HOCHZEIT")
def hochzeit2():
    def bride(cx, foot, s):
        hr = 5.2 * s
        hy = foot - 17.6 * s
        veil = P(f"M{cx - hr - .8 * s} {hy - 1 * s}Q{cx} {hy - hr * 1.9} {cx + hr + .8 * s} {hy - 1 * s}L{cx + hr * 1.7} {foot - 4 * s}H{cx - hr * 1.7}Z", "#F4F4F8", INK, 1)
        body = P(f"M{cx - 3 * s} {foot - 12 * s}L{cx - 8 * s} {foot}H{cx + 8 * s}L{cx + 3 * s} {foot - 12 * s}Z", WHITE, INK, 1.2)
        face = (C(cx, hy, hr, SKIN, INK, 1.2) + P(f"M{cx - hr} {hy - .2 * s}q0-{hr} {hr}-{hr}t{hr} {hr}q-{hr}-{hr / 2}-{2 * hr} 0z", "#7A4A22", INK, .8)
                + P(f"M{cx - 2.9 * s} {hy + .5 * s}q.9-1.1 1.8 0M{cx + 1.1 * s} {hy + .5 * s}q.9-1.1 1.8 0", "none", INK, .7)
                + P(f"M{cx - 1.6 * s} {hy + 2.3 * s}q1.6 1.8 3.2 0", "none", INK, .7)
                + C(cx - 2.6 * s, hy - hr * .9, 1 * s, "#E86A8A", INK, .5) + C(cx + 2.6 * s, hy - hr * .9, 1 * s, "#E86A8A", INK, .5) + C(cx, hy - hr * 1.05, 1 * s, "#F2C04A", INK, .5))
        return veil + body + face
    arch = (P("M3 31.6V14Q3 2 16 2T29 14V31.6", "none", INK, 3.4) + P("M3 31.6V14Q3 2 16 2T29 14V31.6", "none", "#7DB04A", 2)
            + "".join(C(x, y, 1.4, "#E86A8A", INK, .5) for x, y in ((3.4, 22), (3.6, 12.6), (7.4, 5.4), (16, 2), (24.6, 5.4), (28.4, 12.6), (28.6, 22))))
    groom = person(11.4, 31.6, .9, "#3E4E6E", "#3A2A1E", "happy")
    s4 = arch + groom + bride(21, 31.6, .9) + P("M16 23.2q-1.6-1.6-.2-2.6 1-.6 1.6.4.6-1 1.6-.4 1.4 1-.2 2.6l-1.4 1.2z", "#E8434A", INK, .5)
    # @5 anstossende Becher unter Blumengirlande
    def goblet(rot, cx):
        g = (P("M-5 -9h10q0 7-5 8-5-1-5-8z", "#F2D78A", INK, 1.2) + P("M-4.6 -6.4h9.2q-.6 4.6-4.6 5.2-4-.6-4.6-5.2z", "#9A2A4A", None)
             + P("M0 -1v7M-3.6 6.4h7.2", "none", INK, 1.8))
        return f'<g transform="translate({cx} 23) rotate({rot})">{g}</g>'
    gar = (P("M1 3Q16 12 31 3", "none", "#5B8A2E", 1.6) + "".join(C(x, y, 1.6, c, INK, .5) for x, y, c in
           ((5, 5.4, "#E86A8A"), (10.4, 7.6, "#F2C04A"), (16, 8.2, "#E86A8A"), (21.6, 7.6, "#F2C04A"), (27, 5.4, "#E86A8A"))))
    s5 = gar + goblet(16, 10.6) + goblet(-16, 21.4) + sparkle(16, 13.4, 2.4)
    return {"@4": ("0 0 32 32", s4, "Brautpaar unter einem grünen Blumenbogen: Bräutigam im dunklen Gewand, Braut in Weiss mit Schleier und Blumenkranz, ein rotes Herz zwischen ihnen"),
            "@5": ("0 0 32 32", s5, "Zwei Becher mit Rotwein stossen an, darüber eine Blumengirlande")}


@runde2("FIG-ZEICHEN-MAMMON")
def mammon2():
    ped = P("M15.6 31.6V22.6H31.4V31.6Z", STONE, INK, 1.3) + P("M14.4 22.6h18.2", "none", INK, 1.6) + P("M17.6 25.4h12", "none", "#A89E88", .8)
    bag = (P("M20 11.6Q16.4 15.2 16.8 18.6 17.4 22.4 23.6 22.4 29.8 22.4 30.4 18.6 30.8 15.2 27.2 11.6Z", "#C9A15A", INK, 1.3)
           + P("M19.8 11.6Q23.6 12.8 27.4 11.6L26 9.6H21.2Z", "#A6803A", INK, 1)
           + C(23.6, 17.4, 2.8, GOLD, INK, 1) + C(23.6, 17.4, 1.6, "none", "#B8891A", .7)
           + P("M18 9.6L18.6 2.4 21.2 5.6 23.6 1.4 26 5.6 28.6 2.4 29.2 9.6Z", GOLD, INK, 1.1) + C(23.6, 7.4, .9, RED, None))
    s4 = ped + bag + kneel(1.2, 31.6, "#6E8EAE", "#3A2A1E", True)
    s5 = ped + bag + '<g transform="translate(14.6 0) scale(-1 1)">' + kneel(1.2, 31.6, "#6E8EAE", "#3A2A1E", True) + "</g>"
    return {"@4": ("0 0 32 32", s4, "Geldsack mit Goldmünze und grosser goldener Krone auf einem Steinsockel; davor kniet ein Mensch und verneigt sich tief zum Geldsack hin")}


@runde2("FIG-ZEICHEN-NICHT-RICHTEN")
def nicht_richten2():
    block = P("M6.6 25h17v3.4h-17z", "#8A5A30", INK, 1.2)
    # Hammerstiel quer zum Verbotsbalken (Balken von links unten nach rechts oben)
    s4 = block + gavel(6.2, 5.6, 1.05, 52) + P("M7.4 20.6l-2.4-1.4M8.6 17.6l-1.6-2.4M11 23.4l-3-.4", "none", INK, 1.1) + verbot(16, 16, 14.2, 2.6)
    fig = person(16, 29.4, .82, "#B0704A", "#3A2A1E")
    s5 = fig + gavel(5.4, 4.6, .8, 40) + verbot(16, 16, 14.6, 2.6)
    return {"@4": ("0 0 32 32", s4, "Richterhammer schlägt auf einen Holzblock (Stiel von rechts oben), darüber roter Verbotskreis mit Schrägstrich"),
            "@5": ("0 0 32 32", s5, "Ein Richterhammer über einem Menschen, darüber roter Verbotskreis mit Schrägstrich")}


@runde2("FIG-ZEICHEN-RANG")
def rang2():
    """Mk 10,37; 12,39: Sitzplätze nach Rang – drei Stühle, der mittlere golden, erhöht auf einer Stufe; Fassung 5: Podest mit
    Menschen auf allen Stufen, der oberste grösser."""
    def chair(x, base, h, col, back=10):
        return (P(f"M{x} {base}V{base - h}M{x + 6} {base}V{base - h * .55}", "none", INK, 1.4)
                + P(f"M{x - .6} {base - h * .55}h7.2v1.6h-7.2z", col, INK, 1.1)
                + P(f"M{x} {base - h * .55}V{base - h * .55 - back}Q{x + 3} {base - h * .55 - back - 2.4} {x + 6} {base - h * .55 - back}V{base - h * .55}", col, INK, 1.2))
    step = P("M10 31.6V26.4H22V31.6Z", "#B5553A", INK, 1.3)
    s4 = (step + chair(1.6, 31.6, 9, STONE, 7) + chair(24.4, 31.6, 9, STONE, 7)
          + chair(13, 26.4, 10, GOLD, 12) + P("M13.4 4.4l1.2-2.6 1.4 1.6 1-2.2 1 2.2 1.4-1.6 1.2 2.6z", GOLD, INK, .7))
    pod = (P("M1 31.6V24.4H10.6V31.6ZM21.4 31.6V26.6H31V31.6Z", "#C9BFAA", INK, 1.3) + P("M10.6 31.6V19H21.4V31.6Z", GOLD, INK, 1.4))
    s5 = pod + person(16, 19, .74, "#B5553A", "#3A2A1E", "happy") + person(5.8, 24.4, .52, "#6E8EAE", "#5A3A22") + person(26.2, 26.6, .5, "#7E8E5A", "#3A2A1E")
    return {"@4": ("0 0 32 32", s4, "Drei Stühle: zwei einfache graue links und rechts, in der Mitte erhöht auf einer Stufe ein hoher goldener Ehrenstuhl mit kleiner Krone"),
            "@5": ("0 0 32 32", s5, "Treppchen mit drei Stufen, auf jeder steht ein Mensch, auf der höchsten goldenen Stufe der grösste")}


@runde2("FIG-ZEICHEN-SABBAT")
def sabbat2():
    """Sabbat = Ruhetag: die zwei Sabbatkerzen; Fassung 4 mit ruhendem Menschen (liegend, Zzz) neben den Kerzen;
    Fassung 5: Kalenderblatt mit grosser «7» und zwei Kerzen."""
    def candles(x0, y0, s=1.0):
        g = ""
        for dx in (0, 6.4):
            x = x0 + dx * s
            g += (P(f"M{x - 1.4 * s} {y0}h{2.8 * s}v{9 * s}h-{2.8 * s}z", WHITE, INK, .9)
                  + P(f"M{x} {y0 - 5.4 * s}q-{1.8 * s} {2.4 * s}-{1.6 * s} {3.8 * s} .2 {1.4 * s} {1.6 * s} {1.4 * s}t{1.6 * s}-{1.4 * s}q.2-{1.4 * s}-{1.6 * s}-{3.8 * s}z", "#F08A2A", "#B8501A", .6)
                  + P(f"M{x - 3.2 * s} {y0 + 9 * s}h{6.4 * s}l-{1.4 * s} {2.4 * s}h-{3.6 * s}z", GOLD, INK, .9))
        return g
    rest = (P("M1 31.4h18", "none", INK, 1.4) + P("M2 30.6V27.6Q2 25.6 4 25.6H17.6Q19 25.6 19 27.2V30.6Z", "#6E8EAE", INK, 1.2)
            + C(5.4, 23.2, 3, SKIN, INK, 1.1) + P("M2.4 23q0-3 3-3t3 3q-3-1.4-6 0z", "#3A2A1E", INK, .6)
            + P("M4 23.6q.7.6 1.4 0M6 23.6q.7.6 1.4 0", "none", INK, .6)
            + f'<text x="10.4" y="21" font-family="sans-serif" font-size="5" font-weight="bold" fill="#5E7FA8">z</text>'
            + f'<text x="13.4" y="17" font-family="sans-serif" font-size="6.4" font-weight="bold" fill="#5E7FA8">Z</text>')
    s4 = rest + candles(23, 13.6, 1.0)
    cal = (P("M1 6.4h20v25H1z", WHITE, INK, 1.4) + P("M1 6.4h20v5H1z", "#B5553A", INK, 1.4)
           + f'<text x="11" y="28.6" font-family="Georgia,serif" font-size="16" font-weight="bold" text-anchor="middle" fill="{INK}">7</text>')
    s5 = cal + candles(24.6, 15.6, .95)
    return {"@4": ("0 0 32 32", s4, "Ein Mensch liegt ausgestreckt und schläft (Zz), daneben zwei brennende Kerzen in goldenen Leuchtern"),
            "@5": ("0 0 32 32", s5, "Kalenderblatt mit grosser «7», daneben zwei brennende Kerzen in goldenen Leuchtern")}


@runde2("FIG-ZEICHEN-STAMMBAUM")
def stammbaum2():
    """Stammbaum als Ahnentafel: drei Köpfe senkrecht, verbunden durch einen Stamm, Blätter am Stamm (Baum); Fassung 5:
    Baum, dessen drei Äste in Köpfen enden (ohne Medaillons)."""
    def head(cx, cy, r, hair, beard=None):
        g = C(cx, cy, r, SKIN, INK, 1.1)
        g += P(f"M{cx - r:.2f} {cy - .1:.2f}q0-{r:.2f} {r:.2f}-{r:.2f}t{r:.2f} {r:.2f}q-{r:.2f}-{r / 2:.2f}-{2 * r:.2f} 0z", hair, INK, .7)
        if beard:
            g += P(f"M{cx - r * .85:.2f} {cy + .4:.2f}Q{cx:.2f} {cy + r * 1.9:.2f} {cx + r * .85:.2f} {cy + .4:.2f}Q{cx:.2f} {cy + r * .8:.2f} {cx - r * .85:.2f} {cy + .4:.2f}Z", beard, INK, .6)
        g += C(cx - r * .38, cy + .1, .5, INK, None) + C(cx + r * .38, cy + .1, .5, INK, None)
        return g
    trunk = thick("M16 30.6V4", "#8A5E36", 3.2, 1.1) + P("M11 31.4h10", "none", INK, 1.6)
    leaves = "".join(f'<ellipse cx="{x}" cy="{y}" rx="2.4" ry="1.1" transform="rotate({a} {x} {y})" fill="{LEAF}" stroke="{INK}" stroke-width=".55"/>'
                     for x, y, a in ((20.2, 11.6, -25), (11.8, 11.6, 25), (20.2, 22.4, -25), (11.8, 22.4, 25)))
    s4 = trunk + leaves + head(16, 5.2, 3.8, "#8A8A8A", "#E6E2DA") + head(16, 17, 3.8, "#5A3A22", "#5A3A22") + head(16, 27.4, 3.4, "#3A2A1E")
    br = (thick("M16 31Q16.6 24 16 19 15.4 14 9 10.8M16.2 21Q18 15.6 23.6 12.4M16 16Q16.4 10 16 6.4", "#8A5E36", 2.8, 1.1) + P("M10.4 31.4h11.6", "none", INK, 1.6)
          + "".join(f'<ellipse cx="{x}" cy="{y}" rx="2.2" ry="1" transform="rotate({a} {x} {y})" fill="{LEAF}" stroke="{INK}" stroke-width=".5"/>'
                    for x, y, a in ((12.2, 16.4, 30), (20.4, 19.4, -30), (18.6, 11, -40))))
    s5 = br + head(16, 5.6, 4.2, "#8A8A8A", "#E6E2DA") + head(7.6, 11.4, 4, "#5A3A22", "#5A3A22") + head(25, 12, 3.8, "#3A2A1E")
    return {"@4": ("0 0 32 32", s4, "Ein senkrechter brauner Stamm mit Blättern verbindet drei Köpfe übereinander: oben alter Mann mit weissem Bart, Mitte Mann mit braunem Bart, unten junger Mann"),
            "@5": ("0 0 32 32", s5, "Kleiner Baum, dessen drei Äste in drei Köpfen enden: alter Mann mit weissem Bart, Mann mit Bart, junger Mann")}


@runde2("FIG-ZEICHEN-TOERICHT")
def toericht2():
    """🤦 (sich an den Kopf fassen über eine Dummheit): Gesicht, die Hand aus der Handbibliothek (gebend, gedreht) über den Augen;
    Fassung 5: Eselsmütze? nein – Haus auf Sand stürzt, ruhiger gezeichnet."""
    face = (emoji(15, 17, 12)
            + P("M9.6 25.4q5.4-3.4 10.8 0", "none", INK, 1.5)
            + P("M5 9.4q2-2.6 4.8-2.6", "none", INK, 1.3))
    hand = f'<g transform="translate(5.4 5.2) rotate(6) scale(.82)">{H.hand_gebend()}</g>'
    s4 = face + hand
    house = ('<g transform="rotate(18 21 26)">'
             + P("M9 26V13.4H25V26Z", "#E9DDBF", INK, 1.4) + P("M7.4 13.6L17 5.6 26.6 13.6Z", "#B5553A", INK, 1.3)
             + P("M15 26v-6h4v6z", "#8A6A3A", INK, 1) + P("M12.4 14.6l1.8 3.6-1.6 2.4 1.4 3.2", "none", INK, 1.1) + "</g>")
    sand = P("M0 32V28.4Q8 25.6 16 27.2T32 26.4V32Z", "#EBCB8A", INK, 1.2) + P("M1 31.6Q4 29.8 8 31", "none", "#3B6E9E", 1.4)
    s5 = sand + house
    return {"@4": ("0 0 32 32", s4, "Gelbes Emoji-Gesicht mit verzogenem Mund schlägt sich die Hand vor die Augen (🤦, «wie dumm»)"),
            "@5": ("0 0 32 32", s5, "Ein Haus auf Sand kippt schräg und reisst ein")}


@runde2("FIG-ZEICHEN-VERBORGEN")
def verborgen2():
    """Mt 6,6: allein in der Kammer bei geschlossener Tür beten – Schnitt durch ein kleines Haus, innen kniet ein Mensch, die Tür
    ist zu (Riegel); kein Auge (las sich als «Überwachung»)."""
    house = (P("M2.6 31.4V13.6L16 3.4 29.4 13.6V31.4Z", "#F4ECD8", INK, 1.6)
             + P("M1 14.6L16 3 31 14.6", "none", "#B5553A", 2.6)
             + P("M21.6 31.4V18.6H27.4V31.4Z", "#9A6A3A", INK, 1.2) + P("M20.6 23.6h7.8", "none", INK, 1.8)
             + P("M1.6 31.6h28.8", "none", INK, 1.6))
    s4 = house + kneel(5.4, 31.4, "#6E8EAE", "#3A2A1E")
    house5 = house.replace(P("M2.6 31.4V13.6L16 3.4 29.4 13.6V31.4Z", "#F4ECD8", INK, 1.6), P("M2.6 31.4V13.6L16 3.4 29.4 13.6V31.4Z", "#C9BFAA", INK, 1.6))
    s5 = house5 + kneel(5.4, 31.4, "#6E8EAE", "#3A2A1E") + P("M8.6 6.6l-1.6-1.6M11 4.4l-.8-2M6.6 9.4l-2-.8", "none", GOLD, 0)
    return {"@4": ("0 0 32 32", s4, "Schnitt durch ein kleines Haus: innen kniet ein Mensch allein im Gebet, rechts die geschlossene, verriegelte Tür")}


@runde2("FIG-ZEICHEN-VERGEBUNG")
def vergebung2():
    """Kol 2,14: der Schuldschein ist ans Kreuz genagelt (getilgt) – nicht der zerrissene Schuldschein («vergeben»);
    Fassung 5: Herz, dessen dunkler Fleck abgewaschen wird."""
    cross = P("M13.6 1h4.8v8.6h8.6v4.8h-8.6V31.6h-4.8V14.4H5V9.6h8.6z", "#B07E44", INK, 1.4)
    note = (P("M10 12.6h12v13H10z", "#F4F1EA", INK, 1.2) + P("M12.4 16.6h7.2M12.4 19.4h7.2M12.4 22.2h4.6", "none", "#5B4630", .9)
            + C(16, 14.4, 1, "#8A8A8A", INK, .6)
            + P("M11.4 25.4L21 15", "none", "#4E8A3A", 0))
    glow = C(16, 13, 13.6, "#FBEFC0", None)
    s4 = glow + cross + note + sparkle(26, 22, 2.6) + sparkle(6, 21, 1.8)
    heart = P("M16 30Q2 20.6 2.6 11.2 3.4 4.4 9.4 4.2 13.6 4.2 16 8.4 18.4 4.2 22.6 4.2 28.6 4.4 29.4 11.2 30 20.6 16 30Z", "#F4F1EA", INK, 1.5)
    half = P("M16 8.4Q13.6 4.2 9.4 4.2 3.4 4.4 2.6 11.2 2 20.6 16 30Z", "#5A2E3A", None)
    s5 = heart + half + P("M16 8.4V30", "none", INK, 0) + C(16, 17, 0, "none", None) + heart.replace('fill="#F4F1EA"', 'fill="none"') + \
        tear(10, 1.4, .8) + tear(5, 3.6, .7) + sparkle(22, 14.6, 3.2)
    return {"@4": ("0 0 32 32", s4, "Holzkreuz vor hellem Licht, daran ein Schuldschein angenagelt; goldenes Funkeln"),
            "@5": ("0 0 32 32", s5, "Herz: linke Hälfte dunkel befleckt, Wassertropfen fallen darauf, rechte Hälfte weiss und glänzend")}


@runde2("FIG-ZEICHEN-VOLLMACHT")
def vollmacht2():
    """Vollmacht = Befugnis: gesiegelte Urkunde mit Krone im Siegel; Fassung 5: thronende Figur mit Krone und Zepter."""
    doc = (P("M3 3h18v24H3z", "#F4F1EA", INK, 1.3) + P("M6 8h12M6 11.4h12M6 14.8h12M6 18.2h7", "none", "#5B4630", 1.1))
    seal = (P("M19 27.6l-2 4.2 3.4-1.6 2.4 2.6.4-4.4", "#C8323C", "#7A1E22", .7) + P("M23.6 27.6l2 4.2-3.4-1.6", "#C8323C", "#7A1E22", .7)
            + C(21.6, 23, 6.4, "#C8323C", "#7A1E22", 1) + C(21.6, 23, 4.6, "none", "#E07A7A", .7)
            + P("M18.4 25.2l.8-4 1.4 1.6 1-2.4 1 2.4 1.4-1.6.8 4z", GOLD, "#7A1E22", .6))
    s4 = doc + seal
    throne = (P("M5 31.6V8.4Q5 5 8 5H24Q27 5 27 8.4V31.6", GOLD, INK, 1.4) + P("M3 31.6h26", "none", INK, 1.6))
    king = person(16, 30.6, 1.02, "#8E3A4A", "#3A2A1E") + P("M11.6 7.2l1-3 1.6 1.8 1.8-2.6 1.8 2.6 1.6-1.8 1 3z", GOLD, INK, .8)
    sc = thick("M25.6 30.6L25.6 13", GOLD, 1.8, 1) + C(25.6, 11.4, 2.4, GOLD, INK, 1.1) + C(25.6, 11.4, 1, RED, None)
    s5 = throne + king + sc
    return {"@4": ("0 0 32 32", s4, "Beschriebene Urkunde mit grossem rotem Wachssiegel, im Siegel eine goldene Krone, Siegelbänder"),
            "@5": ("0 0 32 32", s5, "Gekrönte Figur auf goldenem Thron, neben ihr ein aufgestelltes goldenes Zepter")}


@runde2("FIG-ZEICHEN-LOESERECHT")
def loeserecht2():
    """Rut 4,7: zwei Männer am Tor, der eine reicht dem anderen seine Sandale (Zeichen der Übergabe des Löserechts); dahinter der
    Acker mit Haus. Die Arme reichen bis zur Sandale, die Sandale verdeckt die Hände."""
    def sandal_top(x, y, s=1.0, rot=0):
        """Sandale von oben: Sohle in Fussform, zwei Riemen."""
        g = (P("M.4 -8.6Q4.6 -8.6 4.6 -3.4 4.6 1 3.4 4.6 2.6 8.8 0 8.8-2.6 8.8-3.2 4.6-4 1-3.8-3.4-3.8-8.6.4-8.6Z", "#C99A62", INK, 1.2)
             + P("M.2 -8.6Q2.6 -8.4 3.4 -6.4 1.6 -6 .2 -6.6Z", "#B07E44", None)
             + P("M-3.6 -.4L.2 -5.4 3.8 -.4", "none", INK, 2.4) + P("M-3.6 -.4L.2 -5.4 3.8 -.4", "none", "#6E4A26", 1.2)
             + C(.2, -5.4, .9, "#6E4A26", INK, .5))
        return f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">{g}</g>'
    field = (P("M0 31.6V25Q16 21.6 34 25V31.6Z", "#B07E44", INK, 1.2)
             + P("M3 31.4L5 25.6M9.6 31.4L10.6 24.6M16.4 31.4L16.6 24M23.2 31.4L22.6 24.2M30 31.4L28.6 24.8", "none", "#7A5430", .9))
    m1 = person(6.6, 27.6, .78, "#6E8EAE", "#3A2A1E", beard="#3A2A1E")
    m2 = person(27.4, 27.6, .78, "#7E5A8E", "#5A3A22", beard="#5A3A22")
    arms = thick("M10.6 19.4Q13.4 18.6 14.6 16.4", "#6E8EAE", 2, 1) + thick("M23.4 19.4Q20.6 18.6 19.4 16.4", "#7E5A8E", 2, 1)
    s4 = field + m1 + m2 + arms + sandal_top(17, 13.6, 1.0, 0)
    house = P("M26 23.4V18.6L29.4 15.6 32.8 18.6V23.4Z", "#E9DDBF", INK, 1) + P("M25.4 19l4-3.6 4 3.6", "none", "#B5553A", 1.4)
    s5 = (P("M0 31.6V22Q17 18.6 34 22V31.6Z", "#B07E44", INK, 1.2)
          + P("M3 31.4L5 22.6M9.6 31.4L10.6 21.6M16.4 31.4L16.6 21M23.2 31.4L22.6 21.2M30 31.4L28.6 21.8", "none", "#7A5430", .9)
          + house + f'<g transform="translate(14.4 -1.2) scale(.6)">{H.hand_gebend("#7E5A8E")}</g>' + sandal_top(15.4, 14.4, .95, -25))
    return {"@4": ("0 0 34 32", s4, "Zwei bärtige Männer stehen einander gegenüber auf einem gepflügten Acker; zwischen ihnen wird eine Sandale (von oben gesehen: Sohle mit zwei Riemen) übergeben"),
            "@5": ("0 0 34 32", s5, "Eine Hand von oben lässt eine Sandale (Sohle mit Riemen) auf einen gepflügten Acker mit kleinem Haus fallen")}


# ---------------------------------------------------------------- Runde 3
Z3 = {}


def runde3(fid):
    def deco(fn):
        prev = Z3.get(fid)
        Z3[fid] = (lambda: {**prev(), **fn()}) if prev else fn
        return fn
    return deco


def limbs(parts, col, ow=1.1):
    """Gliedmassen und Rumpf als Linien einer Silhouette: erst alle Teile breit in Tinte, dann alle in Farbe (Kontur nur aussen).
    parts: [(d, breite)]"""
    return ("".join(P(d, "none", INK, w + 2 * ow) for d, w in parts) + "".join(P(d, "none", col, w) for d, w in parts))


def silf(paths, fill, w=2.4):
    """Flächen als eine Silhouette: alle zuerst mit breiter Tintenkontur, darüber alle in Farbe (Kontur nur aussen)."""
    return ("".join(P(d, INK, INK, w) for d in paths) + "".join(P(d, fill, None) for d in paths))


def gavel2(hx, hy, ang, L=12.0, col="#8A5A30"):
    """Richterhammer: Kopf (quer liegende Walze mit goldenen Bändern) bei hx, hy; Stiel nach Winkel ang (Grad) weg vom Kopf."""
    a = math.radians(ang)
    ex, ey = hx + L * math.cos(a), hy + L * math.sin(a)
    head = (f'<g transform="translate({hx} {hy}) rotate({ang + 90})">'
            + f'<rect x="-6.4" y="-3.2" width="12.8" height="6.4" rx="1.6" fill="{col}" stroke="{INK}" stroke-width="1.3"/>'
            + f'<rect x="-6.4" y="-3.2" width="2.4" height="6.4" rx=".8" fill="{GOLD}" stroke="{INK}" stroke-width=".9"/>'
            + f'<rect x="4" y="-3.2" width="2.4" height="6.4" rx=".8" fill="{GOLD}" stroke="{INK}" stroke-width=".9"/></g>')
    return thick(f"M{hx:.2f} {hy:.2f}L{ex:.2f} {ey:.2f}", "#B07E44", 2.2, 1) + head


@runde3("FIG-ZEICHEN-FRIEDE")
def friede3():
    def leaf(x, y, rot, l=2.3):
        return f'<ellipse cx="{x}" cy="{y}" rx="{l}" ry="{l * .42:.2f}" transform="rotate({rot} {x} {y})" fill="{LEAF}" stroke="{INK}" stroke-width=".55"/>'
    parts = ["M9.4 19.2Q3.4 16.2 1.4 18.4Q.2 21.2 1.4 24.2Q3.8 25.8 9.6 22.6Z",
             "M6.4 21Q8.4 16 13.6 15.6L20.4 15.2Q23.2 12.8 26 13.4Q28.2 14 28.6 15.6L26.8 16.4Q25.6 21.2 18.8 22.6Q12 23.8 6.4 21Z",
             "M11.6 16.8Q10.4 8.4 15.4 2.4Q16.4 7.2 20 8.2Q22.6 9.2 21.8 12.6Q20.6 15.8 15.4 17.2Z"]
    dove = silf(parts, WHITE, 2.6) + P("M14 9.8q1.6 1.4 4.2 1.4M13.8 13q2 1 4.6.8", "none", "#B4C0CC", .9)
    head = C(25.2, 14.6, .8, INK, None) + P("M28.4 14.6l2.4 1-2.2 1z", "#E8A33A", INK, .6)
    twig = (P("M29.4 16.2Q31 19.6 29.2 24.4", "none", "#5B7A2E", 1.3)
            + leaf(31.6, 18.2, -30) + leaf(28, 20.4, 30) + leaf(31.2, 22.6, -20) + C(28.8, 25.2, 1.1, "#5B7A2E", INK, .5))
    return {"@6": ("0 0 33 27", dove + head + twig, "Weisse fliegende Taube als eine ruhige Silhouette (Flügel erhoben, runder Schwanz), im Schnabel ein grüner Ölzweig mit Olive")}


@runde3("FIG-ZEICHEN-SATT")
def satt3():
    face = (emoji(16, 11.4, 9.6)
            + P("M11 10.4q1.5-1.6 3 0M18 10.4q1.5-1.6 3 0", "none", INK, 1.4)
            + P("M12.6 15q3.4 2.4 6.8 0", "none", INK, 1.4)
            + C(10, 13.8, 1.9, "#F4B0A0", None) + C(22, 13.8, 1.9, "#F4B0A0", None))
    bowl = (P("M2 20.6H30Q29.4 31 16 31.2 2.6 31 2 20.6Z", "#E9DDBF", INK, 1.5)
            + E(16, 20.6, 14, 2.6, "#FFF8E6", INK, 1.4)
            + C(10, 20.6, .7, "#B07E44", None) + C(19.4, 21.2, .6, "#B07E44", None) + C(14.6, 20, .55, "#B07E44", None)
            + thick("M22 21L29.6 16.2", "#B9B4A8", 1, .7) + E(21, 21.4, 2, 1, "#B9B4A8", INK, .8))
    return {"@6": ("0 0 32 32", face + bowl, "Gelbes zufriedenes Gesicht mit geschlossenen Augen und Pausbacken direkt hinter einer grossen leeren Schüssel mit Krümeln und Löffel")}


@runde3("FIG-ZEICHEN-BOESES")
def boeses3():
    body = "#3A3442"
    d = ("M4.6 30.8Q1.4 30.6 3.2 28.2 6.4 25 14.2 26 22.4 27.2 24.6 23.4 26 20 21 18.4 14 16 15.8 11.6 17 9.4 19.6 8.6")
    sn = (limbs([(d, 4.2)], body, 1.3)
          + silf(["M18.6 6.4Q23 3.6 27.6 6Q29.8 7.6 28 9.8Q25.6 12.4 20.8 12.4Q17.6 12 17.6 9.4Q17.6 7.6 18.6 6.4Z"], body, 2.6)
          + P("M21.6 6.6l4.6 1.8", "none", INK, 1.5) + C(24.2, 8.8, 1.1, "#F04A2E", None) + P("M24.2 8.1v1.4", "none", INK, .5)
          + P("M22.6 12.2l.5 1.8.7-1.8M25.4 11.8l.4 1.6.7-1.7", WHITE, INK, .4)
          + P("M28.6 8.4l2.4-.4M31 8l1.2-1.1M31 8l1.1 1.1", "none", RED, 1.1))
    return {"@6": ("0 0 33 32", sn, "Schwarze aufgerichtete Schlange als eine Silhouette mit böse gesenkter Braue, rotem Schlitzauge, Giftzähnen und gespaltener Zunge")}


@runde3("FIG-ZEICHEN-HOCHZEIT")
def hochzeit3():
    var = Z2["FIG-ZEICHEN-HOCHZEIT"]()
    vb, svg, gez = var["@4"]
    heart = P("M16 23.2q-1.6-1.6-.2-2.6 1-.6 1.6.4.6-1 1.6-.4 1.4 1-.2 2.6l-1.4 1.2z", "#E8434A", INK, .5)
    svg = svg.replace(heart, "")
    return {"@6": (vb, svg, "Brautpaar unter einem grünen Blumenbogen: Bräutigam im dunklen Gewand, Braut in Weiss mit Schleier und Blumenkranz")}


@runde3("FIG-ZEICHEN-NICHT-RICHTEN")
def nicht_richten3():
    block = P("M14 24.6h14v3.6H14z", "#8A5A30", INK, 1.2)
    s6 = block + gavel2(19.4, 19, -128, 13) + verbot(16, 16, 14.4, 2.6)
    s7 = scale_drawing(16, 4.4, 7.4, pw=4.4) + gavel2(22.8, 22.6, -150, 9) + verbot(16, 16, 14.4, 2.6)
    return {"@6": ("0 0 32 32", s6, "Klassischer Richterhammer (Walzenkopf mit goldenen Bändern) schlägt auf einen Holzblock; darüber roter Verbotskreis mit Schrägstrich quer zum Stiel"),
            "@7": ("0 0 32 32", s7, "Waage und kleiner Richterhammer, darüber roter Verbotskreis mit Schrägstrich")}


@runde3("FIG-ZEICHEN-VOLLMACHT")
def vollmacht3():
    """Mt 16,19 / Offb 1,18: Schlüssel als Zeichen der Vollmacht, mit Krone am Griff; Fassung 7: Zepter und gesiegelte Urkunde
    nebeneinander (nicht überlagert)."""
    key = (thick("M16 13V30", GOLD, 3, 1.1) + P("M16 23.4h5.4v2.4H18.6v2H16", GOLD, INK, 1.1)
           + C(16, 9.6, 5.4, GOLD, INK, 1.4) + C(16, 9.6, 2.2, WHITE, INK, 1)
           + P("M10.6 4.6l1.2-3.4 2.2 2.2 2-3 2 3 2.2-2.2 1.2 3.4z", GOLD, INK, 1) + C(16, 2.6, .6, RED, None))
    s6 = key
    doc = (P("M14 6h16v20H14z", "#F4F1EA", INK, 1.3) + P("M17 10.4h10M17 13.6h10M17 16.8h6", "none", "#5B4630", 1.1)
           + C(25.6, 23.2, 4.4, "#C8323C", "#7A1E22", 1) + P("M23.4 24.6l.6-3 1 1.2.6-1.8.6 1.8 1-1.2.6 3z", GOLD, "#7A1E22", .5))
    scep = (thick("M6 31V10.6", GOLD, 2.6, 1.1) + C(6, 7.4, 3.6, GOLD, INK, 1.3) + C(6, 7.4, 1.5, RED, INK, .7)
            + P("M3.2 4.8l1-2.8 1.8 1.6 1.8-1.6 1 2.8", GOLD, INK, .9) + P("M3.6 14h4.8M3.6 16.6h4.8", "none", INK, 1.4))
    return {"@6": ("0 0 32 32", s6, "Grosser goldener Schlüssel mit einer kleinen Krone über dem Griff"),
            "@7": ("0 0 32 32", scep + doc, "Goldenes Zepter aufrecht neben einer beschriebenen Urkunde mit rotem Siegel")}


@runde3("FIG-ZEICHEN-GERECHT")
def gerecht3():
    fig = person(7.4, 31.4, 1.0, "#F4ECD8", "#3A2A1E")
    sc = scale_drawing(23.4, 6.6, 6.8, pw=4)
    check = C(7.4, 4, 3.6, GREEN, INK, 1.1) + P("M5.6 4l1.3 1.4 2.5-2.8", "none", WHITE, 1.4)
    return {"@6": ("0 0 32 32", fig + sc + check, "Ein aufrechter Mensch mit grünem Häkchen über dem Kopf steht neben einer Waage im Gleichgewicht")}


@runde3("FIG-ZEICHEN-KIND")
def kind3():
    """Mk 10,16: Kind als Hauptmotiv mit Kinderproportionen; eine Hand (Handbibliothek) liegt segnend auf seinem Kopf."""
    var = Z2["FIG-ZEICHEN-KIND"]()  # Kinderfigur aus Runde 2 wiederverwenden
    _, s5, _ = var["@5"]
    child = s5.split('<path d="M20.25', 1)[0] if False else None
    def ch(cx, foot, body, hair, s):
        hr = 5.6 * s
        hy = foot - 15.6 * s
        return (P(f"M{cx - 2.4 * s} {foot - 9 * s}Q{cx - 5.4 * s} {foot - 8.6 * s} {cx - 5.8 * s} {foot - 1.6 * s}H{cx + 5.8 * s}Q{cx + 5.4 * s} {foot - 8.6 * s} {cx + 2.4 * s} {foot - 9 * s}Z", body, INK, 1.2)
                + P(f"M{cx - 2.2 * s} {foot - 1.8 * s}v{1.6 * s}M{cx + 2.2 * s} {foot - 1.8 * s}v{1.6 * s}", "none", INK, 2 * s)
                + C(cx, hy, hr, SKIN, INK, 1.2)
                + P(f"M{cx - hr:.2f} {hy - .4 * s:.2f}q0-{hr:.2f} {hr:.2f}-{hr:.2f}t{hr:.2f} {hr:.2f}q-{hr * .7:.2f}-{hr * .9:.2f}-{hr:.2f}-{hr * .3:.2f}q-{hr * .3:.2f} {hr * .6:.2f}-{hr:.2f} {hr * .3:.2f}z", hair, INK, .8)
                + C(cx - 2.1 * s, hy + .8 * s, .75 * s, INK, None) + C(cx + 2.1 * s, hy + .8 * s, .75 * s, INK, None)
                + C(cx - 3.4 * s, hy + 2.6 * s, 1 * s, "#F09A8A", None) + C(cx + 3.4 * s, hy + 2.6 * s, 1 * s, "#F09A8A", None)
                + P(f"M{cx - 1.6 * s} {hy + 2.8 * s}q{1.6 * s} {1.8 * s} {3.2 * s} 0", "none", INK, .8))
    s6 = ch(14, 31.4, GOLD, "#5A3A22", 1.3) + H.place(H.hand_gebend("#F4ECD8"), 4.6, 2.6, 12, .72)
    adult = person(21, 31.4, 1.28, "#6E8EAE", "#3A2A1E")
    s7 = adult + ch(10.6, 31.4, GOLD, "#5A3A22", 1.0)
    return {"@6": ("0 0 32 32", s6, "Kleines Kind mit grossem Kopf und rosigen Wangen; von oben liegt eine Hand segnend auf seinem Kopf"),
            "@7": ("0 0 32 32", s7, "Kleines Kind mit grossem Kopf vorn, daneben ein Erwachsener, der doppelt so gross ist")}


@runde3("FIG-ZEICHEN-BITTER")
def bitter3():
    face = (emoji(11.6, 15, 10.4)
            + P("M5.4 11.2l3.6 1.6-3.6 1.6M17.8 11.2l-3.6 1.6 3.6 1.6", "none", INK, 1.4)
            + P("M5 8.6q2-1.6 4-1M18.2 8.6q-2-1.6-4-1", "none", INK, 1.2)
            + P("M7.6 21Q9.2 19.4 10.6 21T13.6 21 15.8 20.6", "none", INK, 1.4))
    herbs = ""
    for x, a in ((25.6, -14), (28.2, 6), (30.6, 22)):
        herbs += (f'<g transform="rotate({a} {x} 30)">' + P(f"M{x} 30V15", "none", "#3E5A22", 1.2)
                  + P(f"M{x} 15.6q-3 2-1.6 4.4 1.6-.6 1.6-2.4 0 1.8 1.6 2.4 1.4-2.4-1.6-4.4zM{x} 20.6q-3 1.6-1.6 3.8 1.4-.4 1.6-1.8.2 1.4 1.6 1.8 1.4-2.2-1.6-3.8z", "#5E7A34", INK, .7) + "</g>")
    herbs += P("M23.4 29.4h9.2", "none", "#8A6A3A", 2.2)
    return {"@6": ("0 0 33 32", face + herbs, "Gelbes Gesicht mit zugekniffenen Augen und welligem Mund (bitterer Geschmack), daneben ein Büschel dunkelgrüner Bitterkräuter")}


@runde3("FIG-ZEICHEN-TOERICHT")
def toericht3():
    """Narrenkappe (Tor, Narr): Emoji-Gesicht mit Schellenkappe; Fassung 7: die Kappe allein."""
    def cap(ox, oy, s=1.0):
        g = (P("M2 16Q4 6 1 1.6Q9 3 13 12Q16 2 19 12Q23 3 31 1.6Q28 6 30 16Z", "#C8323C", INK, 1.3)
             + P("M13 12Q14.6 14 16 16H2", "none", "none", 0)
             + P("M16 4.8Q14 9 13 12L16 16 19 12Q18 9 16 4.8Z", GOLD, INK, 1.1)
             + C(1, 1.8, 1.8, GOLD, INK, 1) + C(16, 3.4, 1.8, GOLD, INK, 1) + C(31, 1.8, 1.8, GOLD, INK, 1)
             + P("M1.6 15.4h28.8v2.6H1.6z", GOLD, INK, 1.1))
        return f'<g transform="translate({ox} {oy}) scale({s})">{g}</g>'
    face = (emoji(16, 23, 9.6)
            + C(12.4, 21.4, 1.1, INK, None) + C(19.6, 21.4, 1.1, INK, None)
            + P("M11 25.6q5 4.6 10 0", "none", INK, 1.4) + P("M15.4 27.4q.6 2.6 2.4 1.6.8-.8.4-2", "#E8707A", INK, .8))
    s6 = face + cap(4.4, 2, .72)
    s7 = cap(0, 4, 1.0)
    return {"@6": ("0 0 32 33", s6, "Gelbes Emoji-Gesicht mit einfältigem Grinsen trägt eine rot-goldene Narrenkappe mit drei Schellen"),
            "@7": ("0 0 32 33", s7, "Rot-goldene Narrenkappe mit drei Zipfeln und Schellen")}


@runde3("FIG-ZEICHEN-VERBORGEN")
def verborgen3():
    """«Im Verborgenen»: der Mensch hinter der geschlossenen Tür ist nur als gestrichelter Umriss gezeigt (verdeckt, ungesehen)."""
    wall = (P("M1 31.4V6H31V31.4Z", "#E9DDBF", INK, 1.5) + P("M1 6L16 .6 31 6", "none", "#B5553A", 2.2)
            + P("M19.4 31.4V12.6H28.4V31.4Z", "#9A6A3A", INK, 1.3) + C(26.4, 22.4, 1, INK, None)
            + P("M18.4 18.4h11", "none", INK, 1.8) + P("M.4 31.6h31.2", "none", INK, 1.6))
    dash = ' stroke-dasharray="1.6 1.2"'
    ghost = (P("M4 30.6H13Q13.6 27.6 11 27L11 20.4Q10.4 17.6 7.6 17.6Q4.4 17.6 3.8 21Q3.4 26 4 30.6Z", "none", "#5E7FA8", 1.2, dash)
             + P("M7.8 15.6m-3.2 0a3.2 3.2 0 1 0 6.4 0a3.2 3.2 0 1 0-6.4 0", "none", "#5E7FA8", 1.2, dash))
    s6 = wall + ghost
    return {"@6": ("0 0 32 32", s6, "Hauswand mit geschlossener, verriegelter Tür; dahinter, nur als gestrichelter Umriss, ein kniender Mensch (verborgen)")}


@runde3("FIG-ZEICHEN-VERGEBUNG")
def vergebung3():
    """Reinigung als Vorgang: dunkles, beflecktes Herz → helles, reines Herz mit Funkeln (Jes 1,18)."""
    def heart(x, y, s, fill, stroke=INK):
        return (f'<g transform="translate({x} {y}) scale({s})">'
                + P("M10 18.6Q1 12.6 1.4 6.8 1.8 2.2 5.8 2.2 8.6 2.2 10 5 11.4 2.2 14.2 2.2 18.2 2.2 18.6 6.8 19 12.6 10 18.6Z", fill, stroke, 1.4 / s) + "</g>")
    dark = heart(0, 6, .82, "#5A2E3A") + C(5, 13, 1.4, "#3A1A22", None) + C(9.4, 16, 1, "#3A1A22", None)
    arrow = P("M16.6 15.4h3.4", "none", INK, 1.8) + P("M19.6 13l3 2.4-3 2.4z", INK, INK, .6)
    light = heart(22.6, 4, 1.0, "#FFF8E6") + sparkle(37, 6, 2.6) + sparkle(25.6, 20.6, 1.6)
    s6 = dark + arrow + light
    return {"@6": ("0 0 42 26", s6, "Links ein kleines dunkles, beflecktes Herz, Pfeil, rechts ein grosses weisses, reines Herz mit goldenem Funkeln")}


@runde3("FIG-ZEICHEN-STAMMBAUM")
def stammbaum3():
    """Ahnentafel wie im Leitsystem: drei Brustbilder treppenförmig (Grossvater → Vater → Sohn), durch Linien verbunden."""
    def bust(cx, cy, body, hair, beard=None, r=3.6):
        g = P(f"M{cx - 4.6} {cy + 9}Q{cx - 4.6} {cy + 4.4} {cx} {cy + 4.4}T{cx + 4.6} {cy + 9}Z", body, INK, 1.1) + C(cx, cy, r, SKIN, INK, 1.1)
        g += P(f"M{cx - r:.2f} {cy - .1:.2f}q0-{r:.2f} {r:.2f}-{r:.2f}t{r:.2f} {r:.2f}q-{r:.2f}-{r / 2:.2f}-{2 * r:.2f} 0z", hair, INK, .7)
        if beard:
            g += P(f"M{cx - r * .85:.2f} {cy + .4:.2f}Q{cx:.2f} {cy + r * 1.9:.2f} {cx + r * .85:.2f} {cy + .4:.2f}Q{cx:.2f} {cy + r * .8:.2f} {cx - r * .85:.2f} {cy + .4:.2f}Z", beard, INK, .6)
        g += C(cx - r * .38, cy + .1, .45, INK, None) + C(cx + r * .38, cy + .1, .45, INK, None)
        return g
    lines = P("M10.4 13.4V17.6H16.4M16.4 13.4", "none", "none", 0) + P("M6 13.6V18.4H12.6M16.4 23V27.6H22.8", "none", "#8A5E36", 1.8)
    leaf = (f'<ellipse cx="9.4" cy="17.4" rx="2" ry=".9" transform="rotate(-30 9.4 17.4)" fill="{LEAF}" stroke="{INK}" stroke-width=".5"/>'
            f'<ellipse cx="19.8" cy="26.6" rx="2" ry=".9" transform="rotate(-30 19.8 26.6)" fill="{LEAF}" stroke="{INK}" stroke-width=".5"/>')
    s6 = (lines + leaf + bust(6, 4.4, "#A89E88", "#8A8A8A", "#E6E2DA") + bust(16.4, 14, "#6E8EAE", "#5A3A22", "#5A3A22")
          + bust(26.6, 23.4, GOLD, "#3A2A1E"))
    return {"@6": ("0 0 32 33", s6, "Drei Brustbilder treppenförmig von links oben nach rechts unten, mit braunen Linien verbunden: alter Mann mit weissem Bart, Mann mit Bart, junger Mann")}


@runde3("FIG-ZEICHEN-LOESERECHT")
def loeserecht3():
    """Rut 4,7 als klare Zwei-Hände-Geste: eine Hand von oben gibt eine Sandale (Seitenansicht wie der Gegenstand «Sandale») in
    eine offene Hand."""
    sandal = ('<g transform="translate(5 11.6) rotate(-6 17 10) scale(.66)">'
              + P("M2.4 13.4Q2.6 17 5.4 17.6H28Q32.8 17.2 33 14.4V12.6Q31 15 27 15H5.4Q2.6 15 2.4 12.6z", "#6E4A26", INK, 1.2)
              + P("M2.4 12.6Q1.6 9.4 5.6 9.4 12 10 18 9 26 7.6 31 9.6 34 11 33 12.6 31 15 27 15H5.4Q2.6 15 2.4 12.6z", "#B07E44", INK, 1.2)
              + thick("M14 13.2Q15.6 5.2 21 5.8 25.6 6.6 28.4 11.8", "#8A5E36", 1.6, .9)
              + thick("M4.6 13Q3.8 6.4 8.8 5.8 12.2 5.6 13.4 12.8", "#8A5E36", 1.6, .9) + "</g>")
    sandal = sandal.replace('translate(5 11.6) rotate(-6 17 10) scale(.66)', 'translate(4.4 9.6) rotate(-4 17 10) scale(.62)')
    give = H.place(H.hand_gebend("#7E5A8E"), 33.4, 6.2, 0, 1.0, True)
    take = H.place(H.hand_empfangend("#5E7FA8"), 4.6, 22.6, 0, 1.15)
    return {"@6": ("0 0 34 32", take + sandal + give, "Eine Hand von oben übergibt eine Sandale (Seitenansicht, Riemen) in eine offene Hand darunter")}


@runde3("FIG-ZEICHEN-FRIEDEN")
def frieden3():
    """🫂 mit Händen aus der Handbibliothek: zwei Menschen Seite an Seite, je eine Hand (hand_auf_schulter) liegt auf der
    fernen Schulter des anderen; die Arme liegen hinter den Rücken."""
    g = person(9.8, 31, 1.08, "#6E8EAE", "#3A2A1E", "happy") + person(22.2, 31, 1.08, "#B0704A", "#5A3A22", "happy")
    g += H.place(H.hand_auf_schulter("#B0704A"), 9.2, 18.6, 0, .6, True) + H.place(H.hand_auf_schulter("#6E8EAE"), 22.8, 18.6, 0, .6)
    return {"@7": ("0 0 32 32", g, "Zwei Menschen Seite an Seite, lächelnd mit geschlossenen Augen, jeder legt eine Hand auf die ferne Schulter des anderen (Arme hinter dem Rücken)")}


@runde3("FIG-ZEICHEN-VOLLMACHT")
def vollmacht3b():
    """Wie vom Gutachten vorgeschlagen: eine Hand (Faust aus der Handbibliothek) umgreift ein Zepter mit verziertem Kopf."""
    stab = (P("M8.6 -18V10", "none", INK, 4.4) + P("M8.6 -18V10", "none", GOLD, 2.4)
            + C(8.6, -21.4, 4, GOLD, INK, 1.3) + C(8.6, -21.4, 1.7, RED, INK, .7)
            + P("M5.6 -24.4l1-3 1.9 1.8 .1-2.6.1 2.6 1.9-1.8 1 3", GOLD, INK, .9))
    g = H.place(H.hand_faust("#8E3A4A", griff=stab), 6, 26, 0, 1.0)
    rays = P("M7.4 2.4l-2.6-1.4M7 8l-2.8.4M21.8 2.4l2.6-1.4M22.2 8l2.8.4", "none", GOLD, 1.4)
    return {"@8": ("0 0 32 40", rays + g, "Eine Hand (Faust mit rotem Ärmel) umgreift ein goldenes Zepter mit verziertem Kopf (Krönchen, roter Stein)")}


# ---------------------------------------------------------------- Wahl nach Gestaltungskritik und Blindtest
WAHL = {}  # {"FIG-ZEICHEN-…": "@1"} – nach den Tests eingetragen

LEX = pathlib.Path(__file__).resolve().parents[2] / "data/illustrations/lexicon"
OUT = pathlib.Path(__file__).resolve().parent / "bildsymbole_daten/ueberarbeitet/begriffe2.json"


def fit(res, pad=0.5):
    """viewBox an den gezeichneten Inhalt anpassen: jede Fassung im Browser auf eine Leinwand rastern und die gefärbten
    Pixel messen (mit Konturen); dann viewBox = Inhalt plus schmaler Rand. Nichts abgeschnitten, kein leerer Rand, der das
    Zeichen in Einsatzgrösse verkleinert."""
    import os
    import subprocess
    import tempfile
    keys = list(res)
    data = [[res[k]["svg"], res[k]["vb"]] for k in keys]
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
        json.dump(data, f)
    mod = os.environ.get("PLAYWRIGHT_MODULE", "/opt/npm-tools/node_modules/playwright")
    js = (f"const {{chromium}}=require('{mod}');const fs=require('fs');const D=JSON.parse(fs.readFileSync('{f.name}','utf8'));"
          "(async()=>{const b=await chromium.launch();const p=await b.newPage();const r=await p.evaluate(async(D)=>{const out=[];"
          "for(const [svg,vb] of D){const [x0,y0,w0,h0]=vb.split(' ').map(Number);const M=8;const X=x0-M,Y=y0-M,W=w0+2*M,H=h0+2*M;const S=20;"
          "const src='<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"'+[X,Y,W,H].join(' ')+'\" width=\"'+W*S+'\" height=\"'+H*S+'\">'+svg+'</svg>';"
          "const img=new Image();img.src='data:image/svg+xml;charset=utf-8,'+encodeURIComponent(src);await img.decode();"
          "const c=document.createElement('canvas');c.width=W*S;c.height=H*S;const g=c.getContext('2d');g.drawImage(img,0,0);"
          "const d=g.getImageData(0,0,c.width,c.height).data;let a=1e9,bb=1e9,cc=-1,dd=-1;"
          "for(let y=0;y<c.height;y++)for(let x=0;x<c.width;x++){if(d[(y*c.width+x)*4+3]>20){if(x<a)a=x;if(x>cc)cc=x;if(y<bb)bb=y;if(y>dd)dd=y;}}"
          "out.push([X+a/S,Y+bb/S,(cc-a+1)/S,(dd-bb+1)/S]);}return out;},D);console.log(JSON.stringify(r));await b.close();})();")
    out = json.loads(subprocess.run(["node", "-e", js], capture_output=True, text=True, check=True).stdout)
    os.unlink(f.name)
    for k, (x, y, w, h) in zip(keys, out):
        # Ursprung auf 0 0 schieben: <use> auf ein <symbol> setzt den Ursprung des äusseren viewBox voraus
        x0, y0 = round(x - pad, 1), round(y - pad, 1)
        if x0 or y0:
            res[k]["svg"] = f'<g transform="translate({-x0:g} {-y0:g})">{res[k]["svg"]}</g>'
        res[k]["vb"] = f"0 0 {w + 2 * pad:.1f} {h + 2 * pad:.1f}"
    return res


def alle(ids=None):
    res = {}
    for fid, fn in Z.items():
        if ids and fid not in ids:
            continue
        lx = json.loads((LEX / f"{fid}.json").read_text(encoding="utf-8"))
        bed = lx["names"]["de"] + " – " + lx.get("identity_de", "").replace("Bedeutung: ", "")[:200]
        var = dict(fn())
        if fid in Z2:
            var.update(Z2[fid]())
        if fid in Z3:
            var.update(Z3[fid]())
        for v, (vb, svg, gez) in var.items():
            res[fid + v] = {"vb": vb, "svg": svg, "bedeutung": bed, "gezeichnet": gez}
    return res


def main():
    a = sys.argv[1:]
    if a and a[0] == "--entwuerfe":
        out = pathlib.Path(a[1])
        ids = [x if x.startswith("FIG-") else "FIG-ZEICHEN-" + x for x in a[2:]]
        r = fit(alle(ids or None))
        out.write_text(json.dumps(r, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"PASS: {len(r)} Fassungen nach {out}")
    elif a and a[0] == "--schreiben":
        r = fit(alle())
        data = {fid: {"vb": r[fid + v]["vb"], "svg": r[fid + v]["svg"]} for fid, v in sorted(WAHL.items())}
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"PASS: {len(data)} Zeichen nach {OUT}")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
