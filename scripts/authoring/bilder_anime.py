#!/usr/bin/env python3
"""Autorenwerkzeug: Bildstil «Anime» (Pilot) – comicartige Bilder ohne Text zu den bestehenden Bildaufträgen.

Gleiche Schichten wie beim Stil «Symbol» (docs/BILDSPRACHE.md): Bildlexikon und Bildauftrag bleiben unverändert,
nur die Darstellung wechselt. Unterschiede zum Symbolstil:
- Personen mit Gesicht und Ausdruck (Sorge, Ruhe, Entschlossenheit, Staunen, Freude), Züge und Hautton der Levante
  im 1. Jahrhundert, keine Karikatur; Gott nie als Mensch.
- Manga-Panels mit schrägen Rändern, Brustbilder und Nahaufnahmen, Bewegungs- und Emotionszeichen.
- Sprechblasen nur mit Zeichen (keine Schrift), damit das Bild für alle Sprachen taugt.
Gegenstände und Zeichen übernimmt der Stil aus der Symbol-Bibliothek (umbenannt auf «an-»), damit ein Krug, ein Becher
oder die Sanduhr in beiden Stilen gleich gelesen werden.

Aufruf: python3 scripts/authoring/bilder_anime.py
KI-Entwurf (Claude) vom 2026-10-17 auf Wunsch von Andi Neck; eigene Zeichnungen (CC0), keine fachliche Prüfung.
"""
import json
import math
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _bubble import bubble_path  # noqa: E402
from _lib import D, localize, write  # noqa: E402

DATE = "2026-10-17"
AUTH = "KI-Entwurf (Claude) vom 2026-10-17 auf Wunsch von Andi Neck; eigene Zeichnung, keine fachliche Prüfung."
AUTH_GSW = "KI-Entwurf (Claude) vom 2026-10-17; Mundart noch nicht muttersprachlich geprüft."
LIC = "CC0 1.0 (eigene Zeichnung)"
OUT = D / "illustrations/anime"
SYM_LIB = D / "illustrations/symbol/_bibliothek.svg"

INK, SKIN, SKIN_D, BUBBLE = "#2B211A", "#C98E62", "#A8714A", "#FFFFFF"
HAIR = "#2E2017"

# ---------------------------------------------------------------- Figuren (Kopf in Einheiten: Radius 10)
FACE = "M-10 -1Q-10 9 0 12.6Q10 9 10 -1A10 10.6 0 0 0 -10 -1z"


def eyes(expr, look):
    out = []
    for side in (-1, 1):
        ex, ey = side * 4.2 + look * 1.4, 2.4
        if expr in ("smile",):
            out.append(f'<path d="M{ex - 2:.1f} {ey + .4:.1f}Q{ex:.1f} {ey - 2:.1f} {ex + 2:.1f} {ey + .4:.1f}" fill="none" stroke="{INK}" stroke-width="1.1" stroke-linecap="round"/>')
            continue
        if expr == "surprised":
            out.append(f'<ellipse cx="{ex:.1f}" cy="{ey:.1f}" rx="2.1" ry="2.5" fill="#FFF" stroke="{INK}" stroke-width=".7"/>'
                       f'<circle cx="{ex + look * .5:.1f}" cy="{ey + .2:.1f}" r=".95" fill="{INK}"/>')
            continue
        iris = "#3A2416"
        out.append(f'<ellipse cx="{ex:.1f}" cy="{ey:.1f}" rx="1.75" ry="2.35" fill="{iris}"/>'
                   f'<path d="M{ex - 2.4:.1f} {ey - 1.6:.1f}Q{ex:.1f} {ey - 3.3:.1f} {ex + 2.4:.1f} {ey - 1.6:.1f}" fill="none" stroke="{INK}" stroke-width="1" stroke-linecap="round"/>')
        if expr == "delight":
            sx, sy = ex + .2, ey - .4
            out.append(f'<path d="M{sx:.1f} {sy - 1.3:.1f}l.35 .95.95 .35-.95 .35-.35 .95-.35-.95-.95-.35.95-.35z" fill="#FFF"/>')
        else:
            out.append(f'<circle cx="{ex + .6:.1f}" cy="{ey - .8:.1f}" r=".6" fill="#FFF"/>')
    return "".join(out)


def brows(expr, look, color):
    d = []
    for side in (-1, 1):
        ex = side * 4.2 + look * 1.4
        if expr == "worried":
            a, b = (-3.0, -4.3) if side < 0 else (-4.3, -3.0)
        elif expr == "determined":
            a, b = (-4.0, -2.9) if side < 0 else (-2.9, -4.0)
        elif expr == "surprised":
            a, b = (-4.6, -4.6)
        elif expr == "earnest":
            a, b = (-3.1, -3.1)
        else:
            a, b = (-3.4, -3.4)
        mid = min(a, b) - (.8 if expr in ("calm", "smile", "delight", "surprised") else .2)
        d.append(f"M{ex - 2.2:.1f} {a:.1f}Q{ex:.1f} {mid:.1f} {ex + 2.2:.1f} {b:.1f}")
    return f'<path d="{"".join(d)}" fill="none" stroke="{color}" stroke-width=".9" stroke-linecap="round"/>'


