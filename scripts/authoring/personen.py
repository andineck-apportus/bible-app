#!/usr/bin/env python3
"""Welche Personen ein eigenes Bild im Bildlexikon bekommen (Entscheid Andi Neck 2026-11-22).

Regel: Ein eigenes Porträt bekommen nur Personen, die wiederkehren. Alle anderen Personen erscheinen im Bild als gewöhnlicher
Mensch mit Namensschild beim ersten Auftreten (Entscheid 2026-10-23), nicht als Eintrag im Bildlexikon und nicht als Bild in
Strukturbildern (dort steht ihr Name ohnehin im Text).

Wiederkehrend ist eine Person (Lexikon-Art «person»), wenn
  - sie in den Bildaufträgen und Szenenplänen in mindestens 3 Kapiteln vorkommt, oder
  - sie in mindestens 2 Büchern vorkommt, oder
  - sie in der Liste «kern» steht (Hauptpersonen der biblischen Erzählung, die in vielen Kapiteln handeln, auch wo es noch keine
    Bilder gibt: bilder_aquarell_daten/personen.json).
Gruppen und Rollen (Menge, Jünger, Priester, Soldat, Witwe …) sind allgemeine Typen und bleiben im Bildlexikon.
Gott, Jesus und der Heilige Geist bleiben immer.

    python3 scripts/authoring/personen.py        # Übersicht: wiederkehrend / nur Namensschild
"""
import collections
import glob
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
LEX = ROOT / "data/illustrations/lexicon"
DATEN = ROOT / "scripts/authoring/bilder_aquarell_daten"
_cache = None


def _kapitel(ref):
    m = re.match(r"([1-3A-Z]{3})\.(\d+)", ref or "")
    return (m.group(1), m.group(0)) if m else ((ref or "")[:3], (ref or "")[:3])


def vorkommen():
    """Lexikon-ID → (Bücher, Kapitel), aus allen Bildaufträgen und Aquarell-Szenenplänen."""
    buecher, kapitel = collections.defaultdict(set), collections.defaultdict(set)

    def add(f, ref):
        b, k = _kapitel(ref)
        buecher[f].add(b)
        kapitel[f].add(k)
    for p in glob.glob(str(ROOT / "data/illustrations/briefs/*.json")):
        d = json.loads(pathlib.Path(p).read_text(encoding="utf-8"))
        for pa in d.get("panels", []):
            for f in pa.get("figures", []) + pa.get("objects", []):
                add(f, pa.get("reference") or d.get("reference"))
    for p in glob.glob(str(DATEN / "szenen-*.json")):
        for sz in json.loads(pathlib.Path(p).read_text(encoding="utf-8"))["szenen"].values():
            for f in sz.get("depicts", []):
                add(f, sz.get("reference"))
            sx = sz.get("struktur") or {}
            for e in (sx.get("elemente") or []) + [sx.get("mitte") or {}]:
                for f in e.get("depicts") or []:
                    add(f, e.get("ref") or sz.get("reference"))
    return buecher, kapitel


def daten():
    global _cache
    if _cache is None:
        kern = set(json.loads((DATEN / "personen.json").read_text(encoding="utf-8"))["kern"])
        buecher, kapitel = vorkommen()
        art = {}
        for p in LEX.glob("FIG-*.json"):
            lx = json.loads(p.read_text(encoding="utf-8"))
            art[lx["id"]] = lx.get("kind")
        nur_name = {f for f, k in art.items() if k == "person" and f not in kern and len(kapitel[f]) < 3 and len(buecher[f]) < 2}
        _cache = {"nur_name": nur_name, "art": art, "kapitel": kapitel, "buecher": buecher}
    return _cache


def nur_namensschild(fid):
    """True, wenn die Person kein eigenes Bild bekommt (nur Namensschild)."""
    return fid in daten()["nur_name"]


if __name__ == "__main__":
    d = daten()
    personen = sorted(f for f, k in d["art"].items() if k == "person")
    wieder = [f for f in personen if f not in d["nur_name"]]
    print(f"{len(personen)} Personen: {len(wieder)} wiederkehrend (eigenes Bild), {len(d['nur_name'])} nur Namensschild")
    print("wiederkehrend: " + ", ".join(wieder))
