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
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{fill}" stroke="{FARBE["akzent"] if betont else rand}" '
            f'stroke-width="{2.2 if betont else 1}" stroke-opacity="{1 if betont else .55}"/>')


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


def zeichne(sx):
    """SVG-Inhalt (ohne äusseres svg) für eine Strukturkachel 600 × 400."""
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
            svg, z = zweisprachig(x + 12, y + h / 2 - (5 if e.get("ref") and h > 44 else 0), e, 26, fs=FS if h > 40 else 15,
                                  fill=MUTED if e.get("gestrichen") else INK, strike=e.get("gestrichen"))
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
        svg, _ = zweisprachig(W / 2, y + h / 2 - (4 if h > 46 else 0), e, 40, anchor="middle", weight=600 if e.get("betont") else 400,
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
        o.append(box(x, y, w, h, "a" if e.get("betont") else "n", e.get("betont")))
        o.append(f'<circle cx="{x + 16}" cy="{y + 16}" r="11" fill="{PAPER}" stroke="{FARBE["n"][1]}"/>'
                 f'<text x="{x + 16}" y="{y + 20.5}" font-family="{SANS}" font-size="12.5" text-anchor="middle" fill="{INK}">{i + 1}</text>')
        svg, _ = zweisprachig(x + w / 2, y + h / 2 + 4, e, max(10, int(w / 9.4)), fs=FS if cols < 4 else 15, anchor="middle")
        o.append(svg)
        if e.get("ref"):
            o.append(ref_text(x + w - 8, y + h - 7, e["ref"], "end"))
    return "".join(o)


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
            o.append(svg + ref_text(x - 14, y + 10 + z * 9.3, e.get("ref"), "end"))
        else:
            svg, z = zweisprachig(x + 14, y, e, n, fs=15)
            o.append(svg + ref_text(x + 14, y + 10 + z * 9.3, e.get("ref")))
    if sx.get("mitte"):
        svg, _ = zweisprachig(tief_x, tief_y + 26, sx["mitte"], 44, fs=15, anchor="middle", fill=FARBE["akzent"], italic=True)
        o.append(svg)
    return "".join(o)


def _spiegel(sx, el, y0):
    o = []
    kopf = sx.get("kopf") or {}
    a = [e for e in el if e.get("seite") == "a"]
    b = [e for e in el if e.get("seite") == "b"]
    oben, unten, xl, xr = y0 + 34, H - 64, 80, 520
    o.append(f'<path d="M{xl} {oben} C 230 {oben + 10}, 370 {unten - 10}, {xr} {unten}" fill="none" stroke="{FARBE["b"][1]}" stroke-width="3.5"/>')
    o.append(f'<path d="M{xl} {unten} C 230 {unten - 10}, 370 {oben + 10}, {xr} {oben}" fill="none" stroke="{FARBE["a"][1]}" stroke-width="3.5" stroke-dasharray="9 6"/>')
    # Seite a: unten links → oben rechts; Seite b: oben links → unten rechts
    for reihe, start, ende in ((a, (xl, unten), (xr, oben)), (b, (xl, oben), (xr, unten))):
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
        x = 150 + i * 190
        o.append(f'<line x1="{x}" x2="{x + 36}" y1="{H - 16}" y2="{H - 16}" stroke="{FARBE[s][1]}" stroke-width="3.5" {stil}/>')
        svg, _ = zweisprachig(x + 44, H - 16, kopf[s], 22, fs=14.5, fill=FARBE[s][1], weight=600)
        o.append(svg)
    if sx.get("mitte"):
        o.append(f'<rect x="{W / 2 - 120}" y="{(oben + unten) / 2 - 24}" width="240" height="48" rx="8" fill="{PAPER}" stroke="{RULE}"/>')
        svg, _ = zweisprachig(W / 2, (oben + unten) / 2, sx["mitte"], 28, fs=15, anchor="middle", italic=True)
        o.append(svg)
    return "".join(o)


def _reihe(sx, el, y0):
    o = []
    n = len(el)
    linie_y = y0 + (H - y0) / 2 - 6
    x0, x1 = 50, W - 50
    o.append(f'<line x1="{x0 - 20}" x2="{x1 + 20}" y1="{linie_y}" y2="{linie_y}" stroke="{RULE}" stroke-width="3"/>')
    schritt = (x1 - x0) / max(1, n - 1)
    zeichen = max(9, int(schritt / 8.6))
    for i, e in enumerate(el):
        x = x0 + i * schritt
        farbe = FARBE["akzent"] if e.get("betont") else FARBE["n"][1]
        o.append(f'<circle cx="{x:.0f}" cy="{linie_y}" r="15" fill="{PAPER}" stroke="{farbe}" stroke-width="2"/>'
                 f'<text x="{x:.0f}" y="{linie_y + 5}" font-family="{SANS}" font-size="14" text-anchor="middle" fill="{INK}">{i + 1}</text>')
        oben = i % 2 == 0
        y = linie_y - 40 if oben else linie_y + 44
        svg, z = zweisprachig(x, y - (z_hoch(e, zeichen) - 1) * 9 if oben else y, e, zeichen, fs=15, anchor="middle", weight=600 if e.get("betont") else 400)
        o.append(svg)
        if e.get("ref"):
            o.append(ref_text(x, (linie_y - 22) if oben else (y + z * 18 + 6), e["ref"], "middle") if not oben else
                     ref_text(x, linie_y - 24, e["ref"], "middle"))
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
            svg, _ = zweisprachig(x + 30, y + h / 2, e, max(10, int((w - 40) / 9)), fs=15.5)
            o.append(svg + ref_text(x + w - 8, y + h - 6, e.get("ref"), "end"))
    mitte = sx.get("mitte") or rest
    if mitte:
        y_frei = y0 + stufen * (h + 8) + 4
        hm = min(96, H - y_frei - 12)
        y = y_frei + (H - y_frei - 12 - hm) / 2
        o.append(f'<rect x="{W / 2 - 170}" y="{y}" width="340" height="{hm}" rx="10" fill="#F4E7DA" stroke="{FARBE["akzent"]}" stroke-width="2"/>')
        svg, _ = zweisprachig(W / 2, y + hm / 2 - 4, mitte, 34, fs=17, anchor="middle", weight=600)
        o.append(svg + ref_text(W / 2, y + hm - 8, mitte.get("ref"), "middle"))
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
