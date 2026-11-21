#!/usr/bin/env python3
"""Weitere Zugänge auf der Ebene Bibel: Bibliothek, grosse Geschichte, Zeitleiste, Karte (Entscheid Andi Neck 2026-11-21,
docs/VISUELLE-SPRACHE.md «Entscheide»; Phase 1 «Gerüst»). Der Zoom bleibt Hauptzugang; die übrigen sind Varianten, die man auf
der obersten Ebene umschaltet.

Inhalte: scripts/authoring/zugaenge_daten.json (Texte de/gsw, Stationen, Epochen, Orte). Daraus entsteht mit `daten()` das Paket,
das scripts/build_bible.py in das Übersichtspaket der App legt (Schlüssel «zug»); die App zeichnet die Zugänge daraus (HTML) und
die Karte als SVG. Alle Farben sind Rollen (CSS-Variablen --sk-… mit Vorgabe), wie die Strukturbilder (docs/BILDSTIL.md).

    python3 scripts/authoring/zugaenge.py                  # prüfen (Bücher, Stellen, Mundart) und Übersicht ausgeben
    python3 scripts/authoring/zugaenge.py ne <ordner>      # Umrisse aus Natural Earth 1:50 Mio. (GeoJSON) in vendor/naturalearth/ übernehmen
    python3 scripts/authoring/zugaenge.py vignetten <ordner>  # Pilot-Vignetten G1…G8 (PNG) zugeschnitten als WebP nach pilot/visuell/vignetten/

Quellen: Natural Earth (gemeinfrei) für Küsten, Flüsse und Seen, vereinfacht und auf den Ausschnitt beschnitten; Inhaltsarten
(Schätzung je Kapitel) aus pilot/visuell/inhaltsarten.json; Vignetten der grossen Geschichte aus dem Pilotlauf (ungeprüft).
"""
import base64
import json
import math
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATEN = ROOT / "scripts/authoring/zugaenge_daten.json"
NE = ROOT / "vendor/naturalearth/naturalearth-orient.json"
VIG = ROOT / "pilot/visuell/vignetten"
ARTEN = ROOT / "pilot/visuell/inhaltsarten.json"
NAV = ROOT / "data/navigation/NAV-PROT66-KJV.json"
BOX = (8.0, 22.0, 54.0, 46.0)   # Ausschnitt der übernommenen Umrisse (lon0, lat0, lon1, lat1)


# ------------------------------------------------------------------ Natural Earth übernehmen (einmalig, reproduzierbar)

def _clip(ring, box):
    """Sutherland-Hodgman: Ring (Liste [lon, lat]) auf ein Rechteck beschneiden."""
    x0, y0, x1, y1 = box
    def cut(pts, inside, inter):
        out = []
        for i, p in enumerate(pts):
            q = pts[i - 1]
            if inside(p):
                if not inside(q):
                    out.append(inter(q, p))
                out.append(p)
            elif inside(q):
                out.append(inter(q, p))
        return out
    def ix(x):
        return lambda a, b: [x, a[1] + (b[1] - a[1]) * (x - a[0]) / (b[0] - a[0])]
    def iy(y):
        return lambda a, b: [a[0] + (b[0] - a[0]) * (y - a[1]) / (b[1] - a[1]), y]
    pts = ring
    for inside, inter in ((lambda p: p[0] >= x0, ix(x0)), (lambda p: p[0] <= x1, ix(x1)),
                          (lambda p: p[1] >= y0, iy(y0)), (lambda p: p[1] <= y1, iy(y1))):
        if not pts:
            break
        pts = cut(pts, inside, inter)
    return pts


def _dp(pts, eps):
    """Douglas-Peucker (Grad)."""
    if len(pts) < 3:
        return pts
    a, b = pts[0], pts[-1]
    dx, dy = b[0] - a[0], b[1] - a[1]
    n = math.hypot(dx, dy) or 1e-9
    dmax, imax = 0, 0
    for i in range(1, len(pts) - 1):
        d = abs(dy * pts[i][0] - dx * pts[i][1] + b[0] * a[1] - b[1] * a[0]) / n if n > 1e-9 else math.hypot(pts[i][0] - a[0], pts[i][1] - a[1])
        if d > dmax:
            dmax, imax = d, i
    if dmax <= eps:
        return [a, b]
    return _dp(pts[:imax + 1], eps)[:-1] + _dp(pts[imax:], eps)


