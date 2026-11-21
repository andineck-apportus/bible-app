#!/usr/bin/env python3
"""Bilder in Strukturbildern aus dem Bildlexikon (Rückmeldung Andi Neck 2026-11-21: auf die früheren Definitionen
zurückgreifen, aber gut gezeichnet; Gott wird gezeichnet).

Je Element einer Struktur (und bei «mitte») nennt «depicts» Einträge des Bildlexikons (data/illustrations/lexicon/). Gezeigt wird
der erste Eintrag:
- FIG-GOTT: der goldene Strahlenkranz mit dem Gottesnamen יהוה, gezeichnet (struktur_kachel.gott_zeichen), nie als Mensch;
- sonst das gemalte Einzelbild des Eintrags im Aquarellstil (data/illustrations/aquarell/figuren/<ID>.webp), sobald es die
  automatische Prüfung bestanden hat (bilder_aquarell_figuren.py, Action «auto-figuren»). So sieht ein Ding, ein Ort, eine Person
  oder ein Zeichen überall gleich aus: in den Szenen, im Bildlexikon und in den Strukturbildern.
Fehlt das Bild noch, bleibt das Element ohne Bild.

    python3 scripts/authoring/vignetten.py stand            # Einträge, deren Bild noch fehlt (für «auto-figuren»)
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATEN = ROOT / "scripts/authoring/bilder_aquarell_daten"
STIL = ROOT / "data/illustrations/styles/ILLSTYLE-AQUARELL.json"
GOTT = "FIG-GOTT"
_st = None


def renderings():
    global _st
    if _st is None:
        _st = json.loads(STIL.read_text(encoding="utf-8")).get("renderings", {}) if STIL.exists() else {}
    return _st


def auftraege(nur=None):
    """(Feld, Schlüssel, Lexikon-ID) aus allen Szenenplänen; Schlüssel = Nummer des Elements oder «m» für die Mitte."""
    for p in sorted(DATEN.glob("szenen-*.json")):
        for sid, sz in json.loads(p.read_text(encoding="utf-8"))["szenen"].items():
            if sz.get("form") != "struktur" or (nur and sid not in nur):
                continue
            sx = sz["struktur"]
            for k, e in enumerate(sx.get("elemente") or [], 1):
                if e.get("depicts"):
                    yield sid, str(k), e["depicts"][0]
            if (sx.get("mitte") or {}).get("depicts"):
                yield sid, "m", sx["mitte"]["depicts"][0]


_rahmen = {}


def rahmen(pfad):
    """Ausschnitt mit dem eigentlichen Motiv (ohne leeres Papier), als «x y b h» in Bildpixeln: Die Einzelbilder des Lexikons
    stehen klein auf grossem Hochformat-Papier; in der Kachel soll das Motiv die Fläche füllen."""
    if pfad not in _rahmen:
        from PIL import Image
        im = Image.open(ROOT / pfad).convert("L")
        w, h = im.size
        maske = im.point(lambda v: 255 if v < 200 else 0)
        bb = maske.getbbox() or (0, 0, w, h)
        rand = int(0.06 * max(bb[2] - bb[0], bb[3] - bb[1])) + 2
        x0, y0, x1, y1 = max(0, bb[0] - rand), max(0, bb[1] - rand), min(w, bb[2] + rand), min(h, bb[3] + rand)
        _rahmen[pfad] = (x0, y0, x1 - x0, y1 - y0, w, h)
    return _rahmen[pfad]


def bild(fid):
    """href (relativ zum Ordner der Bilder) und Ausschnitt; «#gott» für den gezeichneten Strahlenkranz."""
    if fid == GOTT:
        return "#gott"
    r = renderings().get(fid) or {}
    c = r.get("check") or {}
    if r.get("image") and c.get("stufe") == "ki-geprueft" and (ROOT / r["image"]).exists():
        return (r["image"].replace("data/illustrations/aquarell/", ""), rahmen(r["image"]))
    return None


def gueltig(sid):
    """Schlüssel → href (relativ zum Ordner der Bilder) bzw. «#gott»."""
    return {k: h for _s, k, fid in auftraege({sid}) if (h := bild(fid))}


def stand():
    fehlt = {}
    for sid, k, fid in auftraege():
        if not bild(fid):
            fehlt.setdefault(fid, []).append(f"{sid}/{k}")
    for fid, wo in sorted(fehlt.items()):
        print(f"{fid}: {'kein Malauftrag (Beschreibung fehlt)' if fid not in renderings() else 'noch nicht gemalt'} – {', '.join(wo[:6])}")
    print(f"{len(fehlt)} Einträge ohne Bild: " + ",".join(sorted(f for f in fehlt if f in renderings())))


if __name__ == "__main__":
    if sys.argv[1:] == ["stand"]:
        stand()
    else:
        print(__doc__)
