#!/usr/bin/env python3
"""Pilot «strukturierte Inhalte mit Bild-KI» (docs/BILDSTIL.md: Szenen werden gemalt, Masse und Strukturen kommen aus Daten).

Drei Versuche, je in zwei Fassungen:
  A  rein aus Daten gezeichnet (SVG, exakt, Aquarell-Anmutung mit SVG-Filtern)
  B  Hybrid: das Bildmodell malt eine Aquarell-Unterlage nach einer exakten Vorlage (bzw. kleine Vignetten);
     darüber liegt die exakte Datenebene (Orte, Masse, Beschriftung, Text) als SVG.

  karte          Johannes 2: Kana → Kafarnaum (hinab, 2,12) → Jerusalem (hinauf, 2,13), mit Höhenprofil
  stiftshuette   Exodus 26–27: Vorhof, Zelt, Heiliges/Allerheiligstes, Geräte, in Ellen, isometrisch
  seligpreisungen Matthäus 5,3–10: Aufbau (acht Glieder, Rahmen 5,3 und 5,10, Gegenwart/Zukunft) mit gemalten Vignetten

  python3 pilot/struktur/struktur.py vorlagen     # exakte SVG, Vorlagen-PNG fürs Bildmodell, auftraege.json
  python3 pilot/struktur/struktur.py zusammen <lauf-ordner>   # gemalte Unterlagen + Datenebene → ergebnis/*.svg, kontaktbogen.html
Malen: pilot/struktur/struktur_gen.py in der Action «bildpilot-struktur».

Daten: Küste, Seen und Jordan aus Natural Earth 1:10 Mio. (gemeinfrei, levante-naturalearth.json). Ortslagen gerundet (±1–2 km);
Kana ist umstritten (Chirbet Kana oder Kafr Kanna). Höhen gerundet. Masse der Stiftshütte nach Ex 25–27 und 30 (Ellen);
Lage der Geräte im Vorhof und Teilung 20 : 10 im Zelt sind Rekonstruktion (R). KI-Entwurf (Claude) vom 2026-10-28 auf Wunsch von
Andi Neck; keine fachliche Prüfung.
"""
import base64
import html
import json
import math
import pathlib
import sys

HIER = pathlib.Path(__file__).resolve().parent
REPO = HIER.parent.parent
VOR = HIER / "vorlagen"
ERG = HIER / "ergebnis"
INK, PAPER = "#4A4D45", "#FBF8F1"
FONT = "font-family=\"Georgia, 'Times New Roman', serif\""
SANS = "font-family=\"system-ui, sans-serif\""

# ------------------------------------------------------------------ gemeinsame Aquarell-Filter (Fassung A)

FILTER = """<defs>
<filter id="nass" x="-10%" y="-10%" width="120%" height="120%">
  <feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="3" seed="7" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="7" xChannelSelector="R" yChannelSelector="G" result="d"/>
  <feGaussianBlur in="d" stdDeviation="0.8" result="b"/>
  <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="3" result="k"/>
  <feColorMatrix in="k" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -0.9 1.25" result="km"/>
  <feComposite in="b" in2="km" operator="in"/>
</filter>
<filter id="linie"><feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="2" seed="11" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="2.2" xChannelSelector="R" yChannelSelector="G"/></filter>
<marker id="pfeil" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
  <path d="M0,1 L9,5 L0,9" fill="none" stroke="#8A3B2A" stroke-width="1.6"/></marker>
</defs>"""


def svg_doc(w, h, inhalt, unterlage=None):
    u = f'<image href="{unterlage}" x="0" y="0" width="{w}" height="{h}" preserveAspectRatio="none"/>' if unterlage else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{FILTER}'
            f'<rect width="{w}" height="{h}" fill="{PAPER}"/>{u}{inhalt}</svg>')


# ------------------------------------------------------------------ 1. Karte Johannes 2

GEBIET = (34.60, 31.40, 36.00, 33.10)   # lon0, lat0, lon1, lat1
KW = 600
KOSLAT = math.cos(math.radians(32.3))
KH = round(KW * (GEBIET[3] - GEBIET[1]) / ((GEBIET[2] - GEBIET[0]) * KOSLAT))

ORTE = {  # (lon, lat, Höhe m, Bezeichnung, Hinweis)
    "Kana": (35.293, 32.783, 200, "Kana", "Lage umstritten: Chirbet Kana (hier) oder Kafr Kanna, 6 km südöstlich (R)"),
    "Kafarnaum": (35.573, 32.880, -200, "Kafarnaum", "am Nordufer des Sees Gennesaret"),
    "Jerusalem": (35.235, 31.778, 750, "Jerusalem", "Tempelberg"),
    "Nazaret": (35.297, 32.700, 350, "Nazaret", "zur Orientierung"),
}
WEG = [("Kana", "Kafarnaum", "JHN.2.12", "hinab"), ("Kafarnaum", "Jerusalem", "JHN.2.13", "hinauf")]


