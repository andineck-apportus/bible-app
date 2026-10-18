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
        ex, ey = side * 4.2 + max(-1.6, min(1.6, look * 1.4)), 2.4
        if expr in ("smile", "delight"):  # Freude mit lachenden Augen (Sternaugen wirkten befremdlich)
            out.append(f'<path d="M{ex - 2:.1f} {ey + .4:.1f}Q{ex:.1f} {ey - 2:.1f} {ex + 2:.1f} {ey + .4:.1f}" fill="none" stroke="{INK}" stroke-width="1.1" stroke-linecap="round"/>')
            continue
        if expr == "sleep":
            out.append(f'<path d="M{ex - 2.1:.1f} {ey + .4:.1f}Q{ex:.1f} {ey + 1.8:.1f} {ex + 2.1:.1f} {ey + .4:.1f}" fill="none" stroke="{INK}" stroke-width="1" stroke-linecap="round"/>')
            continue
        if expr == "pensive":  # offen, Blick gesenkt und zur Seite (nicht geschlossen: wirkte im Blindtest schläfrig/hochmütig)
            out.append(f'<ellipse cx="{ex + .5:.1f}" cy="{ey + .7:.1f}" rx="1.75" ry="2.1" fill="#3A2416"/>'
                       f'<path d="M{ex - 2.2:.1f} {ey - 1.9:.1f}Q{ex:.1f} {ey - 3.4:.1f} {ex + 2.2:.1f} {ey - 1.9:.1f}" fill="none" stroke="{INK}" stroke-width=".6" stroke-linecap="round"/>'
                       f'<circle cx="{ex + 1.1:.1f}" cy="{ey:.1f}" r=".55" fill="#FFF"/>')
            continue
        if expr == "surprised":
            out.append(f'<ellipse cx="{ex:.1f}" cy="{ey:.1f}" rx="2.1" ry="2.5" fill="#FFF" stroke="{INK}" stroke-width=".7"/>'
                       f'<circle cx="{ex + look * .5:.1f}" cy="{ey + .2:.1f}" r=".95" fill="{INK}"/>')
            continue
        iris = "#3A2416"
        # Oberlid als feine Linie über der Pupille: ein dickes Lid auf der Pupille las sich im Blindtest als finsterer Blick (2026-10-17)
        out.append(f'<ellipse cx="{ex:.1f}" cy="{ey:.1f}" rx="1.75" ry="2.35" fill="{iris}"/>'
                   f'<path d="M{ex - 2.2:.1f} {ey - 2.2:.1f}Q{ex:.1f} {ey - 3.9:.1f} {ex + 2.2:.1f} {ey - 2.2:.1f}" fill="none" stroke="{INK}" stroke-width=".6" stroke-linecap="round"/>')
        if expr == "delight":
            sx, sy = ex + .2, ey - .4
            out.append(f'<path d="M{sx:.1f} {sy - 1.3:.1f}l.35 .95.95 .35-.95 .35-.35 .95-.35-.95-.95-.35.95-.35z" fill="#FFF"/>')
        else:
            out.append(f'<circle cx="{ex + .6:.1f}" cy="{ey - .8:.1f}" r=".6" fill="#FFF"/>')
    return "".join(out)


def brows(expr, look, color):
    """Brauen deutlich über dem Lid und nur leicht gebogen: im Blindtest wirkten tiefe, schräge Brauen grimmig (2026-10-17)."""
    d = []
    for side in (-1, 1):
        ex = side * 4.2 + max(-1.6, min(1.6, look * 1.4))
        if expr == "worried":
            a, b = (-4.8, -6.0) if side < 0 else (-6.0, -4.8)
        elif expr == "determined":  # entschlossen: gerade Brauen, nicht nach innen gesenkt (wirkte zornig)
            a, b = (-5.4, -5.4)
        elif expr == "surprised":
            a, b = (-6.4, -6.4)
        else:
            a, b = (-5.3, -5.3)
        mid = min(a, b) - (1.1 if expr in ("calm", "smile", "delight", "surprised", "pensive", "worried") else .7)
        d.append(f"M{ex - 2.2:.1f} {a:.1f}Q{ex:.1f} {mid:.1f} {ex + 2.2:.1f} {b:.1f}")
    return f'<path d="{"".join(d)}" fill="none" stroke="{color}" stroke-width=".75" stroke-linecap="round"/>'


def mouth(expr, look):
    x = look * 1.0
    if expr == "worried":
        return f'<path d="M{x - 1.8:.1f} 8.3q.9-.8 1.8 0t1.8 0" fill="none" stroke="{INK}" stroke-width=".8" stroke-linecap="round"/>'
    if expr == "surprised":
        return f'<ellipse cx="{x:.1f}" cy="8.4" rx="1.1" ry="1.4" fill="#6B2A2A"/>'
    if expr == "pensive":
        return f'<path d="M{x - 1.3:.1f} 8.2Q{x:.1f} 8.7 {x + 1.3:.1f} 8.2" fill="none" stroke="{INK}" stroke-width=".8" stroke-linecap="round"/>'
    if expr in ("determined", "earnest"):
        return f'<path d="M{x - 1.5:.1f} 8.2h3" stroke="{INK}" stroke-width=".85" stroke-linecap="round"/>'
    if expr in ("smile",):
        return f'<path d="M{x - 2.2:.1f} 7.6Q{x:.1f} 9.8 {x + 2.2:.1f} 7.6" fill="none" stroke="{INK}" stroke-width=".9" stroke-linecap="round"/>'
    if expr == "delight":
        return f'<path d="M{x - 2.4:.1f} 7.4Q{x:.1f} 10.6 {x + 2.4:.1f} 7.4z" fill="#5A2A22" stroke="{INK}" stroke-width=".5"/>'
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
    "braeutigam": dict(hair="#24180F", front="M-10.6-1.8Q-11-11.6 0-12Q11-11.6 10.6-1.8Q8-8.6 0-9.2Q-8-8.6-10.6-1.8z",
                       beard="M-8 6.4Q-7 12.4 0 13.4Q7 12.4 8 6.4Q6 10 0 10.6Q-6 10-8 6.4z", robe="#5A3E7A", trim="#D9A441", wreath=True),
    "braut": dict(hair="#2E2017", veil="#FFFFFF", front="M-8-3.4Q0-8.6 8-3.4Q4-5.4 0-5.2Q-4-5.4-8-3.4z", robe="#FBF3E4", flowers=True),
    "juenger": dict(hair="#2E2017", curls=True, beard="M-8 6.4Q-7 12 0 13Q7 12 8 6.4Q6 9.8 0 10.4Q-6 9.8-8 6.4z", robe="#9C7A4C", belt="#5B4630"),
    "juenger2": dict(hair="#4A3020", front="M-10.6 0Q-11.4-10.8 0-11.8Q11.4-10.8 10.6 0Q6-8.2-1-7Q-7-6.4-10.6 0z", robe="#8A6A40", belt="#5B4630"),
    "gast": dict(hair="#2E2017", front="M-10.6-.4Q-11-11.6 0-12Q11-11.6 10.6-.4Q8-6 0-6.6Q-8-6-10.6-.4z", robe="#B4A98F"),
    "haendler": dict(hair="#2E2017", veil="#E9D8B4", front="M-7.6-3.6Q0-8.4 7.6-3.6Q4-5.2 0-5Q-4-5.2-7.6-3.6z",
                     beard="M-8 6.4Q-7 12.4 0 13.4Q7 12.4 8 6.4Q6 10 0 10.6Q-6 10-8 6.4z", robe="#C2884A", belt="#8A6A3A"),
    "menge": dict(hair="#2E2017", front="M-10.6-.4Q-11-11.6 0-12Q11-11.6 10.6-.4Q8-6 0-6.6Q-8-6-10.6-.4z",
                  beard="M-8 6.4Q-7 12.4 0 13.4Q7 12.4 8 6.4Q6 10 0 10.6Q-6 10-8 6.4z", robe="#A8987A", sash="#7E6E52"),
    "menge2": dict(hair="#3A2618", veil="#C9B48E", front="M-7.6-3.6Q0-8.4 7.6-3.6Q4-5.2 0-5Q-4-5.2-7.6-3.6z", robe="#9C8A6A", sash="#6E5E44"),
    "menge3": dict(hair="#24180F", front="M-10.6 0Q-11.4-10.8 0-11.8Q11.4-10.8 10.6 0Q6-8.2-1-7Q-7-6.4-10.6 0z", robe="#8E8A6E", sash="#6A664C"),
    "mose": dict(hair="#D8D2C4", front="M-10.6-1.6Q-11.4-10.8 0-11.8Q11.4-10.8 10.6-1.6Q8-8.8 0-9.4Q-8-8.8-10.6-1.6z",
                 beard="M-8.6 4.6Q-9 15 0 19Q9 15 8.6 4.6Q6.6 10.6 0 11.2Q-6.6 10.6-8.6 4.6z", robe="#7A5A34", mantle="#E7DCC4"),
    "paulus": dict(hair="#3A2618", front="M-10.6 1Q-10.8-6-8.6-8.6Q-6-6.8-6.4-1z M10.6 1Q10.8-6 8.6-8.6Q6-6.8 6.4-1z",
                   beard="M-8.4 5Q-8 14 0 15.6Q8 14 8.4 5Q6.6 10.4 0 11Q-6.6 10.4-8.4 5z", robe="#A79A80", mantle="#6A3F2F"),
    "prophet": dict(hair="#2E2017", veil="#5B4E3C", front="M-7.6-3.6Q0-8.4 7.6-3.6Q4-5.2 0-5Q-4-5.2-7.6-3.6z",
                    beard="M-8.4 5Q-8 15 0 16.6Q8 15 8.4 5Q6.6 10.4 0 11Q-6.6 10.4-8.4 5z", robe="#8A7A62", mantle="#5B4E3C"),
    "koenig": dict(hair="#24180F", front="M-10.6-.4Q-11-11.6 0-12Q11-11.6 10.6-.4Q8-6 0-6.6Q-8-6-10.6-.4z",
                   beard="M-8 6.4Q-7 12.4 0 13.4Q7 12.4 8 6.4Q6 10 0 10.6Q-6 10-8 6.4z", robe="#6A2E5E", trim="#D9A441", crown=True),
    "soldat": dict(hair="#24180F", robe="#8FA3A0", mantle="#8E1F2F", helmet=True),
    "gast2": dict(hair="#3A2618", veil="#C7B9D6", front="M-7.6-3.6Q0-8.4 7.6-3.6Q4-5.2 0-5Q-4-5.2-7.6-3.6z", robe="#8FA3A0"),
}


