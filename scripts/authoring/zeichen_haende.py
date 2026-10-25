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


def figur_teile(cx, boden, h=28, robe=ROBE["braun"], haar=HAIR["dunkel"], gesicht="ruhig", schleier=None, neig=0, r=None):
    """Wie figur(), aber (Gewand, Kopf, Schultern) getrennt, damit Arme und Hände dazwischen gezeichnet werden können.
    Schultern: ((x links, y), (x rechts, y))."""
    r = r or h * .17
    cy = boden - h + r
    top = cy + r + .2
    sh = ((cx - r * 1.15 + 1.2, top + 1.6), (cx + r * 1.15 - 1.2, top + 1.6))
    return rumpf(cx, top, boden, r * 2.3, r * 3.0, robe), kopf(cx, cy, r, haar, gesicht, schleier, neig), sh


def arm(pts, robe, w=4.2):
    """Arm als Ärmel vom Schulterpunkt zum Handgelenk (Punkte als Linie, Kontur nur aussen). Nur vom Körper weg führen,
    nie quer über den eigenen Körper."""
    d = "M" + "L".join(f"{_f(x)} {_f(y)}" for x, y in pts)
    return (f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{_f(w + 2.2)}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{robe}" stroke-width="{_f(w)}" stroke-linecap="round" stroke-linejoin="round"/>')


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
def kruecke(x, y, a=0):
    """Achselkrücke: Polster oben, zwei Holme laufen zusammen, Griff, Fuss; (x,y) oben, a Neigung."""
    d = "M-3 0H3M-2.2 0L0 13V20M2.2 0L0 13M-1.4 7H1.4"
    k = (f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
         f'<path d="{d}" fill="none" stroke="{WOOD}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>')
    return place(k, x, y, a)


def z_beten():
    return {
        # Vorbild 🙏 (Apple/Google): zwei Handflächen, Finger zur Mitte, Daumen vorn, Ärmel schräg auseinander
        "@1": ("-12 -29 24 36", H.haende_betend()),
        # Figur mit gesenktem Blick und gefalteten Händen vor der Brust (Halbfigur)
        "@2": ("0 0 30 32", figur(15, 32, 30, ROBE["braun"], gesicht="geschlossen") + place(H.haende_betend(ROBE["braun"]), 15, 31, 0, .5)),
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
    joy = line("M-22-22l-2.4-1.2M-20.4-27.6l-2-2M-15.6-30.6l-.6-2.6M22-22l2.4-1.2M20.4-27.6l2-2M15.6-30.6l.6-2.6", 1.3, GOLD)
    body, head, sh = figur_teile(18, 34, 24, ROBE["gruen"], gesicht="froh")
    wl, wr = (9.6, 13), (26.4, 13)
    orant = (arm([sh[0], wl], ROBE["gruen"], 3.2) + arm([sh[1], wr], ROBE["gruen"], 3.2) + body + head
             + place(H.hand_offen(cuff_on=False, spreiz=1.3), wl[0], wl[1], -18, .38)
             + place(H.hand_offen(cuff_on=False, spreiz=1.3), wr[0], wr[1], 18, .38, flip=True)
             + line("M18 2.2v-2.4M13.4 3.6l-1.4-2M22.6 3.6l1.4-2", 1.2, GOLD))
    return {
        # Vorbild 🙌: zwei erhobene Hände, Finger gespreizt, Freudenstriche
        "@1": ("-26 -34 52 41", H.haende_erhoben() + joy),
        # Orant: Figur hebt froh beide Arme nach oben
        "@2": ("0 -1 36 35", orant),
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
    h = H.hand_offen(ROBE["weiss"], lang=3) + mal
    h1 = H.hand_offen() + mal
    return {
        # Vorbild: zwei Handflächen ✋ nach vorn gezeigt, je ein dunkles Nagelmal (Thomas, Joh 20,27)
        "@1": ("-23 -25 46 31", place(h1, -10.8, 0, -6, flip=True) + place(h1, 10.8, 0, 6)),
        "@2": ("-12 -25 24 31", h1),
    }


def z_almosen():
    poor = "#8C7A5E"
    b = sitzend(7.4, 34, 18, ROBE["grau"], gesicht="traurig", blick=1)
    w = (14.4, 25.6)
    gb, gh, gs = figur_teile(31, 34, 30, ROBE["blau"])
    gw = (25.4, 14.6)
    return {
        # Vorbild: kauernder Armer streckt die offene Hand (🫴) aus, ein Stehender lässt eine Münze hineinfallen
        "@1": ("0 0 38 34", arm([(11.4, 27.4), w], ROBE["grau"], 3.2) + b + place(H.hand_empfangend(poor, cuff_on=False), w[0], w[1], -6, .5)
               + arm([gs[0], gw], ROBE["blau"], 3.4) + gb + gh + place(H.hand_gebend(cuff_on=False), gw[0], gw[1], 0, .5, flip=True)
               + H.fallstriche(18.6, 17.4, 2, 1.1) + H.muenze(18.6, 21, 2.4)),
    }


def z_geben():
    recv = place(H.hand_empfangend(ROBE["gruen"]), 35, 25, 0, 1, flip=True)
    give = place(H.hand_gebend(), 0, 8.4)
    return {
        # Vorbild: eine flache Hand (🫳) legt ein Paket in eine offene Hand (🫴)
        "@1": ("-5 0 41 31", recv + paket(13.6, 12.8, 8.6, 7) + give),
    }


def z_lohn():
    h = place(H.hand_empfangend(), 0, 20)
    return {
        # Vorbild 🫴 mit Münzstapel auf der Handfläche: der Lohn ist schon ausbezahlt
        "@1": ("-5 3 27 23", h + stapel(13.6, 18.2, 3)),
        "@2": ("-5 1 27 25", h + stapel(13.6, 18.2, 4)),
    }


def z_gnade():
    beam = f'<path d="M-3-34L3-34L11-15H-11Z" fill="{GOLD}" opacity=".45"/>'
    star = (f'<path d="M0-30.4L1.2-27.2L4.4-26L1.2-24.8L0-21.6L-1.2-24.8L-4.4-26L-1.2-27.2Z" fill="{GOLD}" stroke="{INK}" stroke-width=".9" stroke-linejoin="round"/>')
    return {
        # Vorbild 🤲 (zwei offene Hände) empfangen Licht von oben (unverdient geschenkt)
        "@1": ("-17 -35 34 40", beam + H.haende_schale() + star),
        "@2": ("-17 -30 34 35", line("M-5-28l2.4 3.6M5-28l-2.4 3.6M0-29.6v4", 1.4, GOLD) + f'<circle cx="0" cy="-20.6" r="2.6" fill="{GOLD}" stroke="{INK}" stroke-width="1"/>'
               + H.haende_schale()),
    }


def z_glauben():
    gross = place(H.hand_empfangend("#ECE6DA"), 0, 26, 0, 1.6)
    sitz = sitzend(17.6, 24.4, 15, ROBE["blau"], gesicht="froh", blick=1)
    body, head, sh = figur_teile(10, 34, 20, ROBE["blau"], gesicht="froh")
    w = (16.4, 17)
    big = place(H.hand_gebend("#ECE6DA"), 36, 6, 40, 1.05, flip=True)
    return {
        # Vorbild «in Gottes Hand»: kleine Figur sitzt geborgen auf einer grossen offenen Hand (🫴, heller Ärmel)
        "@1": ("-8 4 44 32", gross + sitz),
    }


def z_verdorrt():
    return {
        # Vorbild: gesunde offene Hand neben kleiner, fahler Hand, deren dünne Finger steif zu Haken gekrümmt sind
        "@1": ("-12 -25 38 31", H.hand_offen() + place(H.hand_verdorrt(), 17.6, 0)),
    }


def z_ausliefern():
    cx, cy = 17, 21
    left = place(H.hand_faust(cuff_on=False), cx + 3.4, cy - 3.6, -62, .86)
    right = place(H.hand_faust(cuff_on=False), cx - 3.4, cy - 3.6, 62, .86, flip=True)
    arm_l = cuff(f"M{cx + 3} {cy - 4.6}L{cx + 6.6} {cy - .8}L{cx - 6} {cy + 13}L{cx - 10.4} {cy + 9.6}Z")
    arm_r = cuff(f"M{cx - 3} {cy - 4.6}L{cx - 6.6} {cy - .8}L{cx + 6} {cy + 13}L{cx + 10.4} {cy + 9.6}Z")
    rd = f"M{cx - 4.4} {cy - 1.4}Q{cx} {cy - 3.4} {cx + 4.4} {cy - 1.4}M{cx - 4.4} {cy + 1.4}Q{cx} {cy - .6} {cx + 4.4} {cy + 1.4}"
    rope = (f'<path d="{rd}" fill="none" stroke="{INK}" stroke-width="3.3" stroke-linecap="round"/>'
            f'<path d="{rd}" fill="none" stroke="#C9A06A" stroke-width="1.8" stroke-linecap="round"/>')
    return {
        # Vorbild: gekreuzte Handgelenke frontal, zwei Fäuste oben, Seil um die Gelenke (Fesselung)
        "@1": ("0 0 34 34", arm_l + arm_r + left + right + rope),
    }


def z_beruehren():
    body, head, sh = figur_teile(27, 30, 32, "#B0443C", HAIR["dunkel"])
    hem = f'<path d="M18.2 27.8Q27 29 35.8 27.8L36.2 30.4Q27 31.8 17.8 30.4Z" fill="{SLEEVE}" stroke="{INK}" stroke-width="1" stroke-linejoin="round"/>'
    feet = f'<path d="M21.4 30.6h4.6v2h-5.2zM28.4 30.6h4.6l.6 2h-5.2z" fill="#7A5434" stroke="{INK}" stroke-width=".8" stroke-linejoin="round"/>'
    touch = line("M15.6 25l-1.4-1.2M18 24l-.2-1.8M13.4 27.6l-1.8-.2", 1)
    return {
        # Vorbild ☝ an Stoff: Zeigefinger berührt den Saum (blaue Borte) des Gewands einer stehenden Person, Kontaktstriche
        "@1": ("-3 -2 40 36", feet + body + hem + head + place(H.hand_zeigend(), 1.2, 34.2, -20, .82) + touch),
    }


def z_waschen():
    stream = (f'<path d="M14 7.6Q15.8 13 15.8 22" fill="none" stroke="{INK}" stroke-width="3.4" stroke-linecap="round"/>'
              f'<path d="M14 7.6Q15.8 13 15.8 22" fill="none" stroke="{WATER}" stroke-width="1.8" stroke-linecap="round"/>')
    hands = place(H.hand_empfangend(), 0, 29, -12, .78) + place(H.hand_empfangend(), 31.6, 29, 12, .78, flip=True)
    drops = tropfen(6.4, 33.4, .8) + tropfen(25.2, 33.4, .8) + tropfen(11.6, 19.6, .8) + tropfen(20, 19.6, .8)
    return {
        # Vorbild Händewasch-Piktogramm: Krug giesst Wasser über zwei offene Hände (🫴 + 🫴), Wasser tropft ab
        "@1": ("0 -1 32 37", krug(14, 7.6, 18) + stream + hands + drops),
    }


def z_vergeben():
    l = schein(6.4, 6, 16, 20, -10, "l")
    r = schein(8.6, 7.4, 16, 20, 12, "r")
    fl = place(H.hand_faust(), 2.4, 9.2, -10, .78)
    fr = place(H.hand_faust(), 31.6, 9.6, 12, .78, flip=True)
    pull = line("M-2.6 16.4l-2.6.6M-2.4 19.4l-2.4-.4M36.8 16.8l2.6.6M36.4 19.8l2.4-.4", .9)
    return {
        # Vorbild: zwei Hände zerreissen einen Schuldschein (mit Münze) – die Schuld gilt nicht mehr
        "@1": ("-6 0 46 30", l + r + fl + fr + pull),
        "@2": ("0 0 30 30", schein(3, 6, 12, 16, -12, "l") + schein(8.6, 6.4, 12, 16, 14, "r")),
    }


def z_gute_werke():
    body, head, sh = figur_teile(7, 34, 30, ROBE["gruen"], gesicht="froh")
    w = (15.6, 21.6)
    b = figur(32.4, 34, 24, ROBE["grau"], HAIR["braun"])
    return {
        # Vorbild: eine Person reicht der anderen ein Brot auf der offenen Hand (🫴)
        "@1": ("0 0 38 34", arm([(11, 22.6), w], ROBE["gruen"], 3.6) + body + head + b
               + place(H.hand_empfangend(cuff_on=False), w[0], w[1], -4, .62) + brot(22, 19.2, 9, 3.8)),
        # nur Hände: offene Hand reicht ein Brot, eine flache Hand von rechts greift zu; Herz darüber
        "@2": ("-5 -2 43 28", place(H.hand_empfangend(), 0, 21) + brot(14.6, 16.6, 10.4, 4) + place(H.hand_gebend(ROBE["grau"]), 37, 9, -6, .9, flip=True)
               + herz(9, 4, .9)),
    }


def z_heilen():
    body, head, sh = figur_teile(12, 34, 28, ROBE["gelb"], gesicht="froh")
    wl, wr = (5.6, 12), (18.4, 12)
    arms = arm([sh[0], wl], ROBE["gelb"], 3.2) + arm([sh[1], wr], ROBE["gelb"], 3.2)
    hands = (place(H.hand_offen(cuff_on=False, spreiz=1.2), wl[0], wl[1], -22, .3)
             + place(H.hand_offen(cuff_on=False, spreiz=1.2), wr[0], wr[1], 22, .3, flip=True))
    fall = line("M36.4 14.4l2-.8M36.8 18l2.2.2", 1)
    return {
        # Vorbild Leitsystem/Comic: Geheilter steht auf, hebt froh die Arme, die Krücke fällt weg
        "@1": ("0 0 41 35", arms + body + head + hands + kruecke(31, 12, 26) + fall),
    }


def z_segnen():
    body, head, sh = figur_teile(9, 34, 31, ROBE["braun"])
    w = (16.8, 14.6)
    b = sitzend(25, 34, 15, ROBE["gelb"], HAIR["braun"], gesicht="geschlossen", blick=-1)
    rays = line("M20.4 18.4l-.8 1.4M23.4 18.8v1.6M26.4 18.4l.8 1.4", 1.2, GOLD)
    return {
        # Vorbild: Hand mit der Handfläche nach unten über dem gesenkten Kopf, Lichtstriche gehen von der Hand aus
        "@1": ("0 0 34 34", arm([sh[1], w], ROBE["braun"], 3.6) + body + head + b + place(H.hand_gebend(cuff_on=False), w[0], w[1], 4, .58) + rays),
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
    body, head, sh = figur_teile(7, 34, 31, ROBE["gruen"])
    w = (17.4, 19.8)
    b = sitzend(26.4, 34, 20, ROBE["grau"], gesicht="traurig", blick=1)
    hand = place(H.hand_auf_schulter(cuff_on=False), w[0], w[1], 12, .62)
    tear = tropfen(28.6, 22.6, .6)
    return {
        # Vorbild: stehende Figur streckt den Arm aus und legt die Hand auf die Schulter einer traurig kauernden Figur (Träne)
        "@1": ("0 0 38 34", arm([sh[1], (15, 16.6), w], ROBE["gruen"], 3.6) + body + head + b + hand + tear),
    }


def z_ohrfeige():
    head = kopf(25, 17, 8.4, HAIR["schwarz"], "schmerz", neig=16)
    cheek = '<ellipse cx="18.8" cy="19.6" rx="2" ry="1.4" fill="#E06A6A"/>'
    hand = place(H.hand_offen(), 4.6, 24.6, 70, .58)
    swoosh = bogen("M1.6 13.6Q2.2 19 6.4 21.8", 1.1) + bogen("M5 12Q5.8 16.4 9.4 18.8", 1.1)
    hit = line("M17.2 12.6l.6-2M14.4 12.6l-.8-1.8M20.6 12.4l1.2-1.6", 1)
    return {
        # Vorbild: flache offene Hand (✋ seitlich) trifft die Wange, kurze Schwungbögen, Treffstriche, Kopf weggedreht
        "@1": ("-1 6 36 28", swoosh + head + cheek + hand + hit),
    }


def z_schwur():
    body = rumpf(14, 18, 34, 13, 18, ROBE["braun"]) + kopf(14, 11.6, 5.6, HAIR["dunkel"])
    rs = (19.2, 20.4)
    raised = arm([rs, (24.8, 20.6), (25.4, 15)], ROBE["braun"], 3.4) + place(H.hand_offen(cuff_on=False, geschlossen=True), 25.4, 15.2, 0, .5)
    return {
        # Vorbild: Halbfigur hebt die rechte Hand flach mit geschlossenen Fingern (Schwurhand), vor sich eine grosse Schriftrolle
        "@1": ("0 1 34 33", raised + body + rolle(2, 26, 24, 7.4)),
        "@2": ("0 0 30 34", place(H.hand_offen(geschlossen=True), 15, 29.4, 0, .9) + rolle(1, 26.4, 28, 7)),
    }


def z_treue():
    ba, ha, sa = figur_teile(11, 34, 27, ROBE["lila"], schleier="#B9A2C6", gesicht="froh")
    bb, hb, sb = figur_teile(23.4, 34, 27, ROBE["rost"], schleier="#E2B85A", gesicht="froh")
    over = arm([sa[1], (22, 17.4), (27.6, 17.8)], ROBE["lila"], 3.2)
    hand = place(H.hand_auf_schulter(cuff_on=False), 27.4, 17.8, 4, .5)
    j = (17.2, 27.4)
    clasp = place(H.hand_faust(cuff_on=False), j[0] - 2.2, j[1], 0, .42)
    return {
        # Vorbild 🫂: zwei Figuren Seite an Seite, die eine legt den Arm um die Schultern der anderen
        "@1": ("0 0 34 34", ba + ha + bb + over + hand + hb),
        # Vorbild 👭: zwei Figuren halten sich an der Hand
        "@2": ("0 0 34 34", arm([sa[1], (15.4, 24), j], ROBE["lila"], 3.2) + arm([sb[0], (19, 24), j], ROBE["rost"], 3.2) + ba + ha + bb + hb + clasp),
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
 "FIG-ZEICHEN-BETEN@2": "6.2 0.8 17.6 34.0",
 "FIG-ZEICHEN-GUTE-WERKE@1": "-1.8 2.8 41.5 32.3",
 "FIG-ZEICHEN-GUTE-WERKE@2": "-6.1 0.5 49.0 27.6",
 "FIG-ZEICHEN-GNADE@1": "-18.6 -34.6 37.1 40.8",
 "FIG-ZEICHEN-GNADE@2": "-18.6 -30.9 37.1 37.1",
 "FIG-ZEICHEN-HEILEN@1": "0.3 4.3 39.8 30.9",
 "FIG-ZEICHEN-ABLEHNEN@1": "-15.6 -8.9 21.7 22.7",
 "FIG-ZEICHEN-ABLEHNEN@2": "-15.4 -9.8 23.3 24.4",
 "FIG-ZEICHEN-GEBEN@1": "-6.1 2.7 47.2 29.4",
 "FIG-ZEICHEN-ALMOSEN@1": "0.7 2.8 39.1 32.4",
 "FIG-ZEICHEN-SEGNEN@1": "-0.1 1.8 30.9 33.4",
 "FIG-ZEICHEN-EHE@1": "1.4 0.1 31.1 35.1",
 "FIG-ZEICHEN-ERBARMEN@1": "-2.1 1.8 41.5 33.4",
 "FIG-ZEICHEN-WASCHEN@1": "-5.2 2.4 42.0 32.8",
 "FIG-ZEICHEN-OHRFEIGE@1": "-0.5 5.8 39.4 24.6",
 "FIG-ZEICHEN-SCHWUR@1": "0.8 2.0 28.6 33.2",
 "FIG-ZEICHEN-SCHWUR@2": "-0.2 6.1 30.3 29.1",
 "FIG-ZEICHEN-PREISEN@1": "-26.5 -34.4 53.0 45.4",
 "FIG-ZEICHEN-PREISEN@2": "3.3 -1.4 29.4 36.6",
 "FIG-ZEICHEN-KRAFT@1": "-4.5 -31.4 33.8 43.5",
 "FIG-ZEICHEN-KRAFT@2": "-4.5 -35.3 39.4 47.3",
 "FIG-ZEICHEN-HAND@1": "-12.7 -25.8 21.4 32.1",
 "FIG-ZEICHEN-HAND@2": "-12.9 -25.8 22.1 32.1",
 "FIG-ZEICHEN-LOHN-ERHALTEN@1": "-6.1 11.4 29.8 15.7",
 "FIG-ZEICHEN-LOHN-ERHALTEN@2": "-6.1 9.8 29.7 17.4",
 "FIG-ZEICHEN-GRUESSEN@1": "-11.8 -30.6 29.7 38.4",
 "FIG-ZEICHEN-GRUESSEN@2": "-16.0 -30.6 34.0 38.4",
 "FIG-ZEICHEN-TREUE@1": "2.9 4.2 33.3 30.9",
 "FIG-ZEICHEN-TREUE@2": "2.9 4.2 28.5 30.9",
 "FIG-ZEICHEN-AUSLIEFERN@1": "3.3 4.4 27.4 31.1",
 "FIG-ZEICHEN-BERUEHREN@1": "-5.2 -3.2 42.5 45.2",
 "FIG-ZEICHEN-ZEIGEN@1": "-5.9 -8.8 28.4 17.3",
 "FIG-ZEICHEN-ZEIGEN@2": "-5.9 -8.8 33.8 17.3",
 "FIG-ZEICHEN-WUNDMALE@1": "-21.5 -25.9 42.9 32.9",
 "FIG-ZEICHEN-WUNDMALE@2": "-12.7 -25.8 21.4 32.1",
 "FIG-ZEICHEN-VERGEBEN@1": "-6.2 0.9 46.7 30.6",
 "FIG-ZEICHEN-VERGEBEN@2": "1.8 3.4 19.5 22.6",
 "FIG-ZEICHEN-HAND-VERDORRT@1": "-12.7 -25.8 38.5 32.1",
 "FIG-ZEICHEN-GLAUBEN@1": "-9.4 8.2 46.9 28.8"
}
# AUTO_VB_ENDE


def alle(roh=False):
    out = {}
    for fid, (fn, bed, gez) in ZEICHEN.items():
        for v, (vb, svg) in fn().items():
            k = f"{fid}{v}"
            if not roh:  # Ausschnitt auf 0 0 verschieben (Symbole mit negativem Ursprung wurden im Testblatt beschnitten)
                x, y, w, h = (float(t) for t in AUTO_VB.get(k, vb).split())
                svg, vb = f'<g transform="translate({_f(-x)} {_f(-y)})">{svg}</g>', f"0 0 {_f(w)} {_f(h)}"
            out[k] = {"vb": vb, "svg": svg, "bedeutung": bed, "gezeichnet": gez}
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
