#!/usr/bin/env python3
"""Bildzeichen «Handlungen» neu gezeichnet (docs/SYMBOLPROZESS.md, Runde 11, 2026-10-25).

Durchsicht: Handlungen waren oft blosse Pfeile (bringen, fliehen), Bedien-Symbole (Lautsprecher, Schallbögen) oder
Kegel-Figuren. Regel: Handlung als Figur in Handlung zeigen (wie 🏃 / Leitsystem-Piktogramme), Pfeile höchstens als Zusatz.

Alle Figuren kommen aus einem Baukasten (`figur`): Kopf als Kreis, Rumpf als gerundeter Balken, Glieder als gerundete
Striche mit runder Hand; Kontur nur aussen (zuerst dick in Tinte, darüber farbig, wie haende.sil). Ferne Glieder etwas
dunkler, nahe Glieder mit eigener Kontur darüber. Hände in Gesten aus scripts/authoring/haende.py.

    python3 scripts/authoring/zeichen_handlung.py                    # schreibt bildsymbole_daten/ueberarbeitet/handlung.json (Auswahl FINAL)
    python3 scripts/authoring/zeichen_handlung.py --entwuerfe E.json # alle Fassungen als Entwürfe für zeichen_test.py

KI-Entwurf (Claude), 2026-10-25, CC0.
"""
import json
import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import haende as H  # noqa: E402

INK, SKIN, GOLD = H.INK, H.SKIN, H.GOLD
BLUE, RED, GREEN, WHITE, BROWN = "#5E7FA8", "#B0623E", "#6E8B3D", "#F4EEDF", "#8A6A48"
WATER, WATER_D, STONE, STONE_D = "#5DA7DB", "#2E5478", "#B4AC9C", "#8C8070"
O = 1.1  # Konturbreite je Seite


def f(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


def shade(c, k=.72):
    c = c.lstrip("#")
    return "#" + "".join(f"{int(int(c[i:i + 2], 16) * k):02X}" for i in (0, 2, 4))


def pts(p):
    return "M" + "L".join(f"{f(x)} {f(y)}" for x, y in p)


def stroke(p, w, col):
    return (f'<path d="{pts(p)}" fill="none" stroke="{col}" stroke-width="{f(w)}" stroke-linecap="round" '
            f'stroke-linejoin="round"/>')


def circ(c, r, col):
    return f'<circle cx="{f(c[0])}" cy="{f(c[1])}" r="{f(r)}" fill="{col}"/>'


def ln(d, w=.9, col=INK):
    return f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{f(w)}" stroke-linecap="round" stroke-linejoin="round"/>'


def shape(d, fill, w=1.1):
    return f'<path d="{d}" fill="{fill}" stroke="{INK}" stroke-width="{f(w)}" stroke-linejoin="round"/>'


def limb(p, w, col, hand=True):
    """Glied mit eigener Kontur; Hand als runder Abschluss in Hautfarbe."""
    s = stroke(p, w + 2 * O, INK)
    if hand:
        s += circ(p[-1], w / 2 + .45 + O, INK)
    s += stroke(p, w, col)
    if hand:
        s += circ(p[-1], w / 2 + .45, SKIN)
    return s


def d(a, n=1):
    """Richtung: Winkel in Grad ab senkrecht nach unten, positiv zur Blickrichtung (n = +1 rechts, -1 links)."""
    r = math.radians(a)
    return (math.sin(r) * n, math.cos(r))


def add(p, v, l):
    return (p[0] + v[0] * l, p[1] + v[1] * l)


class Fig:
    """Piktogramm-Figur. hip = Hüfte; lean = Neigung des Rumpfs (Grad, + nach vorn); Glieder als (Oberwinkel, Unterwinkel)
    absolut ab senkrecht unten, + nach vorn. s = Massstab (1 = etwa 36 Einheiten hoch)."""

    def __init__(self, hip, lean=0, an=(10, 10), af=(-10, -10), ln_=(6, 0), lf=(-6, 0), n=1, s=1, col=BLUE,
                 head=None, legs=True, front=False):
        """front=True: Vorderansicht (Arme an beiden Schultern, Winkel des fernen Arms und Beins gespiegelt)."""
        self.n, self.s, self.col, self.front = n, s, col, front
        T, self.A, self.L, self.R = 11 * s, 3.1 * s, 3.5 * s, 4.4 * s
        self.TW = 6.8 * s
        self.hip = hip
        up = d(180 - lean, n)
        self.neck = add(hip, up, T)
        self.sh = add(hip, up, T - 2.5 * s)
        hl = d(180 - (lean if head is None else head), n)
        self.head = add(self.neck, hl, self.R + 1.3 * s)
        U, Lo, Th, Sh = 5.6 * s, 5.4 * s, 7.4 * s, 7.4 * s
        if front:
            dx = self.TW / 2 - .4 * s
            self.arm_n = self._chain((self.sh[0] + dx, self.sh[1]), an, U, Lo)
            self.n = -n
            self.arm_f = self._chain((self.sh[0] - dx, self.sh[1]), af, U, Lo)
            self.leg_f = self._chain((hip[0] - 1.6 * s, hip[1]), lf, Th, Sh)
            self.n = n
            self.leg_n = self._chain((hip[0] + 1.6 * s, hip[1]), ln_, Th, Sh)
        else:
            self.arm_n = self._chain(self.sh, an, U, Lo)
            self.arm_f = self._chain(self.sh, af, U, Lo)
            self.leg_n = self._chain(hip, ln_, Th, Sh)
            self.leg_f = self._chain(hip, lf, Th, Sh)
        self.legs = legs

    def _chain(self, p0, ang, l1, l2):
        if ang is None:
            return None
        if len(ang) == 2:
            a1, a2 = ang
            p1 = add(p0, d(a1, self.n), l1)
            return [p0, p1, add(p1, d(a2, self.n), l2)]
        return [p0, add(p0, d(ang[0], self.n), l1 + l2)]

    def ground(self, y):
        """Figur senkrecht verschieben, sodass der tiefste Fuss auf y steht."""
        low = max(p[-1][1] for p in (self.leg_n, self.leg_f) if p)
        dy = y - low - self.L / 2 - O * .3
        for a in ("hip", "neck", "sh", "head"):
            v = getattr(self, a)
            setattr(self, a, (v[0], v[1] + dy))
        for a in ("arm_n", "arm_f", "leg_n", "leg_f"):
            v = getattr(self, a)
            if v:
                setattr(self, a, [(x, yy + dy) for x, yy in v])
        return self

    def hand_at(self, svg, arm="n", s=.4, da=0):
        """Hand aus haende.py an das Ende des Arms setzen (Handgelenk = Armende, gedreht in Richtung des Unterarms)."""
        p = self.arm_n if arm == "n" else self.arm_f
        (x0, y0), (x1, y1) = p[-2], p[-1]
        a = math.degrees(math.atan2(y1 - y0, x1 - x0)) + da
        return H.place(svg, x1, y1, a, s, False)

    def svg(self, face="", front_extra="", behind="", hand_n=True, hand_f=True):
        c, fc = self.col, shade(self.col)
        if self.front:
            fc = c
        o = behind
        if self.arm_f:
            o += limb(self.arm_f, self.A, fc, hand_f is True) + (hand_f if isinstance(hand_f, str) else "")
        if self.legs and self.leg_f:
            o += limb(self.leg_f, self.L, fc, False)
        # Rumpf und nahes Bein als eine Silhouette
        ink = stroke([self.neck, self.hip], self.TW + 2 * O, INK)
        col = stroke([self.neck, self.hip], self.TW, c)
        if self.legs and self.leg_n:
            ink += stroke(self.leg_n, self.L + 2 * O, INK)
            col += stroke(self.leg_n, self.L, c)
        o += ink + col
        o += circ(self.head, self.R + O, INK) + circ(self.head, self.R, SKIN) + face
        if self.arm_n:
            o += limb(self.arm_n, self.A, c, hand_n is True) + (hand_n if isinstance(hand_n, str) else "")
        return o + front_extra

    def eye(self, dx=1.7, dy=-.4, r=.62):
        return circ((self.head[0] + dx * self.n * self.s, self.head[1] + dy * self.s), r * self.s, INK)


def head_hair(c, r, n=1, col="#4A3828"):
    """Haarkappe für Profilköpfe (Hinterkopf)."""
    x, y = c
    return shape(f"M{f(x - n * r * .2)} {f(y - r * 1.02)}A{f(r * 1.02)} {f(r * 1.02)} 0 0 {0 if n > 0 else 1} "
                 f"{f(x - n * r * .98)} {f(y + r * .35)}Q{f(x - n * r * .5)} {f(y - r * .1)} {f(x - n * r * .2)} {f(y - r * 1.02)}Z", col, .8)


def motion(x, y, n=1, k=3, gap=3.2, l=5, w=1.4):
    """Bewegungsstriche hinter einer Figur (n = Laufrichtung)."""
    return "".join(ln(f"M{f(x)} {f(y + i * gap)}h{f(-n * (l - abs(i - (k - 1) / 2) * 1.4))}", w, STONE_D) for i in range(k))


# ------------------------------------------------------------------------------------------------ Gegenstände
def korb(x, y, w=9, h=6):
    return (shape(f"M{f(x - w / 2)} {f(y)}h{f(w)}l-1.2 {f(h)}h{f(-w + 2.4)}z", "#C9963E", 1)
            + ln(f"M{f(x - w / 2 + 1.6)} {f(y + 2)}h{f(w - 3.2)}M{f(x - w / 2 + 2)} {f(y + 4)}h{f(w - 4)}", .6, "#8A6424")
            + circ((x - 1.8, y - 1.2), 1.7, "#C0463A") + circ((x + 1.4, y - 1.4), 1.7, "#E8B931")
            + ln(f"M{f(x - 3.5)} {f(y - .1)}a1.7 1.7 0 0 1 3.4 0M{f(x - .3)} {f(y - .1)}a1.7 1.7 0 0 1 3.4 0", .8))


def stein(x, y, w=7, h=4.4):
    return shape(f"M{f(x - w / 2)} {f(y)}Q{f(x - w / 2)} {f(y - h)} {f(x)} {f(y - h)}Q{f(x + w / 2)} {f(y - h)} {f(x + w / 2)} {f(y)}Z",
                 STONE, 1)


def wasser(x0, x1, y, h, wave=4):
    n = max(1, int((x1 - x0) / wave))
    step = (x1 - x0) / n
    top = "".join(f"q{f(step / 4)} {-1.2} {f(step / 2)} 0t{f(step / 2)} 0" for _ in range(n))
    return (f'<path d="M{f(x0)} {f(y)}{top}V{f(y + h)}H{f(x0)}Z" fill="{WATER}"/>'
            + f'<path d="M{f(x0)} {f(y)}{top}" fill="none" stroke="{WATER_D}" stroke-width="1"/>')


def schwert(x, y, a=0, l=13):
    """Schwert, Griff bei (x,y), Klinge in Richtung a (Grad ab oben, im Uhrzeigersinn)."""
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(a)})">'
            + shape(f"M-1.1 -2.4L-1.1 {f(-l)}L0 {f(-l - 2)}L1.1 {f(-l)}L1.1 -2.4Z", "#D9DEE4", .8)
            + shape("M-3.4 -2.6h6.8v1.6h-6.8z", GOLD, .7) + shape("M-.9 -1v3.4h1.8v-3.4z", BROWN, .6) + "</g>")


