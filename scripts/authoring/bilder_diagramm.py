#!/usr/bin/env python3
"""Strukturbilder (docs/STRUKTURKATALOG.md, Abschnitt 2c «Darstellungen»): Kacheln, die den Bau eines Textes zeigen statt
einer Szene – Raster, Spalten, Pfeilkette, Weiche, Gliederungsbild, Dialogspalten, Zeitleiste, Waage, Treppe, zwei Ebenen,
Ringe, Spiegelachse, Kette (Stammbaum).

Ein Feld im Bildauftrag trägt dafür `diagram` statt einer Bühne:

    "diagram": {"visual": "grid", "speaker": "FIG-JESUS", "title": {"de": "Selig sind …", "gsw": "…"},
                "span": 1|2, "cols": 2,
                "cells": [Zelle, …]                       # grid, arrows, stairs, timeline, outline, tree
                "head": [Wort, Wort], "rows": [[Zelle, Zelle], …]   # columns, mirror
                "links": [Wort, …]                        # arrows: Beschriftung je Pfeil (z. B. «denn»), optional
                "cond": Zelle, "yes": Zelle, "no": Zelle, "yes_label": Wort, "no_label": Wort   # switch
                "left": [Zelle], "right": [Zelle], "verdict": Wort   # balance
                "top": [Zelle], "bottom": [Zelle], "top_label": Wort, "bottom_label": Wort   # levels
                "ring": Zelle, "core": [Zelle]            # rings (Rahmen und Mitte)
                "turns": [{"who": "FIG-…", "cell": Zelle}]   # dialogue
               }
    Zelle = {"a": Wort (fett), "b": Wort (normal, optional), "icons": ["FIG-…"], "who": "FIG-…" (Porträt),
             "role": Wort (kleine Überschrift, outline), "empty": true, "strike": true, "tone": "old|new|plain"}
    Wort = {"de": "…", "gsw": "…"} oder eine Zeichenkette

Worte stehen je Sprache als eigener Text (Klassen lw-de, lw-gsw), wie die übrigen Worte im Bild. Höhe der Kachel nach Inhalt
(«Kacheln so gross wie nötig», Hinweis Andi Neck 2026-10-24); `span: 2` nimmt die ganze Breite.
"""
import math

import bilder_auto as _auto
from bilder_auto import LANGS, _esc, _lab, text_w

INK = "#3B3226"
MUTED = "#6B5E4B"
FILL = {"plain": "#FFFDF6", "old": "#EFE6D6", "new": "#FFF4D6"}
W1 = 186
GAP = 5


# ------------------------------------------------------------------ Text in mehreren Zeilen
def wrapn(s, fs, maxw, maxlines=6, bold=True):
    k = 1.0 if bold else .94
    words, lines, cur = s.split(" "), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if text_w(t, fs) * k <= maxw or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    if len(lines) > maxlines:
        lines = lines[:maxlines - 1] + [" ".join(lines[maxlines - 1:])]
    return lines


def fit(v, fs, maxw, maxlines=6, bold=True, min_fs=6.5):
    """Schriftgrösse so, dass die längste Wortfolge passt (je Sprache gleich), und Zeilenzahl."""
    lab = _lab(v)
    while True:
        lines = {k: wrapn(s, fs, maxw, maxlines, bold) for k, s in lab.items()}
        too_wide = any(text_w(x, fs) * (1 if bold else .94) > maxw + .5 for ls in lines.values() for x in ls)
        if not too_wide or fs <= min_fs:
            return fs, lines, max(len(ls) for ls in lines.values())
        fs -= .5


def block(x, y, v, fs, maxw, anchor="middle", weight="700", fill=INK, maxlines=6):
    """Text ab Oberkante y, umbrochen; gibt (svg, Höhe) zurück (Höhe der längsten Sprachfassung)."""
    if not v:
        return "", 0
    fs, lines, n = fit(v, fs, maxw, maxlines, weight == "700")
    lh = fs * 1.18
    same = len({tuple(ls) for ls in lines.values()}) == 1
    out = []
    for k, ls in (list(lines.items())[:1] if same else lines.items()):
        cls = "" if same else f' class="lw lw-{k}"'
        spans = "".join(f'<tspan x="{x:.1f}" y="{y + fs * .86 + i * lh:.1f}">{_esc(s)}</tspan>' for i, s in enumerate(ls))
        out.append(f'<text{cls} text-anchor="{anchor}" font-family="sans-serif" font-size="{fs}" font-weight="{weight}" fill="{fill}">{spans}</text>')
    return "".join(out), n * lh