def proj(lon, lat):
    return ((lon - GEBIET[0]) / (GEBIET[2] - GEBIET[0]) * KW, (GEBIET[3] - lat) / (GEBIET[3] - GEBIET[1]) * KH)


def pfad(pts, zu=False):
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in (proj(*p) for p in pts)) + (" Z" if zu else "")


def karte_teile():
    geo = json.loads((HIER / "levante-naturalearth.json").read_text())
    # Meer: Küstenlinie (Nord→Süd sortiert) mit dem Westrand schliessen
    teile = sorted(geo["coastline:coast"], key=lambda ln: -ln[0][1])   # Abschnitte von Nord nach Süd, je in Laufrichtung
    kuste = [p for ln in teile for p in ln]
    kuste = [p for p in kuste if GEBIET[1] - .3 <= p[1] <= GEBIET[3] + .3]
    meer = [[GEBIET[0] - .1, GEBIET[3] + .3]] + kuste + [[GEBIET[0] - .1, GEBIET[1] - .3]]
    seen = [ln for k in ("lakes:Sea of Galilee", "lakes:Dead Sea") for ln in geo.get(k, [])]
    jordan = geo.get("rivers_lake_centerlines:Jordan", [])
    return meer, seen, jordan


def karte_vorlage():
    """Exakte Vorlage fürs Bildmodell: nur Land, Wasser, Fluss – keine Schrift."""
    meer, seen, jordan = karte_teile()
    t = [f'<path d="{pfad(meer, True)}" fill="#9DB8C8"/>']
    t += [f'<path d="{pfad(s, True)}" fill="#9DB8C8"/>' for s in seen]
    t += [f'<path d="{pfad(j)}" fill="none" stroke="#7FA2B5" stroke-width="2.4"/>' for j in jordan]
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {KW} {KH}" width="{KW}" height="{KH}"><rect width="{KW}" height="{KH}" fill="#F3EBDA"/>{"".join(t)}</svg>'


