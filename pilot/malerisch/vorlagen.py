#!/usr/bin/env python3
"""Kompositionsvorlagen für den Pilot «malerische Bilder» (Johannes 2).

Erzeugt je Szene eine Tiefenkarte (hell = nah, dunkel = fern), die das Bildmodell als Steuerbild bekommt.
So legt nicht der Zufall, sondern die Regie fest, wo wer steht, wie gross er ist und wie der Raum aufgebaut ist.
Die Vorlagen sind bewusst grob: Silhouetten und Raumebenen, keine Details.

Aufruf: python3 pilot/malerisch/vorlagen.py            → schreibt pilot/malerisch/vorlagen/*.png
        python3 pilot/malerisch/vorlagen.py --uebersicht → zusätzlich eine Übersicht aller Vorlagen
"""
import pathlib
import sys

from PIL import Image, ImageDraw, ImageFilter

W, H = 1216, 800  # Seitenverhältnis wie die Bilder der App (≈ 1,52 : 1), Vielfache von 16
OUT = pathlib.Path(__file__).resolve().parent / "vorlagen"


def leinwand(horizont, wand=45, boden_fern=70, boden_nah=210):
    """Hintergrundwand bis zum Horizont, darunter ein Boden, der nach vorn heller (näher) wird."""
    img = Image.new("L", (W, H), wand)
    d = ImageDraw.Draw(img)
    for y in range(horizont, H):
        t = (y - horizont) / max(1, H - horizont)
        d.line([(0, y), (W, y)], fill=int(boden_fern + (boden_nah - boden_fern) * t))
    return img, d


def figur(d, x, fuss, hoehe, tiefe, sitzend=False, arm=None, neigung=0):
    """Stehende oder sitzende Figur als Silhouette. arm: (dx, dy) relativ zur Schulter für einen ausgestreckten Arm."""
    if sitzend:
        hoehe = hoehe * 0.68
    kopf_r = hoehe * 0.062
    schulter_y = fuss - hoehe * 0.80
    kopf_x = x + neigung
    kopf_y = schulter_y - kopf_r * 1.25
    breit = hoehe * 0.105
    unten = hoehe * (0.24 if sitzend else 0.14)
    d.polygon([(x + neigung - breit, schulter_y), (x + neigung + breit, schulter_y),
               (x + unten, fuss), (x - unten, fuss)], fill=tiefe)
    d.ellipse([kopf_x - kopf_r, kopf_y - kopf_r, kopf_x + kopf_r, kopf_y + kopf_r], fill=tiefe)
    if arm:
        sx, sy = x + neigung + (breit * 0.8 if arm[0] >= 0 else -breit * 0.8), schulter_y + hoehe * 0.04
        d.line([(sx, sy), (sx + arm[0] * hoehe, sy + arm[1] * hoehe)], fill=tiefe, width=max(4, int(hoehe * 0.05)))


def krug(d, x, boden, hoehe, tiefe):
    """Grosser Steinkrug: bauchig, mit Hals."""
    b = hoehe * 0.42
    d.ellipse([x - b, boden - hoehe * 0.85, x + b, boden], fill=tiefe)
    d.rectangle([x - b * 0.55, boden - hoehe, x + b * 0.55, boden - hoehe * 0.7], fill=tiefe)


def tisch(d, x0, x1, oben, dicke, tiefe, schraeg=0):
    d.polygon([(x0, oben), (x1, oben + schraeg), (x1, oben + schraeg + dicke), (x0, oben + dicke)], fill=tiefe)


def saeule(d, x, oben, unten, breite, tiefe):
    d.rectangle([x - breite / 2, oben, x + breite / 2, unten], fill=tiefe)


def menge(d, x0, x1, fuss, hoehe, tiefe, anzahl):
    for i in range(anzahl):
        x = x0 + (x1 - x0) * (i + 0.5) / anzahl
        figur(d, x, fuss + (i % 2) * 6, hoehe * (0.92 + 0.08 * (i % 3) / 2), tiefe)


def szene_a():
    """Kana 2,1–4: Maria flüstert Jesus zu; Feiernde unscharf hinten."""
    img, d = leinwand(horizont=470, wand=40)
    menge(d, 80, 1150, 470, 210, 85, 9)                     # Gäste hinten
    figur(d, 480, 780, 640, 215, neigung=70, arm=(0.40, 0.44))  # Maria, vorgebeugt, Hand an Jesu Arm
    figur(d, 770, 790, 700, 200, sitzend=True)               # Jesus sitzend
    tisch(d, 560, 1216, 700, 100, 235)                       # niedriger Tisch vorn
    d.ellipse([230, 690, 420, 770], fill=245)                # umgekippter leerer Krug
    return img