def sprechblase(x, y, w, h, tail=(-1, 1), fill="#FFFDF6", zack=False):
    """Sprechblase: Mitte (x,y); tail Richtung des Zipfels."""
    if zack:  # gezackte Blase wie 🗯
        k = 12
        p = []
        for i in range(k * 2):
            a = math.pi * 2 * i / (k * 2)
            r = 1 if i % 2 == 0 else .72
            p.append((x + math.cos(a) * w / 2 * r, y + math.sin(a) * h / 2 * r))
        return shape(pts(p) + "Z", fill, 1.1)
    tx, ty = tail
    bx, by = x + tx * w * .18, y + h / 2 - .6
    return (shape(f"M{f(bx - 2)} {f(by - .4)}L{f(x + tx * w * .42)} {f(y + h / 2 + 3.4 * ty)}L{f(bx + 2.4 * (1 if tx > 0 else -1) * -1 + 0)} {f(by - .2)}Z", fill, 1.1)
            + f'<rect x="{f(x - w / 2)}" y="{f(y - h / 2)}" width="{f(w)}" height="{f(h)}" rx="{f(h / 2.2)}" fill="{fill}" stroke="{INK}" stroke-width="1.1"/>'
            + f'<rect x="{f(bx - 2.6)}" y="{f(by - 1.6)}" width="5.2" height="2" fill="{fill}"/>')


def zzz(x, y, s=1):
    out = ""
    for i, k in enumerate((1, .78, .6)):
        sz = 3.4 * s * k
        xx, yy = x + i * 3.6 * s, y - i * 3.8 * s
        out += ln(f"M{f(xx)} {f(yy)}h{f(sz)}l{f(-sz)} {f(sz)}h{f(sz)}", 1.15 * s * (k + .2), "#4A6A9A")
    return out


# ------------------------------------------------------------------------------------------------ Zeichen
Z = {}


def zeichen(name, bedeutung, gezeichnet):
    def deco(fn):
        Z[name] = (fn, bedeutung, gezeichnet)
        return fn
    return deco


@zeichen("BRINGEN@1", "bringen: eine Figur trägt etwas zu jemandem hin",
         "Figur im Schritt trägt einen Korb mit beiden Armen vor sich, geht auf eine zweite Figur mit offenen Händen zu")
def bringen1():
    a = Fig((14, 22), lean=6, an=(40, 100), af=(30, 95), ln_=(28, 8), lf=(-26, -6), col=BLUE)
    b = Fig((40, 22), lean=-4, an=(35, 75), af=(28, 70), ln_=(4, 0), lf=(-4, 0), n=-1, col=RED)
    k = korb(a.arm_n[2][0] + 1.4, a.arm_n[2][1] - 1.2)
    return "0 0 48 38", motion(5, 14, 1, 3, 3.2, 4) + a.svg(behind="", front_extra=k) + b.svg()


@zeichen("BRINGEN@2", "bringen: eine Figur trägt etwas zu jemandem hin",
         "Figur im Schritt trägt einen grossen Korb vor sich, Bewegungsstriche dahinter, kleiner Pfeil zum Ziel")
def bringen2():
    a = Fig((15, 22), lean=8, an=(45, 100), af=(35, 98), ln_=(30, 10), lf=(-28, -8), col=BLUE)
    k = korb(a.arm_n[2][0] + 2, a.arm_n[2][1] - 1.5, 11, 7)
    arrow = ln("M30 34h8M35.5 31.5l2.5 2.5-2.5 2.5", 1.6)
    return "0 0 40 38", motion(5, 13, 1, 3, 3.4, 4.6) + a.svg(front_extra=k) + arrow


@zeichen("FLIEHEN@1", "fliehen / weggehen: jemand flieht oder läuft davon",
         "Rennende Figur wie Notausgang-Piktogramm, weit ausgreifend, Bewegungsstriche dahinter")
def fliehen1():
    a = Fig((20, 22), lean=20, an=(60, 150), af=(-55, -100), ln_=(72, 8), lf=(-40, -85), col=BLUE).ground(37.4)
    return "0 0 40 38", motion(7, a.hip[1] - 8, 1, 3, 3.6, 5.5) + a.svg(face=a.eye())


@zeichen("FLIEHEN@2", "fliehen / weggehen: jemand flieht oder läuft davon",
         "Rennende Figur blickt erschrocken über die Schulter zurück, Bewegungsstriche dahinter")
def fliehen2():
    a = Fig((20, 22), lean=20, an=(60, 150), af=(-55, -100), ln_=(72, 8), lf=(-40, -85), col=BLUE, head=10).ground(37.4)
    face = a.eye(dx=-1.8, dy=-.6) + ln(f"M{f(a.head[0] - 2.4)} {f(a.head[1] + 2)}a.9 .9 0 0 1 1.6 0z", .9)
    sweat = shape(f"M{f(a.head[0] + 5)} {f(a.head[1] - 4.4)}q1.4 2 0 2.8q-1.4-.8 0-2.8z", "#A9D2F0", .6)
    return "0 0 40 38", motion(7, a.hip[1] - 8, 1, 3, 3.6, 5.5) + a.svg(face=face) + sweat