def mouth(expr, look):
    x = look * 1.0
    if expr == "worried":
        return f'<path d="M{x - 1.8:.1f} 8.3q.9-.8 1.8 0t1.8 0" fill="none" stroke="{INK}" stroke-width=".8" stroke-linecap="round"/>'
    if expr == "surprised":
        return f'<ellipse cx="{x:.1f}" cy="8.4" rx="1.1" ry="1.4" fill="#6B2A2A"/>'
    if expr in ("determined", "earnest"):
        return f'<path d="M{x - 1.5:.1f} 8.2h3" stroke="{INK}" stroke-width=".85" stroke-linecap="round"/>'
    if expr in ("smile",):
        return f'<path d="M{x - 2.2:.1f} 7.6Q{x:.1f} 9.8 {x + 2.2:.1f} 7.6" fill="none" stroke="{INK}" stroke-width=".9" stroke-linecap="round"/>'
    if expr == "delight":
        return f'<path d="M{x - 2.6:.1f} 7.3Q{x:.1f} 11.2 {x + 2.6:.1f} 7.3z" fill="#7A2E2E"/>'
    return f'<path d="M{x - 1.5:.1f} 8.1Q{x:.1f} 8.9 {x + 1.5:.1f} 8.1" fill="none" stroke="{INK}" stroke-width=".8" stroke-linecap="round"/>'


def blush():
    return '<ellipse cx="-6.2" cy="5.8" rx="1.9" ry=".9" fill="#E07A6E" opacity=".55"/><ellipse cx="6.2" cy="5.8" rx="1.9" ry=".9" fill="#E07A6E" opacity=".55"/>'


CHAR = {
    # Haar hinten, Haar vorne, Bart, Gewand, Mantel, Kopfschmuck
    "jesus": dict(hair=HAIR, back="M-10.6 -2Q-12.5 9-10 17L-5.6 16Q-8.4 7-7.6-1z M10.6 -2Q12.5 9 10 17L5.6 16Q8.4 7 7.6-1z",
                  front="M-10.6-1Q-10.5-11.6 0-12Q10.5-11.6 10.6-1Q7-6.4 .8-7.6L0-5.4-.8-7.6Q-7-6.4-10.6-1z",
                  beard="M-8.2 5.6Q-7.6 12.8 0 14.2Q7.6 12.8 8.2 5.6Q6.6 10.4 0 11Q-6.6 10.4-8.2 5.6z",
                  robe="#F4F1EA", mantle="#A33A2E", halo=True),
    "maria": dict(hair="#3A2618", veil="#2E5478", front="M-7.6-3.6Q0-8.4 7.6-3.6Q4-5.2 0-5Q-4-5.2-7.6-3.6z", robe="#3E6E9E", mantle="#2E5478"),
    "diener": dict(hair="#24180F", front="M-10.6-.4Q-11-11.6 0-12Q11-11.6 10.6-.4Q9-5.4 5-6.8Q1-4.6-3-6.8Q-8-5.4-10.6-.4z",
                   robe="#B8A98A", apron=True),
    "diener2": dict(hair="#3A2A1C", front="M-10.6 0Q-11.4-10.8 0-11.8Q11.4-10.8 10.6 0Q8.4-7 0-7.4Q-8.4-7-10.6 0z",
                    robe="#A8987A", apron=True),
    "meister": dict(hair="#6A5646", front="M-10.6 1Q-10.8-6-8.6-8.6Q-6-6.8-6.4-1z M10.6 1Q10.8-6 8.6-8.6Q6-6.8 6.4-1z",
                    mustache=True, robe="#4F7A4A", belt="#D9A441"),
    "braeutigam": dict(hair="#24180F", front="M-10.6-.4Q-11-11.6 0-12Q11-11.6 10.6-.4Q8-6 0-6.6Q-8-6-10.6-.4z",
                       beard="M-8 6.4Q-7 12.4 0 13.4Q7 12.4 8 6.4Q6 10 0 10.6Q-6 10-8 6.4z", robe="#5A3E7A", trim="#D9A441", wreath=True),
    "braut": dict(hair="#2E2017", veil="#FFFFFF", front="M-8-3.4Q0-8.6 8-3.4Q4-5.4 0-5.2Q-4-5.4-8-3.4z", robe="#FBF3E4", flowers=True),
    "juenger": dict(hair="#2E2017", curls=True, beard="M-8 6.4Q-7 12 0 13Q7 12 8 6.4Q6 9.8 0 10.4Q-6 9.8-8 6.4z", robe="#9C7A4C", belt="#5B4630"),
    "juenger2": dict(hair="#4A3020", front="M-10.6 0Q-11.4-10.8 0-11.8Q11.4-10.8 10.6 0Q6-8.2-1-7Q-7-6.4-10.6 0z", robe="#8A6A40", belt="#5B4630"),
    "gast": dict(hair="#2E2017", front="M-10.6-.4Q-11-11.6 0-12Q11-11.6 10.6-.4Q8-6 0-6.6Q-8-6-10.6-.4z", robe="#B4A98F"),
    "haendler": dict(hair="#2E2017", veil="#E9D8B4", front="M-7.6-3.6Q0-8.4 7.6-3.6Q4-5.2 0-5Q-4-5.2-7.6-3.6z",
                     beard="M-8 6.4Q-7 12.4 0 13.4Q7 12.4 8 6.4Q6 10 0 10.6Q-6 10-8 6.4z", robe="#C2884A", belt="#8A6A3A"),
    "menge": dict(hair="#2E2017", front="M-10.6-.4Q-11-11.6 0-12Q11-11.6 10.6-.4Q8-6 0-6.6Q-8-6-10.6-.4z",
                  beard="M-8 6.4Q-7 12.4 0 13.4Q7 12.4 8 6.4Q6 10 0 10.6Q-6 10-8 6.4z", robe="#8E9AAF", sash="#6F7B8F"),
    "menge2": dict(hair="#3A2618", veil="#B9A88C", front="M-7.6-3.6Q0-8.4 7.6-3.6Q4-5.2 0-5Q-4-5.2-7.6-3.6z", robe="#9AA6B8", sash="#7A8698"),
    "menge3": dict(hair="#24180F", front="M-10.6 0Q-11.4-10.8 0-11.8Q11.4-10.8 10.6 0Q6-8.2-1-7Q-7-6.4-10.6 0z", robe="#8592A6", sash="#6F7B8F"),
    "gast2": dict(hair="#3A2618", veil="#C7B9D6", front="M-7.6-3.6Q0-8.4 7.6-3.6Q4-5.2 0-5Q-4-5.2-7.6-3.6z", robe="#8FA3A0"),
}