def block_h(v, fs, maxw, weight="700", maxlines=6):
    if not v:
        return 0
    fs, _, n = fit(v, fs, maxw, maxlines, weight == "700")
    return n * fs * 1.18


# ------------------------------------------------------------------ Zellen
class Cells:
    def __init__(self, comp):
        self.c = comp

    def icon_row_w(self, icons, h):
        return sum(_auto.icon_w(self.c.vb(i), h) for i in icons) + 3 * max(0, len(icons) - 1)

    def icons(self, icons, cx, y, h, maxw):
        if not icons:
            return ""
        w = self.icon_row_w(icons, h)
        if w > maxw:
            h *= maxw / w
            w = maxw
        x, out = cx - w / 2, []
        for i in icons:
            iw = _auto.icon_w(self.c.vb(i), h)
            out.append(self.c.r_icon(i, x, y, iw, h))
            x += iw + 3
        return "".join(out)

    def portrait(self, fid, x, y, s):
        return (f'<circle cx="{x + s / 2:.1f}" cy="{y + s / 2:.1f}" r="{s / 2 + 1:.1f}" fill="#FFFDF6" stroke="{INK}" stroke-width=".8"/>'
                + self.c.r_icon(fid, x + s * .08, y + s * .04, s * .84, s * .9))

    ICON_H = 16
    PAD = 4

    def height(self, z, w):
        """Höhe einer Zelle bei Breite w."""
        if z.get("empty") and not (z.get("a") or z.get("b")):
            return 18
        tw = w - 2 * self.PAD - (20 if z.get("who") else 0)
        h = self.PAD * 2
        if z.get("role"):
            h += block_h(z["role"], 6.5, tw, "700", 2) + 1.5
        if z.get("icons"):
            h += self.ICON_H + 2
        h += block_h(z.get("a"), 8.2, tw, "700")
        if z.get("b"):
            h += block_h(z["b"], 7.6, tw, "400") + (1.5 if z.get("a") else 0)
        if z.get("who"):
            h = max(h, 26)
        return h

    def draw(self, z, x, y, w, h, tone=None):
        tone = z.get("tone") or tone or "plain"
        fill = FILL.get(tone, FILL["plain"])
        dash = ' stroke-dasharray="3 2"' if z.get("empty") else ""
        sw = 1.3 if tone == "new" else .9
        out = [f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="4" fill="{fill}" stroke="{INK}" stroke-width="{sw}"{dash}/>']
        tx, tw = x + w / 2, w - 2 * self.PAD
        if z.get("who"):
            out.append(self.portrait(z["who"], x + 3, y + (h - 18) / 2, 18))
            tx, tw = x + 22 + (w - 22) / 2 - 1, w - 22 - self.PAD - 1
        col = MUTED if tone == "old" else INK
        inner = self.height({k: v for k, v in z.items() if k != "who"}, tw + 2 * self.PAD) - 2 * self.PAD
        yy = y + max(self.PAD, (h - inner) / 2)
        if z.get("role"):
            s, hh = block(tx, yy, z["role"], 6.5, tw, weight="700", fill="#8A6A2A", maxlines=2)
            out.append(s)
            yy += hh + 1.5
        if z.get("icons"):
            out.append(self.icons(z["icons"], tx, yy, self.ICON_H, tw))
            yy += self.ICON_H + 2
        if z.get("a"):
            s, hh = block(tx, yy, z["a"], 8.2, tw, fill=col)
            out.append(s)
            yy += hh + 1.5
        if z.get("b"):
            s, hh = block(tx, yy, z["b"], 7.6, tw, weight="400", fill=col)
            out.append(s)
        if z.get("empty") and not (z.get("a") or z.get("b")):
            out.append(f'<text x="{x + w / 2:.1f}" y="{y + h / 2 + 3:.1f}" text-anchor="middle" font-family="sans-serif" font-size="8" fill="{MUTED}">–</text>')
        if z.get("strike"):
            out.append(f'<path d="M{x + 4:.1f} {y + h - 4:.1f}L{x + w - 4:.1f} {y + 4:.1f}" stroke="#B0413E" stroke-width="1.6" stroke-linecap="round" opacity=".85"/>')
        return "".join(out)


def arrow(x1, y1, x2, y2, col=INK, head=True, dash=False, sw=1.4):
    ang = math.atan2(y2 - y1, x2 - x1)
    h = ""
    if head:
        h = (f'<path d="M{x2 - 5 * math.cos(ang - .5):.1f} {y2 - 5 * math.sin(ang - .5):.1f}L{x2:.1f} {y2:.1f}'
             f'L{x2 - 5 * math.cos(ang + .5):.1f} {y2 - 5 * math.sin(ang + .5):.1f}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>')
    d = ' stroke-dasharray="3 2"' if dash else ""
    return f'<path d="M{x1:.1f} {y1:.1f}L{x2:.1f} {y2:.1f}" stroke="{col}" stroke-width="{sw}" stroke-linecap="round"{d}/>' + h


def small_label(x, y, v, fs=6.8, fill="#8A6A2A", anchor="middle"):
    return _auto.ltext(x, y, v, fs, anchor=anchor, weight="700", fill=fill)


# ------------------------------------------------------------------ Kachel
def diagram(comp, d):
    """SVG-Inhalt und Grösse (w, h) einer Strukturkachel."""
    w = W1 * (2 if d.get("span") == 2 else 1) + (4 if d.get("span") == 2 else 0) - 4 * 0
    if d.get("span") == 2:
        w = 2 * W1 + 2
    C = Cells(comp)
    out, y = [], 6
    # Kopf: Sprecher (Porträt) mit Titel in einer Sprechblase, sonst Titel als Zeile; Feldnummer oben links bleibt frei
    if d.get("speaker") or d.get("title"):
        x0 = 28
        if d.get("speaker"):
            out.append(C.portrait(d["speaker"], x0, 5, 20))
            x0 += 26
        tw = w - x0 - 8
        th = block_h(d.get("title"), 8.6, tw - 8) if d.get("title") else 0
        if d.get("title"):
            bh = max(20, th + 8)
            out.append(f'<rect x="{x0:.1f}" y="4" width="{tw:.1f}" height="{bh:.1f}" rx="7" fill="#FFFFFF" stroke="{INK}" stroke-width="1.1"/>')
            if d.get("speaker"):
                out.append(f'<path d="M{x0 + 1:.1f} 11L{x0 - 5:.1f} 14L{x0 + 1:.1f} 17" fill="#FFFFFF" stroke="{INK}" stroke-width="1.1" stroke-linejoin="round"/>'
                           f'<path d="M{x0 + 1.2:.1f} 11.6V16.4" stroke="#FFFFFF" stroke-width="1.4"/>')
            s, _ = block(x0 + tw / 2, 4 + (bh - th) / 2, d["title"], 8.6, tw - 8)
            out.append(s)
            y = 4 + bh + 6
        else:
            y = 30
    else:
        y = 26
    v = d["visual"]
    fn = VISUALS.get(v)
    if fn is None:
        raise SystemExit(f"FEHLER: Darstellung {v} im Zeichner noch nicht umgesetzt")
    s, y = fn(C, d, w, y)
    out.append(s)
    return "".join(out), w, max(56, y + 8)


def _grid(C, d, w, y, cells=None, cols=None, tone=None):
    cells = cells if cells is not None else d.get("cells", [])
    cols = cols or d.get("cols") or (4 if w > 300 else 2)
    cols = max(1, min(cols, len(cells)))
    cw = (w - 16 - GAP * (cols - 1)) / cols
    out = []
    for r in range(0, len(cells), cols):
        row = cells[r:r + cols]
        h = max(C.height(z, cw) for z in row)
        x = 8 + (w - 16 - (len(row) * cw + GAP * (len(row) - 1))) / 2
        for z in row:
            out.append(C.draw(z, x, y, cw, h, tone))
            x += cw + GAP
        y += h + GAP
    return "".join(out), y - GAP


def _columns(C, d, w, y, mirror=False):
    out = []
    head, rows = d.get("head") or [], d.get("rows") or []
    ncol = max([len(r) for r in rows] + [len(head)] + [1])
    mid = 10 if d.get("arrow", True) and ncol == 2 else 0
    cw = (w - 16 - GAP * (ncol - 1) - mid * (ncol - 1)) / ncol
    xs = [8 + i * (cw + GAP + mid) for i in range(ncol)]
    if head:
        hh = max(block_h(hd, 7.6, cw - 6) for hd in head) + 6
        for i, hd in enumerate(head):
            out.append(f'<rect x="{xs[i]:.1f}" y="{y:.1f}" width="{cw:.1f}" height="{hh:.1f}" rx="3" fill="{"#E3D4BA" if i == 0 and ncol == 2 else "#F2D9A0"}" stroke="{INK}" stroke-width=".9"/>')
            s, _ = block(xs[i] + cw / 2, y + 3, hd, 7.6, cw - 6)
            out.append(s)
        y += hh + 4
    if mirror:  # Spiegelachse
        top = y
    for r in rows:
        h = max(C.height(z, cw) for z in r)
        for i, z in enumerate(r):
            tone = ("old" if i == 0 else "new") if ncol == 2 and not mirror and d.get("tones", True) else None
            out.append(C.draw(z, xs[i], y, cw, h, tone))
        if mid and len(r) == 2:
            ax = xs[0] + cw + GAP / 2
            if mirror:
                out.append(arrow(ax + 1, y + h / 2, ax + mid + GAP - 1, y + h / 2, sw=1.1) + arrow(ax + mid + GAP - 1, y + h / 2, ax + 1, y + h / 2, sw=1.1))
            else:
                out.append(arrow(ax, y + h / 2, ax + mid + GAP - 1, y + h / 2))
        y += h + GAP
    return "".join(out), y - GAP


def _arrows(C, d, w, y, chain=False):
    cells, links = d.get("cells", []), d.get("links") or []
    per = d.get("cols") or (3 if w < 300 else 4)
    if chain:
        per = d.get("cols") or (2 if w < 300 else 4)
    per = max(1, min(per, len(cells)))
    gap = 26 if any(links) else 16
    cw = (w - 16 - gap * (per - 1)) / per
    out, boxes = [], []
    rows = [cells[i:i + per] for i in range(0, len(cells), per)]
    for ri, row in enumerate(rows):
        h = max(C.height(z, cw) for z in row)
        for ci, z in enumerate(row):
            x = 8 + ci * (cw + gap)
            out.append(C.draw(z, x, y, cw, h))
            boxes.append((x, y, cw, h))
        y += h + (18 if ri < len(rows) - 1 else 0)
    for k in range(len(boxes) - 1):
        (x1, y1, w1, h1), (x2, y2, w2, h2) = boxes[k], boxes[k + 1]
        lab = links[k] if k < len(links) else None
        if abs(y1 - y2) < 1:  # gleiche Zeile
            ax1, ay, ax2 = x1 + w1 + 1.5, y1 + h1 / 2, x2 - 1.5
            out.append(arrow(ax1, ay, ax2, ay, head=not chain))
            if lab:
                out.append(small_label((ax1 + ax2) / 2, ay - 4, lab, 6))
        else:  # nächste Zeile: von unten Mitte zum Anfang der nächsten Zeile
            sx, sy, ex, ey = x1 + w1 / 2, y1 + h1 + 1, x2 + w2 / 2, y2 - 1.5
            midy = (sy + ey) / 2
            path = f'M{sx:.1f} {sy:.1f}V{midy:.1f}H{ex:.1f}V{ey - 4:.1f}'
            out.append(f'<path d="{path}" fill="none" stroke="{INK}" stroke-width="1.4" stroke-linejoin="round"/>' + arrow(ex, ey - 5, ex, ey, head=not chain))
            if lab:
                out.append(small_label((sx + ex) / 2, midy - 2.5, lab, 6.2))
    return "".join(out), y


def _switch(C, d, w, y):
    out = []
    cw = min(w - 30, 150 if w < 300 else 220)
    h = C.height(d["cond"], cw)
    cx = w / 2
    out.append(C.draw(d["cond"], cx - cw / 2, y, cw, h))
    y2 = y + h + 22
    bw = (w - 16 - 10) / 2
    hb = max(C.height(d["yes"], bw), C.height(d["no"], bw))
    for i, (k, lk) in enumerate((("yes", "yes_label"), ("no", "no_label"))):
        bx = 8 + i * (bw + 10)
        out.append(f'<path d="M{cx:.1f} {y + h:.1f}V{y + h + 8:.1f}H{bx + bw / 2:.1f}V{y2 - 5:.1f}" fill="none" stroke="{INK}" stroke-width="1.4" stroke-linejoin="round"/>'
                   + arrow(bx + bw / 2, y2 - 6, bx + bw / 2, y2 - 1))
        if d.get(lk):
            out.append(small_label(bx + bw / 2 + (8 if i == 0 else -8), y + h + 18, d[lk], 6.6, anchor="start" if i == 0 else "end"))
        out.append(C.draw(d[k], bx, y2, bw, hb, "new" if i == 0 else "old"))
    return "".join(out), y2 + hb


def _outline(C, d, w, y):
    """Gliederungsbild: benannte Glieder untereinander (Formular, Brief, Gliederung); leere Glieder gestrichelt."""
    out = []
    cells = d.get("cells", [])
    if w > 300 and len(cells) > 3:
        return _grid(C, d, w, y, cols=2)
    for z in cells:
        h = C.height(z, w - 16)
        out.append(C.draw(z, 8, y, w - 16, h))
        y += h + 3
    return "".join(out), y - 3


def _dialogue(C, d, w, y):
    out = []
    for i, t in enumerate(d.get("turns", [])):
        left = i % 2 == 0
        bw = w - 16 - 28
        z = dict(t["cell"])
        h = max(22, C.height(z, bw))
        px = 8 if left else w - 8 - 22
        bx = 8 + 28 if left else 8
        out.append(C.portrait(t["who"], px, y + (h - 22) / 2, 22))
        out.append(C.draw(z, bx, y, bw, h))
        ty = y + h / 2
        if left:
            out.append(f'<path d="M{bx + .5:.1f} {ty - 4:.1f}L{bx - 5:.1f} {ty:.1f}L{bx + .5:.1f} {ty + 4:.1f}" fill="{FILL["plain"]}" stroke="{INK}" stroke-width=".9" stroke-linejoin="round"/>')
        else:
            out.append(f'<path d="M{bx + bw - .5:.1f} {ty - 4:.1f}L{bx + bw + 5:.1f} {ty:.1f}L{bx + bw - .5:.1f} {ty + 4:.1f}" fill="{FILL["plain"]}" stroke="{INK}" stroke-width=".9" stroke-linejoin="round"/>')
        y += h + 5
    return "".join(out), y - 5


def _timeline(C, d, w, y):
    cells = d.get("cells", [])
    n = len(cells)
    if not n:
        return "", y
    cw = (w - 16 - GAP * (n - 1)) / n
    h = max(C.height(z, cw) for z in cells)
    ay = y + 6
    out = [arrow(8, ay, w - 6, ay, sw=1.6)]
    for i, z in enumerate(cells):
        x = 8 + i * (cw + GAP)
        out.append(f'<circle cx="{x + cw / 2:.1f}" cy="{ay:.1f}" r="3" fill="#C08A2A" stroke="{INK}" stroke-width=".8"/>')
        out.append(f'<path d="M{x + cw / 2:.1f} {ay + 3:.1f}V{ay + 10:.1f}" stroke="{INK}" stroke-width=".8"/>')
        out.append(C.draw(z, x, ay + 10, cw, h))
    return "".join(out), ay + 10 + h


def _balance(C, d, w, y):
    out = []
    left, right = d.get("left", []), d.get("right", [])
    pw = (w - 16 - 14) / 2
    hl = sum(C.height(z, pw) + 3 for z in left) - 3
    hr = sum(C.height(z, pw) + 3 for z in right) - 3
    cx, beam_y = w / 2, y + 8
    tilt = 5 if d.get("heavier", "right") == "right" else -5
    out.append(f'<path d="M{cx:.1f} {beam_y - 2:.1f}l-6 -6h12z" fill="#C08A2A" stroke="{INK}" stroke-width=".8"/>')
    out.append(f'<path d="M{8 + pw / 2:.1f} {beam_y - tilt:.1f}L{w - 8 - pw / 2:.1f} {beam_y + tilt:.1f}" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>')
    for side, items, x, dy in (("l", left, 8, -tilt), ("r", right, w - 8 - pw, tilt)):
        yy = beam_y + dy + 8
        out.append(f'<path d="M{x + pw / 2:.1f} {beam_y + dy:.1f}V{yy:.1f}" stroke="{INK}" stroke-width=".9"/>')
        for z in items:
            h = C.height(z, pw)
            out.append(C.draw(z, x, yy, pw, h, "plain" if side == "l" else "new"))
            yy += h + 3
    y2 = beam_y + 8 + max(hl, hr) + abs(tilt) + 4
    if d.get("verdict"):
        s, hh = block(w / 2, y2 + 2, d["verdict"], 8.4, w - 30)
        out.append(s)
        y2 += hh + 4
    return "".join(out), y2


def _stairs(C, d, w, y):
    cells = d.get("cells", [])
    n = len(cells)
    if not n:
        return "", y
    cw = (w - 16 - 3 * (n - 1)) / n
    hs = [C.height(z, cw) for z in cells]
    step = 9
    top = y
    base = y + max(hs) + step * (n - 1)
    out = []
    for i, z in enumerate(cells):
        x = 8 + i * (cw + 3)
        yy = base - hs[i] - step * i if d.get("up", True) else top + step * i
        out.append(C.draw(z, x, yy, cw, hs[i]))
    return "".join(out), base


def _levels(C, d, w, y):
    out = []
    for key, lk in (("top", "top_label"), ("bottom", "bottom_label")):
        if d.get(lk):
            out.append(small_label(10, y + 7, d[lk], 7, anchor="start"))
            y += 10
        s, y = _grid(C, d, w, y, cells=d.get(key, []), cols=len(d.get(key, [])) or 1, tone="new" if key == "bottom" else None)
        out.append(s)
        y += 8
    return "".join(out), y - 8


def _rings(C, d, w, y):
    out = []
    ring = d.get("ring") or {}
    rh = C.height(ring, w - 24)
    s_core, y_core = _grid(C, d, w - 20, 0, cells=d.get("core", []), cols=d.get("cols"))
    inner_h = y_core
    total = rh + inner_h + 16
    out.append(f'<rect x="6" y="{y:.1f}" width="{w - 12:.1f}" height="{total:.1f}" rx="10" fill="#FBEFD5" stroke="{INK}" stroke-width="1.2"/>')
    out.append(C.draw(dict(ring, tone=ring.get("tone", "plain")), 12, y + 4, w - 24, rh))
    out.append(f'<g transform="translate(10 {y + rh + 10:.1f})">{s_core}</g>')
    return "".join(out), y + total


def _tree(C, d, w, y):
    return _arrows(C, d, w, y, chain=True)


VISUALS = {
    "grid": _grid, "columns": _columns, "mirror": lambda C, d, w, y: _columns(C, d, w, y, mirror=True),
    "arrows": _arrows, "switch": _switch, "outline": _outline, "dialogue": _dialogue, "timeline": _timeline,
    "balance": _balance, "stairs": _stairs, "levels": _levels, "rings": _rings, "tree": _tree,
}
