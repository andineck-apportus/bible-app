#!/usr/bin/env python3
"""Layoutprüfung aller Strukturkacheln im Browser (Playwright): überlappende Beschriftungen, Text über den Rand seines Kastens
oder Kreises, Text ausserhalb der Kachel. Je Sprache (de, gsw) getrennt, weil die App nur eine zeigt.

    python3 scripts/authoring/struktur_layout.py            # alle Szenenpläne
    python3 scripts/authoring/struktur_layout.py GEN-B1 …   # einzelne Felder

Rückmeldung Andi Neck 2026-11-21: Texte überlappten in der Zeitreihe und vereinzelt sonst.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts/authoring"))
import struktur_kachel as SK  # noqa: E402
import vignetten as VG  # noqa: E402

RAND_KACHEL, RAND_KASTEN = 6, 3   # Mindestabstand des Textes zum Kachelrand und zum Rand seines Kastens (Rückmeldung 2026-11-21)

JS = """(lg) => {
  const r = [];
  const svg = document.querySelector('svg');
  const t = [...svg.querySelectorAll('text')].filter(x => !x.closest('.sk-zeichen')).filter(x => !x.classList.contains('lw') || x.classList.contains('lw-' + lg));
  const box = e => { if (e.tagName === 'text') { const b = e.getBBox(); return {x: b.x, y: b.y, w: b.width, h: b.height}; }
    const b = e.getBoundingClientRect(); return {x: b.x, y: b.y, w: b.width, h: b.height}; };
  const T = t.map(e => ({b: box(e), s: e.textContent.trim().slice(0, 40)})).filter(o => o.b.w > 0);
  const K = [...svg.querySelectorAll('rect')].filter(x => !x.closest('.sk-zeichen')).map(box).filter(b => b.w < +svg.getAttribute('width') - 2 && b.w > 0);
  const C = [...svg.querySelectorAll('circle')].map(box);
  // Bildfeld: verschachteltes svg nach seinen Attributen (getBoundingClientRect zählt den abgeschnittenen Rest des Bildes mit)
  const I = [...svg.querySelectorAll('image')].map(e => { const p = e.parentElement;
    if (p.tagName === 'svg' && p !== svg) { const v = n => parseFloat(p.getAttribute(n)); return {x: v('x'), y: v('y'), w: v('width'), h: v('height')}; }
    return box(e); });
  const ov = (a, b, m) => a.x + m < b.x + b.w && b.x + m < a.x + a.w && a.y + m < b.y + b.h && b.y + m < a.y + a.h;
  const inside = (a, b, p) => a.x >= b.x + p && a.y >= b.y + p && a.x + a.w <= b.x + b.w - p && a.y + a.h <= b.y + b.h - p;
  const RK = %d, RB = %d; const W = +svg.getAttribute('width'), HH = +svg.getAttribute('height');
  for (let i = 0; i < T.length; i++) {
    const a = T[i].b;
    if (a.x < RK || a.y < RK - 4 || a.x + a.w > W - RK || a.y + a.h > HH - 2) r.push('zu nah am Kachelrand: ' + T[i].s);
    for (let j = i + 1; j < T.length; j++) if (ov(a, T[j].b, 1)) r.push('überlappt: «' + T[i].s + '» / «' + T[j].s + '»');
    for (const k of K) if (ov(a, k, -RB) && !inside(a, k, RB) && !inside(k, a, 0) && !(inside(a, k, 0) && false)) {
      r.push((inside(a, k, 0) ? 'zu nah am Kastenrand: ' : 'über den Rand: ') + T[i].s); break; }
    for (const k of C) if (ov(a, k, 1) && !inside(a, k, -1)) { r.push('auf einem Kreis: ' + T[i].s); break; }
    for (const k of I) if (ov(a, k, 2)) { r.push('auf einem Bild: ' + T[i].s); break; }
  }
  for (let i = 0; i < K.length; i++) {
    if (K[i].x < 2 || K[i].y < 2 || K[i].x + K[i].w > W - 2 || K[i].y + K[i].h > HH - 2) r.push('Kasten am Kachelrand');
    for (let j = i + 1; j < K.length; j++)
      if (ov(K[i], K[j], 0) && !inside(K[i], K[j], 0) && !inside(K[j], K[i], 0)) r.push('Kästen überlappen (' + Math.round(K[i].x) + ',' + Math.round(K[i].y) + ' / ' + Math.round(K[j].x) + ',' + Math.round(K[j].y) + ')');
  }
  for (const im of I) for (const k of K) if (ov(im, k, 1) && !inside(im, k, 2) && !inside(k, im, 0)) { r.push('Bild über den Kastenrand'); break; }
  return r;
}""" % (RAND_KACHEL, RAND_KASTEN)


VIGN = {}   # zum Testen: Schlüssel → href für alle Glieder mit Auftrag (Platzhalter), sonst die geprüften


def plaene():
    for p in sorted((ROOT / "scripts/authoring/bilder_aquarell_daten").glob("szenen-*.json")):
        for sid, sz in json.loads(p.read_text(encoding="utf-8"))["szenen"].items():
            if sz.get("form") == "struktur":
                yield sid, sz["struktur"]


def main():
    from playwright.sync_api import sync_playwright
    global PLATZHALTER
    args = [x for x in sys.argv[1:] if not x.startswith("--")]
    # --platzhalter: jede Vignette mit Auftrag als graues Quadrat (Layout vor dem Malen prüfen)
    PLATZHALTER = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 10 10'><rect width='10' height='10' fill='%23bbb'/></svg>"
                   if "--platzhalter" in sys.argv else None)
    nur = set(args)
    fehler = 0
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width": 340, "height": 1400})
        pg.route("**/*", lambda r: r.abort() if r.request.url.startswith("http") else r.continue_())
        for sid, sx in plaene():
            if nur and sid not in nur:
                continue
            v = VG.gueltig(sid)
            if PLATZHALTER:
                v = {k: PLATZHALTER for _s, k, _e in VG.auftraege({sid})}
            inhalt, h = SK.zeichne(sx, v)
            svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{SK.BREITE}" height="{h:.0f}" viewBox="0 0 {SK.BREITE} {h:.1f}">{inhalt}</svg>'
            pg.set_content(f"<html><body style='margin:0'>{svg}</body></html>")
            for lg in ("de", "gsw"):
                for m in dict.fromkeys(pg.evaluate(JS, lg)):
                    print(f"{sid} [{lg}] {m}")
                    fehler += 1
        b.close()
    print(f"{'PASS' if not fehler else 'FEHLER'}: Layout Strukturkacheln – {fehler} Befunde")
    return 1 if fehler else 0


if __name__ == "__main__":
    sys.exit(main())