def head_inner(key, expr="calm", look=0.0):
    c = CHAR[key]
    o = []
    if c.get("halo"):
        o.append(f'<circle r="15.5" fill="#F7DB9A" stroke="#D9A441" stroke-width="1.2"/><path d="M0-15.5v5M-15.5 0h5M15.5 0h-5" stroke="#C08A2A" stroke-width="2.2"/>')
    if c.get("veil"):
        o.append(f'<path d="M-13 18Q-14.6-4-9.4-10.6Q0-17 9.4-10.6Q14.6-4 13 18z" fill="{c["veil"]}" stroke="{INK}" stroke-width=".7"/>')
    if c.get("back"):
        o.append(f'<path d="{c["back"]}" fill="{c["hair"]}"/>')
    o.append(f'<path d="M-2.4 11h4.8v6h-4.8z" fill="{SKIN_D}"/>')  # Hals
    o.append(f'<path d="{FACE}" fill="{SKIN}" stroke="{INK}" stroke-width=".7"/>')
    o.append(f'<path d="M-10.3 2.4q-1.8.4-1.2 2.6.6 1.6 1.8 1z M10.3 2.4q1.8.4 1.2 2.6-.6 1.6-1.8 1z" fill="{SKIN}" stroke="{INK}" stroke-width=".5"/>')
    if c.get("beard"):
        o.append(f'<path d="{c["beard"]}" fill="{c["hair"]}" opacity=".92"/>')
    if c.get("mustache"):
        o.append(f'<path d="M{look - 3:.1f} 6.6q3-1.6 6 0" fill="none" stroke="{c["hair"]}" stroke-width="1.3" stroke-linecap="round"/>')
    o.append(eyes(expr, look) + brows(expr, look, c["hair"]))
    o.append(f'<path d="M{look * .8:.1f} 4.8l-.6 1.6h1" fill="none" stroke="{SKIN_D}" stroke-width=".7" stroke-linecap="round"/>')
    if expr in ("delight", "worried") or c.get("flowers"):
        o.append(blush())
    o.append(mouth(expr, look))
    if c.get("curls"):
        o.append("".join(f'<circle cx="{x}" cy="{y}" r="3.1" fill="{c["hair"]}"/>' for x, y in ((-8, -4), (-6, -8.6), (-1.6, -10.6), (3.2, -10.4), (7.2, -8), (8.8, -3.6))))
    elif c.get("front"):
        o.append(f'<path d="{c["front"]}" fill="{c["hair"]}"/>')
    if c.get("veil") and c["veil"] != "#FFFFFF":
        o.append(f'<path d="M-10.4 1Q-11.6-8.8 0-12.2Q11.6-8.8 10.4 1Q9-7.8 0-9.4Q-9-7.8-10.4 1z" fill="{c["veil"]}" stroke="{INK}" stroke-width=".7"/>')
    if c.get("veil") == "#FFFFFF":
        o.append(f'<path d="M-10.6 0Q-11.6-9.6 0-12.4Q11.6-9.6 10.6 0Q9-8 0-9.4Q-9-8-10.6 0z" fill="#FFFFFF" stroke="#B4B2A9" stroke-width=".7"/>')
    if c.get("flowers"):
        o.append("".join(f'<circle cx="{x}" cy="{y}" r="1.7" fill="#D4537E"/>' for x, y in ((-7, -7.8), (-3.6, -10.2), (0, -11), (3.6, -10.2), (7, -7.8))))
    if c.get("wreath"):
        leaves = []
        for a in range(200, 345, 18):
            r = math.radians(a)
            x, y = 10.4 * math.cos(r), 10.4 * math.sin(r) - .6
            leaves.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="2.2" ry=".95" transform="rotate({a + 90 + 25} {x:.1f} {y:.1f})" fill="#D9A441" stroke="#9C6F1C" stroke-width=".35"/>')
        o.append("".join(leaves))
    return "".join(o)