def _ringe(geom):
    if geom["type"] == "Polygon":   # Aussenring und Löcher (z. B. Schwarzes Meer, Kaspisches Meer); gezeichnet mit evenodd
        return geom["coordinates"]
    if geom["type"] == "MultiPolygon":
        return [r for p in geom["coordinates"] for r in p]
    if geom["type"] == "LineString":
        return [geom["coordinates"]]
    if geom["type"] == "MultiLineString":
        return geom["coordinates"]
    return []


def ne_import(ordner):
    o = pathlib.Path(ordner)
    land = json.loads((o / "ne_50m_land.geojson").read_text(encoding="utf-8"))
    fluesse = json.loads((o / "ne_50m_rivers_lake_centerlines.geojson").read_text(encoding="utf-8"))
    seen = json.loads((o / "ne_50m_lakes.geojson").read_text(encoding="utf-8"))
    r2 = lambda pts: [[round(x, 3), round(y, 3)] for x, y in pts]  # noqa: E731
    out = {"quelle": "Natural Earth 1:50 Mio. (ne_50m_land, ne_50m_rivers_lake_centerlines, ne_50m_lakes), gemeinfrei, "
                     "https://www.naturalearthdata.com; beschnitten auf lon 8–54, lat 22–46, vereinfacht (Douglas-Peucker 0,01°).",
           "land": [], "fluesse": {}, "seen": {}}
    for f in land["features"]:
        for ring in _ringe(f["geometry"]):
            c = _clip([list(p) for p in ring], BOX)
            if len(c) >= 4:
                c = _dp(c + [c[0]], 0.01)
                if len(c) >= 4:
                    out["land"].append(r2(c))
    for f in fluesse["features"]:
        name = f["properties"].get("name")
        if name in ("Nile", "Euphrates", "Tigris", "Jordan"):
            for line in _ringe(f["geometry"]):
                inner = [p for p in line if BOX[0] <= p[0] <= BOX[2] and BOX[1] <= p[1] <= BOX[3]]
                if len(inner) >= 2:
                    out["fluesse"].setdefault(name, []).append(r2(_dp(inner, 0.005)))
    for f in seen["features"]:
        name = f["properties"].get("name")
        if name in ("Dead Sea", "Sea of Galilee"):
            for ring in _ringe(f["geometry"]):
                out["seen"].setdefault(name, []).append(r2(_dp([list(p) for p in ring], 0.003)))
    NE.parent.mkdir(parents=True, exist_ok=True)
    NE.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"PASS: {NE.relative_to(ROOT)}: {len(out['land'])} Landflächen, Flüsse {sorted(out['fluesse'])}, Seen {sorted(out['seen'])}, "
          f"{NE.stat().st_size // 1024} KB")


def vignetten_import(ordner):
    from PIL import Image
    d = json.loads(DATEN.read_text(encoding="utf-8"))
    VIG.mkdir(parents=True, exist_ok=True)
    for st in d["stationen"]:
        im = Image.open(pathlib.Path(ordner) / f"{st['id']}.png").convert("RGB")
        w, h = im.size
        c = st["crop"]
        im = im.crop((int(c[0] * w), int(c[1] * h), int(c[2] * w), int(c[3] * h)))
        im.thumbnail((480, 480), Image.LANCZOS)
        im.save(VIG / f"{st['id']}.webp", "WEBP", quality=78, method=6)
        print(f"{st['id']}.webp {im.size} {(VIG / (st['id'] + '.webp')).stat().st_size // 1024} KB")


# ------------------------------------------------------------------ Karte (SVG, Farben als Rollen)

def _proj(k):
    (lo0, lo1), (la0, la1), W = k["lon"], k["lat"], k["breite"]
    cos = math.cos(math.radians((la0 + la1) / 2))
    s = W / ((lo1 - lo0) * cos)
    H = round((la1 - la0) * s)
    return (lambda lon, lat: ((lon - lo0) * cos * s, (la1 - lat) * s)), W, H