def karte_daten(mit_grund):
    """Datenebene: Orte, Weg mit Versangabe, Beschriftung, Massstab, Höhenprofil. mit_grund: auch Land/Wasser zeichnen (Fassung A)."""
    meer, seen, jordan = karte_teile()
    t = []
    if mit_grund:
        t.append(f'<g filter="url(#nass)" opacity=".85"><path d="{pfad(meer, True)}" fill="#A9C3CF"/>'
                 + "".join(f'<path d="{pfad(s, True)}" fill="#A9C3CF"/>' for s in seen)
                 + '</g>')
        t += [f'<path d="{pfad(j)}" fill="none" stroke="#7FA2B5" stroke-width="1.8" filter="url(#linie)"/>' for j in jordan]
        t.append(f'<text x="{proj(34.75, 32.0)[0]:.0f}" y="{proj(34.75, 32.0)[1]:.0f}" {FONT} font-style="italic" font-size="16" fill="#5F7F90" text-anchor="middle">Grosses Meer</text>')
        t.append(f'<text x="{proj(35.70, 32.84)[0]:.0f}" y="{proj(35.70, 32.84)[1]:.0f}" {FONT} font-style="italic" font-size="12" fill="#5F7F90">See</text>')
        t.append(f'<text x="{proj(35.62, 31.50)[0]:.0f}" y="{proj(35.62, 31.50)[1]:.0f}" {FONT} font-style="italic" font-size="12" fill="#5F7F90">Salzmeer</text>')
        t.append(f'<text x="{proj(35.60, 32.35)[0]:.0f}" y="{proj(35.60, 32.35)[1]:.0f}" {FONT} font-style="italic" font-size="12" fill="#5F7F90" transform="rotate(80 {proj(35.60, 32.35)[0]:.0f} {proj(35.60, 32.35)[1]:.0f})">Jordan</text>')
    for a, b, ref, wort in WEG:
        (x0, y0), (x1, y1) = proj(*ORTE[a][:2]), proj(*ORTE[b][:2])
        dx, dy = x1 - x0, y1 - y0
        ln = math.hypot(dx, dy)
        k = 22 / ln
        mx, my = (x0 + x1) / 2 - dy * 0.12, (y0 + y1) / 2 + dx * 0.12
        t.append(f'<path d="M{x0 + dx * k:.1f},{y0 + dy * k:.1f} Q{mx:.1f},{my:.1f} {x1 - dx * k:.1f},{y1 - dy * k:.1f}" fill="none" stroke="#8A3B2A" '
                 f'stroke-width="2.2" stroke-dasharray="7 5" marker-end="url(#pfeil)"/>')
        lx, ly = (mx + 10, my) if dx < 0 else (mx, my - 12)
        t.append(f'<text x="{lx:.0f}" y="{ly:.0f}" {SANS} font-size="13" fill="#8A3B2A" text-anchor="{"start" if dx < 0 else "middle"}" paint-order="stroke" stroke="{PAPER}" stroke-width="3">'
                 f'{wort} ({ref.split(".")[1]},{ref.split(".")[2]})</text>')
    for k, (lon, lat, hoehe, name, _) in ORTE.items():
        x, y = proj(lon, lat)
        haupt = k != "Nazaret"
        t.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{5 if haupt else 3}" fill="{"#8A3B2A" if haupt else INK}" stroke="{PAPER}" stroke-width="1.5"/>')
        dx_ = -9 if k in ("Kana", "Nazaret") else 9
        dy_ = 18 if k == "Kana" else 4
        t.append(f'<text x="{x + dx_:.0f}" y="{y + dy_:.0f}" {FONT} font-size="{17 if haupt else 12}" fill="{INK}" text-anchor="{"end" if dx_ < 0 else "start"}" '
                 f'paint-order="stroke" stroke="{PAPER}" stroke-width="3">{name}</text>')
    # Massstab 20 km
    km = 20 / (111.32 * KOSLAT) / (GEBIET[2] - GEBIET[0]) * KW
    t.append(f'<g transform="translate(24 {KH - 166})"><path d="M0,0 h{km:.1f}" stroke="{INK}" stroke-width="2"/><path d="M0,-4 v8 M{km:.1f},-4 v8" stroke="{INK}"/>'
             f'<text x="{km / 2:.1f}" y="-8" {SANS} font-size="11" fill="{INK}" text-anchor="middle">20 km</text></g>')
    # Höhenprofil (Wegpunkte, Höhe gerundet)
    px, py, pw, ph = 24, KH - 128, 250, 100
    t.append(f'<g><rect x="{px - 8}" y="{py - 22}" width="{pw + 92}" height="{ph + 40}" rx="8" fill="{PAPER}" fill-opacity=".9" stroke="#D8D0C0"/>'
             f'<text x="{px}" y="{py - 6}" {SANS} font-size="12" fill="{INK}">Höhe über dem Meer (gerundet)</text>')
    hmax, hmin = 950, -300

    def hy(m):
        return py + ph - (m - hmin) / (hmax - hmin) * ph
    t.append(f'<path d="M{px},{hy(0):.1f} h{pw}" stroke="#9DB8C8" stroke-dasharray="3 3"/><text x="{px + pw + 4}" y="{hy(0) + 4:.1f}" {SANS} font-size="10" fill="#5F7F90">0 m</text>')
    folge = ["Kana", "Kafarnaum", "Jerusalem"]
    pts = [(px + i * pw / 2, hy(ORTE[o][2])) for i, o in enumerate(folge)]
    t.append(f'<path d="M{pts[0][0]},{pts[0][1]:.1f} L{pts[1][0]},{pts[1][1]:.1f} L{pts[2][0]},{pts[2][1]:.1f}" fill="none" stroke="#8A3B2A" stroke-width="2"/>')
    for (x, y), o in zip(pts, folge):
        t.append(f'<circle cx="{x}" cy="{y:.1f}" r="3.5" fill="#8A3B2A"/><text x="{x + (6 if o != "Jerusalem" else -6)}" y="{y - 6:.1f}" {SANS} font-size="11" fill="{INK}" '
                 f'text-anchor="{"start" if o != "Jerusalem" else "end"}">{o} {ORTE[o][2]:+d} m</text>')
    t.append("</g>")
    t.append(f'<text x="{KW - 16}" y="28" {FONT} font-size="20" fill="{INK}" text-anchor="end">Johannes 2: Kana – Kafarnaum – Jerusalem</text>'
             f'<text x="{KW - 16}" y="48" {SANS} font-size="11" fill="#6B6B60" text-anchor="end">Weg gestrichelt: Richtung nach dem Text, Verlauf nicht überliefert</text>')
    return "".join(t)


# ------------------------------------------------------------------ 2. Stiftshütte (Ellen)

E = 6.6                         # px je Elle
IW, IH = 1100, 720


def iso(x, y, z=0):
    """x: Ost (Elle), y: Süd (Elle), z: Höhe. Isometrisch, Osten nach rechts unten."""
    return (IW / 2 + (x - y) * math.cos(math.radians(30)) * E - 120, 150 + (x + y) * math.sin(math.radians(30)) * E - z * E)


