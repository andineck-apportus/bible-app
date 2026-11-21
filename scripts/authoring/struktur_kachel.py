#!/usr/bin/env python3
"""Strukturkacheln: gezeichnete Bildfelder aus Daten (Form je Feld, Entscheid Andi Neck 2026-11-21, docs/VISUELLE-SPRACHE.md).

Wo der Text nicht erzählt, zeigt ein Strukturbild die Gestalt des Textes (Spalten, Kette, Raster, Reihe, Kurve, Spiegel, Ebenen,
Ringe, Lager). Typen und Datenformat: scripts/authoring/buchgeruest.py (FORMAT). Beschriftungen zweisprachig (Klassen lw-de,
lw-gsw; die App blendet die gewählte Sprache ein). Je Glied Bilder des Bildlexikons (vignetten.py), Gott als Strahlenkranz.

Masse (Rückmeldung Andi Neck 2026-11-21: Platz gut nutzen, gute Abstände, wie die früheren gezeichneten Strukturen): gezeichnet in
der Grösse, in der die App die Kachel zeigt (BREITE = 340 Einheiten = 340 px, Schrift 12–15 px), die Höhe ergibt sich aus dem
Inhalt: Kästen so hoch wie ihr Inhalt, gleichmässige Abstände (Innenabstand PAD, Lücke LUECKE, Kachelrand RAND). zeichne() liefert
(svg, hoehe); bilder_aquarell.kachel() skaliert auf die Breite der gemalten Kacheln und hängt das Band an.

Feste Prüfungen (pruefe): Beschriftungen kurz genug, Stellen gültig, beide Sprachen; Layout: struktur_layout.py.
"""
import html
import math

BREITE = 440         # App zeigt gezeichnete und gemalte Kacheln bis 480 px breit (Rückmeldung 2026-11-21: 340 war zu klein)
RAND, PAD, LUECKE = 12, 9, 8
# Frisches Farbschema (Rückmeldung Andi Neck 2026-11-21: Beige und Ränder wirkten alt und verwelkt): helle Fläche, weisse Karten
# mit weichem Schatten statt Rand, klare Akzente Koralle (Seite a), Petrol (Seite b), Sonnengelb (betont).
PAPER, INK, MUTED, RULE = "#F6F9FA", "#1E2629", "#76828A", "#DCE4E7"
FARBE = {"a": ("#FFECE5", "#F0563A"), "b": ("#E2F6F5", "#0E9AA0"), "n": ("#FFFFFF", "#4E9A3E"), "akzent": "#F0563A"}
SANS = "Inter, Helvetica, Arial, sans-serif"
SERIF = SANS
FS, FS_KLEIN, FS_REF, FS_TITEL = 14, 13, 10.5, 17
ZW = 0.56            # mittlere Zeichenbreite (Anteil der Schriftgrösse), mit Reserve; die Layoutprüfung misst nach
ZH = 1.25            # Zeilenhöhe
BILD_H = 56          # Höhe der Bildzeile eines Glieds
BETONT = "#F6FA8C"   # Fläche betonter Glieder (Höhepunkt, Pointe)
_V = {}              # Bilder der Kachel, die gerade gezeichnet wird: Schlüssel («1», «2», …, «m») → Liste


def zeilen(e, breite, fs):
    """Zeilen je Sprache für die Breite; liefert (Zeichen je Zeile, grösste Zeilenzahl)."""
    n = max(4, int(breite / (fs * ZW)))
    return n, max(len(umbruch(e.get(lg) or e.get("de") or "", n)) or 1 for lg in ("de", "gsw"))


def text(x, y_oben, e, breite, fs=FS, anchor="middle", fill=INK, weight=400, serif=False, strike=False, italic=False):
    """Beschriftung in beiden Sprachen ab y_oben; liefert (svg, hoehe)."""
    n, z = zeilen(e, breite, fs)
    out = []
    for lg in ("de", "gsw"):
        t = e.get(lg) or e.get("de") or ""
        zs = umbruch(t, n) or [""]
        spans = "".join(f'<tspan x="{x:.1f}" dy="{(0 if i == 0 else fs * ZH):.1f}">{esc(s)}</tspan>' for i, s in enumerate(zs))
        # bei weniger Zeilen in dieser Sprache vertikal mittig im Platz für z Zeilen
        y0 = y_oben + fs * 0.92 + (z - len(zs)) * fs * ZH / 2
        out.append(f'<text class="lw lw-{lg}" x="{x:.1f}" y="{y0:.1f}" font-family="{SERIF if serif else SANS}" font-size="{fs}" '
                   f'text-anchor="{anchor}" fill="{fill}" font-weight="{weight}"'
                   + (' text-decoration="line-through"' if strike else "") + (' font-style="italic"' if italic else "") + f'>{spans}</text>')
    return "".join(out), z * fs * ZH