@zeichen("NACHFOLGEN@1", "nachfolgen: jemandem nachfolgen, mit ihm gehen («Folge mir!»)",
         "Vordere Figur geht voran, zeigt mit dem Arm nach vorn und blickt zurück; die hintere Figur folgt im gleichen Schritt")
def nachfolgen1():
    b = Fig((14, 22), lean=4, an=(30, 20), af=(-30, -20), ln_=(30, 4), lf=(-28, -8), col=RED, s=.9).ground(37.4)
    a = Fig((34, 22), lean=2, an=(88, 95), af=(-30, -20), ln_=(30, 4), lf=(-28, -8), col=BLUE).ground(37.4)
    return "0 0 46 38", b.svg(face=b.eye()) + a.svg(face=a.eye(dx=-1.8))


@zeichen("NACHFOLGEN@2", "nachfolgen: jemandem nachfolgen, mit ihm gehen («Folge mir!»)",
         "Vordere Figur geht voran und zeigt nach vorn, zwei Figuren folgen ihr im Gleichschritt")
def nachfolgen2():
    c = Fig((9, 23), lean=4, an=(30, 20), af=(-30, -20), ln_=(30, 4), lf=(-28, -8), col=GREEN, s=.8).ground(37.4)
    b = Fig((21, 22.5), lean=4, an=(30, 20), af=(-30, -20), ln_=(30, 4), lf=(-28, -8), col=RED, s=.88).ground(37.4)
    a = Fig((36, 22), lean=2, an=(88, 95), af=(-30, -20), ln_=(30, 4), lf=(-28, -8), col=BLUE).ground(37.4)
    return "0 0 50 38", c.svg(face=c.eye()) + b.svg(face=b.eye()) + a.svg(face=a.eye())


def profilkopf(x, y, r=9, n=1, mund="offen", col=BLUE):
    """Kopf und Schultern im Profil (Blick n), wie 🗣."""
    sh = shape(f"M{f(x - 11 * n)} {f(y + 22)}Q{f(x - 11 * n)} {f(y + 11)} {f(x - 1 * n)} {f(y + 10.5)}Q{f(x + 9 * n)} {f(y + 11)} {f(x + 9 * n)} {f(y + 22)}Z", col, 1.1)
    # Kopf: Kreis mit Nase und Kinn
    hx, hy = x, y
    head = (f'<path d="M{f(hx - n * r * .1)} {f(hy - r)}A{f(r)} {f(r)} 0 0 {0 if n < 0 else 1} {f(hx + n * r * .82)} {f(hy - r * .2)}'
            f'L{f(hx + n * (r + 1.8))} {f(hy + r * .18)}L{f(hx + n * r * .92)} {f(hy + r * .32)}'
            + (f'L{f(hx + n * r * .78)} {f(hy + r * .5)}L{f(hx + n * r * .34)} {f(hy + r * .56)}L{f(hx + n * r * .8)} {f(hy + r * .74)}'
               if mund == "offen" else f'L{f(hx + n * r * .9)} {f(hy + r * .62)}')
            + f'Q{f(hx + n * r * .7)} {f(hy + r * 1.1)} {f(hx + n * r * .1)} {f(hy + r)}'
            f'A{f(r)} {f(r)} 0 0 {0 if n < 0 else 1} {f(hx - n * r * .1)} {f(hy - r)}Z" fill="{SKIN}" stroke="{INK}" stroke-width="1.1" stroke-linejoin="round"/>')
    hair = shape(f"M{f(hx + n * r * .5)} {f(hy - r * .86)}Q{f(hx)} {f(hy - r * 1.25)} {f(hx - n * r * .8)} {f(hy - r * .6)}"
                 f"Q{f(hx - n * r * 1.1)} {f(hy)} {f(hx - n * r * .7)} {f(hy + r * .55)}Q{f(hx - n * r * .3)} {f(hy - r * .1)} {f(hx + n * r * .1)} {f(hy - r * .4)}"
                 f"Q{f(hx + n * r * .4)} {f(hy - r * .6)} {f(hx + n * r * .5)} {f(hy - r * .86)}Z", "#4A3828", .9)
    eye = circ((hx + n * r * .42, hy - r * .12), .85, INK)
    return sh + head + hair + eye


@zeichen("SPRECHEN@1", "sprechen: eine Figur sagt etwas",
         "Kopf und Schultern im Profil mit offenem Mund, davor eine Sprechblase")
def sprechen1():
    return "0 0 44 36", profilkopf(12, 13, 8.4) + sprechblase(33, 10, 18, 13, (-1, 1)) + \
        circ((28, 10), 1.3, INK) + circ((33, 10), 1.3, INK) + circ((38, 10), 1.3, INK)


@zeichen("SPRECHEN@2", "sprechen: eine Figur sagt etwas",
         "Kopf und Schultern im Profil mit offenem Mund, Schallbögen vom Mund weg wie 🗣")
def sprechen2():
    arcs = "".join(ln(f"M{f(26 + i * 4)} {f(10 - 3 - i * 2)}Q{f(29 + i * 4.6)} {f(15)} {f(26 + i * 4)} {f(17 + 3 + i * 2)}", 1.6) for i in range(3))
    return "0 0 42 36", profilkopf(13, 13, 8.4) + arcs


@zeichen("VERKUENDIGEN@1", "verkündigen: eine Botschaft wird öffentlich vielen gesagt",
         "Figur steht erhöht auf einem Felsen, eine Hand am Mund, den anderen Arm erhoben, ruft; Schallbögen zu einer kleinen Menge unten")
def verkuendigen1():
    rock = shape("M1 37.6V31Q4 28.6 10.5 28.8Q17 28.6 20 31V37.6Z", STONE, 1.1)
    a = Fig((10.5, 16), lean=0, an=(60, 150), af=(120, 140), ln_=(5, 0), lf=(-5, 0), col=BLUE, s=.66).ground(29.2)
    a.arm_n = [a.sh, (a.sh[0] + 3, a.sh[1] + 1.2), (a.head[0] + a.R + .7, a.head[1] + 1.2)]
    hx, hy = a.head
    arcs = "".join(ln(f"M{f(hx + 7 + i * 3.4)} {f(hy - 3 - i * 1.6)}Q{f(hx + 10 + i * 4)} {f(hy + 1.5)} {f(hx + 7 + i * 3.4)} {f(hy + 6 + i * 1.6)}", 1.4) for i in range(3))
    crowd = ""
    for x, y, col in ((29.5, 31.4, RED), (38, 31.4, GREEN), (33.7, 33.8, "#C9963E")):
        crowd += shape(f"M{f(x - 4)} 37.6Q{f(x - 4)} {f(y)} {f(x)} {f(y)}Q{f(x + 4)} {f(y)} {f(x + 4)} 37.6Z", col, 1) + \
            circ((x, y - 3.2), 3 + O, INK) + circ((x, y - 3.2), 3, SKIN)
    return "0 0 43 38", rock + a.svg(face=a.eye()) + arcs + crowd


@zeichen("VERKUENDIGEN@2", "verkündigen: eine Botschaft wird öffentlich vielen gesagt",
         "Figur auf einer Erhöhung streckt den Arm über die Menge aus und ruft mit offenem Mund; drei Köpfe unten hören zu")