def quader(x, y, w, d, h, farbe, deckel=None, kontur=INK, alpha=1.0, filt=""):
    """Kasten von (x,y) mit Breite w (Ost), Tiefe d (Süd), Höhe h: sichtbare Flächen Süd, Ost, oben."""
    P = lambda a, b, c: "{:.1f},{:.1f}".format(*iso(a, b, c))  # noqa: E731
    sued = f"{P(x, y + d, 0)} {P(x + w, y + d, 0)} {P(x + w, y + d, h)} {P(x, y + d, h)}"
    ost = f"{P(x + w, y, 0)} {P(x + w, y + d, 0)} {P(x + w, y + d, h)} {P(x + w, y, h)}"
    oben = f"{P(x, y, h)} {P(x + w, y, h)} {P(x + w, y + d, h)} {P(x, y + d, h)}"
    s = f'stroke="{kontur}" stroke-width=".9" stroke-linejoin="round" opacity="{alpha}" {filt}'
    return (f'<polygon points="{sued}" fill="{farbe}" {s}/><polygon points="{ost}" fill="{farbe}" {s} style="filter:brightness(.88)"/>'
            f'<polygon points="{oben}" fill="{deckel or farbe}" {s}/>')


STIFT = {  # Ellen; Vorhof: Westen x=0 … Osten x=100, Norden y=0 … Süden y=50
    "vorhof": (100, 50, 5, "EXO.27.9-EXO.27.18", "B"),
    "tor": (20, "EXO.27.16", "B"),
    "zelt": (30, 10, 10, "EXO.26.15-EXO.26.25", "B"),
    "teilung": (20, 10, "EXO.26.33", "R"),
    "altar": (5, 5, 3, "EXO.27.1", "B"),
    "lade": (2.5, 1.5, 1.5, "EXO.25.10", "B"),
    "tisch": (2, 1, 1.5, "EXO.25.23", "B"),
    "rauch": (1, 1, 2, "EXO.30.1-EXO.30.2", "B"),
}