def head_inner(key, expr="calm", look=0.0, tears=False):
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
    ears = []  # Dreiviertelansicht: bei starkem Blick zur Seite ist das Ohr auf dieser Seite verdeckt
    if look < 2.2:
        ears.append("M10.3 2.4q1.8.4 1.2 2.6-.6 1.6-1.8 1z")
    if look > -2.2:
        ears.append("M-10.3 2.4q-1.8.4-1.2 2.6.6 1.6 1.8 1z")
    o.append(f'<path d="{" ".join(ears)}" fill="{SKIN}" stroke="{INK}" stroke-width=".5"/>')
    if c.get("beard"):
        o.append(f'<path d="{c["beard"]}" fill="{c["hair"]}" opacity=".92"/>')
    if c.get("mustache"):
        o.append(f'<path d="M{look - 3:.1f} 6.6q3-1.6 6 0" fill="none" stroke="{c["hair"]}" stroke-width="1.3" stroke-linecap="round"/>')
    o.append(eyes(expr, look) + brows(expr, look, c["hair"]))
    o.append(f'<path d="M{look * .8:.1f} 4.8l-.6 1.6h1" fill="none" stroke="{SKIN_D}" stroke-width=".7" stroke-linecap="round"/>')
    if expr in ("delight", "worried") or c.get("flowers"):
        o.append(blush())
    o.append(mouth(expr, look))
    if tears:
        for side in (-1, 1):
            ex = side * 4.2 + max(-1.6, min(1.6, look * 1.4))
            o.append(f'<path d="M{ex:.1f} 4.4q-.6 2.6-.2 5.4" fill="none" stroke="#6FA8D8" stroke-width="1.3" stroke-linecap="round"/>'
                     f'<path d="M{ex - .2:.1f} 9.2q1.4 1.8 0 2.8-1.4-1 0-2.8z" fill="#8FC8EE" stroke="#2E6E9E" stroke-width=".4"/>')
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
    if c.get("turban"):
        o.append(f'<path d="M-11-1Q-12.4-13.6 0-14Q12.4-13.6 11-1Q9-7.4 0-7.8Q-9-7.4-11-1z" fill="{c["turban"]}" stroke="{INK}" stroke-width=".7"/>'
                 '<path d="M-10-5Q0-10 10-5M-10.6-8.4Q0-13 10.6-8.4" fill="none" stroke="#C9BFAA" stroke-width=".7"/>')
    if c.get("plate"):
        o.append('<path d="M-4-10.6h8v2.2h-8z" fill="#E0B24E" stroke="#9C6F1C" stroke-width=".4"/>')
    if c.get("band"):
        o.append(f'<path d="M-10.6-4.6Q0-9.6 10.6-4.6v2.4Q0-7.2-10.6-2.2z" fill="{c["band"]}"/>')
    if c.get("old"):
        o.append(f'<path d="M-4-5.2h3M1.4-5.4h3M-7.8 6.4q.6 1.4 1.6 1.8M7.8 6.4q-.6 1.4-1.6 1.8" stroke="{SKIN_D}" stroke-width=".55" stroke-linecap="round" fill="none"/>')
    if c.get("crown"):
        o.append('<path d="M-8.6-6.6l1-6.4 3 3.6 2.6-4.8 2 4.6 2-4.6 2.6 4.8 3-3.6 1 6.4z" fill="#E0B24E" stroke="#9C6F1C" stroke-width=".6"/>'
                 '<circle cx="0" cy="-9.6" r=".9" fill="#A33A2E"/>')
    if c.get("helmet"):
        o.append(f'<path d="M-11 1Q-12-12 0-12.6Q12-12 11 1L8.6 1Q8-7 0-7.6Q-8-7-8.6 1z" fill="#8C8070" stroke="{INK}" stroke-width=".7"/>'
                 f'<path d="M-1.8-12.4Q-2.6-19 0-21Q2.6-19 1.8-12.4z" fill="#8E1F2F" stroke="{INK}" stroke-width=".5"/>')  # Helmbusch längs (von vorn schmal); quer = Hauptmann
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
    o = []
    if c.get("wings"):
        o.append(f'<path d="M-12 22Q-30 10-26-12q8 12 14 22zM12 22q18-12 14-34-8 12-14 22z" fill="#FFFDF6" stroke="#D9A441" stroke-width=".9"/>')
    o.append(f'<path d="M-17 34Q-17 19-7 15.6L7 15.6Q17 19 17 34z" fill="{c["robe"]}" stroke="{INK}" stroke-width=".8"/>')
    if c.get("fur"):
        o.append(f'<path d="M-12 18Q0 14 12 18l3 6Q0 20-15 24z" fill="#8A6A3A" stroke="{INK}" stroke-width=".6"/>')
    if c.get("toga"):
        o.append(f'<path d="M-9 16.4Q4 20 14 30l2 4h-6Q2 24-12 19z" fill="#FFFFFF" stroke="{INK}" stroke-width=".6"/><path d="M10 34Q4 25-10 19.6" fill="none" stroke="{c.get("trim", "#6A2E5E")}" stroke-width="1.6"/>')
    if c.get("breast"):
        o.append('<path d="M-5 21h10v9h-10z" fill="#D9A441" stroke="#9C6F1C" stroke-width=".6"/>'
                 + "".join(f'<circle cx="{-3 + (i % 3) * 3}" cy="{23 + (i // 3) * 2}" r=".8" fill="{col}"/>' for i, col in enumerate(["#A33A2E", "#3E6E9E", "#6E8B3D"] * 4)))
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
    if c.get("trim") and not c.get("toga"):
        o.append(f'<path d="M-4 15.8L0 22 4 15.8" fill="none" stroke="{c["trim"]}" stroke-width="1.4"/>')
    if c.get("chains"):
        o.append('<g fill="none" stroke="#6A6A6A" stroke-width="1"><ellipse cx="-14" cy="30" rx="2.4" ry="1.5"/><ellipse cx="-11" cy="31.6" rx="2.4" ry="1.5"/><ellipse cx="14" cy="30" rx="2.4" ry="1.5"/><ellipse cx="11" cy="31.6" rx="2.4" ry="1.5"/></g>')
    if c.get("bound"):
        o.append(f'<path d="M-6 26h12v6h-12z" fill="{SKIN}" stroke="{INK}" stroke-width=".6"/><path d="M-6 29h12" stroke="#8A6A3A" stroke-width="1.6"/>')
    if arm:
        ang, ln = arm
        import math
        x0, y0 = (12 if math.cos(math.radians(ang)) >= 0 else -12), 21
        x1, y1 = x0 + ln * math.cos(math.radians(ang)), y0 + ln * math.sin(math.radians(ang))
        sleeve = c.get("mantle") or c["robe"]
        o.append(f'<path d="M{x0} {y0}L{x1:.1f} {y1:.1f}" stroke="{INK}" stroke-width="5.4" stroke-linecap="round"/>'
                 f'<path d="M{x0} {y0}L{x1:.1f} {y1:.1f}" stroke="{sleeve}" stroke-width="4" stroke-linecap="round"/>'
                 f'<g transform="translate({x1:.1f} {y1:.1f}) rotate({ang + 90:.0f})"><path d="M-2.4 1.2Q-2.8-2.6-1.6-4.2h3.2Q2.8-2.6 2.4 1.2z" fill="{SKIN}" stroke="{INK}" stroke-width=".6"/>'
                 f'<path d="M3 -.6l1.6-1.8" stroke="{INK}" stroke-width="1.6" stroke-linecap="round"/><path d="M3 -.6l1.6-1.8" stroke="{SKIN}" stroke-width=".8" stroke-linecap="round"/></g>')
    return "".join(o)


def person(key, x, y, s, expr="calm", look=0.0, arm=None, flip=False, tears=False, hold=None):
    """Brustbild: Kopfmitte bei (x, y), s = Massstab (1 = Kopfradius 10); hold = Symbol, das die Figur vor der Brust hält."""
    fl = " scale(-1 1)" if flip else ""
    if CHAR[key].get("baby"):
        return (f'<g transform="translate({x} {y}) scale({s})"><ellipse cx="0" cy="22" rx="14" ry="9" fill="{CHAR[key]["robe"]}" stroke="{INK}" stroke-width=".8"/>'
                f'<g transform="translate(-6 16) scale(.55)">{head_inner(key, "sleep", 0)}</g></g>')
    if CHAR[key].get("child"):
        s *= .74
        y += 9 * s
    if hold and hold.startswith("an-a-"):  # Erkennungszeichen (Schlüssel, Kasse …) gut sichtbar auf der Brust
        held = use(hold, 1, 16, 14, 14)
    else:
        held = use(hold, -4, 13, 16, 12) if hold else ""  # vor der Brust, nicht am unteren Rand
    head = head_inner(key, expr, -look if flip else look, tears)
    if flip:  # abgewandt: Hinterkopf statt Gesicht (Spiegeln allein war im Blindtest nicht sichtbar)
        c = CHAR[key]
        cover = c.get("veil") or c.get("turban") or c["hair"]
        head += (f'<path d="M-10.8 0Q-11.4-12 0-12.4Q11.4-12 10.8 0Q10.6 9 4 12.4H-4Q-10.6 9-10.8 0z" fill="{cover}" stroke="{INK}" stroke-width=".7"/>'
                 f'<path d="M-4 12.4Q0 14 4 12.4" fill="none" stroke="{SKIN_D}" stroke-width="1.2"/>')
    return f'<g transform="translate({x} {y}) scale({s}){fl}">{body_inner(key, arm)}{head}{held}</g>'


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