def body_inner(key, arm=None):
    """Brustbild unter dem Kopf (Einheiten wie Kopf); arm = (Winkel in Grad, Länge) für einen zeigenden Arm, oder None."""
    c = CHAR[key]
    o = [f'<path d="M-17 34Q-17 19-7 15.6L7 15.6Q17 19 17 34z" fill="{c["robe"]}" stroke="{INK}" stroke-width=".8"/>']
    if c.get("mantle"):
        o.append(f'<path d="M-7 15.6Q3 17 9 15.8Q16 19 17 34L4 34Q2 24-7 15.6z" fill="{c["mantle"]}" stroke="{INK}" stroke-width=".7"/>')
    if c.get("veil"):
        o.append(f'<path d="M-13 18Q-17 24-17 34h-.4V20zM13 18Q17 24 17 34V20z" fill="{c["veil"]}"/>')
    if c.get("apron"):
        o.append(f'<path d="M-6 22h12v12h-12z" fill="#FFFDF6" stroke="{INK}" stroke-width=".6"/><path d="M-7 22h14" stroke="#8A7A5A" stroke-width="1"/>')
    if c.get("sash"):
        o.append(f'<path d="M-8 16.6L10 34h-5L-11 18.4z" fill="{c["sash"]}"/>')
    if c.get("belt"):
        o.append(f'<path d="M-15.4 28h30.8v2.6h-30.8z" fill="{c["belt"]}"/>')
    if c.get("trim"):
        o.append(f'<path d="M-4 15.8L0 22 4 15.8" fill="none" stroke="{c["trim"]}" stroke-width="1.4"/>')
    if arm:
        ang, ln = arm
        import math
        x0, y0 = (12 if math.cos(math.radians(ang)) >= 0 else -12), 21
        x1, y1 = x0 + ln * math.cos(math.radians(ang)), y0 + ln * math.sin(math.radians(ang))
        sleeve = c.get("mantle") or c["robe"]
        o.append(f'<path d="M{x0} {y0}L{x1:.1f} {y1:.1f}" stroke="{INK}" stroke-width="5.4" stroke-linecap="round"/>'
                 f'<path d="M{x0} {y0}L{x1:.1f} {y1:.1f}" stroke="{sleeve}" stroke-width="4" stroke-linecap="round"/>'
                 f'<circle cx="{x1:.1f}" cy="{y1:.1f}" r="2.3" fill="{SKIN}" stroke="{INK}" stroke-width=".6"/>')
    return "".join(o)


def person(key, x, y, s, expr="calm", look=0.0, arm=None, flip=False):
    """Brustbild: Kopfmitte bei (x, y), s = Massstab (1 = Kopfradius 10)."""
    fl = " scale(-1 1)" if flip else ""
    return f'<g transform="translate({x} {y}) scale({s}){fl}">{body_inner(key, arm)}{head_inner(key, expr, -look if flip else look)}</g>'


# ---------------------------------------------------------------- Zeichen
def sweat(x, y, s=1):
    return f'<path transform="translate({x} {y}) scale({s})" d="M0-4Q3 0 3 2a3 3 0 0 1-6 0Q-3 0 0-4z" fill="#8FC8EE" stroke="#2E6E9E" stroke-width=".7"/>'


def shock(x, y, s=1):
    return f'<g transform="translate({x} {y}) scale({s})" stroke="{INK}" stroke-width="1.2" stroke-linecap="round"><path d="M-6-6l-3-3M0-8v-4M6-6l3-3"/></g>'


def sparkle(x, y, s=1, c="#F2C76E"):
    return f'<path transform="translate({x} {y}) scale({s})" d="M0-5l1.3 3.7 3.7 1.3-3.7 1.3L0 5l-1.3-3.7L-5 0l3.7-1.3z" fill="{c}" stroke="#C08A2A" stroke-width=".5"/>'


def lines_motion(x, y, w, n=3, ang=0):
    return "".join(f'<path d="M{x} {y + i * 5}h{w}" stroke="{INK}" stroke-width="1" stroke-linecap="round" opacity=".55" transform="rotate({ang} {x} {y})"/>' for i in range(n))


def use(sym, x, y, w, h, extra=""):
    return f'<use href="#{sym}" x="{x}" y="{y}" width="{w}" height="{h}"{extra}/>'


def bubble(x, y, w, h, tx, ty, inner):
    """Sprechblase als eine Form mit eingebauter Spitze zur sprechenden Figur (tx, ty), siehe _bubble.py."""
    return f'<g><path d="{bubble_path(x, y, w, h, tx, ty, 12, 5)}" fill="{BUBBLE}" stroke="{INK}" stroke-width="1.6" stroke-linejoin="round"/>{inner}</g>'


def frame(n, pts, body, bg="#F6EAD7", num=None):
    """Manga-Panel als Vieleck (schräge Ränder) mit Nummer oben links."""
    pid = f"an-cp-{n}"
    poly = " ".join(f"{x},{y}" for x, y in pts)
    nx, ny = num or (pts[0][0] + 13, pts[0][1] + 13)
    return (f'<clipPath id="{pid}"><polygon points="{poly}"/></clipPath><g clip-path="url(#{pid})"><polygon points="{poly}" fill="{bg}"/>{body}</g>'
            f'<polygon points="{poly}" fill="none" stroke="{INK}" stroke-width="2.2" stroke-linejoin="round"/>'
            f'<circle cx="{nx}" cy="{ny}" r="8.5" fill="#FFFDF6" stroke="{INK}" stroke-width="1.2"/><text x="{nx}" y="{ny + 4}" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="700" fill="{INK}">{n}</text>')