def verkuendigen2():
    rock = shape("M1 37.6V30Q4 27.6 10.5 27.8Q17 27.6 20 30V37.6Z", STONE, 1.1)
    a = Fig((10.5, 16), lean=4, an=(115, 130), af=(-20, -10), ln_=(5, 0), lf=(-5, 0), col=BLUE, s=.8).ground(28.2)
    mouth = shape(f"M{f(a.head[0] + 1.6)} {f(a.head[1] + 1)}a1.3 1.3 0 0 0 2.4 .4z", "#7A3A2A", .7)
    arcs = "".join(ln(f"M{f(a.head[0] + 6.4 + i * 3)} {f(a.head[1] - 2.4 - i * 1.4)}Q{f(a.head[0] + 9 + i * 3.6)} {f(a.head[1] + 1)} {f(a.head[0] + 6.4 + i * 3)} {f(a.head[1] + 4.4 + i * 1.4)}", 1.3) for i in range(2))
    crowd = ""
    for x, y, col in ((29.5, 31.4, RED), (38, 31.4, GREEN), (33.7, 33.8, "#C9963E")):
        crowd += shape(f"M{f(x - 4)} 37.6Q{f(x - 4)} {f(y)} {f(x)} {f(y)}Q{f(x + 4)} {f(y)} {f(x + 4)} 37.6Z", col, 1) + \
            circ((x, y - 3.2), 3 + O, INK) + circ((x, y - 3.2), 3, SKIN)
    return "0 0 43 38", rock + a.svg(face=a.eye() + mouth) + arcs + crowd


@zeichen("ABSTAND@1", "Abstand / vertraut sich nicht an: zwischen Personen besteht innerer Abstand",
         "Zwei Figuren mit Abstand, dazwischen gestrichelte Linie; die linke streckt die Hand aus, die rechte ist abgewandt mit verschränkten Armen")
def abstand1():
    a = Fig((10, 22), an=(80, 88), af=(-12, -8), ln_=(4, 0), lf=(-4, 0), col=RED)
    b = Fig((38, 22), an=None, af=None, ln_=(4, 0), lf=(-4, 0), col=BLUE)
    # verschränkte Arme (Blick nach rechts, also abgewandt von a): Balken vor der Brust
    y = b.sh[1] + 3.2
    arms = limb([(b.hip[0] - 3.6, y), (b.hip[0] + 4.2, y)], 3.4, shade(BLUE, .85), False) + \
        circ((b.hip[0] + 4.4, y), 2, INK) + circ((b.hip[0] + 4.4, y), 1.5, SKIN)
    dash = ln("M24.5 4V36", 1.4, STONE_D).replace('stroke-linecap="round"', 'stroke-linecap="round" stroke-dasharray="2.6 2.8"')
    return "0 0 48 38", a.svg(face=a.eye()) + dash + b.svg(face=b.eye()) + arms


@zeichen("ABSTAND@2", "Abstand / vertraut sich nicht an: zwischen Personen besteht innerer Abstand",
         "Zwei Figuren Rücken an Rücken mit Abstand, dazwischen gestrichelte Linie; eine mit verschränkten Armen")
def abstand2():
    a = Fig((10, 22), an=(20, 30), af=(-12, -8), ln_=(4, 0), lf=(-4, 0), col=RED, n=-1)
    b = Fig((38, 22), an=None, af=None, ln_=(4, 0), lf=(-4, 0), col=BLUE)
    y = b.sh[1] + 3.2
    arms = limb([(b.hip[0] - 3.6, y), (b.hip[0] + 4.2, y)], 3.4, shade(BLUE, .85), False) + \
        circ((b.hip[0] + 4.4, y), 2, INK) + circ((b.hip[0] + 4.4, y), 1.5, SKIN)
    dash = ln("M24 4V36", 1.4, STONE_D).replace('stroke-linecap="round"', 'stroke-linecap="round" stroke-dasharray="2.6 2.8"')
    return "0 0 48 38", a.svg(face=a.eye()) + dash + b.svg(face=b.eye()) + arms


def rettende_hand(x, y, a=40, s=.6, A=3.1, col=BLUE, sleeve=WHITE, lang=14):
    """Hand von oben (haende.hand_faust, gespiegelt) umfasst bei (x, y) den senkrecht erhobenen Unterarm einer Figur;
    der Ärmel des Retters führt schräg nach rechts oben (Winkel a ab senkrecht)."""
    gx = 8.6
    griff = (stroke([(gx, -6.5), (gx, 7.5)], (A + 2 * O) / s, INK) + stroke([(gx, -6.5), (gx, 7.5)], A / s, col))
    wx, wy = x + gx * s, y
    r = math.radians(a)
    ex, ey = wx + math.sin(r) * lang, wy - math.cos(r) * lang
    arm = stroke([(wx, wy), (ex, ey)], 6.4, INK) + stroke([(wx, wy), (ex, ey)], 4.4, sleeve)
    return arm + H.place(H.hand_faust(sleeve, griff=griff, cuff_on=False), wx, wy, 0, s, True)


@zeichen("RETTUNG@1", "retten / heraufholen: Gott holt jemanden aus der Not herauf",
         "Figur bis zur Brust im Wasser streckt den Arm hoch; eine Hand von oben aus der Wolke fasst sie am Handgelenk")
def rettung1():
    a = Fig((11, 32), lean=-10, an=(100, 178), af=(110, 130), ln_=(0, 0), lf=(0, 0), col=BLUE)
    hand = a.arm_n[2]
    cloud = shape("M27 9Q25 3 31 3.6Q34 1 38 4Q43 3 43 8Q45 11 41 12H29Q25 12 27 9Z", "#FFFDF6", 1)
    h = rettende_hand(hand[0] - .2, hand[1] + 1.6, 40, .62, a.A, a.col, lang=16)
    return "0 0 44 40", a.svg(face=a.eye(dy=-1.2) + ln(f"M{f(a.head[0] + 1)} {f(a.head[1] + 2)}a1 1 0 0 1 2 0z", .8), hand_n=False) + wasser(0, 44, 28, 12, 5.5) + h + cloud


@zeichen("RETTUNG@2", "retten / heraufholen: Gott holt jemanden aus der Not herauf",
         "Eine Hand von oben zieht eine Figur am Arm aus den Wellen; die Figur ist schon halb aus dem Wasser, Pfeil nach oben")
def rettung2():
    a = Fig((12, 29), lean=-8, an=(100, 178), af=(120, 150), ln_=(-5, 5), lf=(12, 20), col=BLUE)
    hand = a.arm_n[2]
    cloud = shape("M27 9Q25 3 31 3.6Q34 1 38 4Q43 3 43 8Q45 11 41 12H29Q25 12 27 9Z", "#FFFDF6", 1)
    h = rettende_hand(hand[0] - .2, hand[1] + 1.6, 40, .62, a.A, a.col, lang=16)
    arrow = ln("M38 33V20M35 23l3-3 3 3", 1.6)
    return "0 0 44 40", a.svg(face=a.eye(dy=-1.2), hand_n=False) + wasser(0, 44, 31, 9, 5.5) + h + cloud + arrow


@zeichen("VERFOLGEN@1", "verfolgen / Verfolgung: jemand wird verfolgt",
         "Zwei rennende Figuren; die vordere (kleiner) blickt erschrocken zurück, die hintere grössere jagt ihr mit einem Speer nach")
def verfolgen1():
    v = Fig((37, 24), lean=20, an=(60, 150), af=(-55, -100), ln_=(72, 8), lf=(-40, -85), col=BLUE, s=.8, head=10).ground(37.4)
    p = Fig((15, 22), lean=16, an=(70, 110), af=(-55, -100), ln_=(72, 8), lf=(-40, -85), col=RED).ground(37.4)
    h = p.arm_n[2]
    spear = [(h[0] - 9, h[1] + 3.4), (h[0] + 9, h[1] - 3.4)]
    sp = stroke(spear, 3.6, INK) + stroke(spear, 1.5, BROWN) + shape(f"M{f(spear[1][0] - .6)} {f(spear[1][1] - 1.6)}l4 -.4-2.8 2.8z", "#D9DEE4", .8)
    return "0 0 50 38", motion(28.5, v.hip[1] - 6, 1, 3, 3, 3.4, 1.2) + v.svg(face=v.eye(dx=-1.6, dy=-.6)) + p.svg(face=p.eye(), front_extra="") + sp + \
        circ(h, p.A / 2 + .45 + O, INK) + circ(h, p.A / 2 + .45, SKIN)


@zeichen("STOLPERN@1", "zu Fall bringen / Anstoss: jemand stolpert über ein Hindernis und fällt",
         "Gehende Figur stösst mit dem vorderen Fuss an einen Stein, das hintere Bein fliegt hoch, der Oberkörper kippt nach vorn, Arme vorgestreckt")