CUR = ["x"]  # Kennung des Bildes, das gerade gezeichnet wird (für eindeutige Clip-IDs, wenn mehrere Bilder auf einer Seite stehen)


def frame(n, pts, body, bg="#F6EAD7", num=None):
    """Manga-Panel als Vieleck (schräge Ränder) mit Nummer oben links."""
    pid = f"an-cp-{CUR[0]}-{n}"
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
    b5 = bubble(30, 310, 92, 44, 90, 362, use("an-becher", 40, 314, 28, 33) + use("an-z-freude", 74, 322, 36, 24))
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
          + '<g transform="translate(172 128) scale(-1 1)">' + use("an-schaf", 0, 0, 44, 30) + '</g>' + lines_motion(176, 136, 14, 3, 0)
          + use("an-taube-kaefig", 316, 96, 46, 46)
          + person("jesus", 228, 116, 1.9, "earnest", -1.2, arm=(-100, 18)) + '<g transform="translate(214 62) scale(-1 1)">' + use("an-peitsche", 0, 0, 30, 36) + '</g>' + b1)
    b2 = bubble(36, 192, 70, 40, 66, 252, use("an-zeichen", 44, 196, 30, 30) + use("an-z-frage", 80, 196, 16, 28))
    suns = "".join(use("an-sonne", 252 + i * 14, 214, 12, 12) for i in range(3))
    b3 = bubble(158, 190, 214, 46, 314, 250, use("an-p-menge", 162, 195, 17, 25) + use("an-p-menge", 171, 191, 17, 25) + use("an-p-menge", 180, 196, 17, 25) + use("an-tempel-riss", 197, 196, 32, 30) + use("an-z-pfeil", 228, 213, 20, 10) + suns
                + use("an-z-pfeil", 294, 213, 20, 10) + use("an-jesus-kopf", 316, 194, 26, 26) + use("an-tempel", 344, 200, 26, 20))
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
          + person("jesus", 296, 148, 1.9, "pensive", 2.6))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#FFFDF6"/>' + frame(1, p1, s1) + "</svg>")



# ---------------------------------------------------------------- Obere Ebenen und Kapitel: Panels in Feldkoordinaten 186 × 140
FLOOR = '<path d="M0 116h186v24H0z" fill="#E7D3B0"/>'


def tear(x, y, s=1):
    return use("an-z-trauer", x, y, 6 * s, 9 * s)


def crack(x, y, sc=1.0):
    d = "M0 0l-4 8 5 5-4 8 4 6"
    return (f'<g transform="translate({x} {y}) scale({sc})"><path d="{d}" fill="none" stroke="#F6EBD9" stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/></g>')


def dots(d):
    return f'<path d="{d}" fill="none" stroke="#8C8070" stroke-width="1.6" stroke-dasharray="3 4" stroke-linecap="round"/>'


def flame(x, y, s=1):
    return f'<path transform="translate({x} {y}) scale({s})" d="M0-7Q4-2 3 1a3 3 0 0 1-6 0Q-3-3 0-7z" fill="#F08A3C" stroke="#C0502A" stroke-width=".6"/>'


def a_schoepfung():
    b = bubble(80, 10, 40, 34, 70, 30, use("an-licht", 88, 15, 24, 24))
    return use("an-gott", 24, 8, 46, 46) + b + use("an-schoepfung", 50, 44, 134, 112) + sparkle(160, 50, .8) + sparkle(132, 70, .6)


def a_meer():
    staff = '<path d="M70 112V36" stroke="#5B4630" stroke-width="2.6" stroke-linecap="round"/><path d="M70 36q-5-1-5 4" fill="none" stroke="#5B4630" stroke-width="2.6"/>'
    return (use("an-meer", 0, 22, 186, 118) + person("menge2", 124, 98, 1.15, "delight", -.4) + person("menge3", 148, 102, 1.05, "delight", -.6)
            + person("mose", 92, 86, 1.45, "calm", .2, arm=(-110, 16)) + staff)


def a_berg(meer=False):
    sea = use("an-meer", -4, 34, 54, 32, ' opacity=".95"') if meer else ""
    b = bubble(142, 4, 40, 34, 132, 18, use("an-tafeln", 148, 9, 28, 26))
    return (use("an-berg", 52, 22, 134, 86) + sea + use("an-gott", 98, 0, 36, 36) + b + FLOOR
            + person("mose", 44, 86, 1.5, "calm", .9) + use("an-tafeln", 60, 98, 28, 26)
            + person("menge", 124, 98, 1.25, "surprised", -1.0) + person("menge2", 156, 102, 1.15, "delight", -1.0))


def god_to(x, y, tx, ty, s=26):
    from bilder_auto import arrow_svg
    return use("an-gott", x, y, s, s) + arrow_svg(x + s * .55, y + s, tx, ty, "act")


def a_exil():
    b = bubble(44, 18, 40, 34, 34, 68, use("an-z-hoffnung", 51, 22, 26, 26))
    return (use("an-jerusalem", 104, 12, 80, 56) + crack(150, 38) + crack(126, 46, .8) + FLOOR
            + '<g transform="translate(184 92) scale(-1 1)">' + use("an-z-exil", 0, 0, 64, 26) + "</g>"
            + person("menge2", 80, 100, 1.15, "worried", .6, tears=True) + person("menge3", 106, 106, 1.0, "worried", .6, tears=True)
            + person("prophet", 30, 88, 1.45, "calm", 1.4, arm=(-55, 13)) + use("an-schriftrolle", 40, 116, 22, 15) + god_to(26, 2, 26, 64) + b)


def a_kreuz(jesus):
    x0 = 52 if jesus else 22
    out = '<path d="M0 108q60-16 120-6t66 6v32H0z" fill="#D8C59E"/>' + use("an-kreuz", x0, 46, 44, 64) + use("an-grab", x0 + 46, 62, min(90, 182 - x0 - 46), 62)
    if jesus:
        out += person("jesus", 26, 92, 1.35, "calm", .8)
    return out


def a_neu(freude=False):
    out = use("an-neue-schoepfung", 14, 30, 158, 118) + use("an-gott", 72, 0, 42, 42)
    if freude:
        out += (person("menge2", 20, 92, 1.0, "delight", .7) + person("menge3", 168, 92, 1.0, "delight", -.7)
                + sparkle(30, 66, .7) + sparkle(160, 66, .7))
    return out


def a_stimmen():
    return (FLOOR + use("an-schriftrolle", 6, 70, 46, 32) + use("an-leier", 56, 58, 30, 40) + person("prophet", 112, 88, 1.4, "calm", .4)
            + use("an-schriftrolle", 122, 108, 20, 14) + use("an-brief", 146, 86, 36, 27))


