#!/usr/bin/env python3
"""Strukturkacheln: gezeichnete Bildfelder aus Daten, im selben Format wie die gemalten Kacheln (600 × 400 plus Band).

Form je Feld (Entscheid Andi Neck 2026-11-21, docs/VISUELLE-SPRACHE.md): Wo der Text nicht erzählt, zeigt ein Strukturbild die
Gestalt des Textes. Typen und Datenformat: scripts/authoring/buchgeruest.py (FORMAT). Beschriftungen zweisprachig (Klassen lw-de,
lw-gsw wie im Band; die App blendet die gewählte Sprache ein).

Feste Prüfungen (pruefe): genug Elemente, Beschriftungen passen in ihre Felder (Zeichenzahl je Zeile), alle Stellen gültig.
"""
import html
import re

W, H = 600, 400
PAPER, INK, MUTED, RULE = "#FBF8F1", "#3E413B", "#7A7C73", "#DDD5C6"
FARBE = {"a": ("#EFE3D4", "#BD8067"), "b": ("#E3EAEC", "#6F8F9B"), "n": ("#ECEEE6", "#8A9378"), "akzent": "#A4532A"}
SANS = "Inter, Helvetica, Arial, sans-serif"
SERIF = "Georgia, 'Times New Roman', serif"
FS, FS_REF = 17, 12.5
BETONT = "#EDD3B4"   # Fläche betonter Glieder (Höhepunkt, Pointe)


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


def zweisprachig(x, y, e, n, fs=FS, anchor="start", fill=INK, weight=400, serif=False, strike=False, italic=False):
    """Beschriftung in beiden Sprachen (je eine Textgruppe, die App zeigt eine); n Zeichen je Zeile. Liefert (svg, zeilen)."""
    out, z_max = [], 1
    for lg in ("de", "gsw"):
        t = e.get(lg) or e.get("de") or ""
        zeilen = umbruch(t, n)
        z_max = max(z_max, len(zeilen))
        dy = -(len(zeilen) - 1) * fs * 0.62
        spans = "".join(f'<tspan x="{x}" dy="{(dy if i == 0 else fs * 1.24):.1f}">{esc(z)}</tspan>' for i, z in enumerate(zeilen))
        deko = ' text-decoration="line-through"' if strike else ""
        out.append(f'<text class="lw lw-{lg}" x="{x}" y="{y + fs * 0.35:.1f}" font-family="{SERIF if serif else SANS}" font-size="{fs}" '
                   f'text-anchor="{anchor}" fill="{fill}" font-weight="{weight}"{deko}{" font-style=" + chr(34) + "italic" + chr(34) if italic else ""}>{spans}</text>')
    return "".join(out), z_max


def ref_text(x, y, ref, anchor="start"):
    return f'<text x="{x}" y="{y}" font-family="{SANS}" font-size="{FS_REF}" fill="{MUTED}" text-anchor="{anchor}">{esc(stelle(ref))}</text>' if ref else ""


def box(x, y, w, h, seite="n", betont=False, gestrichen=False):
    fill, rand = FARBE.get(seite, FARBE["n"])
    if gestrichen:
        fill = "#EEEAE3"
    if betont:   # betont = wärmere Fläche, kein Rahmen in Akzentfarbe (wirkte wie «ausgewählt», Rückmeldung Andi Neck 2026-11-21)
        fill = BETONT
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{fill}" stroke="{rand}" stroke-width="1" stroke-opacity=".55"/>')