def stolpern1():
    a = Fig((16, 24), lean=50, an=(110, 95), af=(95, 80), ln_=(18, -5), lf=(-70, -110), col=BLUE).ground(37.4)
    foot = a.leg_n[2]
    st = stein(foot[0] + 4.6, 37.6, 7, 4.6)
    hit = ln(f"M{f(foot[0] + 3)} {f(foot[1] - 4.6)}l-.6-1.8M{f(foot[0] + 5.4)} {f(foot[1] - 5.2)}v-2M{f(foot[0] + 7.8)} {f(foot[1] - 4.6)}l.8-1.6", 1, "#C0463A")
    ground = ln("M1 37.6H41", 1, STONE_D)
    return "0 0 42 38", ground + a.svg(face=a.eye(dy=.4)) + st + hit


@zeichen("STOLPERN@2", "zu Fall bringen / Anstoss: jemand stolpert über ein Hindernis und fällt",
         "Figur fällt über einen Stein vornüber, Arme ausgestreckt nach vorn unten, hinteres Bein in der Luft, wie Warnschild «Stolpergefahr»")
def stolpern2():
    a = Fig((15, 22), lean=62, an=(120, 100), af=(100, 85), ln_=(25, -10), lf=(-80, -120), col=BLUE).ground(37.4)
    foot = a.leg_n[2]
    st = stein(foot[0] + 5, 37.6, 8, 5.4)
    ground = ln("M1 37.6H41", 1, STONE_D)
    return "0 0 42 38", ground + a.svg(face=a.eye(dy=.4)) + st


def zeigefinger_lippen(x, y, s=.78):
    """Zeigende Hand (haende.hand_zeigend) senkrecht gedreht: Zeigefinger von unten über die Lippen bei (x, y)."""
    return H.place(H.hand_zeigend(), x + 2.3 * s, y + 20 * s - 3.2, -90, s)


def gesicht(cx, cy, r, augen="offen", mund="", col=SKIN):
    """Emoji-Gesicht (Hautton) mit Haar."""
    o = circ((cx, cy), r + O, INK) + circ((cx, cy), r, col)
    o += shape(f"M{f(cx - r * .98)} {f(cy - r * .1)}Q{f(cx - r)} {f(cy - r * 1.06)} {f(cx)} {f(cy - r)}Q{f(cx + r)} {f(cy - r * 1.06)} {f(cx + r * .98)} {f(cy - r * .1)}"
               f"Q{f(cx + r * .6)} {f(cy - r * .62)} {f(cx)} {f(cy - r * .6)}Q{f(cx - r * .6)} {f(cy - r * .62)} {f(cx - r * .98)} {f(cy - r * .1)}Z", "#4A3828", .9)
    ex, ey = r * .38, cy + r * .02
    if augen == "zu":
        o += ln(f"M{f(cx - ex - 1.6)} {f(ey)}q1.6 1.4 3.2 0M{f(cx + ex - 1.6)} {f(ey)}q1.6 1.4 3.2 0", 1.1)
    else:
        o += circ((cx - ex, ey), r * .1, INK) + circ((cx + ex, ey), r * .1, INK)
    return o


@zeichen("SCHWEIGEN@1", "schweigen: nicht reden, verstummen",
         "Gesicht im Emoji-Stil mit geschlossenem Mund, Zeigefinger senkrecht auf den Lippen wie 🤫")
def schweigen1():
    cx, cy, r = 17, 17, 14
    o = gesicht(cx, cy, r)
    o += ln(f"M{f(cx - 4.6)} {f(cy + 7.4)}q4.6 1.6 9.2 0", 1.2)
    o += zeigefinger_lippen(cx, cy + 6.6)
    return "0 0 34 38", o


@zeichen("SCHWEIGEN@2", "schweigen: nicht reden, verstummen",
         "Gesicht im Emoji-Stil, Mund als gerader Strich, Zeigefinger auf den Lippen, kleines «Psst»-Zeichen")
def schweigen2():
    cx, cy, r = 16, 16, 13.4
    o = gesicht(cx, cy, r, augen="zu")
    o += ln(f"M{f(cx - 5.2)} {f(cy + 7)}h3M{f(cx + 2.4)} {f(cy + 7)}h3", 1.2)
    o += zeigefinger_lippen(cx, cy + 7)
    return "0 0 36 38", o


@zeichen("UNTERORDNEN@1", "sich unterordnen: sich einer Ordnung oder Autorität fügen",
         "Figur verneigt sich tief vor einer stehenden Figur mit Stab auf einer erhöhten Stufe")
def unterordnen1():
    step = shape("M29 37.6V31H47V37.6Z", STONE, 1.1)
    b = Fig((37.6, 17), an=(15, 8), af=(-35, -70), ln_=(3, 0), lf=(-3, 0), n=-1, col=RED, s=.8).ground(31.2)
    hx = b.arm_f[2][0]
    staff = ln(f"M{f(hx)} 31V{f(b.head[1] - 3)}", 3.6) + ln(f"M{f(hx)} 31V{f(b.head[1] - 3)}", 1.6, BROWN)
    a = Fig((9, 24), lean=75, an=(30, 15), af=(20, 8), ln_=(-4, 2), lf=(8, 2), col=BLUE, head=95).ground(37.4)
    return "0 0 48 38", ln("M0 37.6H29", 1, STONE_D) + step + a.svg() + b.svg(face=b.eye(), behind=staff)


@zeichen("UNTERORDNEN@2", "sich unterordnen: sich einer Ordnung oder Autorität fügen",
         "Kniende Figur mit gesenktem Kopf vor einer stehenden Figur mit Krone auf einer Stufe")
def unterordnen2():
    step = shape("M26 37.6V31H46V37.6Z", STONE, 1.1)
    b = Fig((36, 17.4), an=(20, 10), af=(-20, -10), ln_=(3, 0), lf=(-3, 0), n=-1, col=RED, s=.8).ground(31.2)
    hx, hy, r = b.head[0], b.head[1], b.R
    crown = shape(f"M{f(hx - 3.6)} {f(hy - r + .6)}l-.6-4.4 2.2 2 2-3 2 3 2.2-2-.6 4.4z", GOLD, .8)
    a = Fig((10, 28), lean=40, an=(60, 40), af=(50, 30), ln_=(88, 0), lf=(80, 0), col=BLUE, head=75).ground(37.4)
    return "0 0 46 38", ln("M0 37.6H26", 1, STONE_D) + step + a.svg() + b.svg(face=b.eye()) + crown


@zeichen("STREIT@1", "streiten / Streit: miteinander streiten, Zank",
         "Zwei Köpfe im Profil gegeneinander mit offenem Mund, darüber eine gezackte Sprechblase mit rotem Zornzeichen")
def streit1():
    o = profilkopf(9.5, 19, 7.4, 1, col=BLUE) + profilkopf(38.5, 19, 7.4, -1, col=RED)
    o += sprechblase(24, 8.6, 17, 14, zack=True, fill="#FFF3C4")
    o += ln("M20.6 5.4l2.2 2.2M27.4 5.4l-2.2 2.2M20.6 11.8l2.2-2.2M27.4 11.8l-2.2-2.2", 1.7, "#C0463A")
    return "0 0 48 38", o


@zeichen("STREIT@2", "streiten / Streit: miteinander streiten, Zank",
         "Zwei Figuren stehen sich gegenüber, zeigen mit dem Finger aufeinander, gezackte Blase mit Blitz dazwischen")
def streit2():
    a = Fig((10, 22), lean=6, an=(95, 92), af=(-30, 10), ln_=(6, 0), lf=(-6, 0), col=BLUE)
    b = Fig((38, 22), lean=6, an=(95, 92), af=(-30, 10), ln_=(6, 0), lf=(-6, 0), col=RED, n=-1)
    mouth = lambda F: ln(f"M{f(F.head[0] + 1.4 * F.n)} {f(F.head[1] + 1.8)}h{f(2 * F.n)}", 1)
    bub = sprechblase(24, 7, 14, 11, zack=True, fill="#FFF3C4")
    bolt = shape("M25 2L21.6 7.6H24.2L22.6 12L27 6H24.2L26 2Z", "#C0463A", .7)
    return "0 0 48 38", a.svg(face=a.eye() + mouth(a)) + b.svg(face=b.eye() + mouth(b)) + bub + bolt