def stift_daten(mit_grund):
    t = []
    zx, zy = 10, 20          # Zelt: Westteil des Vorhofs (R), mittig
    filt = 'filter="url(#linie)"' if mit_grund else ""
    # Boden des Vorhofs
    P = lambda a, b, c=0: "{:.1f},{:.1f}".format(*iso(a, b, c))  # noqa: E731
    if mit_grund:
        t.append(f'<polygon points="{P(0, 0)} {P(100, 0)} {P(100, 50)} {P(0, 50)}" fill="#EADFC6" filter="url(#nass)"/>')
    # Rückwände Nord und West (nur Linie oben), dann Zelt, Geräte, Vorderwände Süd und Ost halbtransparent
    t.append(f'<polygon points="{P(0, 0)} {P(100, 0)} {P(100, 0, 5)} {P(0, 0, 5)}" fill="#F4EFE4" fill-opacity="{.7 if mit_grund else .9}" stroke="{INK}" stroke-width=".9" {filt}/>')
    t.append(f'<polygon points="{P(0, 0)} {P(0, 50)} {P(0, 50, 5)} {P(0, 0, 5)}" fill="#F4EFE4" fill-opacity="{.7 if mit_grund else .9}" stroke="{INK}" stroke-width=".9" {filt}/>')
    # Zelt: Allerheiligstes (x 10–20) und Heiliges (x 20–40); Decke weggelassen, damit innen sichtbar
    t.append(f'<polygon points="{P(zx, zy)} {P(zx + 30, zy)} {P(zx + 30, zy + 10)} {P(zx, zy + 10)}" fill="#E2D2B0" stroke="{INK}" stroke-width=".9"/>')
    t.append(f'<polygon points="{P(zx, zy)} {P(zx + 30, zy)} {P(zx + 30, zy, 10)} {P(zx, zy, 10)}" fill="#C9A86A" fill-opacity=".55" stroke="{INK}" stroke-width=".9" {filt}/>')
    t.append(f'<polygon points="{P(zx, zy)} {P(zx, zy + 10)} {P(zx, zy + 10, 10)} {P(zx, zy, 10)}" fill="#B8955A" fill-opacity=".55" stroke="{INK}" stroke-width=".9" {filt}/>')
    t.append(quader(zx + 5 - 1.25, zy + 5 - 0.75, 2.5, 1.5, 1.5, "#D9B44A"))                    # Lade
    t.append(f'<polygon points="{P(zx + 10, zy)} {P(zx + 10, zy + 10)} {P(zx + 10, zy + 10, 10)} {P(zx + 10, zy, 10)}" fill="#6E5A8A" fill-opacity=".45" stroke="{INK}" stroke-width=".9"/>')  # Vorhang
    t.append(quader(zx + 12, zy + 4.5, 1, 1, 2, "#D9B44A"))                                       # Räucheraltar
    t.append(quader(zx + 18, zy + 1.2, 2, 1, 1.5, "#D9B44A"))                                     # Tisch Nordseite
    lx, ly = iso(zx + 19, zy + 8.5, 0)
    t.append(f'<path d="M{lx:.1f},{ly:.1f} v-{3 * E:.1f} M{lx - 9:.1f},{ly - 3 * E + 6:.1f} q9,9 18,0 M{lx - 5:.1f},{ly - 3 * E + 3:.1f} q5,5 10,0" stroke="#B8922E" stroke-width="2" fill="none"/>')  # Leuchter Südseite
    # Südwand und Ostwand des Zelts
    t.append(f'<polygon points="{P(zx, zy + 10)} {P(zx + 30, zy + 10)} {P(zx + 30, zy + 10, 10)} {P(zx, zy + 10, 10)}" fill="#C9A86A" fill-opacity=".28" stroke="{INK}" stroke-width=".9" {filt}/>')
    t.append(f'<polygon points="{P(zx + 30, zy)} {P(zx + 30, zy + 10)} {P(zx + 30, zy + 10, 10)} {P(zx + 30, zy, 10)}" fill="#6E5A8A" fill-opacity=".25" stroke="{INK}" stroke-width=".9" {filt}/>')
    # Becken und Altar im Vorhof (Lage R)
    bx, by = iso(zx + 37, zy + 5, 0)
    t.append(f'<ellipse cx="{bx:.1f}" cy="{by:.1f}" rx="{1.6 * E * 1.2:.1f}" ry="{1.6 * E * .7:.1f}" fill="#B98A5E" stroke="{INK}" stroke-width=".9"/>')
    t.append(quader(zx + 47, zy + 2.5, 5, 5, 3, "#B98A5E", "#9F7349"))
    # Vorderwände Süd (ganz) und Ost (mit Tor 20 Ellen in der Mitte)
    op = .35 if mit_grund else .45
    t.append(f'<polygon points="{P(0, 50)} {P(100, 50)} {P(100, 50, 5)} {P(0, 50, 5)}" fill="#F4EFE4" fill-opacity="{op}" stroke="{INK}" stroke-width=".9" {filt}/>')
    for a_, b_ in ((0, 15), (35, 50)):
        t.append(f'<polygon points="{P(100, a_)} {P(100, b_)} {P(100, b_, 5)} {P(100, a_, 5)}" fill="#F4EFE4" fill-opacity="{op}" stroke="{INK}" stroke-width=".9" {filt}/>')
    t.append(f'<polygon points="{P(100, 15)} {P(100, 35)} {P(100, 35, 5)} {P(100, 15, 5)}" fill="#6E5A8A" fill-opacity=".35" stroke="{INK}" stroke-width=".9" {filt}/>')

    # Masslinien (B) und Bezeichnungen
    def mass(a, b, text, off, beleg):
        (x0, y0), (x1, y1) = iso(*a), iso(*b)
        nx, ny = off
        t.append(f'<path d="M{x0 + nx:.1f},{y0 + ny:.1f} L{x1 + nx:.1f},{y1 + ny:.1f}" stroke="#8A3B2A" stroke-width="1" marker-start="url(#pfeil)" marker-end="url(#pfeil)"/>')
        t.append(f'<text x="{(x0 + x1) / 2 + nx * 1.9:.1f}" y="{(y0 + y1) / 2 + ny * 1.9 + 4:.1f}" {SANS} font-size="12" fill="#8A3B2A" text-anchor="middle" '
                 f'paint-order="stroke" stroke="{PAPER}" stroke-width="3">{text} <tspan font-size="10" fill="#6B6B60">{beleg}</tspan></text>')
    mass((0, 50, 0), (100, 50, 0), "100 Ellen", (-10, 16), "B · Ex 27,9")
    mass((100, 0, 0), (100, 50, 0), "50 Ellen", (34, -4), "B · Ex 27,12")
    mass((zx, zy, 10), (zx + 30, zy, 10), "30 Ellen", (9, -16), "B · Ex 26,18")

    schilder = [((zx + 5, zy + 2, 6), "Allerheiligstes 10 × 10 × 10", "R · Ex 26,33", "l"),
                ((zx + 5, zy + 5, 1.5), "Lade 2½ × 1½ × 1½", "B · Ex 25,10", "l"),
                ((zx + 10, zy + 1, 8), "Vorhang", "B · Ex 26,31–33", "l"),
                ((zx + 12.5, zy + 5, 2), "Räucheraltar vor dem Vorhang", "B · Ex 30,1–6", "l"),
                ((zx + 20, zy + 2, 6), "Heiliges 20 × 10 × 10", "R · Ex 26,33", "r"),
                ((zx + 19, zy + 1.7, 1.5), "Tisch, Nordseite", "B · Ex 26,35", "r"),
                ((zx + 19, zy + 8.5, 3), "Leuchter, Südseite", "B · Ex 26,35", "l"),
                ((zx + 37, zy + 5, 0), "Becken", "Lage B · Ex 30,18; Form R", "r"),
                ((zx + 49.5, zy + 5, 3), "Brandopferaltar 5 × 5 × 3", "B · Ex 27,1; Lage R", "r"),
                ((100, 25, 2), "Tor 20 Ellen, Osten", "B · Ex 27,13–16", "r")]
    for seite in ("l", "r"):
        liste = sorted(((iso(*p_), tx, bl) for p_, tx, bl, sd in schilder if sd == seite), key=lambda e: e[0][1])
        ymin, ymax = 110, IH - 30
        n_ = len(liste)
        for k, ((x, y), tx, bl) in enumerate(liste):
            ly = max(ymin + k * 34, min(y - 60, ymax - (n_ - 1 - k) * 34))
            liste[k] = ((x, y), tx, bl, ly)
        for k in range(1, n_):  # Abstände nach unten durchsetzen
            if liste[k][3] < liste[k - 1][3] + 34:
                liste[k] = liste[k][:3] + (liste[k - 1][3] + 34,)
        for (x, y), tx, bl, ly in liste:
            lx = 30 if seite == "l" else IW - 30
            kx = lx + (210 if seite == "l" else -230)
            t.append(f'<path d="M{x:.1f},{y:.1f} L{kx:.1f},{ly - 4:.1f} L{lx + (205 if seite == "l" else -225):.1f},{ly - 4:.1f}" fill="none" stroke="{INK}" stroke-width=".7"/>'
                     f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2" fill="{INK}"/>'
                     f'<text x="{lx}" y="{ly - 8}" {SANS} font-size="12.5" fill="{INK}" text-anchor="{"start" if seite == "l" else "end"}">{tx}</text>'
                     f'<text x="{lx}" y="{ly + 7}" {SANS} font-size="10.5" fill="#6B6B60" text-anchor="{"start" if seite == "l" else "end"}">{bl}</text>')
    t.append(f'<text x="30" y="40" {FONT} font-size="24" fill="{INK}">Die Stiftshütte – Masse nach Exodus 25–27 und 30</text>'
             f'<text x="30" y="62" {SANS} font-size="12.5" fill="#6B6B60">1 Elle ≈ 45 cm. B = steht im Text · R = rekonstruiert. Zeltdecken weggelassen, damit das Innere sichtbar ist.</text>')
    return "".join(t)