def ref_text(x, y_unten, ref, anchor="end"):
    return (f'<text x="{x:.1f}" y="{y_unten - 2:.1f}" font-family="{SANS}" font-size="{FS_REF}" fill="{MUTED}" text-anchor="{anchor}">'
            f'{esc(stelle(ref))}</text>') if ref else ""


def box(x, y, w, h, seite="n", betont=False, gestrichen=False, rx=10):
    fill, _ = FARBE.get(seite, FARBE["n"])
    if gestrichen:
        fill = "#EEF0F0"
    if betont:   # wärmere Fläche statt Rahmen in Akzentfarbe (wirkte wie «ausgewählt», Rückmeldung 2026-11-21)
        fill = BETONT
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" filter="url(#sk-schatten)"/>'


def pfeil(x1, y1, x2, y2, farbe=MUTED):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{farbe}" stroke-width="1.8" stroke-linecap="round" marker-end="url(#sk-pf)"/>'


def marke_svg(x, y, m):
    return (f'<circle cx="{x + 9:.1f}" cy="{y + 9:.1f}" r="9" fill="{INK}" fill-opacity=".86"/>'
            f'<text x="{x + 9:.1f}" y="{y + 13:.1f}" font-family="{SANS}" font-size="11" font-weight="600" text-anchor="middle" fill="#FFFFFF">{esc(m)}</text>')


class Glied:
    """Ein Glied als Kasten, so hoch wie sein Inhalt: Marke oben links, Bilder des Bildlexikons, Beschriftung, Stelle unten rechts."""

    def __init__(self, e, k=None, breite=150, marke=None, seite="n", fs=FS, bild_h=BILD_H, anchor="middle"):
        self.e, self.k, self.b, self.marke, self.seite, self.fs, self.anchor = e, k, breite, marke, seite, fs, anchor
        self.bild = bool(k is not None and _V.get(str(k)))
        self.bild_h = bild_h if self.bild else 0
        self.links = 24 if marke is not None else 0
        self.iw = breite - 2 * PAD - self.links
        laengstes = max((len(w) for lg in ("de", "gsw") for w in (e.get(lg) or "").split()), default=1)
        while laengstes * fs * ZW > self.iw and fs > 9.5:   # langes Wort (z. B. «Versöhnungstag») in schmaler Zelle: Schrift kleiner
            fs -= 0.5
        self.fs = fs
        _, z = zeilen(e, self.iw, fs)
        self.th = z * fs * ZH
        self.ref_h = 13 if e.get("ref") else 0
        oben = max(self.bild_h + (4 if self.bild else 0), 0)
        self.h = PAD + oben + self.th + self.ref_h + PAD
        if marke is not None:
            self.h = max(self.h, 2 * PAD + 18)

    def svg(self, x, y, h=None):
        h = h or self.h
        e = self.e
        o = [box(x, y, self.b, h, self.seite, e.get("betont"), e.get("gestrichen"))]
        if self.marke is not None:
            o.append(marke_svg(x + PAD - 2, y + PAD - 2, self.marke))
        ix = x + PAD + self.links
        inhalt = self.bild_h + (4 if self.bild else 0) + self.th + self.ref_h
        yy = y + PAD + (h - 2 * PAD - inhalt) / 2     # Inhalt mittig, wenn der Kasten höher ist (gleiche Zeilenhöhe)
        if self.bild:
            o.append(vign(self.k, ix, yy, self.iw, self.bild_h))
            yy += self.bild_h + 4
        tx = ix + self.iw / 2 if self.anchor == "middle" else ix
        s, _ = text(tx, yy, e, self.iw, self.fs, anchor=self.anchor, weight=600 if e.get("betont") else 400,
                    fill=MUTED if e.get("gestrichen") else INK, strike=e.get("gestrichen"))
        o.append(s)
        if e.get("ref"):
            o.append(ref_text(x + self.b - PAD, y + h - PAD + 2, e["ref"]))
        return "".join(o)


def titel(sx, y):
    t = sx.get("titel")
    if not t:
        return "", y
    s, h = text(BREITE / 2, y, t, BREITE - 2 * RAND, FS_TITEL, fill=INK, weight=650)
    return s, y + h + LUECKE


def kopf_svg(e, x, y, w, seite):
    s, h = text(x + w / 2, y, e, w, FS, fill=FARBE[seite][1], weight=600)
    return s, h


def zeichne(sx, vignetten=None):
    """SVG-Inhalt (ohne äusseres svg) und Höhe einer Strukturkachel in BREITE-Einheiten."""
    global _V
    _V = dict(vignetten or {})
    teile, y = titel(sx, RAND)
    el = sx.get("elemente") or []
    inhalt, y = globals()[f"_{sx['typ']}"](sx, el, y)
    hoehe = y + RAND
    return (DEFS + f'<rect width="{BREITE}" height="{hoehe:.1f}" fill="{PAPER}"/>'
            + teile + inhalt), hoehe


def spalten_glieder(glieder, x, y, w):
    """Glieder untereinander; liefert (svg, y_ende)."""
    o = []
    for g in glieder:
        o.append(g.svg(x, y))
        y += g.h + LUECKE
    return "".join(o), y - LUECKE


def _spalten(sx, el, y):
    o = []
    kopf = sx.get("kopf") or {}
    w = (BREITE - 2 * RAND - LUECKE) / 2
    xa, xb = RAND, RAND + w + LUECKE
    if sx.get("mitte"):
        s, h = text(BREITE / 2, y, sx["mitte"], BREITE - 2 * RAND, FS_KLEIN, fill=FARBE["akzent"], italic=True)
        o.append(s)
        y += h + 4
    kh = 0
    for x, s_ in ((xa, "a"), (xb, "b")):
        if kopf.get(s_):
            s, h = kopf_svg(kopf[s_], x, y, w, s_)
            o.append(s)
            kh = max(kh, h)
    y += kh + (4 if kh else 0)
    ende = y
    for x, s_ in ((xa, "a"), (xb, "b")):
        gl = [Glied(e, el.index(e) + 1, w, None, s_) for e in el if e.get("seite") == s_]
        s, ye = spalten_glieder(gl, x, y, w)
        o.append(s)
        ende = max(ende, ye)
    return "".join(o), ende


def _kette(sx, el, y):
    o = []
    w = BREITE - 2 * RAND
    for i, e in enumerate(el):
        g = Glied(e, i + 1, w, None, "n")
        o.append(g.svg(RAND, y))
        y += g.h
        if i < len(el) - 1:
            o.append(pfeil(BREITE / 2, y + 1, BREITE / 2, y + 12))
            y += 14
    return "".join(o), y


def gitter(glieder_fn, n, y, spalten):
    """Glieder im Raster; Zeilenhöhe = höchstes Glied der Zeile, letzte Zeile mittig. glieder_fn(i, breite) → Glied."""
    o = []
    w = (BREITE - 2 * RAND - LUECKE * (spalten - 1)) / spalten
    for r0 in range(0, n, spalten):
        reihe = [glieder_fn(i, w) for i in range(r0, min(n, r0 + spalten))]
        h = max(g.h for g in reihe)
        x = RAND + (spalten - len(reihe)) * (w + LUECKE) / 2
        for g in reihe:
            o.append(g.svg(x, y, h))
            x += w + LUECKE
        y += h + LUECKE
    return "".join(o), y - LUECKE


def spaltenzahl(el, mit_bild):
    lang = max((len(e.get(lg) or "") for e in el for lg in ("de", "gsw")), default=0)
    if len(el) <= 2:
        return len(el) or 1
    if lang <= 22 and len(el) not in (4,):
        return 3
    return 2


def _raster(sx, el, y):
    mit_bild = any(_V.get(str(k)) for k in range(1, len(el) + 1))
    sp = spaltenzahl(el, mit_bild)
    return gitter(lambda i, w: Glied(el[i], i + 1, w, str(i + 1), "n", FS if sp < 3 else FS_KLEIN), len(el), y, sp)


def _reihe(sx, el, y):
    if any(_V.get(str(k)) for k in range(1, len(el) + 1)):
        return _raster(sx, el, y)
    o = []   # nummerierte Stationen untereinander, mit Verbindungslinie
    w = BREITE - 2 * RAND
    gl = [Glied(e, i + 1, w, str(i + 1), "n", anchor="start") for i, e in enumerate(el)]
    for i, g in enumerate(gl):
        o.append(g.svg(RAND, y))
        y += g.h + (LUECKE if i < len(gl) - 1 else 0)
    return "".join(o), y


def _kurve(sx, el, y):
    """Abstieg und Aufstieg als V: Einrückung wächst abwärts und schrumpft aufwärts; die Wende (mitte) am tiefsten Punkt."""
    o = []
    ab = [e for e in el if e.get("richtung") == "ab"]
    auf = [e for e in el if e.get("richtung") == "auf"]
    stufe = 18
    voll = BREITE - 2 * RAND
    folge = [(e, i, "ab") for i, e in enumerate(ab)] + ([(sx["mitte"], len(ab), "mitte")] if sx.get("mitte") else []) \
        + [(e, len(auf) - 1 - i, "auf") for i, e in enumerate(auf)]
    for e, tiefe, r in folge:
        einzug = tiefe * stufe
        k = el.index(e) + 1 if r != "mitte" else "m"
        g = Glied({**e, "betont": e.get("betont") or r == "mitte"}, k, voll - 2 * einzug, "↘" if r == "ab" else "↗" if r == "auf" else None,
                  "a" if r == "ab" else "b" if r == "auf" else "n")
        o.append(g.svg(RAND + einzug, y))
        y += g.h + 4
    return "".join(o), y - 4


def _spiegel(sx, el, y):
    """Umkehrung: Seite a fällt (links, von oben nach unten), Seite b steigt (rechts, von unten nach oben); Wende in der Mitte."""
    o = []
    kopf = sx.get("kopf") or {}
    w = (BREITE - 2 * RAND - LUECKE) / 2
    xa, xb = RAND, RAND + w + LUECKE
    kh = 0
    for x, s_ in ((xa, "a"), (xb, "b")):
        if kopf.get(s_):
            s, h = kopf_svg(kopf[s_], x, y, w, s_)
            o.append(s)
            kh = max(kh, h)
    y += kh + (4 if kh else 0)
    a = [e for e in el if e.get("seite") == "a"]
    b = [e for e in el if e.get("seite") == "b"]
    oben = [Glied(a[0], el.index(a[0]) + 1, w, "▼" if False else None, "a"), Glied(b[-1], el.index(b[-1]) + 1, w, None, "b")] if a and b else []
    unten = [Glied(a[-1], el.index(a[-1]) + 1, w, None, "a"), Glied(b[0], el.index(b[0]) + 1, w, None, "b")] if a and b else []
    h1 = max(g.h for g in oben)
    o.append(oben[0].svg(xa, y, h1) + oben[1].svg(xb, y, h1))
    y += h1
    # Mittelzone: Pfeile (a abwärts links, b aufwärts rechts) und die Wende
    mh = 30
    if sx.get("mitte"):
        _, z = zeilen(sx["mitte"], BREITE - 2 * RAND - 90, FS_KLEIN)
        mh = max(30, z * FS_KLEIN * ZH + 12)
    o.append(pfeil(xa + w / 2, y + 3, xa + w / 2, y + mh - 3, FARBE["a"][1]))
    o.append(pfeil(xb + w / 2, y + mh - 3, xb + w / 2, y + 3, FARBE["b"][1]))
    if sx.get("mitte"):
        s, h = text(BREITE / 2, y + (mh - z * FS_KLEIN * ZH) / 2, sx["mitte"], BREITE - 2 * RAND - 90, FS_KLEIN, fill=FARBE["akzent"], italic=True)
        o.append(s)
    y += mh
    h2 = max(g.h for g in unten)
    o.append(unten[0].svg(xa, y, h2) + unten[1].svg(xb, y, h2))
    return "".join(o), y + h2


def _ebenen(sx, el, y):
    o = []
    kopf = sx.get("kopf") or {}
    for s_ in ("a", "b"):
        reihe = [e for e in el if e.get("seite") == s_]
        if not reihe:
            continue
        y_start = y
        teile = []
        yy = y + PAD
        if kopf.get(s_):
            s, h = text(RAND + PAD, yy, kopf[s_], BREITE - 2 * RAND - 2 * PAD, FS, anchor="start", fill=FARBE[s_][1], weight=600)
            teile.append(s)
            yy += h + 4
        sp = min(3, len(reihe))
        s, ye = gitter_innen(reihe, el, yy, sp, s_)
        teile.append(s)
        y = ye + PAD
        fill, rand = FARBE[s_]
        o.append(f'<rect x="{RAND}" y="{y_start:.1f}" width="{BREITE - 2 * RAND}" height="{y - y_start:.1f}" rx="8" fill="{fill}" fill-opacity=".5" '
                 f'stroke="{rand}" stroke-opacity=".4"/>' + "".join(teile))
        y += LUECKE
    return "".join(o), y - LUECKE


def gitter_innen(reihe, el, y, sp, seite):
    o = []
    x0, breite = RAND + PAD, BREITE - 2 * RAND - 2 * PAD
    w = (breite - LUECKE * (sp - 1)) / sp
    for r0 in range(0, len(reihe), sp):
        zeile = [Glied(e, el.index(e) + 1, w, None, seite) for e in reihe[r0:r0 + sp]]
        h = max(g.h for g in zeile)
        x = x0 + (sp - len(zeile)) * (w + LUECKE) / 2
        for g in zeile:
            o.append(g.svg(x, y, h))
            x += w + LUECKE
        y += h + LUECKE
    return "".join(o), y - LUECKE


def _ringe(sx, el, y):
    """Rahmen und Mitte als ineinanderliegende Rahmen: jeder Rahmen trägt oben sein erstes Glied (A), unten das entsprechende
    letzte (A′); innen die Mitte. Höhe nach Inhalt."""
    n = len(el)
    paare = [(el[i], el[n - 1 - i]) for i in range(n // 2)]
    rest = el[n // 2] if n % 2 else None
    mitte = sx.get("mitte") or rest
    if rest is not None and sx.get("mitte"):
        paare.append((rest, None))
    marken = "ABCDEF"
    farben = ["#FFECE5", "#E2F6F5", "#FAFCD2", "#EAF7E6"]
    einzug = 12
    # Höhen der Bänder vorab
    def band(i, e, m):
        if not e:
            return 6, None
        w = BREITE - 2 * (RAND + i * einzug) - 2 * PAD - 20
        g = Glied(e, el.index(e) + 1, w + 2 * PAD + 20, m, "n", anchor="start")
        return g.th + g.ref_h + g.bild_h + (4 if g.bild else 0) + 2 * PAD, g
    oben = [band(i, l, marken[i]) for i, (l, r) in enumerate(paare)]
    unten = [band(i, r, marken[i] + "′") for i, (l, r) in enumerate(paare)]
    mg = None
    if mitte:
        i = len(paare)
        mg = Glied({**mitte, "betont": True}, "m", BREITE - 2 * (RAND + i * einzug), None, "a", FS + 0.5, 54)
    innen_h = mg.h if mg else 0
    gesamt = sum(h for h, _ in oben) + sum(h for h, _ in unten) + innen_h
    o = []
    y_top, y_bot = y, y + gesamt
    for i, ((ho, go), (hu, gu)) in enumerate(zip(oben, unten)):
        x, w = RAND + i * einzug, BREITE - 2 * (RAND + i * einzug)
        o.append(f'<rect x="{x}" y="{y_top:.1f}" width="{w}" height="{y_bot - y_top:.1f}" rx="{10 - i}" fill="{farben[i % 4]}" '
                 f'filter="url(#sk-schatten)"/>')
        for g, yy, hh in ((go, y_top, ho), (gu, y_bot - hu, hu)):
            if not g:
                continue
            o.append(marke_svg(x + PAD - 2, yy + PAD - 2, g.marke))
            s, _ = text(x + PAD + 26, yy + PAD, g.e, w - 2 * PAD - 26, FS, anchor="start", weight=600 if g.e.get("betont") else 400)
            o.append(s + ref_text(x + w - PAD, yy + hh - PAD + 2, g.e.get("ref")))
        y_top += ho
        y_bot -= hu
    if mg:
        o.append(mg.svg(RAND + len(paare) * einzug, y_top))
    return "".join(o), y + gesamt


def _lager(sx, el, y):
    """Lagerplan um eine Mitte (Num 2), Norden oben: West und Ost als Spalten links und rechts über die ganze Höhe, in der Mitte
    Nord, der Ring («innen») mit der Mitte, Süd."""
    o = []
    seiten = {e.get("seite"): e for e in el}
    nr = {e.get("seite"): k for k, e in enumerate(el, 1)}
    sw = 122
    cw = BREITE - 2 * RAND - 2 * sw - 2 * LUECKE
    cx = RAND + sw + LUECKE
    mitte = []
    if seiten.get("n"):
        mitte.append(("g", Glied(seiten["n"], nr["n"], cw, "N")))
    ring = None
    m = dict(sx.get("mitte") or {}, betont=True)
    mg = Glied(m, "m", cw - (2 * PAD if seiten.get("innen") else 0), None, "a", FS + 0.5, 54)
    if seiten.get("innen"):
        e = seiten["innen"]
        _, z = zeilen(e, cw - 2 * PAD - 30, FS_KLEIN)
        kopf_h = z * FS_KLEIN * ZH
        ring = (e, kopf_h, PAD + kopf_h + 4 + mg.h + PAD)
    mitte.append(("ring", ring) if ring else ("g", mg))
    if seiten.get("s"):
        mitte.append(("g", Glied(seiten["s"], nr["s"], cw, "S")))
    hoehe = sum((t[1].h if t[0] == "g" else t[1][2]) for t in mitte) + LUECKE * (len(mitte) - 1)
    yy = y
    for art, g in mitte:
        if art == "g":
            o.append(g.svg(cx, yy))
            yy += g.h + LUECKE
        else:
            e, kh, rh = g
            o.append(f'<rect x="{cx:.1f}" y="{yy:.1f}" width="{cw:.1f}" height="{rh:.1f}" rx="10" fill="none" stroke="{FARBE["b"][1]}" '
                     f'stroke-width="1.2" stroke-dasharray="5 4"/>')
            s, _ = text(cx + PAD, yy + PAD, e, cw - 2 * PAD - 30, FS_KLEIN, anchor="start", fill=FARBE["b"][1], weight=600)
            o.append(s)
            o.append(ref_text(cx + cw - PAD, yy + PAD + FS_KLEIN + 1, e.get("ref")))
            o.append(mg.svg(cx + PAD, yy + PAD + kh + 4))
            yy += rh + LUECKE
    for k, x, m_ in (("w", RAND, "W"), ("o", BREITE - RAND - sw, "O")):
        if seiten.get(k):
            g = Glied(seiten[k], nr[k], sw, m_, bild_h=56)
            o.append(g.svg(x, y, max(g.h, hoehe)))
            hoehe = max(hoehe, g.h)
    return "".join(o), y + hoehe


def esc(s):
    return html.escape(str(s), quote=True)


def stelle(ref):
    """GEN.1.3 → 1,3; GEN.1.3-GEN.1.9 → 1,3–9; GEN.1.3-GEN.2.4 → 1,3 – 2,4; GEN.12 → Kap. 12."""
    if not ref:
        return ""
    a, _, z = ref.partition("-")
    pa = a.split(".")
    if len(pa) == 2:
        return f"Kap. {pa[1]}"
    if not z:
        return f"{pa[1]},{pa[2]}"
    pz = z.split(".")
    if len(pz) == 2:
        return f"{pa[1]},{pa[2]} – Kap. {pz[1]}"
    return f"{pa[1]},{pa[2]}–{pz[2]}" if pz[1] == pa[1] else f"{pa[1]},{pa[2]} – {pz[1]},{pz[2]}"


def umbruch(s, n):
    zeilen, z = [], ""
    for w in str(s).split():
        if len(z) + len(w) + (1 if z else 0) > n and z:
            zeilen.append(z)
            z = w
        else:
            z = (z + " " + w).strip()
    return zeilen + ([z] if z else [])


DEFS = ('<defs><marker id="sk-pf" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
        '<path d="M0 0L10 5L0 10z" fill="#7A8489"/></marker>'
        '<filter id="sk-schatten" x="-10%" y="-10%" width="120%" height="130%"><feDropShadow dx="0" dy="1" stdDeviation="1.6" flood-color="#22292C" flood-opacity=".13"/></filter>'
        '<radialGradient id="sk-wash" cx="30%" cy="25%" r="80%"><stop offset="0" stop-color="#EFE6D6" stop-opacity=".9"/>'
        '<stop offset="1" stop-color="#FBF8F1" stop-opacity="0"/></radialGradient>'
        '<radialGradient id="sk-glorie" r="50%"><stop offset=".3" stop-color="#E9B954" stop-opacity=".95"/><stop offset="1" stop-color="#E9B954" stop-opacity="0"/></radialGradient>'
        '<filter id="sk-aq" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence type="fractalNoise" baseFrequency=".06" numOctaves="2" seed="7"/>'
        '<feDisplacementMap in="SourceGraphic" scale="3.5"/><feGaussianBlur stdDeviation=".35"/></filter>'
        # Papier der gemalten Einzelbilder auf Weiss heben; mit Multiplizieren verschwindet es auf der Kachel
        '<filter id="sk-papier" color-interpolation-filters="sRGB"><feComponentTransfer><feFuncR type="linear" slope="1.12"/>'
        '<feFuncG type="linear" slope="1.12"/><feFuncB type="linear" slope="1.14"/></feComponentTransfer></filter></defs>')


def gott_zeichen(cx, cy, s):
    """Gott nach dem Bildlexikon (FIG-GOTT, Entscheid Andi Neck 2026-10-14): goldener Strahlenkranz um eine helle Scheibe mit dem
    Gottesnamen יהוה; nie als Mensch. Gezeichnet (die Buchstaben müssen stimmen), mit Aquarellrand."""
    import math
    r = s / 2
    o = [f'<g filter="url(#sk-aq)"><circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="url(#sk-glorie)" opacity=".55"/>']
    for k in range(24):
        a = k * math.pi / 12
        lang = r * (0.98 if k % 2 == 0 else 0.78)
        b = 0.075
        p = [(cx + r * 0.36 * math.cos(a - b), cy + r * 0.36 * math.sin(a - b)), (cx + lang * math.cos(a), cy + lang * math.sin(a)),
             (cx + r * 0.36 * math.cos(a + b), cy + r * 0.36 * math.sin(a + b))]
        o.append(f'<path d="M{p[0][0]:.1f} {p[0][1]:.1f}L{p[1][0]:.1f} {p[1][1]:.1f}L{p[2][0]:.1f} {p[2][1]:.1f}z" fill="#D9A441" opacity=".75"/>')
    o.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r * 0.4:.1f}" fill="#FFFDF6" stroke="#D9A441" stroke-width="1.2"/></g>')
    o.append(f'<text x="{cx:.1f}" y="{cy + r * 0.13:.1f}" font-family="\'Ezra SIL\', \'SBL Hebrew\', \'Frank Ruehl CLM\', \'Taamey Frank CLM\', David, \'Times New Roman\', serif" '
             f'font-size="{r * 0.36:.1f}" text-anchor="middle" fill="#8A5A12" direction="rtl" font-weight="600">יהוה</text>')
    return "".join(o)


def _ein_bild(h, x, y, w, hh):
    """Ein Bild des Bildlexikons in das Feld x, y, w × hh (Ausschnitt mit dem Motiv, Papier verschwindet)."""
    if h == "#gott":
        g = min(w, hh)
        return gott_zeichen(x + w / 2, y + hh / 2, g)
    href, r = h if isinstance(h, tuple) else (h, None)
    if r:
        bx, by, bw, bh, iw, ih = r
        return (f'<svg x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{hh:.1f}" viewBox="{bx} {by} {bw} {bh}" preserveAspectRatio="xMidYMid meet">'
                f'<image href="{href}" x="0" y="0" width="{iw}" height="{ih}" filter="url(#sk-papier)" style="mix-blend-mode:multiply"/></svg>')
    return (f'<image href="{href}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{hh:.1f}" preserveAspectRatio="xMidYMid meet" '
            f'filter="url(#sk-papier)" style="mix-blend-mode:multiply"/>')


def _seitenverhaeltnis(h):
    if h == "#gott" or not isinstance(h, tuple) or not h[1]:
        return 1.0
    return h[1][2] / h[1][3]


def vign(k, x, y, s, hoehe=None):
    """Bilder des Bildlexikons für ein Glied im Feld s × hoehe. Mehrere Bilder ordnet das Werkzeug so an, dass sie zusammen am
    grössten werden (nebeneinander, untereinander oder zwei und eins); die Anordnung selbst trägt keine Bedeutung."""
    liste = _V.get(str(k))
    if not liste:
        return ""
    if not isinstance(liste, list):
        liste = [liste]
    hoehe = hoehe or s
    a = [_seitenverhaeltnis(h) for h in liste]
    n, gap = len(liste), 4
    def zeilen_teilung(teilung):   # Liste von Zeilen (Indizes); Bilder je Zeile gleich hoch
        hs = []
        for zeile in teilung:
            summe = sum(a[i] for i in zeile)
            hs.append((s - gap * (len(zeile) - 1)) / summe)   # Höhe, bei der die Zeile die Breite füllt
        gesamt = sum(hs) + gap * (len(teilung) - 1)
        f = min(1.0, (hoehe - gap * (len(teilung) - 1)) / max(1e-6, sum(hs)))
        hs = [h * f for h in hs]
        flaeche = sum(hs[z] ** 2 * a[i] for z, zeile in enumerate(teilung) for i in zeile)
        return flaeche, hs
    moeglich = [[list(range(n))], [[i] for i in range(n)]]
    if n == 3:
        moeglich += [[[0, 1], [2]], [[0], [1, 2]]]
    best = max(moeglich, key=lambda t: zeilen_teilung(t)[0])
    _, hs = zeilen_teilung(best)
    o = []
    gesamt_h = sum(hs) + gap * (len(best) - 1)
    yy = y + (hoehe - gesamt_h) / 2
    for zeile, zh in zip(best, hs):
        breite = sum(a[i] * zh for i in zeile) + gap * (len(zeile) - 1)
        xx = x + (s - breite) / 2
        for i in zeile:
            o.append(_ein_bild(liste[i], xx, yy, a[i] * zh, zh))
            xx += a[i] * zh + gap
        yy += zh + gap
    return "".join(o)


def pruefe(sx, stelle_ok=None):
    """Feste Prüfungen der Strukturkachel. Liefert Liste von Regeln wie die Bildprüfung (id, stufe, de, ergebnis, grund)."""
    erg = []
    el = sx.get("elemente") or []
    lang = [e.get(lg) for e in el + [x for x in (sx.get("mitte"), sx.get("titel")) if x] for lg in ("de", "gsw") if len(e.get(lg) or "") > 40]
    erg.append({"id": "K-LAENGE", "stufe": "pflicht", "de": "Beschriftungen passen in ihre Felder (höchstens 40 Zeichen)",
                "ergebnis": "fehler" if lang else "ok", "grund": "; ".join(lang)})
    zu_lang_zeilen = []
    for e in el:
        for lg in ("de", "gsw"):
            if any(len(w) > 18 for w in (e.get(lg) or "").split()):
                zu_lang_zeilen.append(e.get(lg))
    erg.append({"id": "K-WORT", "stufe": "soll", "de": "Keine Wörter über 18 Zeichen (Zeilenumbruch auf dem Handy)",
                "ergebnis": "fehler" if zu_lang_zeilen else "ok", "grund": "; ".join(zu_lang_zeilen)})
    if stelle_ok:
        falsch = [e.get("ref") for e in el if e.get("ref") and not stelle_ok(e["ref"])]
        erg.append({"id": "K-STELLEN", "stufe": "pflicht", "de": "Alle Stellen gültig", "ergebnis": "fehler" if falsch else "ok", "grund": ", ".join(map(str, falsch))})
    gsw_fehlt = [e.get("de") for e in el if not e.get("gsw")]
    erg.append({"id": "K-SPRACHEN", "stufe": "pflicht", "de": "Jede Beschriftung auch auf Züritüütsch",
                "ergebnis": "fehler" if gsw_fehlt else "ok", "grund": "; ".join(map(str, gsw_fehlt))})
    return erg