@zeichen("TOETEN@1", "töten / Mord: einen Menschen töten",
         "Grosse Figur holt mit dem Schwert aus über einer am Boden liegenden Figur, die abwehrend den Arm hebt")
def toeten1():
    v = Fig((18, 34.4), lean=90, an=(150, 170), af=(170, 180), ln_=(-90, -90), lf=(-80, -100), col=BLUE, s=.8, n=-1)
    a = Fig((37, 21), lean=4, an=(120, 135), af=(30, 10), ln_=(22, 0), lf=(-18, 0), col=RED, n=-1, s=.9).ground(37.4)
    sw = schwert(a.arm_n[2][0], a.arm_n[2][1], -40, 9.5)
    return "0 0 48 38", ln("M1 37.6H47", 1, STONE_D) + v.svg(face=v.eye()) + a.svg(face=a.eye()) + sw + \
        circ(a.arm_n[2], a.A / 2 + .45 + O, INK) + circ(a.arm_n[2], a.A / 2 + .45, SKIN)


@zeichen("TAUFE@1", "taufen: mit Wasser taufen",
         "Zwei Figuren stehen bis zur Hüfte im Wasser; die rechte hält die Hand über den Kopf der linken, Wasser tropft darauf; die linke faltet die Hände")
def taufe1():
    a = Fig((13, 32.5), lean=6, an=(70, 160), af=(60, 155), ln_=(4, 0), lf=(-4, 0), col=WHITE, s=.74, head=12)
    b = Fig((27, 24), lean=2, an=(108, 135), af=(-20, -10), ln_=(4, 0), lf=(-4, 0), col=BROWN, n=-1)
    hb = b.arm_n[2]
    drops = "".join(shape(f"M{f(x)} {f(y)}q1.2 1.7 0 2.4q-1.2-.7 0-2.4z", WATER, .6) for x, y in ((hb[0] - 2.4, hb[1] + 2.2), (hb[0] - .2, hb[1] + 2.8)))
    return "0 0 40 38", a.svg(face=a.eye()) + b.svg(face=b.eye()) + drops + wasser(0, 40, 29.4, 8.6, 5)


@zeichen("TAUFE@2", "taufen: mit Wasser taufen",
         "Figur bis zur Hüfte im Fluss, eine zweite Figur hält die Hand über ihren Kopf, Wasser strömt herab; Wellen")
def taufe2():
    a = Fig((14, 28), lean=10, an=(70, 160), af=(60, 155), ln_=(4, 0), lf=(-4, 0), col=WHITE, s=.86, head=22)
    b = Fig((31, 25), lean=6, an=(115, 120), af=(-20, -10), ln_=(4, 0), lf=(-4, 0), col=BROWN, n=-1)
    hb = b.arm_n[2]
    stream = "".join(ln(f"M{f(hb[0] + dx)} {f(hb[1] + 2.4)}v{f(3.4)}", 1.2, WATER) for dx in (-1.8, 0, 1.8))
    return "0 0 44 38", a.svg(face=a.eye()) + b.svg(face=b.eye()) + stream + wasser(0, 44, 28.4, 9.6, 5.5)


@zeichen("GASTFREUNDSCHAFT@1", "Gastfreundschaft / aufnehmen: Gäste aufnehmen, Reisende beherbergen",
         "Offene Haustür; der Gastgeber in der Tür lädt mit offener Hand ein, ein Gast mit Wanderstab tritt heran")
def gast1():
    house = shape("M24 37.6V12L35 4 46 12V37.6Z", "#D8B48A", 1.1) + shape("M28.4 37.6V20.6Q28.4 17.4 31.6 17.4H38.4Q41.6 17.4 41.6 20.6V37.6Z", "#4A3828", 1) + \
        shape("M41.6 37.6V17.8L45 16.4V37.6Z", "#A97C4A", .9)
    h = Fig((35, 25.4), an=(40, 75), af=(-10, -5), ln_=(3, 0), lf=(-3, 0), n=-1, col=GREEN, s=.72).ground(37.4)
    hand = h.hand_at(H.place(H.hand_empfangend(GREEN, cuff_on=False), 0, 0, 0, 1, False), s=.34)
    hand = H.place(H.hand_empfangend(GREEN, cuff_on=False), h.arm_n[2][0], h.arm_n[2][1], 0, .34, True)
    g = Fig((12, 22), lean=4, an=(40, 30), af=(-20, -10), ln_=(26, 4), lf=(-24, -6), col=BLUE).ground(37.4)
    staff = ln(f"M{f(g.arm_n[2][0] + 1)} {f(g.arm_n[2][1] - 9)}L{f(g.arm_n[2][0] + 3)} 37.4", 3.4) + \
        ln(f"M{f(g.arm_n[2][0] + 1)} {f(g.arm_n[2][1] - 9)}L{f(g.arm_n[2][0] + 3)} 37.4", 1.6, BROWN)
    smile = ln(f"M{f(h.head[0] - .4)} {f(h.head[1] + 1.2)}q-1.2 1.2 -2.6 .2", .8)
    return "0 0 48 38", house + h.svg(face=h.eye() + smile, hand_n=hand) + staff + g.svg(face=g.eye())


@zeichen("UMSTURZ@1", "umstürzen / zugrunde gehen: eine Stadt wird umgestürzt, geht unter",
         "Stadt mit Mauer und Türmen kippt und bricht: ein Turm stürzt schräg um, Steine fallen, Staubwolke am Boden")
def umsturz1():
    wall = shape("M2 37.6V24H6V22H9V24H12V22H15V24H18V37.6Z", "#D8B48A", 1.1) + shape("M8 37.6V31Q10 29 12 31V37.6Z", "#4A3828", .8)
    tower1 = f'<g transform="rotate(-6 10 37)">' + shape("M3 24V12H4.6V10H6.6V12H8.6V10H10.6V12H12.6V24Z", "#C9A574", 1) + "</g>"
    tower2 = f'<g transform="rotate(32 24 37)">' + shape("M20 37.6V9H21.8V6.6H24V9H26V6.6H28.2V9H30V37.6Z", "#D8B48A", 1.1) + \
        ln("M23 15l2 3-1.4 3 2 3", .9) + shape("M23.4 30V26Q25 24.4 26.6 26V30Z", "#4A3828", .7) + "</g>"
    crack = ln("M14 27l-2 3 1.6 2.6-1.4 3", 1)
    stones = shape("M38 20l3.2-1 1 3-3 1z", "#C9A574", .9) + shape("M42 27l2.6.4-.4 2.6-2.6-.4z", "#C9A574", .9) + shape("M35 14l2.4-.6.8 2.4-2.4.6z", "#C9A574", .9)
    dust = shape("M18 37.6Q17 33.4 21 33.6Q23 30.6 27 33Q31 31.4 32 35Q36 34.4 36 37.6Z", "#E4DCCB", .9)
    return "0 0 46 38", tower1 + wall + crack + tower2 + stones + dust


@zeichen("UMSTURZ@2", "umstürzen / zugrunde gehen: eine Stadt wird umgestürzt, geht unter",
         "Zwei Stadttürme mit Rissen brechen auseinander und kippen nach aussen, Trümmer fallen")
def umsturz2():
    t1 = f'<g transform="rotate(-18 12 37)">' + shape("M5 37.6V12H7V9.4H9.4V12H11.6V9.4H14V12H16V37.6Z", "#D8B48A", 1.1) + ln("M10 16l2 3-1.6 3 1.8 3", .9) + \
        shape("M8.4 26V22.4Q10.5 20.6 12.6 22.4V26Z", "#4A3828", .7) + "</g>"
    t2 = f'<g transform="rotate(20 32 37)">' + shape("M26 37.6V8H28V5.4H30.4V8H32.6V5.4H35V8H37V37.6Z", "#C9A574", 1.1) + ln("M31 13l-2 3 1.6 3-1.8 3", .9) + \
        shape("M29.4 24V20.4Q31.5 18.6 33.6 20.4V24Z", "#4A3828", .7) + "</g>"
    stones = shape("M20 9l3-1 1 3-3 1z", "#B89868", .9) + shape("M22.4 17l2.6.4-.4 2.6-2.6-.4z", "#B89868", .9) + shape("M19 24l2.4-.4.4 2.4-2.4.4z", "#B89868", .9)
    dust = shape("M6 37.6Q5 34 9 34Q11 31 16 33Q20 30.6 24 33Q29 31 31 34Q36 33 37 37.6Z", "#E4DCCB", .9)
    return "0 0 44 38", t1 + t2 + stones + dust