# ---------------------------------------------------------------- Johannes 2,1–12 (Kana), vier Panels ohne Text
def kana():
    W, H = 380, 446
    p1 = [(4, 4), (376, 4), (376, 150), (4, 160)]
    p2 = [(4, 168), (196, 160), (176, 296), (4, 296)]
    p3 = [(204, 160), (376, 160), (376, 296), (184, 296)]
    p4 = [(4, 304), (376, 304), (376, 442), (4, 442)]
    # 1: Fest im Hintergrund, Maria (besorgt) zu Jesus (ruhig); Antwort Sanduhr
    bg1 = ('<path d="M4 120h372v40H4z" fill="#E7D3B0"/>'
           '<path d="M190 30q50 34 100 0q50 34 90 0" fill="none" stroke="#6E8B3D" stroke-width="3"/>'
           + "".join(f'<circle cx="{x}" cy="{y}" r="3.2" fill="#D4537E"/>' for x, y in ((214, 42), (240, 47), (266, 42), (314, 42), (340, 47), (366, 42)))
           + '<path d="M196 104h176v8H196z" fill="#FFFDF6" stroke="#8A7A5A"/>'
           + person("gast", 216, 78, .95, "smile", .3) + person("braut", 262, 74, 1.0, "smile", -.2)
           + person("braeutigam", 300, 74, 1.0, "smile", -.4) + person("gast2", 346, 80, .95, "smile", -.6)
           + '<rect x="190" y="18" width="186" height="96" fill="#F6EAD7" opacity=".38"/>'
           + use("an-becher-leer", 230, 92, 12, 14) + use("an-becher-leer", 324, 92, 12, 14))
    b1 = bubble(14, 20, 100, 40, 62, 80, use("an-jar-leer", 22, 22, 26, 36) + use("an-becher-leer", 54, 30, 18, 21) + use("an-z-fehlt", 80, 30, 22, 22))
    b2 = bubble(126, 18, 44, 42, 140, 76, use("an-z-stunde", 136, 22, 24, 33))
    s1 = (bg1 + person("maria", 62, 104, 2.1, "worried", .7, arm=(-15, 14)) + sweat(91, 86, 1.1)
          + person("jesus", 150, 104, 2.1, "calm", -1.9) + b1 + b2)
    # 2: Maria (entschlossen) zeigt den Dienern auf Jesus; Diener staunen
    b3 = bubble(26, 178, 120, 40, 54, 228, use("an-jesus-kopf", 34, 180, 36, 36) + use("an-z-pfeil", 76, 192, 22, 11) + use("an-z-hoeren", 104, 182, 34, 30))
    s2 = (person("maria", 52, 250, 1.9, "calm", 1.2, arm=(-14, 18)) + person("diener", 126, 252, 1.45, "surprised", -1.1)
          + person("diener2", 162, 258, 1.35, "surprised", -1.2) + shock(126, 230, .8) + b3)
    # 3: Jesus (ruhig) weist auf die Krüge; ein Diener giesst Wasser ein (Bewegungslinien); Sprechblase Krug → Speisemeister
    jars = "".join(use("an-jar", 244 + i * 16, 248, 15, 30) for i in range(6))
    pour = (f'<g transform="rotate(-70 344 236)">{use("an-jar", 336, 222, 15, 28)}</g>'
            '<path d="M330 238q-4 4-3 10" fill="none" stroke="#4C9BD6" stroke-width="3" stroke-linecap="round"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="1.4" fill="#8FC8EE"/>' for x, y in ((326, 246), (338, 248), (331, 252))))
    b4 = bubble(212, 168, 108, 40, 230, 222, use("an-jar", 222, 172, 18, 32) + use("an-z-pfeil", 246, 183, 24, 12) + use("an-p-meister-kopf", 276, 170, 34, 34))
    s3 = ('<path d="M184 280h192v16H184z" fill="#E7D3B0"/>' + person("jesus", 222, 252, 1.6, "calm", 1.3, arm=(10, 14))
          + jars + person("diener", 360, 240, 1.4, "determined", -1.2) + pour + sweat(374, 222, .8) + b4)
    # 4: Speisemeister kostet (Freude, Funkeln), spricht zum Bräutigam (staunt); Stern über Jesus; Jünger glauben (Herzen)
    b5 = bubble(46, 310, 54, 44, 90, 362, use("an-becher", 59, 314, 28, 33))
    s4 = ('<path d="M4 420h372v22H4z" fill="#E7D3B0"/>'
          + person("diener2", 40, 410, 1.25, "smile", .5) + use("an-jar-wein", 18, 404, 16, 30)
          + person("meister", 98, 386, 2.0, "delight", 1.4, arm=(-40, 14)) + use("an-becher", 136, 388, 15, 18)
          + sparkle(124, 352, 1.1) + sparkle(70, 366, .8) + sparkle(132, 372, .7)
          + person("braeutigam", 176, 388, 1.85, "surprised", -1.3) + shock(176, 356, .9)
          + use("an-zeichen", 252, 314, 24, 24) + person("jesus", 264, 386, 1.7, "smile", .2)
          + person("juenger", 318, 392, 1.5, "delight", -.4) + person("juenger2", 356, 396, 1.4, "delight", -.6)
          + use("an-z-glauben", 307, 340, 20, 22) + use("an-z-glauben", 346, 346, 18, 20) + b5)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#FFFDF6"/>'
            + frame(1, p1, s1) + frame(2, p2, s2) + frame(3, p3, s3, num=(218, 174)) + frame(4, p4, s4) + "</svg>")