def stift_vorlage():
    """Vorlage fürs Bildmodell: exakte Körper ohne Schrift und Masslinien."""
    teile = stift_daten(False)
    import re
    teile = re.sub(r'<text.*?</text>', "", teile)
    teile = re.sub(r'<path d="M[^"]*" stroke="#8A3B2A"[^>]*/>', "", teile)
    teile = re.sub(r'<path d="M[^"]*" fill="none" stroke="#4A4D45" stroke-width=".7"/><circle[^>]*/>', "", teile)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {IW} {IH}" width="{IW}" height="{IH}">{FILTER}<rect width="{IW}" height="{IH}" fill="#FFFFFF"/>{teile}</svg>'


# ------------------------------------------------------------------ 3. Seligpreisungen

def selig_glieder():
    de = json.loads((REPO / "data/translations/TRANS-MAT-005-001-048-DE-WORKING.json").read_text())["text_by_reference"]
    out = []
    for v in range(3, 11):
        s = de[f"MAT.5.{v}"]
        a, _, b = s.partition(", denn ")
        out.append((v, a, "denn " + b))
    return out


VIGNETTEN = {  # Bildauftrag je Glied (I: Deutung; nichts davon steht so im Text)
    3: "an older man in a plain robe kneeling with empty open hands held up, looking upward with a quiet face",
    4: "a woman weeping with her face in her hands while another woman puts an arm around her shoulders, comforting her",
    5: "a gentle man stepping aside on a narrow path to let an old woman with a bundle pass first",
    6: "a thin traveller holding out an empty clay bowl, looking forward with longing",
    7: "a man kneeling to give water from a jug to a beggar sitting by a wall",
    8: "a young woman with a calm, open, honest face, holding a small oil lamp in both hands",
    9: "two men who had quarrelled shaking hands while a third man stands between them, a hand on each one's shoulder",
    10: "a man walking away from a group of people who shout and point at him; he looks back calmly",
}

SW, SH = 900, 1080