def pfeil(x1, y1, x2, y2, farbe=MUTED):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{farbe}" stroke-width="1.8" marker-end="url(#sk-pf)"/>')


DEFS = ('<defs><marker id="sk-pf" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
        '<path d="M0 0L10 5L0 10z" fill="#7A7C73"/></marker>'
        '<radialGradient id="sk-wash" cx="30%" cy="25%" r="80%"><stop offset="0" stop-color="#EFE6D6" stop-opacity=".9"/>'
        '<stop offset="1" stop-color="#FBF8F1" stop-opacity="0"/></radialGradient></defs>')


def titel(sx):
    t = sx.get("titel")
    if not t:
        return "", 18
    svg, _ = zweisprachig(W / 2, 30, t, 44, fs=20, anchor="middle", serif=True, fill="#4A3B2E")
    return svg, 54


_V = {}   # Vignetten der Kachel, die gerade gezeichnet wird: Schlüssel («1», «2», …, «m») → href


def vign(k, x, y, s):
    """Gemalte Vignette (Hybrid): Papierweiss verschwindet durch Multiplizieren auf dem Kachelpapier."""
    h = _V.get(str(k))
    return (f'<image href="{h}" x="{x:.1f}" y="{y:.1f}" width="{s:.1f}" height="{s:.1f}" preserveAspectRatio="xMidYMid meet" '
            f'style="mix-blend-mode:multiply"/>') if h else ""


def zeichne(sx, vignetten=None):
    """SVG-Inhalt (ohne äusseres svg) für eine Strukturkachel 600 × 400; vignetten: Schlüssel → href gemalter Vignetten."""
    global _V
    _V = dict(vignetten or {})
    typ = sx["typ"]
    o = [DEFS, f'<rect width="{W}" height="{H}" fill="{PAPER}"/>', f'<rect width="{W}" height="{H}" fill="url(#sk-wash)"/>']
    tsvg, y0 = titel(sx)
    o.append(tsvg)
    el = sx.get("elemente") or []
    o.append(globals()[f"_{typ}"](sx, el, y0))
    return "".join(o)


def _spalten(sx, el, y0):
    o = []
    kopf = sx.get("kopf") or {}
    xa, xb, w = 24, 312, 264
    for x, s in ((xa, "a"), (xb, "b")):
        if kopf.get(s):
            svg, _ = zweisprachig(x + w / 2, y0 + 8, kopf[s], 30, fs=18, anchor="middle", fill=FARBE[s][1], weight=600)
            o.append(svg)
    if sx.get("mitte"):
        svg, _ = zweisprachig(W / 2, y0 + 8, sx["mitte"], 14, fs=15, anchor="middle", fill=FARBE["akzent"], italic=True)
        o.append(svg)
    o.append(f'<line x1="{W / 2}" x2="{W / 2}" y1="{y0 + 26}" y2="{H - 12}" stroke="{RULE}" stroke-width="1.4"/>')
    for s, x in (("a", xa), ("b", xb)):
        reihe = [e for e in el if e.get("seite") == s]
        verfuegbar = H - (y0 + 32) - 10
        n_max = max(len([e for e in el if e.get("seite") == x_]) for x_ in "ab")
        h = min(72, (verfuegbar - 8 * (n_max - 1)) / max(1, n_max))
        start = y0 + 32 + (verfuegbar - (n_max * h + 8 * (n_max - 1))) / 2
        for i, e in enumerate(reihe):
            y = start + i * (h + 8)
            o.append(box(x, y, w, h, s, e.get("betont"), e.get("gestrichen")))
            mit_ref = e.get("ref") and h > 44
            k = el.index(e) + 1
            vs = min(h - 8, 60) if _V.get(str(k)) else 0
            if vs:
                o.append(vign(k, x + 6, y + (h - vs) / 2, vs))
            fs, zl = passend(e, w - 22 - (vs + 4 if vs else 0), h - (24 if mit_ref else 8), FS if h > 40 else 15)
            svg, z = zweisprachig(x + 12 + (vs + 4 if vs else 0), y + (h - (14 if mit_ref else 0)) / 2, e, zl, fs=fs,
                                  fill=MUTED if e.get("gestrichen") else INK, strike=e.get("gestrichen"), weight=600 if e.get("betont") else 400)
            o.append(svg)
            if e.get("ref") and h > 44:
                o.append(ref_text(x + w - 10, y + h - 9, e["ref"], "end"))
    return "".join(o)


def _kette(sx, el, y0):
    o = []
    n = len(el)
    gap = 18
    h = min(60, (H - y0 - 14 - gap * (n - 1)) / n)
    for i, e in enumerate(el):
        y = y0 + i * (h + gap)
        o.append(box(90, y, 420, h, "a" if e.get("betont") else "n", e.get("betont"), e.get("gestrichen")))
        vs = min(h - 6, 60) if _V.get(str(i + 1)) else 0
        if vs:
            o.append(vign(i + 1, 96, y + (h - vs) / 2, vs))
        svg, _ = zweisprachig(W / 2 + (vs / 2 if vs else 0), y + h / 2 - (4 if h > 46 else 0), e, 40 - (int(vs / 9) if vs else 0), anchor="middle", weight=600 if e.get("betont") else 400,
                              fill=MUTED if e.get("gestrichen") else INK, strike=e.get("gestrichen"))
        o.append(svg)
        if e.get("ref"):
            o.append(ref_text(500, y + h - 7, e["ref"], "end"))
        if i < n - 1:
            o.append(pfeil(W / 2, y + h + 2, W / 2, y + h + gap - 2))
    return "".join(o)


def _raster(sx, el, y0):
    o = []
    n = len(el)
    cols = 2 if n <= 4 else 3 if n <= 9 else 4
    rows = (n + cols - 1) // cols
    gap = 10
    w = (W - 40 - gap * (cols - 1)) / cols
    h = min(96, (H - y0 - 14 - gap * (rows - 1)) / rows)
    for i, e in enumerate(el):
        r, c = divmod(i, cols)
        x, y = 20 + c * (w + gap), y0 + r * (h + gap)
        o.append(box(x, y, w, h, "n", e.get("betont"), e.get("gestrichen")))
        o.append(f'<text x="{x + 9}" y="{y + 15}" font-family="{SANS}" font-size="11.5" fill="{MUTED}">{i + 1}</text>')
        oben, unten = y + 18, y + h - (17 if e.get("ref") else 6)   # Textfläche zwischen Nummer und Stelle
        if _V.get(str(i + 1)):   # Vignette oben in der Mitte, Text darunter
            vs = min((unten - oben) * 0.58, w * 0.6)
            o.append(vign(i + 1, x + (w - vs) / 2, y + 6, vs))
            oben = y + 6 + vs + 2
        fs, zl = passend(e, w - 18, unten - oben, FS if cols < 4 else 15)
        svg, _ = zweisprachig(x + w / 2, (oben + unten) / 2, e, zl, fs=fs, anchor="middle", weight=600 if e.get("betont") else 400,
                              fill=MUTED if e.get("gestrichen") else INK, strike=e.get("gestrichen"))
        o.append(svg)
        if e.get("ref"):
            o.append(ref_text(x + w - 8, y + h - 6, e["ref"], "end"))
    return "".join(o)


def passend(e, breite, hoehe, fs=FS, fs_min=11.5):
    """Grösste Schrift (bis fs), bei der beide Sprachen in die Fläche passen; liefert (Schriftgrösse, Zeichen je Zeile)."""
    while True:
        zl = max(6, int(breite / (fs * 0.56)))
        z = max(len(umbruch(e.get(lg) or e.get("de") or "", zl)) for lg in ("de", "gsw"))
        if z * fs * 1.24 <= hoehe or fs <= fs_min:
            return fs, zl
        fs -= 0.5


def _kurve(sx, el, y0):
    o = []
    ab = [e for e in el if e.get("richtung") == "ab"]
    auf = [e for e in el if e.get("richtung") == "auf"]
    tief_y, tief_x, halb = H - 50, W / 2, 150
    pts = []
    for i, e in enumerate(ab):
        t = (i + 1) / (len(ab) + 1)
        pts.append((tief_x - halb + halb * t, y0 + 6 + (tief_y - y0 - 6) * t, e, "ab"))
    for i, e in enumerate(auf):
        t = (i + 1) / (len(auf) + 1)
        pts.append((tief_x + halb * t, tief_y - (tief_y - y0 - 6) * t, e, "auf"))
    weg = [(tief_x - halb, y0 + 6)] + [(p[0], p[1]) for p in pts if p[3] == "ab"] + [(tief_x, tief_y)] + [(p[0], p[1]) for p in pts if p[3] == "auf"] + [(tief_x + halb, y0 + 6)]
    o.append('<path d="M' + " L".join(f"{x:.0f} {y:.0f}" for x, y in weg) + f'" fill="none" stroke="#D9CBB6" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>')
    for x, y, e, r in pts:
        farbe = "#62665D" if r == "ab" else "#BD8067"
        o.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="6" fill="{farbe}"/>')
        n = int((x - 14) / 8.4) if r == "ab" else int((W - x - 14) / 8.4)
        if r == "ab":
            svg, z = zweisprachig(x - 14, y, e, n, fs=15, anchor="end")
            o.append(svg + ref_text(x + 10, y - 8, e.get("ref"), "start"))   # Stelle innen neben dem Punkt, abwärts darüber, aufwärts darunter
        else:
            svg, z = zweisprachig(x + 14, y, e, n, fs=15)
            o.append(svg + ref_text(x - 10, y + 18, e.get("ref"), "end"))
    if sx.get("mitte"):
        svg, _ = zweisprachig(tief_x, tief_y + 26, sx["mitte"], 44, fs=15, anchor="middle", fill=FARBE["akzent"], italic=True)
        o.append(svg)
    return "".join(o)


def _spiegel(sx, el, y0):
    o = []
    kopf = sx.get("kopf") or {}
    a = [e for e in el if e.get("seite") == "a"]
    b = [e for e in el if e.get("seite") == "b"]
    oben, unten, xl, xr = y0 + 34, H - 84, 80, 520   # unten Platz für zwei Zeilen und die Legende
    # Seite a fällt (oben links → unten rechts, gestrichelt), Seite b steigt (unten links → oben rechts); so schreiben es alle Buchgerüste
    o.append(f'<path d="M{xl} {oben} C 230 {oben + 10}, 370 {unten - 10}, {xr} {unten}" fill="none" stroke="{FARBE["a"][1]}" stroke-width="3.5" stroke-dasharray="9 6"/>')
    o.append(f'<path d="M{xl} {unten} C 230 {unten - 10}, 370 {oben + 10}, {xr} {oben}" fill="none" stroke="{FARBE["b"][1]}" stroke-width="3.5"/>')
    for reihe, start, ende in ((a, (xl, oben), (xr, unten)), (b, (xl, unten), (xr, oben))):
        paar = [reihe[0], reihe[-1]] if len(reihe) > 1 else reihe
        for e, (x, y) in zip(paar, [start, ende]):
            anchor = "start" if x < W / 2 else "end"
            xx = 18 if anchor == "start" else W - 18
            dy = -22 if y == oben else 26
            svg, z = zweisprachig(xx, y + dy, e, 26, fs=15, anchor=anchor)
            o.append(svg + f'<circle cx="{x}" cy="{y}" r="5" fill="{INK}"/>')
    leg = []
    for s, stil in (("a", 'stroke-dasharray="9 6"'), ("b", "")):
        if kopf.get(s):
            leg.append((s, stil))
    for i, (s, stil) in enumerate(leg):
        x = 70 + i * 250
        o.append(f'<line x1="{x}" x2="{x + 36}" y1="{H - 16}" y2="{H - 16}" stroke="{FARBE[s][1]}" stroke-width="3.5" {stil}/>')
        svg, _ = zweisprachig(x + 44, H - 16, kopf[s], 60, fs=14.5, fill=FARBE[s][1], weight=600)
        o.append(svg)
    if sx.get("mitte"):
        o.append(f'<rect x="{W / 2 - 120}" y="{(oben + unten) / 2 - 24}" width="240" height="48" rx="8" fill="{PAPER}" stroke="{RULE}"/>')
        svg, _ = zweisprachig(W / 2, (oben + unten) / 2, sx["mitte"], 28, fs=15, anchor="middle", italic=True)
        o.append(svg)
    return "".join(o)


def _reihe(sx, el, y0):
    """Nummerierte Stationen senkrecht (Ablauf von oben nach unten); waagrecht überlappten die Beschriftungen."""
    o = []
    n = len(el)
    schritt = min(64, (H - y0 - 16) / n)
    start = y0 + (H - y0 - 16 - schritt * n) / 2 + schritt / 2
    xk = 62
    o.append(f'<line x1="{xk}" x2="{xk}" y1="{start - schritt / 2 + 6}" y2="{start + schritt * (n - 0.5) - 6}" stroke="{RULE}" stroke-width="3"/>')
    for i, e in enumerate(el):
        y = start + i * schritt
        fuell = BETONT if e.get("betont") else PAPER
        o.append(f'<circle cx="{xk}" cy="{y:.1f}" r="14" fill="{fuell}" stroke="{FARBE["n"][1]}" stroke-width="1.6"/>'
                 f'<text x="{xk}" y="{y + 4.8:.1f}" font-family="{SANS}" font-size="13.5" text-anchor="middle" fill="{INK}">{i + 1}</text>')
        vs = min(schritt - 4, 58) if _V.get(str(i + 1)) else 0
        if vs:
            o.append(vign(i + 1, xk + 22, y - vs / 2, vs))
        tx = xk + 28 + (vs + 6 if vs else 0)
        fs, zl = passend(e, 410 - (vs + 6 if vs else 0), schritt - 8, FS)
        svg, _ = zweisprachig(tx, y, e, zl, fs=fs, weight=600 if e.get("betont") else 400)
        o.append(svg)
        if e.get("ref"):
            o.append(ref_text(W - 22, y + 4, e["ref"], "end"))
    return "".join(o)


def z_hoch(e, n):
    return max(len(umbruch(e.get(lg) or "", n)) for lg in ("de", "gsw"))


def _ebenen(sx, el, y0):
    o = []
    kopf = sx.get("kopf") or {}
    mitte_y = y0 + (H - y0) / 2
    for s, (y1, y2) in (("a", (y0, mitte_y - 8)), ("b", (mitte_y + 8, H - 12))):
        fill, rand = FARBE[s]
        o.append(f'<rect x="16" y="{y1}" width="{W - 32}" height="{y2 - y1}" rx="9" fill="{fill}" fill-opacity=".55" stroke="{rand}" stroke-opacity=".4"/>')
        if kopf.get(s):
            svg, _ = zweisprachig(30, y1 + 20, kopf[s], 30, fs=15, fill=rand, weight=600)
            o.append(svg)
        reihe = [e for e in el if e.get("seite") == s]
        n = max(1, len(reihe))
        w = (W - 60 - 10 * (n - 1)) / n
        for i, e in enumerate(reihe):
            x = 30 + i * (w + 10)
            yy = y1 + 38
            hh = y2 - y1 - 48
            o.append(box(x, yy, w, hh, s, e.get("betont")))
            svg, _ = zweisprachig(x + w / 2, yy + hh / 2 - 4, e, max(10, int(w / 9)), anchor="middle")
            o.append(svg + ref_text(x + w / 2, yy + hh - 7, e.get("ref"), "middle"))
    return "".join(o)


def _ringe(sx, el, y0):
    o = []
    n = len(el)
    paare = [(el[i], el[n - 1 - i]) for i in range(n // 2)]
    rest = el[n // 2] if n % 2 else None
    stufen = len(paare)
    h = min(58, (H - y0 - 70) / max(1, stufen) - 8)
    marken = "ABCDEF"
    for i, (l, r) in enumerate(paare):
        y = y0 + i * (h + 8)
        einzug = i * 34
        for e, x, w, anchor, m in ((l, 20 + einzug, 250 - einzug, "start", marken[i]), (r, W - 20 - (250 - einzug), 250 - einzug, "start", marken[i] + "′")):
            o.append(box(x, y, w, h, "a" if x < W / 2 else "b", e.get("betont")))
            o.append(f'<text x="{x + 10}" y="{y + 18}" font-family="{SERIF}" font-size="13" fill="{FARBE["akzent"]}">{m}</text>')
            fs, zl = passend(e, w - 40, h - (20 if e.get("ref") else 8), 15.5)
            svg, _ = zweisprachig(x + 30, y + (h - (12 if e.get("ref") else 0)) / 2, e, zl, fs=fs)
            o.append(svg + ref_text(x + w - 8, y + h - 6, e.get("ref"), "end"))
    mitte = sx.get("mitte") or rest
    y_frei = y0 + stufen * (h + 8) + 4
    if rest is not None and sx.get("mitte"):   # ungerade Zahl mit eigener Mitte: innerstes Glied nicht verlieren (Num 2, Dtn 6, Jud, Klgl)
        hr = min(52, (H - y_frei - 12) / 2 - 6)
        x, w = W / 2 - 170, 340
        o.append(box(x, y_frei, w, hr, "n", rest.get("betont")))
        o.append(f'<text x="{x + 10}" y="{y_frei + 18}" font-family="{SERIF}" font-size="13" fill="{FARBE["akzent"]}">{marken[stufen]}</text>')
        fs, zl = passend(rest, w - 60, hr - (18 if rest.get("ref") else 8), 15.5)
        svg, _ = zweisprachig(W / 2, y_frei + (hr - (12 if rest.get("ref") else 0)) / 2, rest, zl, fs=fs, anchor="middle")
        o.append(svg + ref_text(x + w - 8, y_frei + hr - 6, rest.get("ref"), "end"))
        y_frei += hr + 8
    if mitte:
        hm = min(96, H - y_frei - 12)
        y = y_frei + (H - y_frei - 12 - hm) / 2
        o.append(f'<rect x="{W / 2 - 170}" y="{y}" width="340" height="{hm}" rx="10" fill="{BETONT}" stroke="{FARBE["a"][1]}" stroke-opacity=".55"/>')
        mvs = min(hm - 12, 70) if _V.get("m") else 0
        if mvs:
            o.append(vign("m", W / 2 - 165, y + (hm - mvs) / 2, mvs))
        fs, zl = passend(mitte, 300 - (mvs + 6 if mvs else 0), hm - (22 if mitte.get("ref") else 8), 17)
        svg, _ = zweisprachig(W / 2 + (mvs / 2 if mvs else 0), y + hm / 2 - (6 if mitte.get("ref") else 0), mitte, zl, fs=fs, anchor="middle", weight=600)
        o.append(svg + ref_text(W / 2, y + hm - 8, mitte.get("ref"), "middle"))
    return "".join(o)


def _lager(sx, el, y0):
    """Lagerplan um eine Mitte (Num 2): Norden oben, Osten rechts; «innen» als Ring um die Mitte. Elemente mit seite n/o/s/w/innen."""
    o = []
    cx, cy = W / 2, y0 + (H - y0 - 8) / 2
    mv = _V.get("m")
    mw, mh = (170, 100) if mv else (150, 56)
    seiten = {e.get("seite"): e for e in el}
    nr = {e.get("seite"): k for k, e in enumerate(el, 1)}
    if seiten.get("innen"):
        rw, rh = mw + 60, mh + 58
        o.append(f'<rect x="{cx - rw / 2}" y="{cy - rh / 2}" width="{rw}" height="{rh}" rx="16" fill="none" stroke="{FARBE["b"][1]}" '
                 f'stroke-width="1.6" stroke-dasharray="6 5"/>')
        e = seiten["innen"]
        vi = 30 if _V.get(str(nr["innen"])) else 0
        if vi:
            o.append(vign(nr["innen"], cx - rw / 2 + 8, cy - rh / 2 + 2, vi))
        svg, _ = zweisprachig(cx + vi / 2, cy - rh / 2 + 15, e, 30, fs=13, anchor="middle", fill=FARBE["b"][1], weight=600)
        o.append(svg + ref_text(cx, cy + rh / 2 - 7, e.get("ref"), "middle"))
    m = sx.get("mitte") or {}
    o.append(f'<rect x="{cx - mw / 2}" y="{cy - mh / 2}" width="{mw}" height="{mh}" rx="9" fill="{BETONT}" stroke="{FARBE["a"][1]}" stroke-opacity=".55"/>')
    if mv:
        o.append(vign("m", cx - 31, cy - mh / 2 + 4, 62))
    fs, zl = passend(m, mw - 16, (mh - 70) if mv else (mh - 8), 15.5)
    svg, _ = zweisprachig(cx, (cy + mh / 2 - 16) if mv else cy, m, zl, fs=fs, anchor="middle", weight=600)
    o.append(svg)
    bw, bh = 176, 66
    lage = {"n": (cx - bw / 2, y0 + 2, "N"), "s": (cx - bw / 2, H - 12 - bh, "S"),
            "w": (12, cy - bh / 2, "W"), "o": (W - 12 - bw, cy - bh / 2, "O")}
    for k, (x, y, marke) in lage.items():
        e = seiten.get(k)
        if not e:
            continue
        o.append(box(x, y, bw, bh, "n", e.get("betont")))
        o.append(f'<text x="{x + 9}" y="{y + 16}" font-family="{SERIF}" font-size="13" fill="{FARBE["akzent"]}">{marke}</text>')
        vs = 48 if _V.get(str(nr[k])) else 0
        if vs:
            o.append(vign(nr[k], x + 6, y + 16, vs))
        tl = x + 22 + (vs - 12 if vs else 0)
        fs, zl = passend(e, x + bw - 8 - tl, bh - (20 if e.get("ref") else 8), 15)
        svg, _ = zweisprachig((tl + x + bw - 6) / 2, y + (bh - (12 if e.get("ref") else 0)) / 2 + 2, e, zl, fs=fs, anchor="middle")
        o.append(svg + ref_text(x + bw - 8, y + bh - 6, e.get("ref"), "end"))
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
    erg.append({"id": "K-SPRACHEN", "stufe": "pflicht", "de": "Jede Beschriftung auch auf Züridüütsch",
                "ergebnis": "fehler" if gsw_fehlt else "ok", "grund": "; ".join(map(str, gsw_fehlt))})
    return erg
