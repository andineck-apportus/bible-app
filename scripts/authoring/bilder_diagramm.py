#!/usr/bin/env python3
"""Strukturbilder (docs/STRUKTURKATALOG.md, Abschnitt 2c «Darstellungen»): Kacheln, die den Bau eines Textes zeigen statt
einer Szene – Raster, Spalten, Pfeilkette, Weiche, Gliederungsbild, Dialogspalten, Zeitleiste, Waage, Treppe, zwei Ebenen,
Ringe, Spiegelachse, Kette (Stammbaum), Kreis.

Ein Feld im Bildauftrag trägt dafür `diagram` statt einer Bühne:

    "diagram": {"visual": "grid", "speaker": "FIG-JESUS", "title": {"de": "Selig sind …", "gsw": "…"},
                "span": 1|2, "cols": 2,
                "cells": [Zelle, …]                       # grid, arrows, stairs, timeline, outline, tree
                "head": [Wort, Wort], "rows": [[Zelle, Zelle], …]   # columns, mirror
                "head_tones": ["old", "new"], "tones": false, "arrow": false   # columns: Farben, ohne Pfeil (keine Paare)
                "links": [Wort, …]                        # arrows: Beschriftung je Pfeil (z. B. «denn»), optional
                "cond": Zelle, "yes": Zelle, "no": Zelle, "yes_label": Wort, "no_label": Wort   # switch
                "left": [Zelle], "right": [Zelle], "verdict": Wort   # balance
                "top": [Zelle], "bottom": [Zelle], "top_label": Wort, "bottom_label": Wort   # levels
                "ring": Zelle, "core": [Zelle]            # rings (Rahmen und Mitte)
                "turns": [{"who": "FIG-…", "cell": Zelle}]   # dialogue
                "cells" + "there"/"back": Wort         # circle (zwei Glieder: hin und zurück; mehr: Kreislauf)
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
def wrapn(s, fs, maxw, maxlines=14, bold=True):
    k = 1.0 if bold else .94
    words = []
    for w in s.split(" "):  # zu langes Wort (schmale Zelle): mit Trennstrich teilen, nicht über den Rand
        while text_w(w, fs) * k > maxw and len(w) > 6:
            cut = max(3, min(len(w) - 3, int(len(w) * maxw / (text_w(w, fs) * k)) - 1))
            words.append(w[:cut] + "-")
            w = w[cut:]
        words.append(w)
    lines, cur = [], ""
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


def fit(v, fs, maxw, maxlines=14, bold=True, min_fs=6.5):
    """Schriftgrösse so, dass die längste Wortfolge passt (je Sprache gleich), und Zeilenzahl."""
    lab = _lab(v)
    while True:
        lines = {k: wrapn(s, fs, maxw, maxlines, bold) for k, s in lab.items()}
        too_wide = any(text_w(x, fs) * (1 if bold else .94) > maxw + .5 for ls in lines.values() for x in ls)
        if not too_wide or fs <= min_fs:
            return fs, lines, max(len(ls) for ls in lines.values())
        fs -= .5


def block(x, y, v, fs, maxw, anchor="middle", weight="700", fill=INK, maxlines=14):
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


def block_h(v, fs, maxw, weight="700", maxlines=14):
    if not v:
        return 0
    fs, _, n = fit(v, fs, maxw, maxlines, weight == "700")
    return n * fs * 1.18


EMPTY_NOTE = {"de": "im Text nicht genannt", "gsw": "im Text nöd gnännt"}


def initials(v):
    """Anfangsbuchstaben je Sprache («Selig sind die Armen» → «S. s. d. A.») für die Fassung «ohne Worte»."""
    if not v:
        return None
    def one(t):
        out = []
        for w in str(t).replace("–", " ").replace("→", " ").split():
            c = next((ch for ch in w if ch.isalnum()), "")
            if c:
                out.append(c + ".")
        return " ".join(out)
    return {k: one(t) for k, t in v.items()} if isinstance(v, dict) else one(v)


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

    ICON_H = 20  # gut erkennbar (Hinweis Andi Neck 2026-10-24: Zeichen mit Händen zu klein)
    PAD = 4

    def height(self, z, w):
        """Höhe einer Zelle bei Breite w."""
        if z.get("empty") and not (z.get("a") or z.get("b")):
            return max(18, block_h(EMPTY_NOTE, 6.8, w - 8, "400", 3) + 8)
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
        out = [f'<g class="dg-cell"><rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="4" fill="{fill}" stroke="{INK}" stroke-width="{sw}"{dash}/>']
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
            # leeres Glied: sagen, dass der Text hier nichts nennt (Hinweis Andi Neck 2026-10-25: ein Strich wirkte wie ein Fehler);
            # bleibt auch ohne Worte sichtbar (class dg-keep), weil es nichts aufzudecken gibt
            nh = block_h(EMPTY_NOTE, 6.8, w - 8, "400", 3)
            s, _ = block(x + w / 2, y + (h - nh) / 2, EMPTY_NOTE, 6.8, w - 8, weight="400", fill=MUTED, maxlines=3)
            out.append(f'<g class="dg-keep">{s}</g>')
        full = "".join(out[1:])
        out = [out[0], f'<g class="dg-full">{full}</g>', self.nowords(z, x, y, w, h, col)]
        if z.get("strike"):
            out.append(f'<path d="M{x + 4:.1f} {y + h - 4:.1f}L{x + w - 4:.1f} {y + 4:.1f}" stroke="#B0413E" stroke-width="1.3" stroke-linecap="round" opacity=".5"/>')
        return "".join(out) + "</g>"

    def nowords(self, z, x, y, w, h, col):
        """Fassung «ohne Worte» (Hinweise Andi Neck 2026-10-25). Stufe 0 (nw0): Zeichen gross und mittig im ganzen Kästchen;
        Stufe 1 (nw1, auf Antippen): Zeichen kleiner, darunter die Anfangsbuchstaben; Stufe 2 zeigt die App mit dg-full.
        Hat die Zelle kein eigenes Zeichen, wird eines über die Worte gesucht (nw_icons), sonst das Porträt; ohne Treffer
        stehen gleich die Anfangsbuchstaben (nie ein leeres Feld). Die App blendet die Gruppe nur «ohne Worte» ein."""
        if z.get("empty") and not (z.get("a") or z.get("b")):
            return ""
        icons = list(z.get("icons") or []) or _auto.nw_icons(self.c, z.get("a") or z.get("b"), getattr(self, "cands", ()))
        if not icons and z.get("who"):
            icons = [z["who"]]
        ini = initials(z.get("a") or z.get("b"))
        tw = w - 2 * self.PAD
        if not icons:
            th = block_h(ini, 8.2, tw, "700", 4)
            s0, _ = block(x + w / 2, y + max(self.PAD, (h - th) / 2), ini, 8.2, tw, fill=col, maxlines=4)
            return f'<g class="dg-nw" display="none"><g class="nw0">{s0}</g></g>'
        big = max(12, (h - 2 * self.PAD) * .88)  # etwas Luft: manche Zeichen reichen über ihre Box
        s0 = self.icons(icons, x + w / 2, y + (h - big) / 2, big, tw * .85)  # Rand: manche Zeichen reichen etwas über ihre Box
        if self.icon_row_w(icons, big) > tw * .85:  # durch die Breite begrenzt: senkrecht mitten
            hh = big * tw * .85 / self.icon_row_w(icons, big)
            s0 = self.icons(icons, x + w / 2, y + (h - hh) / 2, hh, tw * .85)
        ih_txt = block_h(ini, 7.6, tw, "700", 3) if ini else 0
        ih = max(12, min(h - 2 * self.PAD - ih_txt - 3, 36))
        tot = ih + (ih_txt + 2 if ini else 0)
        yy = y + max(self.PAD, (h - tot) / 2)
        s1 = self.icons(icons, x + w / 2, yy, ih, tw * .85)
        if ini:
            t1, _ = block(x + w / 2, yy + ih + 2, ini, 7.6, tw, fill=col, maxlines=3)
            s1 += t1
        return f'<g class="dg-nw" display="none"><g class="nw0">{s0}</g><g class="nw1">{s1}</g></g>'


def arrow(x1, y1, x2, y2, col=INK, head=True, dash=False, sw=1.4):
    ang = math.atan2(y2 - y1, x2 - x1)
    h = ""
    if head:
        h = (f'<path d="M{x2 - 5 * math.cos(ang - .5):.1f} {y2 - 5 * math.sin(ang - .5):.1f}L{x2:.1f} {y2:.1f}'
             f'L{x2 - 5 * math.cos(ang + .5):.1f} {y2 - 5 * math.sin(ang + .5):.1f}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>')
    d = ' stroke-dasharray="3 2"' if dash else ""
    return f'<path d="M{x1:.1f} {y1:.1f}L{x2:.1f} {y2:.1f}" stroke="{col}" stroke-width="{sw}" stroke-linecap="round"{d}/>' + h


def label_w(v, fs=6.4):
    return _auto.lwidth(v, fs) + 6 if v else 0


def link(svg, x1, y1, x2, y2):
    """Verbindung zwischen zwei Zellen: Anfang und Ende als Daten, damit pruefe_bilder.py prüft, dass sie an den Zellen sitzen."""
    return f'<g class="dg-link" data-a="{x1:.1f},{y1:.1f}" data-b="{x2:.1f},{y2:.1f}">{svg}</g>'


def small_label(x, y, v, fs=6.8, fill="#8A6A2A", anchor="middle"):
    """Beschriftung (Pfeil, Zweig) auf einem hellen Schild, damit sie nichts überdeckt und lesbar bleibt; y = Grundlinie."""
    w = _auto.lwidth(v, fs) + 5
    x0 = x - w / 2 if anchor == "middle" else (x - 2.5 if anchor == "start" else x - w + 2.5)
    return (f'<g class="dg-label"><rect x="{x0:.1f}" y="{y - fs * .9:.1f}" width="{w:.1f}" height="{fs * 1.25:.1f}" rx="{fs * .6:.1f}" fill="#FFF8E8" stroke="#C9B48A" stroke-width=".5"/>'
            + _auto.ltext(x, y, v, fs, anchor=anchor, weight="700", fill=fill) + "</g>")


# ------------------------------------------------------------------ Kachel
def diagram(comp, d):
    """SVG-Inhalt und Grösse (w, h) einer Strukturkachel."""
    w = W1 * (2 if d.get("span") == 2 else 1) + (4 if d.get("span") == 2 else 0) - 4 * 0
    if d.get("span") == 2:
        w = 2 * W1 + 2
    C = Cells(comp)
    C.cands = _auto.panel_icons({"diagram": d})
    # Kästchen ohne eigenes Zeichen bekommen eines (geprüfte Zuordnung, sonst über die Worte), auch neben den Worten
    # (Hinweis Andi Neck 2026-10-25); Porträt-Zellen und leere Zellen bleiben, wie sie sind
    def _fill(o):
        if isinstance(o, dict):
            if (o.get("a") or o.get("b")) and not o.get("icons") and not o.get("who") and not o.get("empty"):
                ic = _auto.zeichen(comp, "zelle", o.get("a") or o.get("b"), C.cands)
                if ic:
                    o = dict(o, icons=ic)
            return {k: _fill(v) for k, v in o.items()}
        if isinstance(o, list):
            return [_fill(v) for v in o]
        return o
    d = _fill(d)
    out, y = [], 6
    # Kopf: Sprecher (Porträt) mit Titel in einer Sprechblase, sonst Titel als Zeile; Feldnummer oben links bleibt frei
    if d.get("speaker") or d.get("title"):
        x0 = 28
        if d.get("speaker"):
            out.append(C.portrait(d["speaker"], x0, 8, 20))
            x0 += 26
        tw = w - x0 - 8
        ti = _auto.zeichen(comp, "titel", d["title"], C.cands) if d.get("title") else []
        tiw = C.icon_row_w(ti, 14) + 4 if ti else 0
        th = block_h(d.get("title"), 8.6, tw - 8 - tiw) if d.get("title") else 0
        if d.get("title"):
            bh = max(20, th + 8)
            frame = f'<rect x="{x0:.1f}" y="8" width="{tw:.1f}" height="{bh:.1f}" rx="7" fill="#FFFFFF" stroke="{INK}" stroke-width="1.1"/>'
            if d.get("speaker"):
                frame += (f'<path d="M{x0 + 1:.1f} 15L{x0 - 5:.1f} 18L{x0 + 1:.1f} 21" fill="#FFFFFF" stroke="{INK}" stroke-width="1.1" stroke-linejoin="round"/>'
                          f'<path d="M{x0 + 1.2:.1f} 15.6V20.4" stroke="#FFFFFF" stroke-width="1.4"/>')
            s, _ = block(x0 + tiw + (tw - tiw) / 2, 8 + (bh - th) / 2, d["title"], 8.6, tw - 8 - tiw)
            if ti:  # Zeichen links in der Blase, neben den Worten
                s = C.icons(ti, x0 + 4 + (tiw - 4) / 2, 8 + (bh - 14) / 2, 14, tiw - 4) + s
            # ohne Worte: die Blase zeigt passende Zeichen (sonst die Anfangsbuchstaben), nie leer (Hinweis Andi Neck 2026-10-25)
            out.append(_auto.sw(s, _auto.nw_fill(comp, x0 + 4, 10, tw - 8, bh - 4, ti, d["title"]), frame))
            y = 8 + bh + 6
        else:
            y = 34
    else:
        y = 28
    v = d["visual"]
    fn = VISUALS.get(v)
    if fn is None:
        raise SystemExit(f"FEHLER: Darstellung {v} im Zeichner noch nicht umgesetzt")
    s, y = fn(C, d, w, y)
    out.append(f'<g class="dg-vis" data-visual="{v}">{s}</g>')
    return "".join(out), w, max(56, y + 10)  # Abstand zum Rahmen (Hinweis Andi Neck 2026-10-24)


def _grid(C, d, w, y, cells=None, cols=None, tone=None):
    cells = cells if cells is not None else d.get("cells", [])
    cols = cols or d.get("cols") or (4 if w > 300 else 2)
    cols = max(1, min(cols, len(cells)))
    out = []
    rows = [cells[r:r + cols] for r in range(0, len(cells), cols)]
    # jede Zeile füllt die Breite, auch eine kürzere letzte (keine Zelle ohne Nachbarn mit Leerraum daneben, Hinweis Andi Neck 2026-10-24)
    for row in rows:
        cw = (w - 16 - GAP * (len(row) - 1)) / len(row)
        h = max(C.height(z, cw) for z in row)
        x = 8
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
        hic = [_auto.zeichen(C.c, "kopf", hd, C.cands)[:1] for hd in head]
        hiw = [C.icon_row_w(ic, 12) + 3 if ic else 0 for ic in hic]
        hh = max(max(block_h(hd, 7.6, cw - 6 - hiw[i]) for i, hd in enumerate(head)) + 6, 16 if any(hic) else 0)
        for i, hd in enumerate(head):
            ht = (d.get("head_tones") or [])[i] if i < len(d.get("head_tones") or []) else (
                ("old" if i == 0 else "new") if ncol == 2 and d.get("tones", True) and not mirror else "plain")
            hf = {"old": "#E3D4BA", "new": "#F2D9A0", "plain": "#EADFC8"}.get(ht, "#EADFC8")
            frame = f'<rect x="{xs[i]:.1f}" y="{y:.1f}" width="{cw:.1f}" height="{hh:.1f}" rx="3" fill="{hf}" stroke="{INK}" stroke-width=".9"/>'
            th_ = block_h(hd, 7.6, cw - 6 - hiw[i])
            s, _ = block(xs[i] + hiw[i] + (cw - hiw[i]) / 2, y + (hh - th_) / 2, hd, 7.6, cw - 6 - hiw[i])
            if hic[i]:  # Zeichen links im Kopf, neben den Worten
                s = C.icons(hic[i], xs[i] + 3 + (hiw[i] - 3) / 2, y + (hh - 12) / 2, 12, hiw[i] - 3) + s
            out.append(_auto.sw(s, _auto.nw_fill(C.c, xs[i] + 2, y + 1.5, cw - 4, hh - 3, hic[i], hd), frame))
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
                a1, a2 = xs[0] + cw + 1.5, xs[1] - 1.5
                out.append(link(arrow(a1, y + h / 2, a2, y + h / 2, sw=1.1) + arrow(a2, y + h / 2, a1, y + h / 2, sw=1.1), a1, y + h / 2, a2, y + h / 2))
            else:
                a1, a2 = xs[0] + cw + 1.5, xs[1] - 1.5  # Pfeil genau von Zelle zu Zelle (Hinweis Andi Neck 2026-10-24)
                out.append(link(arrow(a1, y + h / 2, a2, y + h / 2), a1, y + h / 2, a2, y + h / 2))
        y += h + GAP
    return "".join(out), y - GAP


def _arrows(C, d, w, y, chain=False):
    cells, links = d.get("cells", []), d.get("links") or []
    per = d.get("cols") or (3 if w < 300 else 4)
    if chain:
        per = d.get("cols") or (2 if w < 300 else 4)
    per = max(1, min(per, len(cells)))
    while per > 1 and (w - 16) / per < 74:  # Zellen nicht zu schmal (Handy)
        per -= 1
    gap = max([16] + [label_w(lk) + 10 for lk in links if lk])
    gap = min(gap, (w - 16) / per * .6)
    cw = (w - 16 - gap * (per - 1)) / per
    out, boxes = [], []
    rows = [cells[i:i + per] for i in range(0, len(cells), per)]
    for ri, row in enumerate(rows):
        rw = (w - 16 - gap * (len(row) - 1)) / len(row)  # Zeile füllt die Breite, auch die letzte
        h = max(C.height(z, rw) for z in row)
        for ci, z in enumerate(row):
            x = 8 + ci * (rw + gap)
            out.append(C.draw(z, x, y, rw, h))
            boxes.append((x, y, rw, h))
        y += h + (18 if ri < len(rows) - 1 else 0)
    for k in range(len(boxes) - 1):
        (x1, y1, w1, h1), (x2, y2, w2, h2) = boxes[k], boxes[k + 1]
        lab = links[k] if k < len(links) else None
        if abs(y1 - y2) < 1:  # gleiche Zeile
            ax1, ay, ax2 = x1 + w1 + 1.5, y1 + h1 / 2, x2 - 1.5
            out.append(link(arrow(ax1, ay, ax2, ay, head=not chain), ax1, ay, ax2, ay))
            if lab:
                out.append(small_label((ax1 + ax2) / 2, ay - 4, lab, 6.2))
        else:  # nächste Zeile: von unten Mitte zum Anfang der nächsten Zeile
            sx, sy, ex, ey = x1 + w1 / 2, y1 + h1 + 1, x2 + w2 / 2, y2 - 1.5
            midy = (sy + ey) / 2
            path = f'M{sx:.1f} {sy:.1f}V{midy:.1f}H{ex:.1f}V{ey - 4:.1f}'
            out.append(link(f'<path d="{path}" fill="none" stroke="{INK}" stroke-width="1.4" stroke-linejoin="round"/>' + arrow(ex, ey - 5, ex, ey, head=not chain), sx, sy, ex, ey))
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
        out.append(link(f'<path d="M{cx:.1f} {y + h:.1f}V{y + h + 8:.1f}H{bx + bw / 2:.1f}V{y2 - 5:.1f}" fill="none" stroke="{INK}" stroke-width="1.4" stroke-linejoin="round"/>'
                   + arrow(bx + bw / 2, y2 - 6, bx + bw / 2, y2 - 1.5), cx, y + h, bx + bw / 2, y2 - 1.5))
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
    if cw < 72:  # schmal (Handy): Zeitleiste senkrecht, Stationen untereinander
        out, x0, bw = [], 20, w - 28
        top = y + 2
        for z in cells:
            h = C.height(z, bw)
            out.append(f'<circle cx="12" cy="{y + h / 2:.1f}" r="3" fill="#C08A2A" stroke="{INK}" stroke-width=".8"/>'
                       f'<path d="M15 {y + h / 2:.1f}H{x0:.1f}" stroke="{INK}" stroke-width=".8"/>')
            out.append(C.draw(z, x0, y, bw, h))
            y += h + 4
        out.insert(0, arrow(12, top, 12, y, sw=1.6))
        return "".join(out), y
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
    hs = [max(C.height(z, cw) for z in cells)] * n  # gleich hohe Stufen
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


def _circle(C, d, w, y):
    """Kreislauf oder Spiegelstrafe: Glieder auf einem Kreis, Pfeile im Kreis herum (zwei Glieder: hin und zurück)."""
    cells = d.get("cells", [])
    n = len(cells)
    if not n:
        return "", y
    cw = (w - 16 - 40) / 2 if n <= 2 else min(110 if w > 300 else 62, (w - 24) / 3)
    hs = [C.height(z, cw) for z in cells]
    rx = (w - 16 - cw) / 2 * (1 if n <= 2 else .82)
    ry = max(26, max(hs) * (.9 if n <= 2 else 1.7))
    cx, cy = w / 2, y + max(hs) / 2 + ry
    pos = []
    for i in range(n):
        a = -math.pi / 2 + 2 * math.pi * i / n if n > 2 else (math.pi if i == 0 else 0)
        pos.append((cx + rx * math.cos(a), cy + ry * math.sin(a) * (1 if n > 2 else 0)))
    out = []
    if n <= 2:  # zwei Glieder nebeneinander, oben Pfeil hin, unten Pfeil zurück
        h = max(hs)
        x1, x2 = 8, w - 8 - cw
        y0 = y + (14 if d.get("there") else 6)
        out.append(C.draw(cells[0], x1, y0, cw, h))
        if n == 2:
            out.append(C.draw(cells[1], x2, y0, cw, h, "new"))
        a1, a2 = x1 + cw + 4, x2 - 4
        out.append(f'<path d="M{a1:.1f} {y0 + h * .3:.1f}Q{w / 2:.1f} {y0 - 8:.1f} {a2:.1f} {y0 + h * .3:.1f}" fill="none" stroke="{INK}" stroke-width="1.4"/>'
                   + arrow(a2 - 3, y0 + h * .3 - 2.5, a2, y0 + h * .3))
        out.append(f'<path d="M{a2:.1f} {y0 + h * .7:.1f}Q{w / 2:.1f} {y0 + h + 8:.1f} {a1:.1f} {y0 + h * .7:.1f}" fill="none" stroke="{INK}" stroke-width="1.4"/>'
                   + arrow(a1 + 3, y0 + h * .7 + 2.5, a1, y0 + h * .7))
        for k, lk in ((0, "there"), (1, "back")):
            if d.get(lk):
                out.append(small_label(w / 2, (y0 - 4) if k == 0 else (y0 + h + 10), d[lk], 6.4))
        return "".join(out), y0 + h + (16 if d.get("back") else 12)
    out.append(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="none" stroke="{INK}" stroke-width="1.3" stroke-dasharray="4 3"/>')
    for i in range(n):  # Pfeilspitze auf dem Kreis zwischen zwei Gliedern
        a = -math.pi / 2 + 2 * math.pi * (i + .5) / n
        px, py = cx + rx * math.cos(a), cy + ry * math.sin(a)
        tx, ty = -rx * math.sin(a), ry * math.cos(a)
        L = math.hypot(tx, ty) or 1
        out.append(arrow(px - tx / L * 4, py - ty / L * 4, px + tx / L * 2, py + ty / L * 2))
    for (px, py), z, h in zip(pos, cells, hs):
        out.append(C.draw(z, px - cw / 2, py - h / 2, cw, h))
    return "".join(out), cy + ry + max(hs) / 2


VISUALS = {
    "grid": _grid, "columns": _columns, "mirror": lambda C, d, w, y: _columns(C, d, w, y, mirror=True),
    "arrows": _arrows, "switch": _switch, "outline": _outline, "dialogue": _dialogue, "timeline": _timeline,
    "balance": _balance, "stairs": _stairs, "levels": _levels, "rings": _rings, "tree": _tree, "circle": _circle,
}
