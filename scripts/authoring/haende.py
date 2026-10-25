#!/usr/bin/env python3
"""Gemeinsame Handbibliothek für Bildzeichen (docs/SYMBOLPROZESS.md, Runde 11, 2026-10-25).

Hände wurden bisher in jedem Zeichen neu gezeichnet und waren oft Fäustlinge, Keile oder Balken (Durchsicht: «Hände fast
durchweg mangelhaft»). Alle Zeichen mit Händen setzen ihre Hände aus diesen Bausteinen zusammen.

Bauweise: Jede Hand besteht aus einer Handfläche (Fläche) und Fingern als runde Striche (Kapseln). Gezeichnet wird zuerst
die ganze Hand dick in Tinte (Kontur nur aussen), darüber dieselben Teile hautfarben ohne Strich. Finger liegen mit kleinem
Abstand nebeneinander; die Tinte darunter bleibt als Fuge zwischen den Fingern bis zur Handfläche stehen. Teile, die vor
anderen liegen (Daumen vor der Faust, vordere Finger), bekommen eine feine Innenlinie.

Jede Funktion gibt SVG-Inhalt in einem eigenen Koordinatensystem zurück: das Handgelenk liegt bei (0, 0), die Richtung der
Hand steht im Docstring. Platzieren mit `place(svg, x, y, winkel, massstab, spiegeln)`.

Regeln: eine Silhouette mit Kontur nur aussen, Daumen klar abgesetzt, Finger verschieden lang, Ärmel als Manschette.
Keine IDs, Filter oder Verläufe (die Zeichen werden als <symbol> in eine gemeinsame Bibliothek gesetzt).
"""
INK, SKIN, SLEEVE, GOLD = "#3B3226", "#E2AE80", "#5E7FA8", "#E8B931"
O_AUSSEN, O_INNEN = 1.0, .5   # Konturbreite aussen und Innenlinie (je Seite)