def a_verkuendet(vier=False):
    rolls = "".join(use("an-schriftrolle", 100 + (i % 2) * 15, 116 + (i // 2) * 10, 14, 10) for i in range(4)) if vier else ""
    b = bubble(60, 6, 122, 38, 146, 64, use("an-gott", 66, 9, 32, 32) + use("an-z-umkehr", 108, 15, 26, 20) + use("an-z-glauben", 146, 11, 24, 26))
    return (FLOOR + person("menge", 26, 96, 1.3, "surprised", 1.0) + person("menge2", 56, 102, 1.2, "delight", 1.0)
            + person("menge3", 84, 106, 1.1, "calm", 1.2) + rolls + person("jesus", 148, 88, 1.5, "calm", -1.4, arm=(200, 12)) + b)


def a_nt_geist():
    return (FLOOR + use("an-geist", 18, 4, 46, 46) + flame(26, 70, .9) + flame(52, 76, .9)
            + person("juenger", 24, 98, 1.25, "delight", .8) + person("juenger2", 52, 104, 1.1, "delight", .8)
            + use("an-z-ausbreiten", 74, 64, 38, 28) + use("an-brief", 124, 20, 32, 24) + use("an-gemeinde", 104, 62, 82, 60))


def a_nt_ende():
    return use("an-gott", 26, 4, 40, 40) + use("an-z-gericht", 8, 76, 46, 40) + use("an-neue-schoepfung", 60, 32, 124, 94)


def a_koenig():
    return (use("an-jerusalem", 64, 14, 118, 82) + FLOOR + person("koenig", 38, 86, 1.5, "smile", 1.0)
            + person("menge2", 132, 104, 1.1, "smile", -.6) + person("menge3", 158, 106, 1.0, "smile", -.6))


def a_zerstoert():
    return (use("an-jerusalem", 6, 14, 92, 64) + crack(58, 40) + crack(30, 52, .8) + FLOOR + use("an-z-exil", 12, 90, 80, 32)
            + person("menge2", 124, 98, 1.25, "worried", -.4, tears=True) + person("menge", 158, 96, 1.3, "worried", -.4, tears=True))


def a_gebet():
    b = bubble(66, 26, 54, 32, 44, 68, use("an-z-trauer", 75, 31, 12, 20) + use("an-z-freude", 92, 34, 22, 15))
    return (FLOOR + use("an-gott", 136, 4, 42, 42) + person("menge3", 40, 88, 1.5, "smile", 1.2) + use("an-leier", 62, 102, 20, 26) + b)


def a_liebe():
    return (FLOOR + use("an-z-hochzeit", 40, 8, 106, 42) + person("braut", 70, 86, 1.5, "smile", .8) + person("braeutigam", 118, 86, 1.5, "smile", -.8)
            + sparkle(94, 52, .9) + sparkle(54, 60, .6) + sparkle(136, 58, .6))


def a_weisheit():
    return (FLOOR + person("menge3", 40, 88, 1.5, "earnest", 1.0) + use("an-schriftrolle", 64, 102, 40, 28)
            + use("an-z-stunde", 110, 22, 26, 36) + use("an-z-gericht", 140, 28, 44, 38))


def a_prophet(zwoelf=False):
    rolls = "".join(use("an-schriftrolle", 112 + (i % 6) * 12, 6 + (i // 6) * 10, 11, 8) for i in range(12)) if zwoelf else ""
    b = bubble(40, 14, 72, 34, 34, 66, use("an-z-gericht", 46, 18, 30, 26) + use("an-z-umkehr", 82, 22, 24, 18))
    return (FLOOR + rolls + person("menge", 124, 98, 1.25, "worried", -.9) + person("menge2", 152, 102, 1.15, "worried", -.9)
            + person("menge3", 174, 106, 1.0, "surprised", -.9) + person("prophet", 30, 86, 1.5, "calm", 1.4) + use("an-schriftrolle", 42, 112, 24, 16) + god_to(26, 2, 26, 62) + b)


def a_aufbau():
    return (use("an-gott", 74, 0, 36, 36) + use("an-jerusalem", 52, 34, 84, 59) + FLOOR + use("an-z-hoffnung", 14, 86, 30, 30)
            + person("menge2", 146, 100, 1.2, "delight", -.6) + person("menge3", 170, 104, 1.05, "delight", -.6) + sparkle(160, 66, .8))


def a_pfingsten():
    return (use("an-jerusalem", 98, 38, 86, 60, ' opacity=".75"') + FLOOR + use("an-geist", 40, 0, 52, 52)
            + person("juenger", 26, 96, 1.3, "delight", .5) + person("juenger2", 60, 100, 1.2, "delight", .3) + person("juenger", 92, 104, 1.1, "delight", -.2)
            + flame(26, 70) + flame(60, 76) + flame(92, 82, .9))


def a_rom():
    return (use("an-jerusalem", 2, 30, 50, 35) + use("an-z-ausbreiten", 50, 22, 40, 30) + use("an-rom", 92, 14, 92, 64, ' opacity=".8"') + FLOOR
            + person("paulus", 116, 94, 1.3, "calm", .6, hold="an-brief") + person("soldat", 160, 96, 1.25, "calm", -.6))


def a_paulus():
    b = bubble(12, 16, 64, 34, 34, 68, use("an-kreuz", 20, 19, 18, 26) + use("an-z-glauben", 46, 21, 22, 24))
    return (FLOOR + person("paulus", 34, 88, 1.5, "calm", 1.0, hold="an-brief") + dots("M52 108Q72 60 88 62") + use("an-brief", 84, 50, 30, 22)
            + dots("M116 62Q126 66 132 74") + use("an-gemeinde", 104, 58, 82, 60) + b)


def a_briefe():
    letters = "".join(use("an-brief", 12, y, 30, 22) for y in (24, 54, 84))
    lines = "".join(dots(f"M46 {y + 11}Q72 {y + 11} 96 84") for y in (24, 54, 84))
    hearts = "".join(use("an-z-glauben", x, y, 18, 20) for x, y in ((112, 34), (138, 28), (164, 34)))
    return FLOOR + letters + lines + use("an-gemeinde", 96, 58, 90, 66) + hearts


def a_herrschaft():
    return (FLOOR + use("an-gott", 62, 0, 62, 62) + person("koenig", 30, 96, 1.25, "earnest", .5) + person("soldat", 62, 98, 1.2, "earnest", .4)
            + person("menge2", 132, 100, 1.2, "worried", -.6, tears=True) + person("menge3", 160, 104, 1.1, "worried", -.6, tears=True))


def a_kana_kap():
    jars = "".join(use("an-jar", 54 + i * 15, 92, 14, 26) for i in range(3))
    return (FLOOR + use("an-z-hochzeit", 120, 10, 66, 28) + person("braut", 140, 96, 1.05, "smile", -.4) + person("braeutigam", 170, 96, 1.05, "smile", -.6)
            + person("jesus", 26, 88, 1.4, "calm", 1.0) + jars + use("an-z-pfeil", 98, 100, 14, 8) + use("an-jar-wein", 112, 86, 18, 32)
            + use("an-zeichen", 110, 56, 22, 22) + sparkle(98, 64, .6))


def a_tempel_kap():
    b = bubble(110, 4, 72, 30, 132, 50, use("an-tempel", 116, 8, 26, 20) + use("an-muenzen", 144, 13, 16, 10) + use("an-z-fehlt", 162, 11, 15, 15))
    return (use("an-tempel", 70, 10, 116, 88, ' opacity=".5"') + FLOOR + person("haendler", 22, 90, 1.25, "surprised", -1.2, flip=True) + shock(22, 66, .7)
            + use("an-muenzen", 50, 70, 18, 11) + '<g transform="translate(86 100) scale(-1 1)">' + use("an-schaf", 0, 0, 34, 23) + "</g>" + lines_motion(88, 106, 10, 3, 0)
            + person("jesus", 140, 88, 1.45, "earnest", -1.0, arm=(-100, 15)) + '<g transform="translate(130 46) scale(-1 1)">' + use("an-peitsche", 0, 0, 24, 29) + "</g>" + b)


def a_glaube_kap():
    return (use("an-tempel", 112, 10, 72, 54, ' opacity=".45"') + FLOOR + use("an-zeichen", 20, 8, 16, 16) + use("an-zeichen", 52, 4, 13, 13)
            + "".join(use("an-z-glauben", x, y, 14, 16) for x, y in ((14, 46), (44, 40), (74, 48)))
            + person("menge2", 22, 98, 1.15, "delight", .8) + person("menge", 52, 94, 1.25, "delight", .9) + person("menge3", 82, 100, 1.1, "delight", .8)
            + use("an-z-abstand", 106, 58, 8, 76) + person("jesus", 148, 90, 1.45, "pensive", 2.6))


PANEL_SHAPES = [[(2, 2), (184, 2), (184, 136), (2, 138)], [(2, 2), (184, 4), (184, 138), (2, 136)],
                [(2, 4), (184, 2), (184, 138), (2, 138)], [(2, 2), (184, 2), (184, 138), (2, 136)]]


def apanel(i, n, body):
    pid = f"an-cp-{CUR[0]}-{n}"
    poly = " ".join(f"{x},{y}" for x, y in PANEL_SHAPES[i % 4])
    return (f'<clipPath id="{pid}"><polygon points="{poly}"/></clipPath><g clip-path="url(#{pid})"><polygon points="{poly}" fill="#F6EAD7"/>{body}</g>'
            f'<polygon points="{poly}" fill="none" stroke="{INK}" stroke-width="2.2" stroke-linejoin="round"/>'
            f'<circle cx="14" cy="14" r="8.5" fill="#FFFDF6" stroke="{INK}" stroke-width="1.2"/><text x="14" y="18" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="700" fill="{INK}">{n}</text>')


def alayout(bodies):
    n = len(bodies)
    head = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}"><rect width="{w}" height="{h}" fill="#FFFDF6"/>'
    if n == 1:
        return head.format(w=380, h=290) + f'<g transform="translate(4 4) scale(2)">' + apanel(0, 1, bodies[0]) + "</g></svg>"
    if n == 2:
        return head.format(w=380, h=148) + "".join(f'<g transform="translate({4 + i * 188} 4)">' + apanel(i, i + 1, b) + "</g>" for i, b in enumerate(bodies)) + "</svg>"
    if n == 3:
        sc = 124 / 186
        return head.format(w=380, h=100) + "".join(f'<g transform="translate({2 + i * 126} 2) scale({sc:.4f})">' + apanel(i, i + 1, b) + "</g>" for i, b in enumerate(bodies)) + "</svg>"
    return head.format(w=380, h=290) + "".join(f'<g transform="translate({4 + (i % 2) * 188} {4 + (i // 2) * 144})">' + apanel(i, i + 1, b) + "</g>" for i, b in enumerate(bodies)) + "</svg>"


def a_buch():
    rays = "".join(f'<path d="M190 40L{x} {y}"/>' for x, y in ((0, 0), (380, 0), (0, 140), (380, 140), (100, 0), (280, 0), (0, 70), (380, 70)))
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 250"><rect width="380" height="250" fill="#FFFDF6"/>'
            f'<clipPath id="an-cp-{CUR[0]}-1"><polygon points="4,4 376,4 376,246 4,240"/></clipPath><g clip-path="url(#an-cp-{CUR[0]}-1)">'
            '<rect width="380" height="250" fill="#1F2A44"/>'
            f'<g stroke="#F2C76E" stroke-width="2" opacity=".12">{rays}</g>'
            + use("an-licht", 150, 2, 80, 80) + use("an-adler", 78, 30, 224, 157) + use("an-schriftrolle", 128, 190, 124, 50)
            + sparkle(90, 60, 1.2) + sparkle(300, 70, 1.0) + sparkle(60, 170, .8) + sparkle(330, 180, .9)
            + f'</g><polygon points="4,4 376,4 376,246 4,240" fill="none" stroke="{INK}" stroke-width="2.4"/></svg>')


UPPER = {
    "BIBLE": [a_berg, lambda: a_kreuz(True), a_neu, a_stimmen],
    "OT": [a_schoepfung, a_meer, a_berg, a_exil],
    "NT": [a_verkuendet, lambda: a_kreuz(False), a_nt_geist, a_nt_ende],
    "GROUP-01": [a_schoepfung, lambda: upper_auto("GROUP-01", 2), lambda: a_berg(meer=True)],
    "GROUP-02": [lambda: upper_auto("GROUP-02", 1), a_koenig, a_zerstoert, lambda: upper_auto("GROUP-02", 4)],
    "GROUP-03": [a_gebet, a_liebe, a_weisheit],
    "GROUP-04": [a_prophet, a_exil],
    "GROUP-05": [lambda: a_prophet(zwoelf=True), a_aufbau],
    "GROUP-06": [lambda: a_verkuendet(vier=True), lambda: a_kreuz(False)],
    "GROUP-07": [a_pfingsten, a_rom],
    "GROUP-08": [a_paulus],
    "GROUP-09": [lambda: upper_auto("GROUP-09", 1)],
    "GROUP-10": [a_herrschaft, lambda: a_neu(freude=True)],
    "JHN-002": [a_kana_kap, a_tempel_kap, a_glaube_kap],
}


# ---------------------------------------------------------------- Bibliothek
COPY = ["ill-jar", "ill-jar-leer", "ill-jar-wein", "ill-traube", "ill-becher", "ill-becher-leer", "ill-z-fehlt", "ill-z-stunde", "ill-z-hoeren",
        "ill-z-pfeil", "ill-zeichen", "ill-z-glauben", "ill-z-freude", "ill-z-hochzeit", "ill-tempel", "ill-tempel-riss", "ill-sonne",
        "ill-peitsche", "ill-schaf", "ill-taube-tier", "ill-taube-kaefig", "ill-muenzen", "ill-z-frage", "ill-z-abstand",
        "ill-gott", "ill-geist", "ill-kreuz", "ill-grab", "ill-jerusalem", "ill-berg", "ill-haus", "ill-boot", "ill-tafeln", "ill-meer",
        "ill-schoepfung", "ill-leier", "ill-z-hoffnung", "ill-z-umkehr", "ill-z-gericht", "ill-neue-schoepfung", "ill-z-exil",
        "ill-z-ausbreiten", "ill-brief", "ill-z-beten", "ill-z-trauer", "ill-licht", "ill-adler", "ill-schriftrolle", "ill-weg"]
PORTRAITS = {"FIG-JESUS": ("jesus", "calm"), "FIG-MARIA-MUTTER-JESU": ("maria", "calm"), "FIG-ROLLE-DIENER": ("diener", "calm"),
             "FIG-ROLLE-SPEISEMEISTER": ("meister", "calm"), "FIG-ROLLE-BRAEUTIGAM": ("braeutigam", "calm"), "FIG-ROLLE-BRAUT": ("braut", "calm"),
             "FIG-ROLLE-GAST": ("gast", "calm"), "FIG-ROLLE-JUENGER": ("juenger", "calm"), "FIG-ROLLE-HAENDLER": ("haendler", "calm"),
             "FIG-GRUPPE-MENGE": ("menge", "calm"), "FIG-MOSE": ("mose", "calm"), "FIG-PAULUS": ("paulus", "calm"),
             "FIG-ROLLE-PROPHET": ("prophet", "earnest"), "FIG-ROLLE-KOENIG": ("koenig", "calm"), "FIG-ROLLE-SOLDAT": ("soldat", "earnest")}
OBJ = {"FIG-OBJ-KRUG-WASSER": "an-jar", "FIG-OBJ-KRUG-WEIN-LEER": "an-jar-leer", "FIG-OBJ-KRUG-WEIN": "an-jar-wein", "FIG-OBJ-BECHER-VOLL": "an-becher",
       "FIG-OBJ-BECHER-LEER": "an-becher-leer", "FIG-ZEICHEN-FEHLT": "an-z-fehlt", "FIG-ZEICHEN-STUNDE": "an-z-stunde", "FIG-ZEICHEN-HOEREN": "an-z-hoeren",
       "FIG-ZEICHEN-BRINGEN": "an-z-pfeil", "FIG-ZEICHEN-STERN": "an-zeichen", "FIG-ZEICHEN-GLAUBEN": "an-z-glauben", "FIG-ZEICHEN-FREUDE": "an-z-freude",
       "FIG-ZEICHEN-HOCHZEIT": "an-z-hochzeit", "FIG-ORT-TEMPEL": "an-tempel", "FIG-ZEICHEN-NIEDERREISSEN": "an-tempel-riss", "FIG-ZEICHEN-TAGE": "an-sonne",
       "FIG-OBJ-PEITSCHE": "an-peitsche", "FIG-OBJ-SCHAF": "an-schaf", "FIG-OBJ-TAUBE": "an-taube-kaefig", "FIG-OBJ-MUENZEN": "an-muenzen",
       "FIG-ZEICHEN-FRAGEN": "an-z-frage", "FIG-ZEICHEN-ABSTAND": "an-z-abstand",
       "FIG-GOTT": "an-gott", "FIG-HEILIGER-GEIST": "an-geist", "FIG-OBJ-KREUZ": "an-kreuz", "FIG-ORT-GRAB": "an-grab", "FIG-ORT-JERUSALEM": "an-jerusalem",
       "FIG-ORT-BERG": "an-berg", "FIG-ORT-HAUS": "an-haus", "FIG-ORT-WEG": "an-weg", "FIG-OBJ-BOOT": "an-boot", "FIG-OBJ-GESETZESTAFELN": "an-tafeln", "FIG-ORT-MEER": "an-meer",
       "FIG-ZEICHEN-SCHOEPFUNG": "an-schoepfung", "FIG-OBJ-LEIER": "an-leier", "FIG-ZEICHEN-HOFFNUNG": "an-z-hoffnung", "FIG-ZEICHEN-UMKEHR": "an-z-umkehr",
       "FIG-ZEICHEN-GERICHT": "an-z-gericht", "FIG-ZEICHEN-NEUE-SCHOEPFUNG": "an-neue-schoepfung", "FIG-ZEICHEN-EXIL": "an-z-exil",
       "FIG-ZEICHEN-AUSBREITEN": "an-z-ausbreiten", "FIG-OBJ-BRIEF": "an-brief", "FIG-GRUPPE-GEMEINDE": "an-gemeinde", "FIG-ZEICHEN-BETEN": "an-z-beten",
       "FIG-ZEICHEN-TRAUER": "an-z-trauer", "FIG-ZEICHEN-LICHT": "an-licht", "FIG-SYMBOL-ADLER": "an-adler", "FIG-OBJ-SCHRIFTROLLE": "an-schriftrolle"}


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
    parts.append('<symbol id="an-gemeinde" viewBox="0 0 60 44">' + use("an-haus", 20, 0, 40, 36) + person("menge2", 9, 24, .5, "smile", .6)
                 + person("menge", 22, 26, .52, "smile", .4) + person("menge3", 35, 28, .48, "smile", .3) + "</symbol>")
    parts.append(_fg.anime_attrs())
    # Gruppen als Zeichen in Sprechblasen: drei Köpfe (Mehrzahl, nie eine Einzelfigur)
    for fid, (key, expr) in PORTRAITS.items():
        if fid.startswith("FIG-GRUPPE-") and fid != "FIG-GRUPPE-GEMEINDE":
            ks = GROUP_KEYS.get(fid, (key, key, key))
            parts.append(f'<symbol id="an-p-{key}-gruppe" viewBox="0 0 54 50"><g transform="translate(14 20) scale(.62)">{body_inner(ks[0])}{head_inner(ks[0], "calm")}</g>'
                         f'<g transform="translate(40 20) scale(.62)">{body_inner(ks[1])}{head_inner(ks[1], "calm")}</g>'
                         f'<g transform="translate(27 17) scale(.72)">{body_inner(ks[2])}{head_inner(ks[2], "calm")}</g></symbol>')
            vb[fid] = (f"an-p-{key}-gruppe", "0 0 54 50")
    parts.append(f'<symbol id="an-jesus-kopf" viewBox="0 0 34 34"><g transform="translate(17 17)">{head_inner("jesus", "calm")}</g></symbol>')
    parts.append(f'<symbol id="an-p-meister-kopf" viewBox="0 0 28 30"><g transform="translate(14 15)">{head_inner("meister", "calm")}</g></symbol>')
    lib = ('<svg xmlns="http://www.w3.org/2000/svg" width="0" height="0" aria-hidden="true" style="position:absolute"><defs>\n'
           '<!-- Bildsprache «Anime» (Pilot): Figuren mit Gesicht; Gegenstände und Zeichen aus der Symbol-Bibliothek übernommen (an-). '
           'Eigene Zeichnung (KI-Entwurf, Claude, 2026-10-17), CC0. -->\n' + "\n".join(parts) + "\n</defs></svg>\n")
    for fid, sid in OBJ.items():
        if fid.startswith("_"):
            continue
        m = re.search(r'<symbol id="%s" viewBox="([^"]+)"' % re.escape(sid), lib)
        vb[fid] = (sid, m.group(1))
    return lib, vb


# ---------------------------------------------------------------- Automatisch gesetzte Bilder (bilder_auto.py)
import bilder_auto as _auto  # noqa: E402
import bildsymbole as _bs  # noqa: E402
import figuren as _fg  # noqa: E402

for _k, _v in _fg.anime_chars().items():
    CHAR.setdefault(_k, _v)
_SYMS = _bs.all_symbols()
KEY = {fid: k for fid, (k, _) in PORTRAITS.items()}
for _fid, _p in _fg.FIGS.items():
    if _p is not None:
        KEY.setdefault(_fid, _fg.slug(_fid))
        PORTRAITS.setdefault(_fid, (_fg.slug(_fid), "calm"))
for _k, _v in _SYMS.items():
    OBJ.setdefault(_k, "an-" + _v["sym"][4:])
    if _v["sym"] not in COPY:
        COPY.append(_v["sym"])
EXTRA_META = {k: (v["place"], tuple(v["size"])) for k, v in _SYMS.items()}
GROUP_KEYS = {"FIG-GRUPPE-MENGE": ("menge2", "menge3", "menge"), "FIG-GRUPPE-ZWOELF": ("juenger2", "juenger", "andreas")}
POSE_SHIFT = {"sit": 6, "kneel": 4}


class AniComposer(_auto.Composer):
    water_feet, water_lift = 140, 26  # Brustbild: Wellen am unteren Bildrand der Figur
    _hr = 12

    def vb(self, fid):
        return self.vbmap[fid][1]

    def head_r(self):
        return self._hr

    def icon_h(self):
        return 24

    def r_floor(self):
        return FLOOR

    def r_band(self, t):
        w, h = self.m(t)[1]
        return use(OBJ[t], 0, 140 - h, w, h)

    def r_back(self, t, x, y, w, h):
        return use(OBJ[t], round(x, 1), round(y, 1), w, h, '' if t == "FIG-GRUPPE-GEMEINDE" else ' opacity=".6"')

    def r_sym(self, t, x, y, w, h, flip=False):
        sym = OBJ.get(t) or self.vbmap[t][0]
        if flip:
            return f'<g transform="translate({x + w:.1f} {y:.1f}) scale(-1 1)">{use(sym, 0, 0, w, h)}</g>'
        return use(sym, round(x, 1), round(y, 1), w, h)

    def r_icon(self, t, x, y, w, h):
        return use(self.vbmap[t][0], round(x, 1), round(y, 1), round(w, 1), round(h, 1))

    def r_bubble(self, x, y, w, h, tx, ty, inner):
        return bubble(round(x, 1), round(y, 1), round(w, 1), round(h, 1), round(tx, 1), round(ty, 1), inner)

    def r_head_sign_native(self, t):
        return t in ("FIG-ZEICHEN-TRAUER", "FIG-ZEICHEN-FREUDE")

    def _feel(self, fid, p, speaking):
        st = p.get("stage") or {}
        who = st.get("signs_who") or {}
        humans = [f for f in p["figures"] if f not in ("FIG-GOTT", "FIG-HEILIGER-GEIST", "FIG-JESUS")]
        tears = "FIG-ZEICHEN-TRAUER" in p["signs"] and fid in who.get("FIG-ZEICHEN-TRAUER", humans)
        joy = "FIG-ZEICHEN-FREUDE" in p["signs"] and fid in who.get("FIG-ZEICHEN-FREUDE", humans)
        expr = (st.get("mood") or {}).get(fid)
        if not expr:
            expr = "worried" if tears else "delight" if joy else "calm"
        if (st.get("pose") or {}).get(fid) == "sleep":
            expr = "sleep"
        return expr, tears, joy

    def _draw(self, fid, x, y, s, expr, look, arm, tears, hold, pose, out, joy=False, p_stage=None):
        key = KEY[fid]
        ang = {1: -24, -1: 204}.get(arm) if arm is not None else None
        a = (ang, 10) if ang is not None else None
        if hold == "PRAY":
            hold = "an-z-beten"
        wear = ((p_stage or {}).get("wear") or {}).get(fid)
        if wear:
            key = self._sackkey(key, wear)
        if hold is None and pose == "kneel":  # Knien: gefaltete Hände machen die Haltung lesbar
            hold = "an-z-beten"
        if hold is None and CHAR[key].get("attr"):
            hold = CHAR[key]["attr"]
        elif hold is not None and not hold.startswith("an-"):
            hw, hh = self.m(hold)[1]
            if hw >= 26 or hh >= 30:  # grosse Gegenstände (Kreuz, Krug) neben die Figur statt klein vor die Brust
                out.append(self.r_sym(hold, x + 12 * s, y - 6 * s, hw * 1.1, hh * 1.1))
                hold = None
            else:
                hold = OBJ.get(hold) or self.vbmap[hold][0]
        flip = pose == "away"
        if fid in GROUP_KEYS or (fid.startswith("FIG-GRUPPE-") and fid != "FIG-GRUPPE-GEMEINDE"):
            keys = GROUP_KEYS.get(fid, (key, key, key))
            if wear:
                keys = tuple(self._sackkey(k, wear) for k in keys)
            sp = 13 * s
            bk = f'<g opacity=".75">{person(keys[1], x - 6 * s, y - 5 * s, s * .66, expr, look, None, flip, tears)}{person(keys[0], x + 7 * s, y - 6 * s, s * .64, expr, look, None, flip, tears)}</g>'
            g = (bk + person(keys[0], x - sp, y + 3 * s, s * .82, expr, look, None, flip, tears)
                 + person(keys[1], x + sp, y + 4 * s, s * .8, expr, look, None, flip, tears)
                 + person(keys[2], x, y, s, expr, look, a, flip, tears, hold))
        else:
            g = person(key, x, y, s, expr, look, a, flip, tears, hold)
        if pose in ("lie", "sleep"):
            mat = (f'<path d="M{x - 34 * s:.1f} {y + 29 * s:.1f}h{56 * s:.1f}v{5 * s:.1f}h{-56 * s:.1f}z" fill="#C9B48E" stroke="{INK}" stroke-width="{.8 * s:.1f}"/>')
            g = mat + f'<g transform="rotate(-80 {x:.1f} {y + 20 * s:.1f})">{g}</g>'
        elif pose == "kneel":  # Brustbild deutlich vorgeneigt zur angesprochenen bzw. gegenüberstehenden Seite (Blindtest: 18° wurde als Stehen gelesen)
            g = f'<g transform="rotate({26 if (look or 0) >= 0 else -26} {x:.1f} {y + 30 * s:.1f})">{g}</g>'
        elif pose == "fall":
            g = f'<g transform="rotate(32 {x:.1f} {y + 18 * s:.1f})">{g}</g>'
        out.append(g)
        if joy:
            out.append(sparkle(x - 13 * s, y - 10 * s, .7 * s) + sparkle(x + 13 * s, y - 12 * s, .6 * s))

    def _sackkey(self, k, wear="sack"):
        """Kleidung wechseln: sack, binden oder Mantelfarbe (#RRGGBB)."""
        if "~" in k:
            return k
        k2 = k + "~" + wear
        if k2 not in CHAR:
            c = dict(CHAR[k])
            if wear == "sack":
                c = {a: v for a, v in c.items() if a not in ("mantle", "trim", "sash", "toga", "breast", "belt", "apron")}
                c["robe"], c["belt"] = "#6A5E52", "#4E453C"
            elif wear == "binden":
                c = {a: v for a, v in c.items() if a not in ("mantle", "trim", "sash", "toga", "breast", "belt", "apron")}
                c["robe"], c["sash"] = "#F4F1EA", "#C9BFAA"
            else:
                c["mantle"] = wear
            CHAR[k2] = c
        return k2

    def r_person(self, s, n, look, arm, hold, p, out):
        fid, x = s["fid"], s["x"]
        st = p.get("stage") or {}
        pose = (st.get("pose") or {}).get(fid)
        sc = {1: 1.5, 2: 1.4, 3: 1.22, 4: 1.06, 5: .94}.get(n, .84)
        if any(_auto.meta(t, self.lex, EXTRA_META)[0] == "big" for t in p["objects"] + p["signs"]):
            sc = min(sc, 1.0)
        if s["group"]:
            sc *= .92
        self._hr = 12 * sc
        y = 140 - 34 * sc + 4 + POSE_SHIFT.get(pose, 0) * sc
        half = (17 + (11 if (fid in GROUP_KEYS or fid.startswith("FIG-GRUPPE-")) else 0)) * sc + 3
        if pose in ("lie", "sleep"):  # liegende Figur ganz ins Feld (Blindtest: rechts abgeschnitten)
            x = max(36 * sc, min(_auto.W - 26 * sc, x))
            s["x"] = x
        elif pose != "fall":
            x = max(half, min(_auto.W - half, x))
            s["x"] = x
        expr, tears, joy = self._feel(fid, p, False)
        self._draw(fid, x, y, sc, expr, look * 1.6, arm, tears, hold, pose, out, joy, st)
        if pose in ("lie", "sleep"):
            return (x - 18 * sc, y + 22 * sc)
        if pose == "fall":
            return (x + 8 * sc, y + 4 * sc)
        return (x, y)

    def r_inside(self, fid, cx, cy, w, p, out):
        st = p.get("stage") or {}
        pose = (st.get("pose") or {}).get(fid)
        sc = .62 if w > 90 else .5
        expr, tears, joy = self._feel(fid, p, False)
        self._hr = 12 * sc
        y = cy - 10 * sc
        self._draw(fid, cx, y, sc, expr, 0, None, tears, None, pose, out, joy, st)
        if pose in ("lie", "sleep"):
            return (cx - 18 * sc, y + 22 * sc)
        return (cx, y)


def upper_auto(key, n):
    brief = json.loads((D / "illustrations/briefs" / f"BRIEF-{key}.json").read_text(encoding="utf-8"))
    c = AniComposer(_auto.gather_lex(), EXTRA_META)
    c.vbmap = _VB
    c.uid = "a" + key.lower()
    return c.panel(brief["panels"][n - 1])


def auto_svg(suffix, vb):
    lex = _auto.gather_lex()
    brief = json.loads((D / "illustrations/briefs" / f"BRIEF-{suffix}.json").read_text(encoding="utf-8"))
    c = AniComposer(lex, EXTRA_META)
    c.vbmap = vb
    c.uid = "a" + suffix.lower()
    return alayout([c.panel(p) for p in brief["panels"]])


ILL_UPPER_ALT = {'BIBLE': ('Comic in vier Bildern ohne Text: 1 Am Berg spricht Gott (Strahlenkranz mit dem Gottesnamen) und gibt die Tafeln; Mose hält sie, das Volk staunt. 2 Jesus, das Kreuz und das leere Grab. 3 Die leuchtende Stadt mit Strom und Baum, darüber der Strahlenkranz. 4 Schriftrolle, Leier, ein Prophet und ein Brief.', 'Comic i vier Bilder ohni Text: 1 Am Bärg redt Gott (Strahlechranz mit em Gottesname) und git d Tafle; de Mose hebt si, s Volk stuunt. 2 De Jesus, s Chrüz und s lääre Grab. 3 Di lüüchtend Stadt mit Strom und Baum, drüber de Strahlechranz. 4 Schriftrolle, Leier, en Prophet und en Brief.'), 'OT': ('Comic in vier Bildern ohne Text: 1 Gott spricht «Licht»; Sonne, Mond, Sterne und Pflanze entstehen. 2 Mose hebt den Stab, das Volk geht froh durch das geteilte Meer. 3 Am Berg spricht Gott und gibt die Tafeln; Mose hält sie, das Volk staunt. 4 Jerusalem mit Rissen, Menschen in Tränen auf dem Weg weg und zurück; ein Prophet spricht von Hoffnung (Spross).', 'Comic i vier Bilder ohni Text: 1 Gott redt «Liecht»; Sunne, Mond, Stärn und Pflanze entstönd. 2 De Mose hebt de Stab, s Volk gaat froh dur s teilte Meer. 3 Am Bärg redt Gott und git d Tafle; de Mose hebt si, s Volk stuunt. 4 Jerusalem mit Riss, Mänsche i Träne uf em Wäg ewäg und zrugg; en Prophet redt vo Hoffnig (Schoss).'), 'NT': ('Comic in vier Bildern ohne Text: 1 Jesus spricht zur aufmerksamen Menge (Gottesname, Umkehr-Pfeil, Herz). 2 Kreuz und leeres Grab. 3 Die Geist-Taube über zwei Jüngern mit Flammen und leuchtenden Augen; Pfeile zu einer Gemeinde, ein Brief. 4 Strahlenkranz, Waage und die leuchtende Stadt.', 'Comic i vier Bilder ohni Text: 1 De Jesus redt zur ufmerksame Mängi (Gottesname, Umchehr-Pfiil, Härz). 2 Chrüz und lääres Grab. 3 D Geischt-Tube über zwei Jünger mit Flamme und lüüchtende Auge; Pfiil zu ere Gmeind, en Brief. 4 Strahlechranz, Waag und di lüüchtend Stadt.'), 'GROUP-01': ('Comic in zwei Bildern ohne Text: 1 Gott spricht «Licht»; Sonne, Mond, Sterne und Pflanze entstehen. 2 Hinter dem Volk das geteilte Meer; am Berg spricht Gott und gibt die Tafeln, Mose hält sie, das Volk staunt.', 'Comic i zwei Bilder ohni Text: 1 Gott redt «Liecht»; Sunne, Mond, Stärn und Pflanze entstönd. 2 Hinder em Volk s teilte Meer; am Bärg redt Gott und git d Tafle, de Mose hebt si, s Volk stuunt.'), 'GROUP-02': ('Comic in zwei Bildern ohne Text: 1 Ein König mit Krone vor Jerusalem, zufriedene Menschen. 2 Jerusalem mit Rissen; Menschen in Tränen, Weg weg und gestrichelt zurück.', 'Comic i zwei Bilder ohni Text: 1 En Chünig mit Chrone vor Jerusalem, zfrideni Mänsche. 2 Jerusalem mit Riss; Mänsche i Träne, Wäg ewäg und gstrichlet zrugg.'), 'GROUP-03': ('Comic in drei Bildern ohne Text: 1 Ein Mensch mit Leier spricht mit geschlossenen Augen zu Gott (Träne und Freude). 2 Braut und Bräutigam lächeln unter der Girlande. 3 Ein Mensch mit Schriftrolle denkt nach; Sanduhr und Waage.', 'Comic i drüü Bilder ohni Text: 1 En Mänsch mit Leier redt mit zuene Auge zu Gott (Träne und Fröid). 2 Brut und Brüütigam lächled under de Girlande. 3 En Mänsch mit Schriftrolle dänkt nache; Sanduhr und Waag.'), 'GROUP-04': ('Comic in zwei Bildern ohne Text: 1 Ein Prophet spricht zur besorgten Menge (Gottesname, Waage, Umkehr-Pfeil). 2 Jerusalem mit Rissen, Menschen in Tränen weggeführt; der Prophet spricht von Hoffnung (Spross).', 'Comic i zwei Bilder ohni Text: 1 En Prophet redt zur bsorgte Mängi (Gottesname, Waag, Umchehr-Pfiil). 2 Jerusalem mit Riss, Mänsche i Träne wäggfüert; de Prophet redt vo Hoffnig (Schoss).'), 'GROUP-05': ('Comic in zwei Bildern ohne Text: 1 Zwölf kleine Schriftrollen; ein Prophet spricht zur besorgten Menge (Gottesname, Waage, Umkehr-Pfeil). 2 Strahlenkranz über dem heilen Jerusalem, ein Spross, Menschen freuen sich.', 'Comic i zwei Bilder ohni Text: 1 Zwölf chlini Schriftrolle; en Prophet redt zur bsorgte Mängi (Gottesname, Waag, Umchehr-Pfiil). 2 Strahlechranz über em ganze Jerusalem, en Schoss, Mänsche fröied sich.'), 'GROUP-06': ('Comic in zwei Bildern ohne Text: 1 Vier kleine Schriftrollen; Jesus spricht zur aufmerksamen Menge (Gottesname, Umkehr-Pfeil, Herz). 2 Kreuz und leeres Grab.', 'Comic i zwei Bilder ohni Text: 1 Vier chlini Schriftrolle; de Jesus redt zur ufmerksame Mängi (Gottesname, Umchehr-Pfiil, Härz). 2 Chrüz und lääres Grab.'), 'GROUP-07': ('Comic in zwei Bildern ohne Text: 1 Die Geist-Taube kommt herab, über drei strahlenden Jüngern Flammen, dahinter Jerusalem. 2 Von Jerusalem gehen Pfeile zu einer Gemeinde; ein Schiff; Paulus mit einem Soldaten.', 'Comic i zwei Bilder ohni Text: 1 D Geischt-Tube chunnt abe, über drüü strahlende Jünger Flamme, dehinder Jerusalem. 2 Vo Jerusalem gönd Pfiil zu ere Gmeind; es Schiff; de Paulus mit eme Soldat.'), 'GROUP-08': ('Paulus spricht (Sprechblase: Kreuz und Herz); ein Brief fliegt zu einer Gemeinde vor einem Haus.', 'De Paulus redt (Sprächblase: Chrüz und Härz); en Brief flügt zu ere Gmeind vor eme Huus.'), 'GROUP-09': ('Drei Briefe gehen zu einer Gemeinde vor einem Haus; über der Gemeinde Herzen.', 'Drüü Brief gönd zu ere Gmeind vor eme Huus; über de Gmeind Härz.'), 'GROUP-10': ('Comic in zwei Bildern ohne Text: 1 Oben gross der Strahlenkranz; darunter schauen ein König und ein Soldat erstaunt hinauf, daneben Menschen in Tränen. 2 Die leuchtende Stadt mit Strom und Baum, darüber der Strahlenkranz; Menschen freuen sich.', 'Comic i zwei Bilder ohni Text: 1 Obe gross de Strahlechranz; drunder lueged en Chünig und en Soldat erstuunt ufe, dernäbe Mänsche i Träne. 2 Di lüüchtend Stadt mit Strom und Baum, drüber de Strahlechranz; Mänsche fröied sich.'), 'JHN-002': ('Comic in drei Bildern ohne Text: 1 Hochzeit: Jesus, Wasserkrüge, Pfeil zum Weinkrug, ein Stern; Braut und Bräutigam lächeln. 2 Jesus hebt die Geissel über dem davonlaufenden Schaf, ein Händler weicht zurück. 3 Menschen mit leuchtenden Augen und Herzen; eine gestrichelte Linie, Jesus wendet sich ernst ab.', 'Comic i drüü Bilder ohni Text: 1 Hochziit: de Jesus, Wasserchrüeg, Pfiil zum Wiichrueg, en Stern; Brut und Brüütigam lächled. 2 De Jesus hebt d Geissle über em Schaf, wo dervo rennt, en Händler wiicht zrugg. 3 Mänsche mit lüüchtende Auge und Härz; e gstrichleti Linie, de Jesus wändet sich ernscht ab.'), 'JHN': ('Ein brauner Adler mit ausgebreiteten Flügeln unter einem Licht mit Strahlen und funkelnden Sternchen, darunter eine Schriftrolle, auf nachtblauem Grund.', 'En brune Adler mit uusbreitete Flügel under eme Liecht mit Strahle und funkelnde Stärnli, drunder e Schriftrolle, uf nachtblauem Grund.')}


# Überarbeitung der oberen Ebenen (2026-10-17)
ILL_UPPER_ALT.update({'GROUP-01': ('Comic in drei Bildern ohne Text: 1 Der Strahlenkranz spricht (Licht); Erde mit Pflanze, Sonne, Mond und Sternen. 2 Gott spricht zu Abraham (Sprechblase: Sternenhimmel über grünem Land). 3 Hinter dem Volk das geteilte Meer; am Berg spricht der Strahlenkranz (Tafeln); Mose mit den Tafeln, das Volk.', 'Comic i drüü Bilder ohni Text: 1 De Strahlechranz redt (Liecht); Erde mit Pflanze, Sunne, Mond und Stärn. 2 Gott redt zum Abraham (Sprächblase: Stärnehimmel über grüenem Land). 3 Hinder em Volk s teilte Meer; am Bärg redt de Strahlechranz (Tafle); de Mose mit de Tafle, s Volk.'), 'GROUP-02': ('Comic in vier Bildern ohne Text: 1 Menschen ziehen in ein grünes Land mit Fluss. 2 Ein König vor Jerusalem, daneben Menschen. 3 Jerusalem mit Rissen; Menschen mit Tränen; ein Weg mit Pfeil weg und gestrichelt zurück. 4 Menschen freuen sich vor Jerusalem; Steine werden aufeinandergesetzt (Pfeil nach oben).', 'Comic i vier Bilder ohni Text: 1 Mänsche zieh i es grüens Land mit eme Fluss. 2 En Chünig vor Jerusalem, dernäbe Mänsche. 3 Jerusalem mit Riss; Mänsche mit Träne; en Wäg mit Pfiil ewäg und gstrichlet zrugg. 4 Mänsche fröied sich vor Jerusalem; Stei wärdet ufenand gsetzt (Pfiil ufe).'), 'GROUP-04': ('Comic in zwei Bildern ohne Text: 1 Oben der Strahlenkranz, eine goldene Linie führt zum Propheten; er spricht zur Menge (Waage, Umkehr-Pfeil). 2 Strahlenkranz mit Linie zum Propheten; Jerusalem mit Rissen, Menschen mit Tränen auf dem Weg weg und zurück; der Prophet spricht von Hoffnung (Spross).', 'Comic i zwei Bilder ohni Text: 1 Obe de Strahlechranz, e goldigi Linie füert zum Prophet; er redt zur Mängi (Waag, Umchehr-Pfiil). 2 Strahlechranz mit Linie zum Prophet; Jerusalem mit Riss, Mänsche mit Träne uf em Wäg ewäg und zrugg; de Prophet redt vo Hoffnig (Schoss).'), 'GROUP-05': ('Comic in zwei Bildern ohne Text: 1 Zwölf kleine Schriftrollen; der Strahlenkranz mit goldener Linie zum Propheten, der zur Menge spricht (Waage, Umkehr-Pfeil). 2 Strahlenkranz über dem heilen Jerusalem, ein Spross, Menschen freuen sich.', 'Comic i zwei Bilder ohni Text: 1 Zwölf chlini Schriftrolle; de Strahlechranz mit goldiger Linie zum Prophet, wo zur Mängi redt (Waag, Umchehr-Pfiil). 2 Strahlechranz über em ganze Jerusalem, en Schoss, Mänsche fröied sich.'), 'GROUP-07': ('Comic in zwei Bildern ohne Text: 1 Die Geist-Taube über drei Jüngern mit Flammen über den Köpfen, dahinter Jerusalem. 2 Von Jerusalem gehen Pfeile aus nach Rom (Säulenhalle mit rotem Dach); davor Paulus mit Brief und ein Soldat.', 'Comic i zwei Bilder ohni Text: 1 D Geischt-Tube über drüü Jünger mit Flamme über de Chöpf, dehinder Jerusalem. 2 Vo Jerusalem gönd Pfiil uus uf Rom (Süülehalle mit rotem Dach); devor de Paulus mit Brief und en Soldat.'), 'GROUP-09': ('Ein Bote mit Brief spricht zu einer Gemeinde vor einem Haus (Sprechblase: Herz mit Strahlen, Anker, zwei Herzen, zwei Schriftrollen mit Haken und Kreuz).', 'En Bott mit Brief redt zu ere Gmeind vor eme Huus (Sprächblase: Härz mit Strahle, Anker, zwei Härz, zwei Schriftrolle mit Hake und Chrüz).')})
ILL_UPPER_ALT['OT'] = (ILL_UPPER_ALT['OT'][0] + ' Oben der Strahlenkranz mit Linie zum Propheten.', ILL_UPPER_ALT['OT'][1] + ' Obe de Strahlechranz mit Linie zum Prophet.')


ILL = {
    "ILL-ANI-JHN-002-013-022": ("BRIEF-JHN-002-013-022", tempel,
                                "Comic in zwei Bildern ohne Text: 1 Vor dem Tempel hält Jesus ernst die Geissel erhoben; ein Tisch kippt, Münzen fliegen, ein Händler weicht erschrocken zurück, "
                                "über dem davonlaufenden Schaf die erhobene Geissel, Tauben im Käfig; Sprechblase: Tempel, Münzen, durchgestrichen. 2 Menschen aus der Menge fragen nach einem Zeichen (Stern, Fragezeichen); "
                                "Jesus antwortet: Menge, Tempel mit Riss, drei Sonnen, Jesus, Tempel.",
                                "Comic i zwei Bilder ohni Text: 1 Vor em Tämpel hebt de Jesus ernscht d Geissle uf; en Tisch kippt, Münz flüüged, en Händler wiicht verschrocke zrugg, "
                                "über em Schaf, wo dervo rennt, di ufghabeni Geissle, Tube im Chäfig; Sprächblase: Tämpel, Münz, durgstriche. 2 Mänsche us de Mängi fröged nach eme Zeiche (Stern, Fragezeiche); "
                                "de Jesus antwortet: Mängi, Tämpel mit Riss, drüü Sunne, Jesus, Tämpel."),
    "ILL-ANI-JHN-002-023-025": ("BRIEF-JHN-002-023-025", glaube,
                                "Menschen in Jerusalem mit leuchtenden Augen unter goldenen Sternen (Zeichen), über ihnen Herzen (sie glauben); eine gestrichelte Linie trennt sie von Jesus, "
                                "der sich ernst zur Seite abwendet; im Hintergrund der Tempel.",
                                "Mänsche z Jerusalem mit lüüchtende Auge under goldige Stärn (Zeiche), über ine Härz (si glaubed); e gstrichleti Linie trännt si vom Jesus, "
                                "wo sich ernscht uf d Siite abwändet; im Hindergrund de Tämpel."),
    "ILL-ANI-JHN-002-001-012": ("BRIEF-JHN-002-001-012", kana,
                                "Comic in vier Bildern ohne Text: 1 Beim Hochzeitsfest zeigt Maria besorgt auf den leeren Weinkrug und den leeren Becher; Jesus antwortet ruhig mit der Sanduhr. "
                                "2 Maria zeigt den Dienern: Jesus und das Ohr (hört auf ihn); die Diener staunen. 3 Jesus weist auf die sechs Krüge, ein Diener giesst Wasser ein; Sprechblase: Krug, Pfeil, Speisemeister. "
                                "4 Der Speisemeister kostet strahlend und zeigt den Becher dem staunenden Bräutigam (Sprechblase: Becher und Funken – ausgezeichnet); über Jesus ein Stern, die Jünger mit leuchtenden Augen und Herzen.",
                                "Comic i vier Bilder ohni Text: 1 Am Hochziitsfäscht zeigt d Maria bsorget uf de läär Wiichrueg und de läär Becher; de Jesus antwortet ruhig mit de Sanduhr. "
                                "2 D Maria zeigt de Diener: de Jesus und s Ohr (losed uf ihn); d Diener stuuned. 3 De Jesus zeigt uf di sächs Chrüeg, en Diener schüttet Wasser ii; Sprächblase: Chrueg, Pfiil, Spiismeischter. "
                                "4 De Spiismeischter probiert strahlend und zeigt de Becher em stuunende Brüütigam (Sprächblase: Becher und Funke – usgezeichnet); über em Jesus en Stern, d Jünger mit lüüchtende Auge und Härz."),
}


ILL.update({f"ILL-ANI-{k}": (f"BRIEF-{k}", (lambda k=k: alayout([f() for f in UPPER[k]])), a, g) for k, (a, g) in ILL_UPPER_ALT.items() if k in UPPER})
ILL["ILL-ANI-JHN"] = ("BRIEF-JHN", a_buch, *ILL_UPPER_ALT["JHN"])
_VB = {}
for _b in _auto.load_briefs():
    ILL[f"ILL-ANI-{_b['suffix']}"] = (f"BRIEF-{_b['suffix']}", (lambda s=_b["suffix"]: auto_svg(s, _VB)),
                                      _auto.alt_text(_b, "de", anime=True), _auto.alt_text(_b, "gsw", anime=True))


def run():
    OUT.mkdir(parents=True, exist_ok=True)
    lex = {p.stem for p in (D / "illustrations/lexicon").glob("FIG-*.json")}
    lib, vb = library()
    _VB.update(vb)
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
        CUR[0] = rid.replace("ILL-ANI-", "").lower()
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