def selig_daten(bilder=None):
    """Aufbau exakt: acht Zeilen, links «Selig sind …», rechts «denn …»; Klammer 5,3 ↔ 5,10 (gleiche Verheissung, Gegenwart),
    5,4–9 Zukunft. bilder: {Vers: href} für Vignetten (Fassung B), sonst Kreis-Platzhalter (Fassung A)."""
    t = [f'<text x="40" y="52" {FONT} font-size="26" fill="{INK}">Die Seligpreisungen</text>'
         f'<text x="40" y="76" {SANS} font-size="13" fill="#6B6B60">Matthäus 5,3–10 · acht Glieder · gleiche Verheissung am Anfang und am Ende</text>']
    y0, zh = 110, 118
    for i, (v, a, b) in enumerate(selig_glieder()):
        y = y0 + i * zh
        gegenwart = v in (3, 10)
        if bilder and v in bilder:
            t.append(f'<clipPath id="c{v}"><rect x="40" y="{y}" width="150" height="100" rx="10"/></clipPath>'
                     f'<image href="{bilder[v]}" x="40" y="{y}" width="150" height="100" preserveAspectRatio="xMidYMid slice" clip-path="url(#c{v})"/>'
                     f'<rect x="40" y="{y}" width="150" height="100" rx="10" fill="none" stroke="#D8D0C0"/>')
        else:
            t.append(f'<circle cx="115" cy="{y + 50}" r="36" fill="#E9DFC9" filter="url(#nass)"/>'
                     f'<text x="115" y="{y + 58}" {FONT} font-size="24" fill="{INK}" text-anchor="middle">{v}</text>')
        t.append(f'<text x="215" y="{y + 30}" {SANS} font-size="11" fill="#6B6B60">5,{v}</text>')
        wrap_a = _umbruch(a, 34)
        for k, z in enumerate(wrap_a):
            t.append(f'<text x="215" y="{y + 52 + k * 22}" {FONT} font-size="19" fill="{INK}">{html.escape(z)}</text>')
        farbe = "#8A3B2A" if gegenwart else "#4F6F86"
        for k, z in enumerate(_umbruch(b, 30)):
            t.append(f'<text x="575" y="{y + 52 + k * 22}" {FONT} font-size="19" font-style="italic" fill="{farbe}">{html.escape(z)}</text>')
        t.append(f'<path d="M558,{y + 20} v70" stroke="#D8D0C0"/>')
    # Klammer 5,3 ↔ 5,10
    ya, yb = y0 + 40, y0 + 7 * zh + 40
    t.append(f'<path d="M868,{ya} h12 V{yb} h-12" fill="none" stroke="#8A3B2A" stroke-width="1.6"/>'
             f'<text x="890" y="{(ya + yb) / 2}" {SANS} font-size="12" fill="#8A3B2A" transform="rotate(90 890 {(ya + yb) / 2})" text-anchor="middle">'
             f'«ihnen gehört das Reich der Himmel» – Gegenwart (5,3 und 5,10)</text>')
    t.append(f'<text x="575" y="{y0 + 8 * zh + 10}" {SANS} font-size="12" fill="#4F6F86">blau: Zukunft («sie werden …», 5,4–9)</text>')
    t.append(f'<text x="40" y="{y0 + 8 * zh + 10}" {SANS} font-size="12" fill="#6B6B60">Bilder: gedeutet (I) – der Text beschreibt keine Szenen.</text>')
    return "".join(t)


def _umbruch(text, n):
    out, cur = [], ""
    for w in text.split():
        if cur and len(cur) + 1 + len(w) > n:
            out.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    return out + [cur]


# ------------------------------------------------------------------ Ausgabe

STIL = ("Very reduced, loose watercolour sketch on warm white paper, like a quick painted study: few thin broken ink lines, "
        "flat transparent pale washes that bleed softly, lots of untouched paper, no shading detail, no texture, no lettering. "
        "Small muted palette: sand, ochre, terracotta, blue-grey, olive, soft ink grey.")