def szene_b():
    """Kana 2,6–8: sechs Steinkrüge schräg in die Tiefe, Diener giessen, Jesus seitlich, Maria im Türrahmen."""
    img, d = leinwand(horizont=360, wand=50, boden_fern=80, boden_nah=225)
    d.rectangle([700, 150, 840, 360], fill=10)               # Türöffnung (fern)
    figur(d, 770, 360, 170, 70)                              # Maria im Türrahmen
    for i in range(6):                                       # Krüge: vorn links gross, hinten rechts klein
        t = i / 5
        krug(d, 110 + t * 560, 790 - t * 400, 300 - t * 200, int(245 - t * 150))
    figur(d, 360, 620, 430, 160, arm=(-0.16, 0.10))          # Diener hinter den vorderen Krügen, giesst
    figur(d, 590, 500, 300, 125, arm=(-0.14, 0.12))          # zweiter Diener weiter hinten
    figur(d, 1010, 770, 640, 200, arm=(-0.22, 0.05))         # Jesus rechts mit Geste
    return img


def szene_c():
    """Kana 2,9–11: Speisemeister hebt den Becher, Bräutigam, Diener hinten, Jesus und Jünger am Rand im Schatten."""
    img, d = leinwand(horizont=430, wand=45)
    menge(d, 300, 640, 470, 300, 110, 2)                     # zwei Diener hinten
    menge(d, 1090, 1210, 540, 300, 70, 2)                    # Jünger am rechten Rand
    figur(d, 1030, 550, 320, 80)                             # Jesus bei ihnen, im Schatten
    figur(d, 470, 790, 700, 220, arm=(0.20, -0.22))          # Speisemeister, Becher erhoben
    figur(d, 790, 790, 650, 195, neigung=-20)                # Bräutigam
    tisch(d, 0, 1216, 720, 80, 240, schraeg=-20)             # Festtafel vorn
    return img


def szene_d():
    """Tempel 2,14–16: Säulenhalle, Jesus mit erhobener Geissel stösst einen Tisch um, Händler weichen zurück."""
    img, d = leinwand(horizont=500, wand=30, boden_fern=60, boden_nah=215)
    for i in range(6):                                       # Säulenreihe links, nach hinten kleiner
        t = i / 5
        saeule(d, 60 + t * 420, 0, 500 + (1 - t) * 260, 110 - t * 70, int(200 - t * 140))
    figur(d, 820, 790, 760, 210, arm=(0.10, -0.42), neigung=-30)  # Jesus, Geissel erhoben (Untersicht)
    tisch(d, 520, 900, 610, 70, 235, schraeg=140)            # umkippender Tisch, diagonal
    figur(d, 360, 760, 560, 180, neigung=-70, arm=(-0.25, -0.2))  # Händler weicht zurück
    figur(d, 200, 700, 470, 150, neigung=-50)                # zweiter Händler
    d.ellipse([1000, 640, 1180, 760], fill=170)              # Schaf/Rind rechts
    for x, y in [(990, 180), (1060, 120), (1120, 230), (930, 260)]:  # auffliegende Tauben
        d.ellipse([x - 22, y - 12, x + 22, y + 12], fill=120)
    return img


def szene_e():
    """Tempel 2,18–21: riesiges Tempelhaus hinten, Jesus klein und ruhig, Gruppe der Fragenden gegenüber."""
    img, d = leinwand(horizont=560, wand=20, boden_fern=70, boden_nah=200)
    d.rectangle([250, 40, 1000, 560], fill=45)               # Tempelhaus (fern, monumental)
    d.rectangle([520, 250, 730, 560], fill=25)               # Portal
    for x in range(290, 1000, 90):
        saeule(d, x, 230, 560, 26, 55)
    figur(d, 400, 720, 300, 175, arm=(0.0, 0.12))            # Jesus, Hand auf der Brust
    menge(d, 640, 1130, 740, 310, 165, 5)                    # Gruppe der Fragenden
    d.rectangle([150, 740, 330, 770], fill=200)              # umgestürzter Tisch am Boden
    return img


SZENEN = {
    "PILOT-JHN-002-A": szene_a,
    "PILOT-JHN-002-B": szene_b,
    "PILOT-JHN-002-C": szene_c,
    "PILOT-JHN-002-D": szene_d,
    "PILOT-JHN-002-E": szene_e,
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    bilder = {}
    for sid, fn in SZENEN.items():
        img = fn().filter(ImageFilter.GaussianBlur(6))
        img.save(OUT / f"{sid}.png", optimize=True)
        bilder[sid] = img
        print("geschrieben:", OUT / f"{sid}.png")
    if "--uebersicht" in sys.argv:
        t = Image.new("L", (W // 2 * 3 + 40, H // 2 * 2 + 30), 255)
        for i, img in enumerate(bilder.values()):
            t.paste(img.resize((W // 2, H // 2)), (10 + (i % 3) * (W // 2 + 10), 10 + (i // 3) * (H // 2 + 10)))
        t.save(OUT.parent / "vorlagen_uebersicht.png")


if __name__ == "__main__":
    main()