# ---------------------------------------------------------------- Johannes 2,13–22 (Tempel), zwei Panels
def tempel():
    W, H = 380, 316
    p1 = [(4, 4), (376, 4), (376, 168), (4, 176)]
    p2 = [(4, 184), (376, 176), (376, 312), (4, 312)]
    bg = ('<path d="M4 132h372v44H4z" fill="#E7D3B0"/>' + use("an-tempel", 150, 8, 200, 150, ' opacity=".5"'))
    table = (f'<g transform="rotate(-24 116 156)"><rect x="84" y="148" width="64" height="8" fill="#B07A3E" stroke="{INK}"/>'
             f'<path d="M92 156v13M140 156v13" stroke="{INK}" stroke-width="3"/></g>')
    coins = "".join(use("an-muenzen", x, y, 20, 12) for x, y in ((86, 118), (124, 104), (104, 90), (150, 160)))
    b1 = bubble(196, 14, 104, 40, 214, 76, use("an-tempel", 204, 18, 40, 30) + use("an-muenzen", 248, 26, 22, 13) + use("an-z-fehlt", 274, 22, 22, 22))
    s1 = (bg + table + coins + lines_motion(16, 132, 22, 3, 8)
          + person("haendler", 46, 112, 1.55, "surprised", -1.2, flip=True) + shock(46, 82, .8)
          + '<g transform="translate(198 124) scale(-1 1)">' + use("an-schaf", 0, 0, 48, 32) + '</g>' + lines_motion(200, 132, 14, 3, 0)
          + use("an-taube-kaefig", 316, 96, 46, 46)
          + person("jesus", 228, 116, 1.9, "earnest", -1.2, arm=(-125, 18)) + '<g transform="translate(190 95) scale(-1 1)">' + use("an-peitsche", 0, 0, 30, 36) + '</g>' + b1)
    b2 = bubble(36, 192, 70, 40, 66, 252, use("an-zeichen", 44, 196, 30, 30) + use("an-z-frage", 80, 196, 16, 28))
    suns = "".join(use("an-sonne", 252 + i * 15, 214, 13, 13) for i in range(3))
    b3 = bubble(158, 190, 214, 46, 314, 250, use("an-tempel-riss", 166, 194, 46, 36) + use("an-z-pfeil", 218, 213, 26, 13) + suns
                + use("an-z-pfeil", 302, 213, 26, 13) + use("an-tempel", 332, 198, 34, 26))
    s2 = ('<path d="M4 290h372v22H4z" fill="#E7D3B0"/>'
          + person("menge2", 30, 282, 1.45, "determined", .8) + person("menge", 66, 274, 1.6, "determined", 1.0)
          + person("menge3", 104, 286, 1.4, "calm", 1.0) + person("jesus", 314, 278, 1.8, "earnest", -1.2, arm=(196, 14)) + b2 + b3)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#FFFDF6"/>'
            + frame(1, p1, s1) + frame(2, p2, s2) + "</svg>")


# ---------------------------------------------------------------- Johannes 2,23–25, ein Panel
def glaube():
    W, H = 380, 210
    p1 = [(4, 4), (376, 4), (376, 206), (4, 206)]
    crowd = (person("menge2", 34, 150, 1.5, "delight", .9) + person("menge", 76, 140, 1.7, "delight", 1.0)
             + person("menge3", 120, 152, 1.5, "delight", .9) + person("menge2", 162, 160, 1.3, "delight", .8))
    stars = use("an-zeichen", 40, 24, 26, 26) + use("an-zeichen", 96, 12, 20, 20) + use("an-zeichen", 146, 28, 24, 24)
    hearts = "".join(use("an-z-glauben", x, y, 20, 22) for x, y in ((24, 92), (66, 80), (110, 94), (152, 106)))
    s1 = ('<path d="M4 184h372v22H4z" fill="#E7D3B0"/>' + use("an-tempel", 226, 14, 150, 112, ' opacity=".45"')
          + stars + hearts + crowd + use("an-z-abstand", 210, 78, 12, 120)
          + person("jesus", 296, 148, 1.9, "earnest", 1.6, flip=True))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#FFFDF6"/>' + frame(1, p1, s1) + "</svg>")


# ---------------------------------------------------------------- Bibliothek
COPY = ["ill-jar", "ill-jar-leer", "ill-jar-wein", "ill-traube", "ill-becher", "ill-becher-leer", "ill-z-fehlt", "ill-z-stunde", "ill-z-hoeren",
        "ill-z-pfeil", "ill-zeichen", "ill-z-glauben", "ill-z-freude", "ill-z-hochzeit", "ill-tempel", "ill-tempel-riss", "ill-sonne",
        "ill-peitsche", "ill-schaf", "ill-taube-tier", "ill-taube-kaefig", "ill-muenzen", "ill-z-frage", "ill-z-abstand"]
PORTRAITS = {"FIG-JESUS": ("jesus", "calm"), "FIG-MARIA-MUTTER-JESU": ("maria", "calm"), "FIG-ROLLE-DIENER": ("diener", "calm"),
             "FIG-ROLLE-SPEISEMEISTER": ("meister", "calm"), "FIG-ROLLE-BRAEUTIGAM": ("braeutigam", "calm"), "FIG-ROLLE-BRAUT": ("braut", "calm"),
             "FIG-ROLLE-GAST": ("gast", "calm"), "FIG-ROLLE-JUENGER": ("juenger", "calm"), "FIG-ROLLE-HAENDLER": ("haendler", "calm"),
             "FIG-GRUPPE-MENGE": ("menge", "calm")}