def auftraege():
    a = {"karte": {"vorlage": "vorlagen/karte_vorlage.png", "groesse": "1024x1536",
                   "prompt": "Paint this exact map as a soft watercolour landscape map of the land of Israel in the first century, seen from above. "
                             "Keep every coastline, lake and river EXACTLY where they are in the attached template (same shapes, same positions, same scale) – "
                             "the template is a precise map and will be overlaid with place names later. Water as pale blue-grey washes; "
                             "the land in sand and pale olive washes, a few soft hill shadows in Galilee and the Judean hills, the deep Jordan valley a little darker. "
                             "No place names, no lettering, no symbols, no roads, no compass, no border, no frame. " + STIL},
         "stiftshuette": {"vorlage": "vorlagen/stiftshuette_vorlage.png", "groesse": "1536x1024",
                          "prompt": "Paint this exact isometric drawing of the ancient tabernacle court as a soft watercolour illustration. "
                                    "Keep every shape EXACTLY where it is in the attached template – same outlines, same proportions, same positions – "
                                    "because measurements will be drawn on top later. The court walls are white linen hangings on posts; the tent walls are "
                                    "gilded acacia boards; the veil and the east gate are woven in blue, purple and scarlet; the altar and basin are bronze; "
                                    "ark, table, incense altar and lampstand are gold. The ground is plain sand. No people, no animals, no lettering, no frame. " + STIL}}
    for v, (vv, a_, b_) in zip(VIGNETTEN, selig_glieder()):
        a[f"selig-{v}"] = {"vorlage": None, "groesse": "1536x1024",
                           "prompt": f"A small vignette in the style of a Bible watercolour sketch, first-century Galilee, adults with natural proportions and simple, "
                                     f"expressive faces: {VIGNETTEN[v]}. One simple scene, centred, everything inside the picture with white paper around it; "
                                     f"no background except one pale wash. No halo, no light effects, no lettering. " + STIL}
    return a


def png(svg_text, pfad, w, h):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        s = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=2)
        s.set_content(f'<html><body style="margin:0">{svg_text}</body></html>')
        s.wait_for_timeout(300)
        s.screenshot(path=str(pfad), clip={"x": 0, "y": 0, "width": w, "height": h})
        b.close()


def vorlagen():
    VOR.mkdir(exist_ok=True)
    ERG.mkdir(exist_ok=True)
    png(karte_vorlage(), VOR / "karte_vorlage.png", KW, KH)
    png(stift_vorlage(), VOR / "stiftshuette_vorlage.png", IW, IH)
    (VOR / "auftraege.json").write_text(json.dumps(auftraege(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    # Fassung A
    for name, w, h, inhalt in (("karte", KW, KH, karte_daten(True)), ("stiftshuette", IW, IH, stift_daten(True)), ("seligpreisungen", SW, SH, selig_daten())):
        svg = svg_doc(w, h, inhalt)
        (ERG / f"{name}_A.svg").write_text(svg, encoding="utf-8")
        png(svg, ERG / f"{name}_A.png", w, h)
    print("Vorlagen und Fassung A geschrieben:", VOR, ERG)


def data_uri(p):
    p = pathlib.Path(p)
    typ = "image/png" if p.suffix == ".png" else "image/webp"
    return f"data:{typ};base64," + base64.b64encode(p.read_bytes()).decode()


def zusammen(lauf):
    """Gemalte Unterlagen (lauf/<name>.png) mit der Datenebene zusammensetzen (Fassung B)."""
    from PIL import Image
    lauf = pathlib.Path(lauf)
    ERG.mkdir(exist_ok=True)
    klein = ERG / "img"
    klein.mkdir(exist_ok=True)

    def ablegen(name, w, h):
        src = lauf / f"{name}.png"
        if not src.is_file():
            return None
        ziel = klein / f"{name}.webp"
        Image.open(src).convert("RGB").resize((w * 2, h * 2) if w * 2 <= 1600 else (w, h), Image.LANCZOS).save(ziel, quality=80, method=6)
        return ziel
    k = ablegen("karte", KW, KH)
    if k:
        svg = svg_doc(KW, KH, karte_daten(False), data_uri(k))
        (ERG / "karte_B.svg").write_text(svg, encoding="utf-8")
        png(svg, ERG / "karte_B.png", KW, KH)
    s_ = ablegen("stiftshuette", IW, IH)
    if s_:
        import re
        ueber = stift_daten(False)
        # nur Masslinien, Schilder und Titel über das gemalte Bild legen
        nur = "".join(re.findall(r'<path d="M[^"]*" stroke="#8A3B2A"[^>]*/>|<path d="M[^"]*" fill="none" stroke="#4A4D45" stroke-width=".7"/><circle[^>]*/>|<text.*?</text>', ueber))
        svg = svg_doc(IW, IH, nur, data_uri(s_))
        (ERG / "stiftshuette_B.svg").write_text(svg, encoding="utf-8")
        png(svg, ERG / "stiftshuette_B.png", IW, IH)
    bilder = {}
    for v in VIGNETTEN:
        p = ablegen(f"selig-{v}", 300, 200)
        if p:
            bilder[v] = data_uri(p)
    if bilder:
        svg = svg_doc(SW, SH, selig_daten(bilder))
        (ERG / "seligpreisungen_B.svg").write_text(svg, encoding="utf-8")
        png(svg, ERG / "seligpreisungen_B.png", SW, SH)
    print("Fassung B geschrieben:", ERG)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "vorlagen":
        vorlagen()
    elif len(sys.argv) > 2 and sys.argv[1] == "zusammen":
        zusammen(sys.argv[2])
    else:
        sys.exit(__doc__)
