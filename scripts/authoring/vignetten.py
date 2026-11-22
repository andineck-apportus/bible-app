#!/usr/bin/env python3
"""Bilder in Strukturbildern aus dem Bildlexikon (Rückmeldung Andi Neck 2026-11-21: auf die früheren Definitionen
zurückgreifen, aber gut gezeichnet; Gott wird gezeichnet).

Je Element einer Struktur (und bei «mitte») nennt «depicts» Einträge des Bildlexikons (data/illustrations/lexicon/), höchstens drei
(z. B. Fisch und Vogel); sie stehen nebeneinander:
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

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import personen as P  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATEN = ROOT / "scripts/authoring/bilder_aquarell_daten"
STIL = ROOT / "data/illustrations/styles/ILLSTYLE-AQUARELL.json"
GOTT = "FIG-GOTT"
GEZEICHNET = {"FIG-ZEICHEN-SABBAT"}
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
            # Personen, die nicht wiederkehren, zeigt das Strukturbild nicht als Bild: ihr Name steht im Text (personen.py)
            for k, e in enumerate(sx.get("elemente") or [], 1):
                for fid in [f for f in (e.get("depicts") or []) if not P.nur_namensschild(f)][:3]:
                    yield sid, str(k), fid
            for fid in [f for f in ((sx.get("mitte") or {}).get("depicts") or []) if not P.nur_namensschild(f)][:3]:
                yield sid, "m", fid


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
    if fid in GEZEICHNET:   # Zeichen, deren Aussage Ziffern oder Schrift braucht: gezeichnet (struktur_kachel.GEZEICHNET)
        return "#" + fid
    r = renderings().get(fid) or {}
    c = r.get("check") or {}
    if r.get("image") and c.get("stufe") == "ki-geprueft" and (ROOT / r["image"]).exists():
        return (r["image"].replace("data/illustrations/aquarell/", ""), rahmen(r["image"]))
    return None


def gueltig(sid):
    """Schlüssel → Liste der Bilder (href relativ zum Ordner der Bilder mit Ausschnitt, bzw. «#gott»), höchstens drei je Glied
    (z. B. Fisch und Vogel); ein Glied erscheint nur mit Bild, wenn alle seine Einträge ein Bild haben."""
    alle, fehlt = {}, set()
    for _s, k, fid in auftraege({sid}):
        h = bild(fid)
        if h:
            alle.setdefault(k, []).append(h)
        else:
            fehlt.add(k)
    return {k: v for k, v in alle.items() if k not in fehlt}


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


_frei = {}
FREI_FASSUNG = "1"   # erhöhen, wenn sich das Verfahren ändert (macht den Zwischenspeicher ungültig)


def freistellen(pfad):
    """Einzelbild des Bildlexikons ohne Papier (WebP mit Transparenz), für Strukturbilder in hell und dunkel (Rückmeldung Andi Neck
    2026-11-21: weisses Lamm auf weisser Karte unsichtbar, im Dunkeln gelb-schwarz). Hintergrund = das Papier, das vom Bildrand her
    zusammenhängt (Flutfüllung mit Toleranz); weiss Gemaltes innerhalb der Umrisse (Lamm, Kleid) bleibt deckend. Weiche Kante aus dem
    Farbabstand zum Papier; dazu etwas kräftigere Farben (Sättigung, Kontrast). Wird beim Bau der App erzeugt, nicht gespeichert."""
    if pfad in _frei:
        return _frei[pfad]
    # Zwischenspeicher auf der Platte (nicht im Repo; im Bau-Workflow über actions/cache): Freistellen dauert rund 2,5 s je Bild,
    # bei über 600 Bildern sprengte das die Bauzeit (Bau am 2026-11-21 nach 30 Minuten abgebrochen)
    import hashlib
    roh = (ROOT / pfad).read_bytes()
    ablage = ROOT / ".cache/freistellen" / (hashlib.sha1(roh + FREI_FASSUNG.encode()).hexdigest() + ".webp")
    if ablage.is_file():
        _frei[pfad] = ablage.read_bytes()
        return _frei[pfad]
    import io
    from PIL import Image, ImageChops, ImageEnhance, ImageFilter, ImageDraw
    im = Image.open(ROOT / pfad).convert("RGB")
    w, h = im.size
    rand = [im.getpixel((x, y)) for x in range(0, w, 8) for y in (0, h - 1)] + [im.getpixel((x, y)) for y in range(0, h, 8) for x in (0, w - 1)]
    papier = tuple(sorted(c[i] for c in rand)[len(rand) // 2] for i in range(3))
    diff = ImageChops.difference(im, Image.new("RGB", im.size, papier)).convert("L")   # Farbabstand zum Papier
    # Flutfüllung über «nahe am Papier» vom Rand aus: nur zusammenhängendes Papier wird Hintergrund
    # Umrisse sind oft gestrichelt: Motiv-Maske erst verdicken (Lücken schliessen), dann fluten, dann Hintergrund wieder zurücknehmen
    motiv = diff.point(lambda v: 255 if v >= 22 else 0).filter(ImageFilter.MaxFilter(15))
    nah = motiv.point(lambda v: 0 if v else 255)
    flut = nah.copy()
    for x, y in ((0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1), (w // 2, 0), (w // 2, h - 1), (0, h // 2), (w - 1, h // 2)):
        if flut.getpixel((x, y)) == 255:
            ImageDraw.floodfill(flut, (x, y), 128)
    hinter = flut.point(lambda v: 255 if v == 128 else 0).filter(ImageFilter.MaxFilter(15))
    weich = diff.point(lambda v: max(0, min(255, (v - 6) * 255 // 22)))            # Lavierung am Rand bleibt halb sichtbar
    alpha = ImageChops.composite(weich, Image.new("L", im.size, 255), hinter).filter(ImageFilter.GaussianBlur(0.6))
    farbig = ImageEnhance.Contrast(ImageEnhance.Color(im).enhance(1.35)).enhance(1.12)
    farbig.putalpha(alpha)
    b = io.BytesIO()
    farbig.save(b, "WEBP", quality=82, method=6)   # WebP mit Transparenz (PNG wäre rund achtmal grösser)
    _frei[pfad] = b.getvalue()
    ablage.parent.mkdir(parents=True, exist_ok=True)
    ablage.write_bytes(_frei[pfad])
    return _frei[pfad]