OBJ = {"FIG-OBJ-KRUG-WASSER": "an-jar", "FIG-OBJ-KRUG-WEIN-LEER": "an-jar-leer", "FIG-OBJ-KRUG-WEIN": "an-jar-wein", "FIG-OBJ-BECHER-VOLL": "an-becher",
       "FIG-OBJ-BECHER-LEER": "an-becher-leer", "FIG-ZEICHEN-FEHLT": "an-z-fehlt", "FIG-ZEICHEN-STUNDE": "an-z-stunde", "FIG-ZEICHEN-HOEREN": "an-z-hoeren",
       "FIG-ZEICHEN-BRINGEN": "an-z-pfeil", "FIG-ZEICHEN-STERN": "an-zeichen", "FIG-ZEICHEN-GLAUBEN": "an-z-glauben", "FIG-ZEICHEN-FREUDE": "an-z-freude",
       "FIG-ZEICHEN-HOCHZEIT": "an-z-hochzeit", "FIG-ORT-TEMPEL": "an-tempel", "FIG-ZEICHEN-NIEDERREISSEN": "an-tempel-riss", "FIG-ZEICHEN-TAGE": "an-sonne",
       "FIG-OBJ-PEITSCHE": "an-peitsche", "FIG-OBJ-SCHAF": "an-schaf", "FIG-OBJ-TAUBE": "an-taube-kaefig", "FIG-OBJ-MUENZEN": "an-muenzen",
       "FIG-ZEICHEN-FRAGEN": "an-z-frage", "FIG-ZEICHEN-ABSTAND": "an-z-abstand"}


def library():
    sym = SYM_LIB.read_text(encoding="utf-8")
    parts = []
    for sid in COPY:
        m = re.search(r'<symbol id="%s"[^>]*>.*?</symbol>' % re.escape(sid), sym, re.S)
        if not m:
            raise SystemExit(f"{sid} fehlt in der Symbol-Bibliothek")
        parts.append(m.group(0).replace('id="ill-', 'id="an-').replace('href="#ill-', 'href="#an-'))
    vb = {}
    for fid, (key, expr) in PORTRAITS.items():
        sid = f"an-p-{key}"
        parts.append(f'<symbol id="{sid}" viewBox="0 0 38 54"><g transform="translate(19 18)">{body_inner(key)}{head_inner(key, expr)}</g></symbol>')
        vb[fid] = (sid, "0 0 38 54")
    parts.append(f'<symbol id="an-jesus-kopf" viewBox="0 0 34 34"><g transform="translate(17 17)">{head_inner("jesus", "calm")}</g></symbol>')
    parts.append(f'<symbol id="an-p-meister-kopf" viewBox="0 0 28 30"><g transform="translate(14 15)">{head_inner("meister", "calm")}</g></symbol>')
    lib = ('<svg xmlns="http://www.w3.org/2000/svg" width="0" height="0" aria-hidden="true" style="position:absolute"><defs>\n'
           '<!-- Bildsprache «Anime» (Pilot): Figuren mit Gesicht; Gegenstände und Zeichen aus der Symbol-Bibliothek übernommen (an-). '
           'Eigene Zeichnung (KI-Entwurf, Claude, 2026-10-17), CC0. -->\n' + "\n".join(parts) + "\n</defs></svg>\n")
    for fid, sid in OBJ.items():
        m = re.search(r'<symbol id="%s" viewBox="([^"]+)"' % re.escape(sid), lib)
        vb[fid] = (sid, m.group(1))
    return lib, vb