def kette(x, y, a=0, n=2):
    o = f'<g transform="translate({f(x)} {f(y)}) rotate({f(a)})">'
    for i in range(n):
        o += f'<rect x="{f(i * 4.2 - 2.6)}" y="-1.6" width="5.2" height="3.2" rx="1.6" fill="none" stroke="{INK}" stroke-width="2.4"/>' \
             f'<rect x="{f(i * 4.2 - 2.6)}" y="-1.6" width="5.2" height="3.2" rx="1.6" fill="none" stroke="#9AA0A8" stroke-width="1.1"/>'
    return o + "</g>"


@zeichen("LOESEN@1", "loskaufen / befreien: jemand wird gegen Lösegeld freigekauft",
         "Figur reckt beide Arme hoch, an den Handgelenken offene Fesseln, die Kette gesprengt; daneben legt eine Hand Münzen als Lösegeld hin")
def loesen1():
    a = Fig((31, 22), an=(140, 160), af=(140, 160), ln_=(6, 4), lf=(6, 4), col=BLUE, s=.92, front=True).ground(37.4)
    cuffs, links = "", ""
    for arm, k in ((a.arm_n, 1), (a.arm_f, -1)):
        p = add(arm[1], (arm[2][0] - arm[1][0], arm[2][1] - arm[1][1]), .45)
        cuffs += f'<rect x="{f(p[0] - 2.5)}" y="{f(p[1] - 1.3)}" width="5" height="2.6" rx=".8" fill="#9AA0A8" stroke="{INK}" stroke-width=".9"/>'
        links += kette(p[0] + k * 3.4, p[1] + 3.4, k * 60, 1)
    burst = ln(f"M{f(a.head[0] - 9)} {f(a.head[1] - 7)}l-1.4-1.4M{f(a.head[0] + 9)} {f(a.head[1] - 7)}l1.4-1.4M{f(a.head[0])} {f(a.head[1] - 7.6)}v-2", 1.2, GOLD)
    coins = "".join(H.muenze(x, y, 2.6) for x, y in ((5, 35), (10.4, 35), (7.7, 31)))
    hand = H.place(H.hand_gebend(), 0.5, 21.5, 25, .6)
    face = a.eye(dx=-1.4, dy=-.6) + a.eye(dx=1.4, dy=-.6) + ln(f"M{f(a.head[0] - 1.6)} {f(a.head[1] + 1.4)}q1.6 1.6 3.2 0", .9)
    return "0 0 44 38", a.svg(face=face) + cuffs + links + burst + coins + hand


@zeichen("LOESEN@2", "loskaufen / befreien: jemand wird gegen Lösegeld freigekauft",
         "Gesprengte Kette (Glieder brechen auseinander) über einer Waagschale mit Goldmünzen")
def loesen2():
    k = kette(5, 10, 0, 3) + kette(30, 10, 0, 3)
    burst = ln("M21.5 3v3M17.6 4.4l1.6 2.4M25.4 4.4l-1.6 2.4M21.5 17v-3M17.6 15.6l1.6-2.4M25.4 15.6l-1.6-2.4", 1.4, GOLD)
    coins = "".join(H.muenze(x, y, 3) for x, y in ((15, 34), (21.5, 34), (28, 34), (18.2, 30), (24.8, 30), (21.5, 26)))
    return "0 0 44 38", k + burst + coins


def grab(x, y, w=26, h=22):
    return (shape(f"M{f(x - w / 2)} {f(y)}V{f(y - h * .55)}Q{f(x - w / 2)} {f(y - h)} {f(x)} {f(y - h)}Q{f(x + w / 2)} {f(y - h)} {f(x + w / 2)} {f(y - h * .55)}V{f(y)}Z", "#C2B8A4", 1.1))


@zeichen("AUFERSTEHUNG@1", "Auferstehung / auferstehen: Tote stehen auf, werden auferweckt",
         "Felsengrab mit weggerolltem Stein; aus der dunklen Öffnung steigt eine helle Figur mit erhobenen Armen, Lichtstrahlen")
def aufer1():
    o = grab(16, 37.6, 30, 33)
    o += shape("M7 37.6V22Q7 12.6 16 12.6Q25 12.6 25 22V37.6Z", "#3A3028", 1)
    a = Fig((16, 33), an=(135, 160), af=(135, 160), ln_=None, lf=None, col=WHITE, s=.8, legs=False, front=True)
    hx, hy = a.head
    rays = "".join(ln(f"M{f(hx + math.sin(math.radians(t)) * 6.8)} {f(hy - math.cos(math.radians(t)) * 6.8)}l{f(math.sin(math.radians(t)) * 2.4)} {f(-math.cos(math.radians(t)) * 2.4)}", 1.4, GOLD) for t in (-30, 0, 30))
    st = circ((37.4, 31), 6.2 + O, INK) + circ((37.4, 31), 6.2, STONE) + ln("M34.2 27.6q3 2 2.4 6", .8, STONE_D)
    face = a.eye(dx=-1.4, dy=-.4) + a.eye(dx=1.4, dy=-.4) + ln(f"M{f(hx - 1.4)} {f(hy + 1.6)}q1.4 1.2 2.8 0", .8)
    return "0 0 46 38", o + a.svg(face=face) + rays + st + ln("M0 37.6H46", 1, STONE_D)


@zeichen("AUFERSTEHUNG@2", "Auferstehung / auferstehen: Tote stehen auf, werden auferweckt",
         "Felsengrab mit weggerolltem Stein; ein goldener Pfeil steigt aus der Öffnung empor, Lichtstrahlen")
def aufer2():
    o = grab(16, 37.6, 28, 26)
    o += shape("M9 37.6V28Q9 21 16 21Q23 21 23 28V37.6Z", "#3A3028", 1)
    arrow = ln("M16 35V6M10 12l6-6 6 6", 4.4) + ln("M16 35V6M10 12l6-6 6 6", 2.4, GOLD)
    st = circ((36, 31), 6.4 + O, INK) + circ((36, 31), 6.4, STONE) + ln("M32.8 27.6q3 2 2.4 6", .8, STONE_D)
    return "0 0 44 38", o + arrow + st + ln("M0 37.6H44", 1, STONE_D)


@zeichen("SCHLAFEN@1", "schlafen: jemand schläft",
         "Liegender Kopf mit geschlossenen Augen auf einem Kissen, zugedeckt, darüber «Zzz» wie 💤")
def schlafen1():
    pillow = shape("M2 30Q1 23 8 22.6H16Q21 23 20 30Z", "#FFFDF6", 1)
    blanket = shape("M14 37.6V29Q14 25.6 18 25.6H44V37.6Z", "#7E9AC4", 1.1) + ln("M18 29.6H44", .8, "#5E7FA8")
    cx, cy, r = 12.6, 21, 7.4
    head = circ((cx, cy), r + O, INK) + circ((cx, cy), r, SKIN) + \
        shape(f"M{f(cx - r * .96)} {f(cy + 1.6)}Q{f(cx - r * 1.1)} {f(cy - r * 1)} {f(cx + 1)} {f(cy - r)}Q{f(cx + r * .3)} {f(cy - r * .4)} {f(cx - r * .3)} {f(cy - r * .1)}Q{f(cx - r * .7)} {f(cy + .4)} {f(cx - r * .96)} {f(cy + 1.6)}Z", "#4A3828", .8) + \
        ln(f"M{f(cx + .4)} {f(cy + .4)}q1.4 1.2 2.8 0M{f(cx + 4)} {f(cy - .2)}q1 1 2 .2", 1) + ln(f"M{f(cx + 2.2)} {f(cy + 3.8)}h1.6", .8)
    return "0 0 46 38", pillow + head + blanket + zzz(26, 14, 1.25)