def _pfad(pts, p, zu):
    return "M" + "L".join("%.1f %.1f" % p(x, y) for x, y in pts) + ("Z" if zu else "")


def karte_svg(name, k, ne, mit_rahmen=None):
    p, W, H = _proj(k)
    (lo0, lo1), (la0, la1) = k["lon"], k["lat"]
    box = (lo0 - 0.5, la0 - 0.5, lo1 + 0.5, la1 + 0.5)
    land = []
    for ring in ne["land"]:
        c = _clip(ring, box)
        if len(c) >= 3:
            land.append(_pfad(c, p, True))
    o = [f'<svg class="zg-map-svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" preserveAspectRatio="xMidYMid meet" aria-hidden="true" focusable="false">',
         f'<rect width="{W}" height="{H}" style="fill:var(--sk-b,#DDF2F3)"/>',
         f'<path class="zg-land" d="{"".join(land)}" style="fill:var(--sk-karte,#FFFFFF);fill-rule:evenodd;stroke:var(--sk-linie,#DCE4E7);stroke-width:.8"/>']
    breit = 1.6 if name == "ausschnitt" else 1.1
    for fl, linien in sorted(ne["fluesse"].items()):
        for ln in linien:
            o.append(f'<path d="{_pfad(ln, p, False)}" style="fill:none;stroke:var(--sk-b-text,#00939A);stroke-opacity:.55;stroke-width:{breit};stroke-linejoin:round;stroke-linecap:round"/>')
    for se, ringe in sorted(ne["seen"].items()):
        for ring in ringe:
            o.append(f'<path d="{_pfad(ring, p, True)}" style="fill:var(--sk-b,#DDF2F3);stroke:var(--sk-b-text,#00939A);stroke-opacity:.45;stroke-width:.6"/>')
    if mit_rahmen:   # Lage des Ausschnitts «Land Israel» auf der Übersichtskarte
        (a0, a1), (b0, b1) = mit_rahmen["lon"], mit_rahmen["lat"]
        x0, y0 = p(a0, b1)
        x1, y1 = p(a1, b0)
        o.append(f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{x1 - x0:.1f}" height="{y1 - y0:.1f}" rx="2" style="fill:none;stroke:var(--sk-a-text,#E76444);stroke-width:1.2;stroke-dasharray:3 2"/>')
    o.append("</svg>")
    return "".join(o), p, W, H


# ------------------------------------------------------------------ Paket für die App

def daten():
    d = json.loads(DATEN.read_text(encoding="utf-8"))
    nav = json.loads(NAV.read_text(encoding="utf-8"))
    arten = json.loads(ARTEN.read_text(encoding="utf-8"))
    ab = d["abkuerzungen"].split()
    abk = dict(zip(ab[0::2], ab[1::2]))
    fam_von = {a: f["k"] for f in d["familien"] for a in f["arten"]}
    verse = {b["code"]: sum(b["verses_per_chapter"]) for b in nav["books"]}
    gruppen = [{"id": g["id"], "t": g["testament"], "de": g["de"], "gsw": d["gruppen_gsw"][g["id"]], "b": g["books"]} for g in nav["groups"]]
    buecher = {}
    for code, n in verse.items():
        f = {}
        for a, v in arten["je_buch"].get(code, {}).items():
            f[fam_von[a]] = f.get(fam_von[a], 0) + v
        buecher[code] = {"v": n, "a": abk[code], "f": [f.get(x["k"], 0) for x in d["familien"]]}
    story = []
    for st in d["stationen"]:
        f = VIG / f"{st['id']}.webp"
        img = "data:image/webp;base64," + base64.b64encode(f.read_bytes()).decode() if f.exists() else None
        story.append({"id": st["id"], "ref": st["ref"], "img": img, "de": st["de"], "gsw": st["gsw"]})
    ne = json.loads(NE.read_text(encoding="utf-8"))
    karten = {}
    k = d["karte"]
    for name in ("haupt", "ausschnitt"):
        svg, p, W, H = karte_svg(name, k[name], ne, k["ausschnitt"] if name == "haupt" else None)
        orte = []
        for o in sorted((o for o in k["orte"] if o["karte"] == name), key=lambda o: o["prio"]):
            x, y = p(o["lon"], o["lat"])
            orte.append({"id": o["id"], "x": round(100 * x / W, 2), "y": round(100 * y / H, 2), "de": o["de"], "gsw": o["gsw"], "b": o["b"],
                         **({"u": 1} if o.get("unsicher") else {}), **({"zu": "ausschnitt"} if o.get("ausschnitt") else {})})
        wasser = []
        for w in (w for w in k["wasser"] if w["karte"] == name):
            x, y = p(w["lon"], w["lat"])
            wasser.append({"id": w["id"], "x": round(100 * x / W, 2), "y": round(100 * y / H, 2), "de": w["de"], "gsw": w["gsw"]})
        karten[name] = {"svg": svg, "w": W, "h": H, "orte": orte, "wasser": wasser}
    return {"labels": d["labels"], "fam": [{"k": f["k"], "de": f["de"], "gsw": f["gsw"]} for f in d["familien"]], "groups": gruppen,
            "books": buecher, "story": story, "time": d["zeit"], "map": karten}


def pruefen():
    """Bücher und Stellen gültig, Mundart nach scripts/mundart.py, Bilder vorhanden."""
    sys.path.insert(0, str(ROOT / "scripts"))
    import mundart
    d = json.loads(DATEN.read_text(encoding="utf-8"))
    codes = {b["code"] for b in json.loads(NAV.read_text(encoding="utf-8"))["books"]}   # 66 Bücher des Navigationsgerüsts
    fehler = []
    def bk(liste, wo):
        for x in liste:
            if x[0] not in codes:
                fehler.append(f"{wo}: unbekanntes Buch {x[0]}")
    z = d["zeit"]
    for e in z["folge"] + z["epochen"]:
        bk(e["b"], e["id"])
    bk(z["frei"], "frei")
    for o in d["karte"]["orte"]:
        bk(o["b"], o["id"])
    for st in d["stationen"]:
        if st["ref"].split(".")[0] not in codes:
            fehler.append(f"{st['id']}: Stelle {st['ref']}")
        if not (VIG / f"{st['id']}.webp").exists():
            fehler.append(f"{st['id']}: Bild fehlt ({VIG.relative_to(ROOT)})")
    zeit_buecher = {b[0] for e in z["folge"] + z["epochen"] for b in e["b"]} | {b[0] for b in z["frei"]}
    fehlt = sorted(codes - zeit_buecher)
    if fehlt:
        fehler.append("Zeitleiste ohne Bücher: " + ", ".join(fehlt))
    gsw = []
    def sammle(o):
        if isinstance(o, dict):
            for k_, v in o.items():
                if k_ == "gsw" and isinstance(v, str):
                    gsw.append(v)
                elif k_ == "gsw" and isinstance(v, dict):
                    gsw.extend(x for x in v.values() if isinstance(x, str))
                else:
                    sammle(v)
        elif isinstance(o, list):
            for v in o:
                sammle(v)
    sammle(d)
    gsw.extend(d["labels"]["gsw"].values())
    for s in gsw:
        for m in mundart.pruefe(s):
            fehler.append(f"Mundart: «{s}»: {m}")
    for s in [x for x in d["labels"]["de"].values()] + [st["de"]["x"] for st in d["stationen"]]:
        if "ß" in s:
            fehler.append(f"ß in «{s}» (Schweizer Schreibung)")
    return fehler


def main(argv):
    if argv[:1] == ["ne"]:
        ne_import(argv[1])
        return 0
    if argv[:1] == ["vignetten"]:
        vignetten_import(argv[1])
        return 0
    f = pruefen()
    p = daten()
    roh = len(json.dumps(p, ensure_ascii=False))
    print(f"Zugänge: {len(p['books'])} Bücher, {len(p['story'])} Stationen ({sum(1 for s in p['story'] if s['img'])} mit Bild), "
          f"{len(p['time']['folge']) + len(p['time']['epochen'])} Epochen, {sum(len(k['orte']) for k in p['map'].values())} Orte; {roh // 1024} KB")
    for x in f:
        print("FEHLER:", x)
    print("PASS: Zugänge geprüft" if not f else f"FAIL: {len(f)} Fehler")
    return 1 if f else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
