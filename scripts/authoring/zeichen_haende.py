#!/usr/bin/env python3
"""Zeichen mit Händen und Gesten aus der Handbibliothek (haende.py) – Neuzeichnung nach der Durchsicht Runde 11
(docs/SYMBOLPROZESS.md, «Durchsicht und Gestaltungsregeln», 2026-10-25).

    python3 scripts/authoring/zeichen_haende.py --entwuerfe E.json        # alle Fassungen als Entwürfe für zeichen_test.py
    python3 scripts/authoring/zeichen_haende.py --schreiben               # gewählte, bestandene Fassungen nach
                                                                         # bildsymbole_daten/ueberarbeitet/haende.json

Jedes Zeichen hat ein benanntes Vorbild (Emoji, Piktogramm) und eine bis drei Fassungen (@1, @2, @3). GEWAEHLT hält fest,
welche Fassung die Gestaltungskritik bestanden hat; nur diese werden geschrieben.
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import haende as H  # noqa: E402
from haende import INK, SKIN, SLEEVE, GOLD, place, line, cuff  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "scripts/authoring/bildsymbole_daten/ueberarbeitet/haende.json"

RED, WATER, WOOD, PAPER = "#C8423A", "#5BA7D9", "#8A5A34", "#F4EAD2"
ROBE = {"blau": "#5E7FA8", "gruen": "#3E7A6E", "braun": "#A86A4A", "lila": "#7E5A8E", "rost": "#A85A3E", "gelb": "#E2C25A",
        "grau": "#A79A80", "weiss": "#ECE6DA"}
HAIR = {"dunkel": "#4A3424", "braun": "#6A4A2A", "schwarz": "#2E2420", "grau": "#B8B0A4"}


def _f(v):
    return H._f(v)


# ------------------------------------------------------------------ Figuren (einfach, flach, wie die bisherigen Zeichen)
def kopf(cx, cy, r=4.6, haar=HAIR["dunkel"], gesicht="ruhig", schleier=None, neig=0):
    """Kopf mit Haarkappe und Gesicht. gesicht: ruhig | froh | traurig | schmerz | geschlossen."""
    s = ""
    if schleier:
        s += (f'<path d="M{_f(cx - r * 1.2)} {_f(cy + r * 1.5)}Q{_f(cx - r * 1.3)} {_f(cy - r * 1.35)} {_f(cx)} {_f(cy - r * 1.35)}'
              f'Q{_f(cx + r * 1.3)} {_f(cy - r * 1.35)} {_f(cx + r * 1.2)} {_f(cy + r * 1.5)}Z" fill="{schleier}" stroke="{INK}" stroke-width="1.1" stroke-linejoin="round"/>')
    s += f'<circle cx="{_f(cx)}" cy="{_f(cy)}" r="{_f(r)}" fill="{SKIN}" stroke="{INK}" stroke-width="1.15"/>'
    hc = schleier or haar
    s += (f'<path d="M{_f(cx - r)} {_f(cy - .1)}Q{_f(cx - r)} {_f(cy - r * 1.02)} {_f(cx)} {_f(cy - r * 1.02)}T{_f(cx + r)} {_f(cy - .1)}'
          f'Q{_f(cx)} {_f(cy - r * .52)} {_f(cx - r)} {_f(cy - .1)}Z" fill="{hc}" stroke="{INK}" stroke-width=".8" stroke-linejoin="round"/>')
    ex, ey = r * .4, cy + r * .12
    if gesicht in ("ruhig", "froh"):
        s += f'<circle cx="{_f(cx - ex)}" cy="{_f(ey)}" r=".55" fill="{INK}"/><circle cx="{_f(cx + ex)}" cy="{_f(ey)}" r=".55" fill="{INK}"/>'
        if gesicht == "froh":
            s += line(f"M{_f(cx - r * .3)} {_f(cy + r * .5)}Q{_f(cx)} {_f(cy + r * .8)} {_f(cx + r * .3)} {_f(cy + r * .5)}", .6)
    elif gesicht in ("geschlossen", "traurig"):
        s += line(f"M{_f(cx - ex - .6)} {_f(ey)}q.6.5 1.2 0M{_f(cx + ex - .6)} {_f(ey)}q.6.5 1.2 0", .6)
        if gesicht == "traurig":
            s += line(f"M{_f(cx - r * .25)} {_f(cy + r * .7)}Q{_f(cx)} {_f(cy + r * .5)} {_f(cx + r * .25)} {_f(cy + r * .7)}", .6)
    elif gesicht == "schmerz":
        s += line(f"M{_f(cx - ex - .7)} {_f(ey - .5)}l1.2.5-1.2.5M{_f(cx + ex + .7)} {_f(ey - .5)}l-1.2.5 1.2.5", .6)
        s += line(f"M{_f(cx - r * .25)} {_f(cy + r * .65)}h{_f(r * .5)}", .6)
    if neig:
        s = f'<g transform="rotate({_f(neig)} {_f(cx)} {_f(cy + r)})">{s}</g>'
    return s


def rumpf(cx, top, bottom, w_top, w_bot, robe):
    """Gewand als Trapez mit runden Schultern."""
    return (f'<path d="M{_f(cx - w_top / 2)} {_f(top + 2)}Q{_f(cx - w_top / 2)} {_f(top)} {_f(cx - w_top / 2 + 2)} {_f(top)}'
            f'H{_f(cx + w_top / 2 - 2)}Q{_f(cx + w_top / 2)} {_f(top)} {_f(cx + w_top / 2)} {_f(top + 2)}'
            f'L{_f(cx + w_bot / 2)} {_f(bottom)}H{_f(cx - w_bot / 2)}Z" fill="{robe}" stroke="{INK}" stroke-width="1.15" stroke-linejoin="round"/>')


def figur(cx, boden, h=28, robe=ROBE["braun"], haar=HAIR["dunkel"], gesicht="ruhig", schleier=None, neig=0, r=None):
    """Stehende Figur (Halbfigur bis zum Boden des Zeichens): Kopf oben, Gewand darunter."""
    r = r or h * .17
    cy = boden - h + r
    return rumpf(cx, cy + r + .2, boden, r * 2.3, r * 3.0, robe) + kopf(cx, cy, r, haar, gesicht, schleier, neig)


def sitzend(cx, boden, h=18, robe=ROBE["grau"], haar=HAIR["braun"], gesicht="traurig", neig=0, blick=1):
    """Sitzende, kauernde Figur (Knie nach vorn, blick=1 nach rechts, -1 nach links)."""
    r = h * .25
    cy = boden - h + r
    b = blick
    body = (f'<path d="M{_f(cx - b * r * 1.2)} {_f(boden)}Q{_f(cx - b * r * 1.4)} {_f(cy + r * 1.3)} {_f(cx - b * r * .2)} {_f(cy + r * 1.05)}'
            f'Q{_f(cx + b * r * .9)} {_f(cy + r * 1.1)} {_f(cx + b * r * 1.1)} {_f(cy + r * 2.2)}L{_f(cx + b * r * 2.2)} {_f(boden - r * .9)}'
            f'Q{_f(cx + b * r * 2.6)} {_f(boden)} {_f(cx + b * r * 2.0)} {_f(boden)}Z" fill="{robe}" stroke="{INK}" stroke-width="1.15" stroke-linejoin="round"/>')
    return body + kopf(cx, cy, r, haar, gesicht, None, neig)


def strahlen(cx, cy, r0, r1, winkel, col=GOLD, w=1.3):
    import math
    d = ""
    for a in winkel:
        t = math.radians(a)
        d += f"M{_f(cx + r0 * math.cos(t))} {_f(cy + r0 * math.sin(t))}L{_f(cx + r1 * math.cos(t))} {_f(cy + r1 * math.sin(t))}"
    return line(d, w, col)


def bogen(d, w=1.0):
    return line(d, w, INK)


# ------------------------------------------------------------------ Gegenstände
def brot(cx, cy, w=8, h=4.4):
    return (f'<ellipse cx="{_f(cx)}" cy="{_f(cy)}" rx="{_f(w / 2)}" ry="{_f(h / 2)}" fill="#D9A55A" stroke="{INK}" stroke-width="1.1"/>'
            + line(f"M{_f(cx - w * .22)} {_f(cy - h * .3)}l{_f(w * .08)} {_f(h * .45)}M{_f(cx + w * .04)} {_f(cy - h * .36)}l{_f(w * .08)} {_f(h * .5)}"
                   f"M{_f(cx + w * .28)} {_f(cy - h * .28)}l{_f(w * .06)} {_f(h * .4)}", .7, "#9A6A2A"))


def paket(x, y, w=7, h=5.4):
    return (f'<rect x="{_f(x)}" y="{_f(y)}" width="{_f(w)}" height="{_f(h)}" rx=".6" fill="#C99A5E" stroke="{INK}" stroke-width="1.1"/>'
            + line(f"M{_f(x + w / 2)} {_f(y)}v{_f(h)}M{_f(x)} {_f(y + h / 2)}h{_f(w)}", .8, "#7A4E24"))


def stapel(cx, base, n=3, r=3.0):
    """Münzstapel: n Münzen von der Seite, oberste mit Prägung von oben angedeutet."""
    s = ""
    for i in range(n):
        y = base - i * 1.7
        s += (f'<path d="M{_f(cx - r)} {_f(y - 1)}V{_f(y)}Q{_f(cx)} {_f(y + 1.4)} {_f(cx + r)} {_f(y)}V{_f(y - 1)}Z" fill="#C9981E" stroke="{INK}" stroke-width=".9" stroke-linejoin="round"/>')
    y = base - (n - 1) * 1.7 - 1
    s += f'<ellipse cx="{_f(cx)}" cy="{_f(y)}" rx="{_f(r)}" ry="1.3" fill="{GOLD}" stroke="{INK}" stroke-width=".9"/>'
    return s


def krug(x, y, a=0):
    """Wasserkrug, Ausguss rechts; (x,y) Ausguss."""
    k = (f'<path d="M-9.6-6.4Q-12.2-1.8-10.4 2.8Q-8.6 6.2-4.8 6.2Q-1 6.2.4 2.6Q1.8-1.6-.4-6.4Z" fill="#B9763E" stroke="{INK}" stroke-width="1.1" stroke-linejoin="round"/>'
         f'<path d="M-8.8-6.6H.2L1.8-8.4Q.4-9.6-1.4-8.8H-8.4Q-9.6-8.6-8.8-6.6Z" fill="#B9763E" stroke="{INK}" stroke-width="1.1" stroke-linejoin="round"/>'
         f'<path d="M-10.4-3.6Q-14-3-13.2.6Q-12.6 2.4-10.6 1.8" fill="none" stroke="{INK}" stroke-width="1.1"/>'
         + line("M-10.4-1.6Q-5.2-.4-.2-1.8", .7, "#7A4A22"))
    return place(place(k, -1.8, 8.4), x, y, a)


def tropfen(x, y, s=1.0):
    return (f'<path d="M{_f(x)} {_f(y - 1.7 * s)}Q{_f(x + 1.2 * s)} {_f(y)} {_f(x + .9 * s)} {_f(y + .5 * s)}A1 1 0 0 1 {_f(x - .9 * s)} {_f(y + .5 * s)}'
            f'Q{_f(x - 1.2 * s)} {_f(y)} {_f(x)} {_f(y - 1.7 * s)}Z" fill="{WATER}" stroke="{INK}" stroke-width=".7"/>')


def schale(cx, y, w=18):
    return (f'<path d="M{_f(cx - w / 2)} {_f(y)}Q{_f(cx - w * .42)} {_f(y + 5)} {_f(cx)} {_f(y + 5.2)}Q{_f(cx + w * .42)} {_f(y + 5)} {_f(cx + w / 2)} {_f(y)}Z" '
            f'fill="#9AA9B4" stroke="{INK}" stroke-width="1.1" stroke-linejoin="round"/>'
            f'<path d="M{_f(cx - w / 2 + 1.4)} {_f(y + .3)}H{_f(cx + w / 2 - 1.4)}" stroke="{WATER}" stroke-width="1.2"/>')


def rolle(x, y, w=16, h=5):
    """Schriftrolle waagrecht, links oben (x, y)."""
    return (f'<rect x="{_f(x + 1.4)}" y="{_f(y + .6)}" width="{_f(w - 2.8)}" height="{_f(h - 1.2)}" fill="{PAPER}" stroke="{INK}" stroke-width="1.1"/>'
            f'<rect x="{_f(x)}" y="{_f(y)}" width="2.6" height="{_f(h)}" rx="1.2" fill="#C9A56A" stroke="{INK}" stroke-width="1.1"/>'
            f'<rect x="{_f(x + w - 2.6)}" y="{_f(y)}" width="2.6" height="{_f(h)}" rx="1.2" fill="#C9A56A" stroke="{INK}" stroke-width="1.1"/>'
            + line(f"M{_f(x + 4)} {_f(y + h * .38)}h{_f(w - 8)}M{_f(x + 4)} {_f(y + h * .66)}h{_f(w - 10)}", .7, "#8A7A5A"))


def ring(cx, cy, r=3.4):
    return (f'<circle cx="{_f(cx)}" cy="{_f(cy)}" r="{_f(r)}" fill="none" stroke="{INK}" stroke-width="2.6"/>'
            f'<circle cx="{_f(cx)}" cy="{_f(cy)}" r="{_f(r)}" fill="none" stroke="{GOLD}" stroke-width="1.3"/>')


def herz(cx, cy, s=1.0):
    return (f'<path d="M{_f(cx)} {_f(cy + 3 * s)}Q{_f(cx - 4.2 * s)} {_f(cy)} {_f(cx - 3.2 * s)} {_f(cy - 2 * s)}Q{_f(cx - 2 * s)} {_f(cy - 3.6 * s)} '
            f'{_f(cx)} {_f(cy - 1.6 * s)}Q{_f(cx + 2 * s)} {_f(cy - 3.6 * s)} {_f(cx + 3.2 * s)} {_f(cy - 2 * s)}Q{_f(cx + 4.2 * s)} {_f(cy)} {_f(cx)} {_f(cy + 3 * s)}Z" '
            f'fill="#D9536A" stroke="{INK}" stroke-width=".9" stroke-linejoin="round"/>')


def schein(x, y, w=10, h=12, a=0, teil=None):
    """Schuldschein mit Münzzeichen; teil='l'/'r' für die zerrissenen Hälften (Rissrand gezackt)."""
    if teil == "l":
        d = f"M0 0H{_f(w * .55)}L{_f(w * .42)} {_f(h * .25)}L{_f(w * .58)} {_f(h * .5)}L{_f(w * .44)} {_f(h * .75)}L{_f(w * .54)} {_f(h)}H0Z"
    elif teil == "r":
        d = f"M{_f(w * .55)} 0H{_f(w)}V{_f(h)}H{_f(w * .54)}L{_f(w * .44)} {_f(h * .75)}L{_f(w * .58)} {_f(h * .5)}L{_f(w * .42)} {_f(h * .25)}Z"
    else:
        d = f"M0 0H{_f(w)}V{_f(h)}H0Z"
    s = f'<path d="{d}" fill="{PAPER}" stroke="{INK}" stroke-width="1.1" stroke-linejoin="round"/>'
    if teil != "r":
        s += line(f"M1.6 {_f(h * .62)}h{_f(w * .28)}M1.6 {_f(h * .8)}h{_f(w * .22)}", .8, "#8A7A5A")
        s += H.muenze(w * .27, h * .3, 1.8)
    if teil != "l":
        s += line(f"M{_f(w * .66)} {_f(h * .25)}h{_f(w * .22)}M{_f(w * .62)} {_f(h * .45)}h{_f(w * .26)}M{_f(w * .64)} {_f(h * .65)}h{_f(w * .22)}", .8, "#8A7A5A")
    return place(s, x, y, a)


# ------------------------------------------------------------------ Zeichen
def z_beten():
    return {
        # Vorbild 🙏 (Apple/Google): zwei Handflächen, Finger zur Mitte, Daumen vorn, Ärmel schräg auseinander
        "@1": ("-12 -29 24 36", H.haende_betend()),
        # Figur mit gesenktem Kopf und gefalteten Händen vor der Brust (Halbfigur)
        "@2": ("0 0 30 32", figur(15, 32, 30, ROBE["braun"], gesicht="geschlossen") + place(H.haende_betend(ROBE["braun"]), 15, 31, 0, .62)),
    }


def z_ablehnen():
    return {
        # Vorbild 👎: Faust von der Seite, Daumen kräftig nach unten, Ärmel seitlich
        "@1": ("-14.6 -8.6 21 23", place(H.hand_daumen(), 0, 0, 180)),
        "@2": ("-15 -10 23 26", place(H.hand_daumen(), 0, 0, 160)),
    }


def z_hand():
    return {
        # Vorbild ✋: Handfläche, vier verschieden lange Finger, Daumen abgespreizt, Ärmel
        "@1": ("-12 -25 24 31", H.hand_offen()),
        "@2": ("-13 -26 26 33", H.hand_offen(spreiz=1.4)),
    }


def z_zeigen():
    return {
        # Vorbild 👉: Zeigefinger gestreckt, Faust eingerollt, Daumen oben
        "@1": ("-6 -8.5 27 17", H.hand_zeigend()),
        "@2": ("-6 -9 31 18", H.hand_zeigend() + line("M23 -6.4l3.6 4.1-3.6 4.1", 1.3)),
    }


def z_gruessen():
    arcs = bogen("M9.6-26.8Q13.4-23.4 12.8-18.6", 1.2) + bogen("M12.6-29.4Q17.6-24.8 16.6-17.8", 1.2)
    arcs_l = bogen("M-12.6-25.6Q-15.8-21.6-14.4-17", 1.2)
    h = place(H.hand_offen(spreiz=1.35), 0, 0, 14)
    return {
        # Vorbild 👋: offene Hand leicht geneigt, Finger gespreizt, zwei Bewegungsbögen
        "@1": ("-14 -31 33 37", h + arcs),
        "@2": ("-17 -31 36 37", h + arcs + arcs_l),
    }


def z_preisen():
    sparks = (strahlen(-15.4, -29.6, 0, 0, []) + line("M-17.6-28.4l-1.6-2.2M-13.4-30.2l-.2-2.8M-9.6-28.6l1.2-2.4", 1.2)
              + line("M17.6-28.4l1.6-2.2M13.4-30.2l.2-2.8M9.6-28.6l-1.2-2.4", 1.2))
    orant = (figur(18, 34, 22, ROBE["gruen"], gesicht="froh")
             + place(H.hand_offen(ROBE["gruen"], lang=4, spreiz=1.3), 7.4, 18.6, -22, .62)
             + place(H.hand_offen(ROBE["gruen"], lang=4, spreiz=1.3), 28.6, 18.6, 22, .62, flip=True))
    return {
        # Vorbild 🙌: zwei erhobene Hände, Finger gespreizt, kleine Freudenstriche
        "@1": ("-24 -34 48 41", H.haende_erhoben() + sparks),
        # Orant: Figur mit erhobenen Armen
        "@2": ("0 0 36 34", orant),
    }


def z_kraft():
    rays = line("M27.8-31.4l1.6-2.6M30.6-27.8l2.8-1.2M30.8-23.4l2.8.2", 1.3, INK)
    return {
        # Vorbild 💪: Oberarm waagrecht mit Bizeps, Unterarm senkrecht, Faust
        "@1": ("-4 -32 32 44", H.arm_kraft()),
        "@2": ("-4 -35 38 47", H.arm_kraft() + rays),
    }


def z_wundmale():
    mal = '<circle cx="0" cy="-6.4" r="1.9" fill="#8E2A2A" stroke="#5A1A1A" stroke-width=".6"/>'
    h = H.hand_offen("#ECE6DA") + mal
    return {
        # Vorbild: zwei Handflächen ✋ nach vorn gezeigt, je ein dunkles Nagelmal (Thomas, Joh 20,27)
        "@1": ("-23 -25 46 31", place(h, -10.8, 0, -6, flip=True) + place(h, 10.8, 0, 6)),
        "@2": ("-12 -25 24 31", h),
    }


def z_almosen():
    poor = "#8C7A5E"
    recv = place(H.hand_empfangend(poor), 2, 25)
    give = place(H.hand_gebend(), 33.4, 5.6, 0, 1, flip=True)
    return {
        # Vorbild: gebende Hand von oben (🫳) lässt eine Münze in die offene Hand (🫴) fallen; Fallstriche
        "@1": ("-3 -1 38 32", give + H.fallstriche(13.2, 11.6, 2, 1.4) + H.muenze(13.2, 16.6, 2.6) + recv),
    }


def z_geben():
    recv = place(H.hand_empfangend(ROBE["gruen"]), 35, 24, 0, 1, flip=True)
    give = place(H.hand_gebend(), 0, 7)
    return {
        # Vorbild: eine Hand reicht einen neutralen Gegenstand (Paket), die andere (🫴) nimmt ihn entgegen
        "@1": ("-5 0 41 31", give + paket(14.6, 13.2) + recv),
    }


def z_lohn():
    h = place(H.hand_empfangend(), 0, 20)
    return {
        # Vorbild 🫴 mit Münzstapel auf der Handfläche: der Lohn ist schon ausbezahlt
        "@1": ("-5 3 27 23", h + stapel(13.6, 18.2, 3)),
        "@2": ("-5 1 27 25", h + stapel(13.6, 18.2, 4)),
    }


def z_gnade():
    gift = (paket(-4, -24.4, 8, 6.4).replace("#C99A5E", GOLD).replace("#7A4E24", "#B0443C")
            + line("M-2.2-26.4Q-2.6-28.6 0-24.6Q2.6-28.6 2.2-26.4", 1, "#B0443C"))
    return {
        # Vorbild 🤲 (zwei offene Hände) empfangen ein Geschenk von oben (unverdient geschenkt)
        "@1": ("-17 -30 34 35", line("M-6.4-29l1.2 2M6.4-29l-1.2 2", 1.2, GOLD) + gift + H.haende_schale()),
        # empfangen Licht von oben
        "@2": ("-17 -30 34 35", line("M-5-28l2.4 3.6M5-28l-2.4 3.6M0-29.6v4", 1.4, GOLD) + f'<circle cx="0" cy="-20.6" r="2.6" fill="{GOLD}" stroke="{INK}" stroke-width="1"/>'
               + H.haende_schale()),
    }


def z_glauben():
    gross = place(H.hand_empfangend("#ECE6DA"), 0, 22, 0, 1.45)
    klein = place(H.hand_gebend(), 8.2, 12.2, 14, .66)
    return {
        # Vorbild: kleine Hand liegt vertrauend in einer grossen offenen Hand (🫴), Ärmel hell (Gott)
        "@1": ("-7 4 38 26", gross + klein),
    }


def z_verdorrt():
    return {
        # Vorbild: gesunde offene Hand neben kleiner, fahler Hand mit steif eingekrümmten Fingern (Seitenansicht)
        "@1": ("-12 -25 38 31", H.hand_offen() + place(H.hand_verdorrt(), 16, 0)),
        "@2": ("-9 -19 18 24", H.hand_verdorrt()),
    }


def z_ausliefern():
    cx, cy = 17, 21
    left = place(H.hand_faust(cuff_on=False), cx + 3.4, cy - 3.6, -62, .86)
    right = place(H.hand_faust(cuff_on=False), cx - 3.4, cy - 3.6, 62, .86, flip=True)
    arm_l = cuff(f"M{cx + 3} {cy - 4.6}L{cx + 6.6} {cy - .8}L{cx - 6} {cy + 13}L{cx - 10.4} {cy + 9.6}Z")
    arm_r = cuff(f"M{cx - 3} {cy - 4.6}L{cx - 6.6} {cy - .8}L{cx + 6} {cy + 13}L{cx + 10.4} {cy + 9.6}Z")
    rd = f"M{cx - 6} {cy - 1}Q{cx} {cy - 4} {cx + 6} {cy - 1}M{cx - 6.4} {cy + 2}Q{cx} {cy - 1} {cx + 6.4} {cy + 2}"
    tail = f"M{cx + 1} {cy + 1}Q{cx + 2} {cy + 6} {cx + 5.4} {cy + 9}"
    rope = (f'<path d="{rd}{tail}" fill="none" stroke="{INK}" stroke-width="3.3" stroke-linecap="round"/>'
            f'<path d="{rd}{tail}" fill="none" stroke="#C9A06A" stroke-width="1.8" stroke-linecap="round"/>')
    return {
        # Vorbild: gekreuzte Handgelenke frontal, zwei Fäuste oben, Seil um die Gelenke (Fesselung)
        "@1": ("0 0 34 34", arm_l + arm_r + left + right + rope),
    }


def z_beruehren():
    mantel = (f'<path d="M18 0H38V20Q35 22.6 31.4 21Q28 23.2 24.4 21.2Q21 22.8 18 20.6Z" fill="#B0443C" stroke="{INK}" stroke-width="1.15" stroke-linejoin="round"/>'
              + line("M24.4 1v19M31.4 1v19", .7, "#7A2A24")
              + f'<path d="M24.6 21.6v2.6" stroke="{INK}" stroke-width="1"/><path d="M23.2 24.2h2.8l.7 3.8h-4.2z" fill="{GOLD}" stroke="{INK}" stroke-width=".9" stroke-linejoin="round"/>')
    touch = line("M19.6 25.6l-.6 1.8M22.6 26.6l.2 1.8M16.8 23.4l-1.6.6", .9)
    h = place(H.hand_zeigend(), 0, 30, -30)
    return {
        # Vorbild ☝ an Stoff: Hand mit Zeigefinger berührt von unten den Saum eines Mantels mit Quaste, Kontaktstriche
        "@1": ("-5 -1 43 36", mantel + h + touch),
    }


def z_waschen():
    stream = (f'<path d="M14 7.6Q15.6 12 15.4 17.4" fill="none" stroke="{INK}" stroke-width="3.4" stroke-linecap="round"/>'
              f'<path d="M14 7.6Q15.6 12 15.4 17.4" fill="none" stroke="{WATER}" stroke-width="1.8" stroke-linecap="round"/>')
    hands = place(H.haende_schale(), 15.4, 33, 0, .78)
    drops = tropfen(5.6, 21, .9) + tropfen(25.6, 21.4, .9)
    return {
        # Vorbild: Händewasch-Piktogramm – Krug giesst Wasser über zwei offene Hände (🤲), Tropfen
        "@1": ("0 -1 32 37", krug(14, 7.6, 18) + stream + hands + drops),
        "@2": ("0 -1 32 43", krug(14, 7.6, 18) + stream + hands + drops + schale(15.4, 35.6, 26)),
    }


def z_vergeben():
    give = place(H.hand_gebend(), 0, 4)
    return {
        # Vorbild: Schuldschein (mit Münze) quer zerrissen, die Hand lässt die Hälften fallen
        "@1": ("-5 -1 36 35", give + schein(10.6, 13, 14, 17, -14, "l") + schein(15, 14.4, 14, 17, 16, "r")),
        "@2": ("0 0 30 30", schein(3, 6, 12, 16, -12, "l") + schein(8.6, 6.4, 12, 16, 14, "r")),
    }


def z_gute_werke():
    a = figur(7, 34, 30, ROBE["gruen"], gesicht="froh")
    b = figur(32, 34, 25, ROBE["grau"], HAIR["braun"])
    give = place(H.hand_empfangend(ROBE["gruen"]), 13.2, 22.6, 0, .7)
    take = place(H.hand_gebend(ROBE["grau"]), 27.2, 17.2, -8, .58, flip=True)
    return {
        # Vorbild: eine Person reicht der anderen Brot (Hand wie 🫴), die andere greift danach
        "@1": ("0 0 38 34", a + b + give + brot(20.6, 19.6, 7.4, 4) + take),
        # nur Hände: offene Hand reicht Brot, eine zweite Hand von rechts greift zu; Herz darüber
        "@2": ("-5 -2 43 28", place(H.hand_empfangend(), 0, 21) + brot(14, 16.4, 8, 4.4) + place(H.hand_gebend(ROBE["grau"]), 36, 8, -6, .9, flip=True)
               + herz(9, 4, .9)),
    }


def z_heilen():
    a = figur(7, 34, 32, ROBE["blau"])
    b = sitzend(25.6, 34, 18, ROBE["grau"], gesicht="geschlossen", blick=-1)
    hand = place(H.hand_gebend(ROBE["blau"]), 11.6, 15.4, 12, .66)
    rays = line("M17.4 13.2l-.6-2.4M21.6 11.8l.2-2.4M25.6 13l1.2-2", 1.1, GOLD)
    jump = figur(13, 32, 28, ROBE["gelb"], gesicht="froh")
    krueck = (f'<g transform="rotate(32 27 22)"><path d="M27 10v22M24.6 10.6h4.8" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>'
              f'<path d="M27 10v22M24.6 10.6h4.8" fill="none" stroke="{WOOD}" stroke-width="1.5" stroke-linecap="round"/></g>')
    return {
        # Vorbild: Hand legt sich auf den Kopf einer sitzenden Figur (Heilung durch Handauflegen)
        "@1": ("0 0 36 34", a + b + hand + rays),
        # Vorbild Leitsystem: Figur steht auf und lässt die Krücke fallen
        "@2": ("0 0 36 33", jump + krueck + line("M30.4 30.6l2.4 1.2M28 32.4h3", .9)),
    }


def z_segnen():
    head = sitzend(17, 36, 17, ROBE["gelb"], HAIR["braun"], gesicht="geschlossen")
    hl = place(H.hand_gebend(), 1, 8.4, 24, .8)
    hr = place(H.hand_gebend(), 33, 8.4, 24, .8, flip=True)
    rays = line("M12.2 17.2l-1 1.6M17 17.4v2M21.8 17.2l1 1.6", 1.2, GOLD)
    a = figur(7, 34, 32, ROBE["braun"])
    b = sitzend(26, 34, 15, ROBE["gelb"], gesicht="geschlossen", blick=-1)
    hand = place(H.hand_gebend(ROBE["braun"]), 11.2, 13.2, 10, .64)
    return {
        # Vorbild: zwei Hände, Handflächen nach unten, über dem gesenkten Kopf; Lichtstriche gehen von den Händen aus
        "@1": ("0 0 34 36", head + hl + hr + rays),
        "@2": ("0 0 36 34", a + b + hand + line("M18.6 19.4l-.4 1.8M22 18.6v2", 1.1, GOLD)),
    }


def z_ehe():
    m = figur(9, 34, 25, ROBE["blau"])
    w = figur(25, 34, 25, ROBE["lila"], gesicht="ruhig", schleier="#C8A2D0")
    rings = ring(14.8, 5.4) + ring(19.2, 5.4)
    return {
        # Vorbild: Mann und Frau nebeneinander, zwei ineinander verschlungene Ringe über ihnen
        "@1": ("0 0 34 34", m + w + rings),
    }


def z_erbarmen():
    a = figur(8, 34, 31, ROBE["gruen"])
    b = sitzend(24, 34, 19, ROBE["grau"], gesicht="traurig", blick=1)
    hand = place(H.hand_auf_schulter(ROBE["gruen"]), 13, 20.6, 4, .6)
    tear = tropfen(26.2, 25.4, .55)
    return {
        # Vorbild: stehende Figur legt die Hand auf die Schulter einer traurig kauernden Figur
        "@1": ("0 0 36 34", a + b + hand + tear),
        "@2": ("0 -2 36 36", a + b + hand + tear + herz(16, 3.4, .75)),
    }


def z_ohrfeige():
    head = kopf(24, 17, 9, HAIR["schwarz"], "schmerz", neig=14)
    cheek = f'<ellipse cx="17.6" cy="20.8" rx="2" ry="1.4" fill="#E06A6A" opacity=".9"/>'
    hand = place(H.hand_offen(), 7, 30, 62, .64)
    arcs = bogen("M2.8 12.4Q.2 16.4 1.4 21.4", 1.1) + bogen("M5.6 10.4Q3 14.6 4 19.6", 1.1)
    return {
        # Vorbild: flache offene Hand (✋ seitlich) mit Bewegungsbögen trifft die Wange, Kopf zur Seite
        "@1": ("0 4 34 30", head + cheek + arcs + hand),
    }


def z_schwur():
    body = rumpf(14, 18, 34, 13, 18, ROBE["braun"]) + kopf(14, 11.6, 5.6, HAIR["dunkel"])
    raised = place(H.hand_offen(ROBE["braun"], lang=5), 26.6, 18.4, 8, .64)
    scroll = rolle(1, 26.4, 22, 6.4)
    rest = place(H.hand_gebend(ROBE["braun"]), 2.4, 25.4, -4, .56)
    return {
        # Vorbild: Halbfigur hebt die rechte Hand flach (Schwurhand), die andere liegt auf einer Schriftrolle
        "@1": ("0 1 36 33", body + scroll + rest + raised),
        # ohne Figur: erhobene Schwurhand über einer Schriftrolle
        "@2": ("0 0 30 34", rolle(2, 27, 26, 6.4) + place(H.hand_offen(), 15, 24.6, 0, .9)),
    }


def z_treue():
    a = figur(10, 34, 27, ROBE["lila"], schleier="#B9A2C6", gesicht="froh")
    b = figur(24, 34, 27, ROBE["rost"], schleier="#E2B85A", gesicht="froh")
    hand = place(H.hand_auf_schulter(ROBE["lila"]), 14.6, 18.4, 0, .72)
    return {
        # Vorbild 🫂/👭: zwei Figuren Seite an Seite, die eine legt den Arm um die Schulter der anderen
        "@1": ("0 0 34 34", a + b + hand),
    }


ZEICHEN = {
    "FIG-ZEICHEN-BETEN": (z_beten, "beten (sich mit gefalteten Händen an Gott wenden)", "zwei betende Hände (gefaltet), Daumen vorn"),
    "FIG-ZEICHEN-GUTE-WERKE": (z_gute_werke, "gute Werke (Gutes tun, anderen helfen)", "eine Person reicht einer anderen ein Brot"),
    "FIG-ZEICHEN-GNADE": (z_gnade, "Gnade (Gottes unverdientes Geschenk)", "zwei offene Hände empfangen Licht von oben"),
    "FIG-ZEICHEN-HEILEN": (z_heilen, "heilen (ein Kranker wird gesund)", "Hand auf dem Kopf einer sitzenden Figur bzw. Figur lässt Krücke fallen"),
    "FIG-ZEICHEN-ABLEHNEN": (z_ablehnen, "verwerfen / ablehnen", "Faust mit Daumen nach unten"),
    "FIG-ZEICHEN-GEBEN": (z_geben, "geben (jemandem etwas reichen)", "eine Hand reicht ein Paket in eine offene Hand"),
    "FIG-ZEICHEN-ALMOSEN": (z_almosen, "Almosen geben (einem Armen Geld geben)", "Hand lässt eine Münze in eine offene Hand fallen"),
    "FIG-ZEICHEN-SEGNEN": (z_segnen, "segnen (jemandem Gutes von Gott zusprechen)", "Hände über dem gesenkten Kopf einer Person, Lichtstriche"),
    "FIG-ZEICHEN-EHE": (z_ehe, "Ehe / Ehepaar", "Mann und Frau, zwei verschlungene Ringe darüber"),
    "FIG-ZEICHEN-ERBARMEN": (z_erbarmen, "Mitleid / Erbarmen", "Figur legt die Hand auf die Schulter einer traurigen, kauernden Figur"),
    "FIG-ZEICHEN-WASCHEN": (z_waschen, "Hände waschen (rituell vor dem Essen)", "Krug giesst Wasser über zwei Hände"),
    "FIG-ZEICHEN-OHRFEIGE": (z_ohrfeige, "auf die Wange schlagen (Ohrfeige)", "offene Hand schlägt auf die Wange, Kopf zur Seite"),
    "FIG-ZEICHEN-SCHWUR": (z_schwur, "schwören / Schwur", "Figur hebt die Hand, andere Hand auf einer Schriftrolle"),
    "FIG-ZEICHEN-PREISEN": (z_preisen, "preisen / loben (Gott)", "zwei erhobene Hände mit Freudenstrichen"),
    "FIG-ZEICHEN-KRAFT": (z_kraft, "Kraft / stark machen", "angespannter Arm mit Bizeps und Faust"),
    "FIG-ZEICHEN-HAND": (z_hand, "Hand (rechte Hand, Körperteil)", "offene Hand"),
    "FIG-ZEICHEN-LOHN-ERHALTEN": (z_lohn, "Lohn schon erhalten (ausbezahlt)", "offene Hand mit Münzstapel"),
    "FIG-ZEICHEN-GRUESSEN": (z_gruessen, "grüssen, willkommen heissen", "winkende Hand mit Bewegungsbögen"),
    "FIG-ZEICHEN-TREUE": (z_treue, "Treue / zusammenhalten", "zwei Frauen Seite an Seite, Arm um die Schulter"),
    "FIG-ZEICHEN-AUSLIEFERN": (z_ausliefern, "ausliefern / gefangen nehmen (binden)", "gekreuzte Handgelenke mit Fäusten, Seil"),
    "FIG-ZEICHEN-BERUEHREN": (z_beruehren, "berühren (den Mantel Jesu berühren)", "Finger berührt den Saum eines Mantels mit Quaste"),
    "FIG-ZEICHEN-ZEIGEN": (z_zeigen, "zeigen / weisen", "zeigende Hand"),
    "FIG-ZEICHEN-WUNDMALE": (z_wundmale, "Wundmale an den Händen (des Auferstandenen)", "zwei Handflächen mit Nagelmalen"),
    "FIG-ZEICHEN-VERGEBEN": (z_vergeben, "vergeben (Schuld wird erlassen)", "zerrissener Schuldschein fällt aus der Hand"),
    "FIG-ZEICHEN-HAND-VERDORRT": (z_verdorrt, "verdorrte (gelähmte) Hand", "gesunde Hand neben fahler, steif gekrümmter Hand"),
    "FIG-ZEICHEN-GLAUBEN": (z_glauben, "glauben, vertrauen", "kleine Hand liegt in einer grossen offenen Hand"),
}
# Hände waschen: zwei Lexikon-Einträge mit derselben Bedeutung (Mk 7 / Mt 15) – dieselbe Zeichnung
GLEICH = {"FIG-ZEICHEN-HAENDE-WASCHEN": "FIG-ZEICHEN-WASCHEN"}

# Fassungen, die die Gestaltungskritik bestanden haben (Mehrheit «ok», alle Mittel ≥ 4); nur diese werden geschrieben
GEWAEHLT = {}


# AUTO_VB: Bildausschnitt aus dem Umriss (Playwright getBBox mit Strichbreite, Rand .6), erzeugt mit dem Arbeitswerkzeug bbox.py
AUTO_VB = {
 "FIG-ZEICHEN-BETEN@1": "-11.5 -29.4 23.0 36.5",
 "FIG-ZEICHEN-BETEN@2": "6.2 0.8 17.6 34.8",
 "FIG-ZEICHEN-GUTE-WERKE@1": "-1.8 2.8 41.4 32.3",
 "FIG-ZEICHEN-GUTE-WERKE@2": "-6.1 0.5 48.0 27.6",
 "FIG-ZEICHEN-GNADE@1": "-18.6 -30.2 37.1 36.4",
 "FIG-ZEICHEN-GNADE@2": "-18.6 -30.9 37.1 37.1",
 "FIG-ZEICHEN-HEILEN@1": "-2.3 0.8 34.6 34.4",
 "FIG-ZEICHEN-HEILEN@2": "4.7 2.8 32.8 31.0",
 "FIG-ZEICHEN-ABLEHNEN@1": "-15.6 -8.9 21.7 24.6",
 "FIG-ZEICHEN-ABLEHNEN@2": "-15.4 -9.8 23.3 26.1",
 "FIG-ZEICHEN-GEBEN@1": "-6.1 1.3 47.2 29.8",
 "FIG-ZEICHEN-ALMOSEN@1": "-4.1 -0.1 43.6 32.2",
 "FIG-ZEICHEN-SEGNEN@1": "-4.9 -1.3 44.0 38.5",
 "FIG-ZEICHEN-SEGNEN@2": "-2.3 0.8 34.1 34.4",
 "FIG-ZEICHEN-EHE@1": "1.4 0.1 31.1 35.1",
 "FIG-ZEICHEN-ERBARMEN@1": "-1.1 1.8 37.5 33.4",
 "FIG-ZEICHEN-ERBARMEN@2": "-1.1 0.3 37.5 34.9",
 "FIG-ZEICHEN-WASCHEN@1": "-4.8 2.4 34.8 35.5",
 "FIG-ZEICHEN-WASCHEN@2": "-4.8 2.4 34.8 39.6",
 "FIG-ZEICHEN-OHRFEIGE@1": "-0.1 5.2 38.4 31.3",
 "FIG-ZEICHEN-SCHWUR@1": "-1.4 1.6 35.5 33.5",
 "FIG-ZEICHEN-SCHWUR@2": "0.9 1.3 28.3 33.2",
 "FIG-ZEICHEN-PREISEN@1": "-26.6 -34.2 53.3 45.2",
 "FIG-ZEICHEN-PREISEN@2": "-3.1 3.4 42.1 31.8",
 "FIG-ZEICHEN-KRAFT@1": "-4.5 -31.8 32.9 43.9",
 "FIG-ZEICHEN-KRAFT@2": "-4.5 -35.3 39.4 47.3",
 "FIG-ZEICHEN-HAND@1": "-12.8 -25.8 21.5 32.1",
 "FIG-ZEICHEN-HAND@2": "-13.0 -25.8 22.2 32.1",
 "FIG-ZEICHEN-LOHN-ERHALTEN@1": "-6.1 11.4 29.7 15.7",
 "FIG-ZEICHEN-LOHN-ERHALTEN@2": "-6.1 9.8 29.7 17.4",
 "FIG-ZEICHEN-GRUESSEN@1": "-11.9 -30.6 29.9 38.4",
 "FIG-ZEICHEN-GRUESSEN@2": "-16.0 -30.6 34.0 38.4",
 "FIG-ZEICHEN-TREUE@1": "1.9 4.2 30.1 30.9",
 "FIG-ZEICHEN-AUSLIEFERN@1": "3.3 4.4 27.4 31.1",
 "FIG-ZEICHEN-BERUEHREN@1": "-8.2 -1.2 47.4 40.8",
 "FIG-ZEICHEN-ZEIGEN@1": "-5.9 -8.8 28.4 17.3",
 "FIG-ZEICHEN-ZEIGEN@2": "-5.9 -8.8 33.8 17.3",
 "FIG-ZEICHEN-WUNDMALE@1": "-21.5 -25.9 42.9 32.9",
 "FIG-ZEICHEN-WUNDMALE@2": "-12.8 -25.8 21.5 32.1",
 "FIG-ZEICHEN-VERGEBEN@1": "-6.1 -1.7 35.7 37.5",
 "FIG-ZEICHEN-VERGEBEN@2": "1.8 3.4 19.5 22.6",
 "FIG-ZEICHEN-HAND-VERDORRT@1": "-12.8 -25.8 37.6 32.1",
 "FIG-ZEICHEN-HAND-VERDORRT@2": "-8.2 -19.0 17.0 24.9",
 "FIG-ZEICHEN-GLAUBEN@1": "-8.6 7.6 42.6 24.4"
}
# AUTO_VB_ENDE


def alle(roh=False):
    out = {}
    for fid, (fn, bed, gez) in ZEICHEN.items():
        for v, (vb, svg) in fn().items():
            k = f"{fid}{v}"
            out[k] = {"vb": vb if roh else AUTO_VB.get(k, vb), "svg": svg, "bedeutung": bed, "gezeichnet": gez}
    return out


def main():
    a = sys.argv[1:]
    if "--entwuerfe" in a:
        p = pathlib.Path(a[a.index("--entwuerfe") + 1])
        only = a[a.index("--nur") + 1].split(",") if "--nur" in a else None
        e = {k: v for k, v in alle("--roh" in a).items() if not only or any(k.startswith(o if o.startswith("FIG-") else "FIG-ZEICHEN-" + o) for o in only)}
        p.write_text(json.dumps(e, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"PASS: {len(e)} Entwürfe in {p}")
    if "--schreiben" in a:
        e = alle()
        res = {}
        for fid, v in GEWAEHLT.items():
            x = e[f"{fid}{v}"]
            res[fid] = {"vb": x["vb"], "svg": x["svg"]}
        for dup, src in GLEICH.items():
            if src in res:
                res[dup] = dict(res[src])
        for fid, x in res.items():
            assert "id=" not in x["svg"] and "filter" not in x["svg"] and "Gradient" not in x["svg"], fid
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"PASS: {len(res)} Zeichen nach {OUT}")


if __name__ == "__main__":
    main()