def _f(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


def _parts(parts, col, extra):
    """parts: ("f", d) Fläche oder ("s", d, breite) Kapsel; col Farbe; extra zusätzliche Breite (2 × Kontur)."""
    out = []
    for p in parts:
        if p[0] == "f":
            out.append(f'<path d="{p[1]}" fill="{col}"' + (f' stroke="{col}" stroke-width="{_f(extra)}" stroke-linejoin="round"' if extra else "") + "/>")
        else:
            out.append(f'<path d="{p[1]}" fill="none" stroke="{col}" stroke-width="{_f(p[2] + extra)}" stroke-linecap="round" stroke-linejoin="round"/>')
    return "".join(out)


def sil(*groups, fill=SKIN, o=O_AUSSEN, oi=O_INNEN):
    """Teile als eine Silhouette: alle Gruppen zuerst dick in Tinte (Kontur nur aussen), dann Gruppe für Gruppe hautfarben;
    ab der zweiten Gruppe mit feiner Innenlinie (liegt vor der ersten)."""
    allp = [p for g in groups for p in g]
    s = _parts(allp, INK, 2 * o)
    for i, g in enumerate(groups):
        if i:
            s += _parts(g, INK, 2 * oi)
        s += _parts(g, fill, 0)
    return s


def schichten(*layers, fill=SKIN, o=O_AUSSEN):
    """Wie sil(), aber jede Schicht (parts, innenlinie) mit eigener Innenlinie; 0 = ohne. Für Finger: jeder Finger eine
    Schicht mit Innenlinie (gibt die Fugen), die Handfläche zuletzt ohne Innenlinie darüber (verdeckt die Fingeransätze,
    sodass keine Linie quer über die Handfläche läuft)."""
    allp = [p for g, _ in layers for p in g]
    s = _parts(allp, INK, 2 * o)
    for g, oi in layers:
        if oi:
            s += _parts(g, INK, 2 * oi)
        s += _parts(g, fill, 0)
    return s


def line(d, w=.7, col=INK):
    return f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{_f(w)}" stroke-linecap="round" stroke-linejoin="round"/>'


def cuff(d, fill=SLEEVE):
    return f'<path d="{d}" fill="{fill}" stroke="{INK}" stroke-width="{_f(2 * O_AUSSEN * .9)}" stroke-linejoin="round"/>'


def place(svg, x=0, y=0, a=0, s=1, flip=False):
    t = f"translate({_f(x)} {_f(y)})"
    if a:
        t += f" rotate({_f(a)})"
    if s != 1 or flip:
        t += f" scale({_f(-s if flip else s)} {_f(s)})"
    return f'<g transform="{t}">{svg}</g>'


def manschette(w=13, h=4.6, y=0, sleeve=SLEEVE, lang=0):
    """Ärmel unterhalb des Handgelenks (Hand zeigt nach oben): Rechteck von y bis y+h (+lang für Unterarm)."""
    return cuff(f"M{_f(-w / 2)} {_f(y - .6)}H{_f(w / 2)}L{_f(w / 2 + lang * .12)} {_f(y + h + lang)}H{_f(-w / 2 - lang * .12)}Z", sleeve)


# ------------------------------------------------------------------ Einzelhände
def _finger(x0, y0, x1, y1, w=2.4, cx=None, cy=None):
    d = f"M{_f(x0)} {_f(y0)}" + (f"Q{_f(cx)} {_f(cy)} " if cx is not None else "L") + f"{_f(x1)} {_f(y1)}"
    return [("s", d, w)]


def hand_offen(sleeve=SLEEVE, cuff_on=True, lang=0, spreiz=1.0, geschlossen=False):
    """Offene Hand, Handfläche zum Betrachter, Finger nach oben (wie ✋); Daumen links. Handgelenk (0,0), Finger bis y≈-23.
    spreiz: Fächerung der Finger (1 normal, 1.5 gespreizt wie 🙌/👋); geschlossen: Finger parallel aneinander, Daumen
    angelegt (Schwurhand)."""
    if geschlossen:
        palm = [("f", "M-5.6 0L-6-8.6Q-6.1-12.2-3-12.4L3.2-12.4Q6.1-12.2 5.9-9L5.4 0Z")]
        fing = [_finger(x0, -10.5, x0, tip, 2.75) for x0, tip in ((-4.3, -21.2), (-1.4, -22.9), (1.5, -22.1), (4.3, -19.2))]
        thumb = [("s", "M-4.4-3.2Q-7-5.4-7.4-9.6", 2.8)]
        s = schichten(*[(f, O_INNEN) for f in fing], (thumb, 0), (palm, 0))
        return (manschette(13, 4.8, 0, sleeve, lang) if cuff_on else "") + s
    palm = [("f", "M-5.8 0L-6.4-8.6Q-6.5-12.2-3.2-12.4L3.4-12.4Q6.5-12.2 6.3-9L5.6 0Z")]
    fing = [_finger(x0, -10.5, x0 + dx * spreiz, tip, 2.6) for x0, tip, dx in
            ((-4.7, -21.2, -1.1), (-1.55, -22.9, -.35), (1.6, -22.1, .45), (4.6, -19.0, 1.2))]
    thumb = [("s", f"M-4.2-3.4Q-7.6-5-{_f(9.7 + .6 * (spreiz - 1))} {_f(-10.2 - .8 * (spreiz - 1))}", 2.75)]
    s = schichten(*[(f, O_INNEN) for f in fing], (thumb, 0), (palm, 0))
    s += line("M-3.4-3.6Q-1.8-7.2-3.6-9.8", .55)  # Daumenballen (fein, nur gross sichtbar)
    return (manschette(13.6, 4.8, 0, sleeve, lang) if cuff_on else "") + s


def hand_zeigend(sleeve=SLEEVE, cuff_on=True):
    """Zeigende Hand von der Seite (wie 👉): Handrücken zum Betrachter, Zeigefinger nach rechts (+x), Daumen oben,
    drei Finger eingerollt. Handgelenk (0,0); Fingerspitze bei (20, -2.3)."""
    palm = ("f", "M0-4.8Q4-5.6 7.6-5L9.4-3.4L10.2 5.4Q6 7.8 0 6.2Z")
    index = ("s", "M6.4-2.3H19.4", 2.9)
    curled = [("s", f"M6.6 {_f(y)}H{_f(x1)}", 2.45) for y, x1 in ((.9, 11.4), (3.4, 11.0), (5.7, 10.1))]
    thumb = ("s", "M2.4-5Q6.4-6.6 10.8-5.4", 2.6)
    s = sil([palm, index] + curled, [thumb])
    return (cuff("M.6-5.8H-4.4V6.8H.6Z", sleeve) if cuff_on else "") + s


def hand_faust(sleeve=SLEEVE, griff="", cuff_on=True):
    """Geschlossene Hand von der Seite, greifend: Handrücken zum Betrachter, Finger rechts eingerollt, Daumen oben darüber.
    Handgelenk (0,0); Griffloch (für einen senkrechten Stab) bei x≈8.6, y -6…7. griff: SVG eines gehaltenen Gegenstands,
    wird zwischen Handfläche und Fingern gezeichnet."""
    palm = [("f", "M0-4.6Q4-5.6 7.4-5L8.6 6.6Q5 7.6 0 6.4Z")]
    curled = [("s", f"M6.2 {_f(y)}H{_f(x1)}", 2.45) for y, x1 in ((-3.0, 11.2), (-.5, 11.6), (2.0, 11.3), (4.5, 10.4))]
    thumb = [("s", "M2.2-4.9Q6.6-6.8 10.6-5", 2.6)]
    s = _parts(palm + curled + thumb, INK, 2 * O_AUSSEN) + _parts(palm, SKIN, 0) + griff
    s += _parts(curled, INK, 2 * O_INNEN * 1.2) + _parts(curled, SKIN, 0) + _parts(thumb, INK, 2 * O_INNEN) + _parts(thumb, SKIN, 0)
    return (cuff("M.6-5.6H-4.4V6.6H.6Z", sleeve) if cuff_on else "") + s


def hand_daumen(sleeve=SLEEVE, cuff_on=True):
    """Faust mit Daumen nach oben (wie 👍), von der Seite: Handgelenk (0,0) links, Finger rechts als gestapelte Rundungen
    (Fingerknöchel), Daumen oben bis y≈-13. Für 👎 um 180° drehen."""
    palm = ("f", "M0-5Q3-6 6-5.6L11.2-4.6L11.6 6.4Q6 8 0 6.6Z")
    curled = [("s", f"M5.2 {_f(y)}H{_f(x1)}", 2.5) for y, x1 in ((-3.1, 12.2), (-.4, 12.8), (2.3, 12.5), (5.0, 11.4))]
    thumb = ("s", "M3.4-4.4Q4-8 3.8-10.6", 3.3)
    s = sil([palm, thumb], curled)
    return (cuff("M.6-6.2H-4.6V7.2H.6Z", sleeve) if cuff_on else "") + s


def hand_empfangend(sleeve=SLEEVE, cuff_on=True):
    """Offene Hand, Handfläche nach oben, leicht gewölbt (wie 🫴): Handgelenk (0,0) links, Finger nach rechts, Fingerspitzen
    leicht nach oben, Daumen oben kurz abgespreizt. Finger bis x≈21; Mulde der Hand bei etwa (9, -1.5)."""
    palm = [("f", "M0-1.4Q5-1.8 9.4-1.2L10.2 4Q5 5.4 0 4.4Z")]
    f3 = [("s", "M8.2 3.9Q13.6 4.8 17.2 3.4Q18 3 18.5 2.3", 2.5)]
    f2 = [("s", "M8.4 1.6Q14.8 2.6 18.6.6Q19.5 0 19.9-.9", 2.5)]
    f1 = [("s", "M8.6-.8Q15.4-.2 19.4-2.6Q20.4-3.3 20.8-4.3", 2.5)]
    thumb = [("s", "M3.8-1Q6.4-2.4 8-4.8", 3.0)]
    s = schichten((thumb, 0), (f3, 0), (f2, O_INNEN), (f1, O_INNEN), (palm, 0))
    return (cuff("M.6-2.4H-4.6V5.4H.6Z", sleeve) if cuff_on else "") + s


def hand_gebend(sleeve=SLEEVE, cuff_on=True):
    """Flache Hand von der Seite, Handrücken oben, Finger gestreckt nach rechts und leicht abwärts (wie 🫳: legt etwas hin,
    lässt etwas fallen): Handgelenk (0,0) links; Fingerspitzen bei etwa (19, 3), Daumen unten bei (11, 5.6)."""
    palm = [("f", "M0-3.2Q5-3.8 9.2-2.8L9.4 3.2Q5 4 0 3Z")]
    f1 = [("s", "M8-1.6Q14.6-1.6 18.6 1.4", 2.5)]
    f2 = [("s", "M8 .8Q14 1 17.6 3.6", 2.4)]
    f3 = [("s", "M7.8 2.6Q12.4 3.2 15.2 5.2", 2.3)]
    thumb = [("s", "M4.6 2.4Q8 4.4 11 5.4", 2.6)]
    s = schichten((f3, 0), (f2, O_INNEN), (f1, O_INNEN), (palm, 0), (thumb, O_INNEN))
    s += line("M3.4-1.2Q6.2-.6 8.2-1.4", .55)  # Knöchel (fein)
    return (cuff("M.6-4.2H-4.6V4H.6Z", sleeve) if cuff_on else "") + s


def hand_auf_schulter(sleeve=SLEEVE, cuff_on=True):
    """Hand liegt auf einer Schulter (von der Seite): Handgelenk (0,0) links, Handfläche waagrecht, Finger nach rechts
    über die Schulter nach unten gebogen; Fingerspitzen bei etwa (14, 6.6)."""
    palm = [("f", "M0-3Q5-3.6 9-2.6L9.6 2.4Q5 3.2 0 2.6Z")]
    f1 = [("s", "M8-1.4Q12.6-1.6 13.8 2Q14.4 4.2 14.2 6.6", 2.45)]
    f2 = [("s", "M7.6 1Q10.8 1 11.6 3.6Q12 5.2 11.8 7", 2.45)]
    thumb = [("s", "M4.6 1.6Q6.6 3.4 7.6 5.4", 2.5)]
    s = schichten((f1, 0), (f2, O_INNEN), (palm, 0), (thumb, O_INNEN))
    return (cuff("M.6-4H-4.6V3.6H.6Z", sleeve) if cuff_on else "") + s


def hand_verdorrt(sleeve=SLEEVE, cuff_on=True, haut="#B7A58C"):
    """Verdorrte, gelähmte Hand (Mt 12,10), von der Seite: das Handgelenk knickt kraftlos nach unten, die dünnen Finger
    sind steif zur Handfläche eingekrümmt; fahle Haut. Handgelenk (0,0) links (Unterarm waagrecht), Hand hängt bis y≈11."""
    palm = [("f", "M-.4-2.6Q3.6-3.2 5.2-.4L5.6 6.2Q3 7.6.4 6.4L-.4 2.4Z")]
    fing = [[("s", f"M{_f(x0)} 5.6Q{_f(x0 + .4)} {_f(yb)} {_f(x0 - 2.2)} {_f(yb + .2)}Q{_f(x0 - 3.6)} {_f(yb)} {_f(x0 - 3.2)} {_f(yb - 1.8)}", 1.9)]
            for x0, yb in ((4.6, 10.6), (3.4, 11.2), (2.0, 10.4))]
    thumb = [("s", "M.6 4.4Q-.6 6.6.4 8.2", 2)]
    s = schichten(*[(f, O_INNEN) for f in fing], (palm, 0), (thumb, O_INNEN), fill=haut)
    s += line("M1.4 1Q2.8 1.8 4.2 1", .5) + line("M1.6 3.2Q3 4 4.4 3.2", .5)  # Falten
    return (cuff("M.6-3.6H-6V3.6H.6Z", sleeve) if cuff_on else "") + s


def arm_kraft(sleeve=SLEEVE):
    """Angespannter Arm (wie 💪): Ärmel links, Oberarm waagrecht mit hohem Bizeps, Ellbogen unten rechts, Unterarm
    aufrecht, Faust oben (Finger zum Kopf hin). Box etwa -4 -33 32 44."""
    arm = ("f", "M2-.6Q5-13.4 12.6-11.6Q16.6-10.4 16.8-6.8L16.4-17.2L24.8-18.6L26 2Q26 9.8 19 10L2 9.4Z")
    s = place(hand_faust(cuff_on=False), 20.4, -16.4, -100, 1.05)
    s = sil([arm]) + s
    s += line("M10-2.8Q13-4.6 15.8-3", .75)  # Bizepsfalte
    return cuff("M2.6-2.6H-3V10.6H2.6Z", sleeve) + s


# ------------------------------------------------------------------ Zwei Hände
def haende_betend(sleeve=SLEEVE):
    """Betende Hände (wie 🙏): zwei Handflächen aneinander, lange Finger nach oben zur Mitte geneigt, Spitzen oben zusammen,
    beide Daumen vorn abgesetzt, Ärmel schräg nach unten auseinander. Mitte unten (0,0), Fingerspitzen bei y≈-27."""
    def one(fl):
        palm = [("f", "M0 .6L0-12.4Q3.8-12 6.8-8.4Q8.4-5.4 7.6-1.4L5.6 1Z")]
        fing = [_finger(x0, y0, x1, y1, 2.45) for x0, y0, x1, y1 in
                ((1.3, -10, 1.25, -26.6), (3.8, -9.4, 3.15, -24.6), (6.0, -7.8, 5.0, -21.6), (7.7, -5.2, 6.7, -17.2))]
        return place(schichten(*[(f, O_INNEN) for f in fing[::-1]], (palm, 0)), flip=fl)
    thumbs = [("s", "M-1.5-1.2Q-2.3-6-1.2-10.6", 2.6), ("s", "M1.5-1.2Q2.3-6 1.2-10.6", 2.6)]
    th = _parts(thumbs, INK, 2 * O_INNEN * 1.5) + _parts(thumbs, SKIN, 0)
    cuffs = (cuff("M-7-.4H-.3L-1.4 5.6L-10 4.4Z", sleeve) + cuff("M7-.4H.3L1.4 5.6L10 4.4Z", sleeve))
    return cuffs + one(False) + one(True) + th


def haende_schale(sleeve=SLEEVE):
    """Zwei offene Hände nebeneinander, Handflächen nach oben (wie 🤲): kleine Finger in der Mitte aneinander, Daumen aussen,
    Finger leicht nach aussen geneigt. Mitte unten (0,0), Fingerspitzen bei y≈-19."""
    def one(fl):
        palm = [("f", "M.4 0L.2-6.6Q.4-10 3-10.4L8.4-10.2Q10.6-9.6 10.4-6.6L9.2 0Z")]
        fing = [_finger(x0, -8.4, x0 + dx, tip, 2.45) for x0, tip, dx in
                ((1.75, -15.4, -.5), (4.85, -18.2, 0), (7.95, -18.6, .4))]
        thumb = [("s", "M9.2-2.8Q12.6-4.6 14.6-9.4", 2.8)]
        h = schichten(*[(f, O_INNEN) for f in fing], (thumb, 0), (palm, 0)) + cuff("M.2-.5H9.6L10 3.8H.4Z", sleeve)
        return place(place(h, .2, 0, 5), flip=fl)
    return one(False) + one(True)


def haende_erhoben(sleeve=SLEEVE, abstand=11, winkel=16):
    """Zwei erhobene offene Hände mit Unterarm (wie 🙌), Finger gespreizt, leicht nach aussen geneigt. Mitte unten (0,0)."""
    h = hand_offen(sleeve, lang=3, spreiz=1.5)
    return place(h, -abstand, 0, -winkel, flip=False) + place(h, abstand, 0, winkel, flip=True)


# ------------------------------------------------------------------ Kleinteile
def muenze(cx, cy, r=2.6):
    """Münze mit Prägung (Kopf im Profil; Detailregel Runde 6: die Prägung trägt)."""
    return (f'<circle cx="{_f(cx)}" cy="{_f(cy)}" r="{_f(r)}" fill="{GOLD}" stroke="{INK}" stroke-width="1.1"/>'
            f'<path d="M{_f(cx - r * .25)} {_f(cy + r * .5)}Q{_f(cx - r * .45)} {_f(cy - r * .05)} {_f(cx - r * .05)} {_f(cy - r * .5)}'
            f'Q{_f(cx + r * .45)} {_f(cy - r * .4)} {_f(cx + r * .3)} {_f(cy + r * .1)}L{_f(cx + r * .1)} {_f(cy + r * .5)}" fill="#B8891A"/>')


def fallstriche(x, y, n=3, l=1.6, col=INK):
    """Kurze Fallstriche über einem Gegenstand (Bewegung nach unten)."""
    d = "".join(f"M{_f(x + dx)} {_f(y)}v{_f(l)}" for dx in ((-1.8, 0, 1.8) if n == 3 else (-1, 1)))
    return line(d, .8, col)


def almosen():
    """Almosen geben: gebende Hand von oben legt eine Münze in eine offene, empfangende Hand. viewBox 0 0 34 30."""
    return (place(hand_gebend(), 13, 6, 0, 1) + fallstriche(28.6, 13.6, 2, 1.4) + muenze(28.8, 18.2, 2.5)
            + place(hand_empfangend(), 5, 23, 0, 1.05))