@zeichen("SCHLAFEN@2", "schlafen: jemand schläft",
         "Figur liegt ausgestreckt auf einer Matte, Kopf auf dem Kissen, darüber grosses «Zzz»")
def schlafen2():
    mat = shape("M2 37.6V33H44V37.6Z", "#C9963E", 1)
    pillow = shape("M3 33Q2 28.6 7 28.4H12Q15 28.6 14.6 33Z", "#FFFDF6", .9)
    body = shape("M11 33V28.4Q12 25.4 17 25.4H40Q44 25.6 44 29.6V33Z", "#7E9AC4", 1.1)
    head = circ((9.4, 25.6), 5 + O, INK) + circ((9.4, 25.6), 5, SKIN) + ln("M10 25.4q1.2 1 2.4 0", .9)
    return "0 0 46 38", mat + pillow + body + head + zzz(20, 16, 1.4)


@zeichen("VERSTORBEN@1", "gestorben / Verstorbener: jemand ist gestorben, ein Leichnam",
         "Ganz in Leinentücher gewickelter Körper mit Binden, auch der Kopf verhüllt, auf einer Bahre ohne Kissen")
def verstorben1():
    bier = shape("M2 28.6H44V31H2Z", BROWN, 1) + ln("M6 31V36.6M40 31V36.6", 2.4) + ln("M6 31V36.6M40 31V36.6", 1, BROWN)
    body = shape("M5 28.6Q3.4 28.6 3.4 25.4Q3.4 20.2 8.6 20.2Q12.4 20.2 13.2 22.4Q20 21.6 30 22Q41 22.4 42 25.6Q42.4 28.6 40 28.6Z", "#EDE6D6", 1.1)
    bands = ln("M8.2 20.6L6.6 28.4M11.6 21.4L10.6 28.4M17 22L16.6 28.4M23 22L22.8 28.4M29 22.2V28.4M35 22.8L35.4 28.4", .8, "#A89C84")
    return "0 0 46 38", bier + body + bands


@zeichen("VERSTORBEN@2", "gestorben / Verstorbener: jemand ist gestorben, ein Leichnam",
         "Verhüllter Körper auf einer Bahre, von zwei Personen getragen (Trauerzug)")
def verstorben2():
    bier = shape("M4 22.6H42V24.6H4Z", BROWN, 1)
    body = shape("M7 22.6Q5.6 22.6 5.6 19.6Q5.6 15.4 10 15.4Q13 15.4 13.8 17.2Q22 16.6 30 17Q39 17.4 39.8 20Q40 22.6 38 22.6Z", "#EDE6D6", 1.1)
    bands = ln("M10 15.8L8.6 22.4M17 17.2V22.4M24 17.2V22.4M31 17.4V22.4", .8, "#A89C84")
    a = Fig((8, 26), an=(140, 175), af=(150, 175), ln_=(14, 0), lf=(-14, 0), col="#6A6A70", s=.62)
    b = Fig((38, 26), an=(140, 175), af=(150, 175), ln_=(14, 0), lf=(-14, 0), col="#6A6A70", s=.62, n=-1)
    return "0 0 46 38", a.svg() + b.svg() + bier + body + bands


def waage(x, y, s=1, tilt=0):
    o = f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">'
    o += ln("M0 0V14M-4 14h8", 1.6) + ln("M-9 1H9", 1.6)
    for sx in (-9, 9):
        o += ln(f"M{sx} 1l-3 6M{sx} 1l3 6", .8) + shape(f"M{sx - 4} 7h8q-1 3.4-4 3.4t-4-3.4z", GOLD, .9)
    return o + circ((0, -.2), 1.4, GOLD) + "</g>"


@zeichen("BESONNEN@1", "besonnen / beherrscht: sich selbst im Griff haben, massvoll und überlegt",
         "Ruhig stehende Figur mit geschlossenen Augen, eine Hand an der Brust; daneben eine ausgeglichene Waage")
def besonnen1():
    a = Fig((13, 22), an=(150, 40), af=(-10, -8), ln_=(3, 0), lf=(-3, 0), col=BLUE, s=.94).ground(37.4)
    a.arm_n = [a.sh, (a.sh[0] + 4, a.sh[1] + 5), (a.sh[0] + .6, a.sh[1] + 2.4)]
    face = ln(f"M{f(a.head[0] - 2.6)} {f(a.head[1] - .2)}q1 .8 2 0M{f(a.head[0] + .6)} {f(a.head[1] - .2)}q1 .8 2 0", .8) + \
        ln(f"M{f(a.head[0] - 1.2)} {f(a.head[1] + 2)}q1.2 .8 2.4 0", .8)
    return "0 0 46 38", a.svg(face=face) + waage(33.5, 18, 1)


@zeichen("SANFTMUT@1", "Sanftmut / sanftmütig: sanft, ohne Gewalt und Härte",
         "Offene Hand (wie 🫴) trägt behutsam eine kleine weisse Taube")
def sanftmut1():
    hand = H.place(H.hand_empfangend(), 7, 27, 0, 1.4)
    dove = (shape("M14 18.6Q13 12.6 18.6 11.4Q20.4 6.6 24.6 7.8Q27.4 8.8 26.6 11.6L29.4 12.4L26.4 13.4Q26.4 19 20 20.4Q16 20.8 14 18.6Z", "#FFFDF6", 1.1)
            + shape("M12 15.4Q8.6 13 6 13.6Q9 17.4 14.4 18Z", "#FFFDF6", 1)
            + shape("M17.4 14.6Q20.6 11.4 24 14.8Q22 18.4 17.4 14.6Z", "#E6E0D2", .8)
            + circ((24.4, 10.6), .8, INK))
    return "0 0 40 36", hand + f'<g transform="translate(-1 3.4)">{dove}</g>'


@zeichen("FREUNDLICH@1", "freundlich / gütig: freundlich und gütig mit anderen umgehen",
         "Zwei Personen; die eine wendet sich der anderen lächelnd mit offener, einladender Hand zu, beide lächeln")
def freundlich1():
    a = Fig((12, 22), lean=6, an=(45, 80), af=(-12, -8), ln_=(5, 0), lf=(-5, 0), col=BLUE).ground(37.4)
    b = Fig((36, 22), an=(-10, -6), af=(10, 6), ln_=(4, 0), lf=(-4, 0), col=RED, n=-1).ground(37.4)
    sa = ln(f"M{f(a.head[0] + .2)} {f(a.head[1] + 1.4)}q1.6 1.6 3.4 .2", .9) + a.eye(dx=1.9, dy=-1.2)
    sb = ln(f"M{f(b.head[0] - .2)} {f(b.head[1] + 1.4)}q-1.6 1.6 -3.4 .2", .9) + b.eye(dx=1.9, dy=-1.2)
    hand = a.hand_at(H.hand_empfangend(BLUE, cuff_on=False), s=.42)
    return "0 0 48 38", a.svg(face=sa, hand_n=hand) + b.svg(face=sb)


# ------------------------------------------------------------------------------------------------ Auswahl
FINAL = {}  # Name ohne @ → Fassung, wird nach den Tests gesetzt


def build(name):
    vb, svg = Z[name][0]()
    return vb, svg


def main():
    args = sys.argv[1:]
    if "--entwuerfe" in args:
        out = pathlib.Path(args[args.index("--entwuerfe") + 1])
        nur = args[args.index("--nur") + 1].split(",") if "--nur" in args else None
        e = {}
        for k, (fn, bed, gez) in Z.items():
            if nur and k not in nur and k.split("@")[0] not in nur:
                continue
            vb, svg = fn()
            e[f"FIG-ZEICHEN-{k}"] = {"vb": vb, "svg": svg, "bedeutung": bed, "gezeichnet": gez}
        out.write_text(json.dumps(e, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{len(e)} Entwürfe → {out}")
        return
    res = {}
    for base, ver in FINAL.items():
        vb, svg = build(f"{base}@{ver}")
        res[f"FIG-ZEICHEN-{base}"] = {"vb": vb, "svg": svg}
    p = pathlib.Path(__file__).resolve().parent / "bildsymbole_daten/ueberarbeitet/handlung.json"
    p.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(res)} Zeichen → {p}")


if __name__ == "__main__":
    main()