ILL = {
    "ILL-ANI-JHN-002-013-022": ("BRIEF-JHN-002-013-022", tempel,
                                "Comic in zwei Bildern ohne Text: 1 Vor dem Tempel hält Jesus ernst die Geissel erhoben; ein Tisch kippt, Münzen fliegen, ein Händler weicht erschrocken zurück, "
                                "über dem davonlaufenden Schaf die erhobene Geissel, Tauben im Käfig; Sprechblase: Tempel, Münzen, durchgestrichen. 2 Menschen aus der Menge fragen nach einem Zeichen (Stern, Fragezeichen); "
                                "Jesus antwortet: Tempel mit Riss, drei Sonnen, Tempel.",
                                "Comic i zwei Bilder ohni Text: 1 Vor em Tämpel hebt de Jesus ernscht d Geissle uf; en Tisch kippt, Münz flüüged, en Händler wiicht verschrocke zrugg, "
                                "über em Schaf, wo dervo rennt, di ufghabeni Geissle, Tube im Chäfig; Sprächblase: Tämpel, Münz, durgstriche. 2 Mänsche us de Mängi fröged nach eme Zeiche (Stern, Fragezeiche); "
                                "de Jesus antwortet: Tämpel mit Riss, drüü Sunne, Tämpel."),
    "ILL-ANI-JHN-002-023-025": ("BRIEF-JHN-002-023-025", glaube,
                                "Menschen in Jerusalem mit leuchtenden Augen unter goldenen Sternen (Zeichen), über ihnen Herzen (sie glauben); eine gestrichelte Linie trennt sie von Jesus, "
                                "der sich ernst zur Seite abwendet; im Hintergrund der Tempel.",
                                "Mänsche z Jerusalem mit lüüchtende Auge under goldige Stärn (Zeiche), über ine Härz (si glaubed); e gstrichleti Linie trännt si vom Jesus, "
                                "wo sich ernscht uf d Siite abwändet; im Hindergrund de Tämpel."),
    "ILL-ANI-JHN-002-001-012": ("BRIEF-JHN-002-001-012", kana,
                                "Comic in vier Bildern ohne Text: 1 Beim Hochzeitsfest zeigt Maria besorgt auf den leeren Weinkrug und den leeren Becher; Jesus antwortet ruhig mit der Sanduhr. "
                                "2 Maria zeigt den Dienern: Jesus und das Ohr (hört auf ihn); die Diener staunen. 3 Jesus weist auf die sechs Krüge, ein Diener giesst Wasser ein; Sprechblase: Krug, Pfeil, Speisemeister. "
                                "4 Der Speisemeister kostet strahlend und zeigt den Becher dem staunenden Bräutigam; über Jesus ein Stern, die Jünger mit leuchtenden Augen und Herzen.",
                                "Comic i vier Bilder ohni Text: 1 Am Hochziitsfäscht zeigt d Maria bsorget uf de läär Wiichrueg und de läär Becher; de Jesus antwortet ruhig mit de Sanduhr. "
                                "2 D Maria zeigt de Diener: de Jesus und s Ohr (losed uf ihn); d Diener stuuned. 3 De Jesus zeigt uf di sächs Chrüeg, en Diener schüttet Wasser ii; Sprächblase: Chrueg, Pfiil, Spiismeischter. "
                                "4 De Spiismeischter probiert strahlend und zeigt de Becher em stuunende Brüütigam; über em Jesus en Stern, d Jünger mit lüüchtende Auge und Härz."),
}


def run():
    OUT.mkdir(parents=True, exist_ok=True)
    lex = {p.stem for p in (D / "illustrations/lexicon").glob("FIG-*.json")}
    lib, vb = library()
    n = 0
    f = OUT / "_bibliothek.svg"
    if not f.exists() or f.read_text(encoding="utf-8") != lib:
        f.write_text(lib, encoding="utf-8")
        n += 1
    for k in vb:
        if k not in lex:
            raise SystemExit(f"{k} nicht im Bildlexikon")
    style = {"id": "ILLSTYLE-ANIME", "type": "illustration_style", "status": "draft", "tags": [], "key": "anime",
             "labels": {"de": "Anime", "en": "Anime"},
             "description_de": "Comicartige Bilder ohne Text: Personen mit Gesicht und Ausdruck (Züge und Hautton der Levante im 1. Jahrhundert, keine Karikatur), "
                               "Manga-Panels mit schrägen Rändern, Bewegungs- und Emotionszeichen; Sprechblasen nur mit Zeichen. Gott nie als Mensch. Pilot.",
             "library": "data/illustrations/anime/_bibliothek.svg",
             "renderings": {k: {"symbol": v[0], "viewbox": v[1]} for k, v in sorted(vb.items())},
             "license": LIC, "authorship_de": AUTH, "knowledge": {"asserted_at": DATE, "supersedes": None}}
    n += write(D / "illustrations/styles/ILLSTYLE-ANIME.json", style, "Stil «Anime» (Pilot) angelegt")
    for rid, (brief_id, gen, alt, alt_g) in ILL.items():
        svg = gen()
        f = OUT / f"{rid}.svg"
        if not f.exists() or f.read_text(encoding="utf-8").strip() != svg:
            f.write_text(svg + "\n", encoding="utf-8")
            n += 1
        brief = json.loads((D / "illustrations/briefs" / f"{brief_id}.json").read_text(encoding="utf-8"))
        depicts = sorted({x for p in brief["panels"] for k in ("figures", "objects", "signs") for x in p[k]}
                         | {x for p in brief["panels"] for sp in p["speech"] for x in (sp["from"], sp["to"], *sp["icons"])})
        missing = [x for x in depicts if x not in vb]
        rec = {"id": rid, "type": "illustration", "status": "draft", "tags": brief.get("tags", []), "style": "ILLSTYLE-ANIME",
               "brief": brief_id, "level": brief["level"], **({"reference": brief["reference"]} if brief.get("reference") else {}),
               "target": brief["target"], "file": f"data/illustrations/anime/{rid}.svg", "depicts": [x for x in depicts if x in vb],
               **({"not_rendered": missing} if missing else {}), "alt_de": alt, "license": LIC, "authorship_de": AUTH,
               "knowledge": {"asserted_at": DATE, "supersedes": None}}
        old = OUT / f"{rid}.json"
        if old.exists():
            o = json.loads(old.read_text(encoding="utf-8"))
            if "check" in o:
                rec["check"] = o["check"]
        n += write(old, rec, "Bild im Stil Anime nach Bildauftrag gezeichnet")
        n += localize(rid, rec, {"alt_de": alt_g}, "gsw-u-sd-chzh", "GSW-ZH", "CTX-CH-ZH-GSW-2026", AUTH_GSW, DATE)
    print(f"PASS: Bildstil Anime – {len(vb)} Darstellungen, {len(ILL)} Bilder; {n} Dateien geschrieben")


if __name__ == "__main__":
    run()
