#!/usr/bin/env node
// Anordnung Text/Bild je Breite im echten Browser (Hinweis Andi Neck 2026-10-25: «die Bilder brauchen eine sinnvolle
// Mindestbreite, sonst früher umbrechen»). Drei Stufen:
//   Handy (< 600 px)   Kacheln einzeln zum Wischen, jede mindestens 280 px breit
//   mittel             Bild in voller Breite unter dem Text
//   breit              Text links, Bild rechts, sobald der Lesebereich (ohne Seitenleiste) 770 px hat; Seitenleiste ab 1200 px
// Überall: kein Bild ragt aus dem Fenster, keine Kachel unter 220 px, «Legende» bündig unter der ersten Kachel.
//   node scripts/test_bible_layout.cjs
const http = require('http'), fs = require('fs'), path = require('path');
const {chromium} = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const ROOT = path.join(__dirname, '..', 'build', 'bible-txt');
const srv = http.createServer((q, r) => {const f = path.join(ROOT, decodeURIComponent(q.url.split('?')[0]).replace(/^\/$/, '/index.html'));
  fs.readFile(f, (e, d) => {if (e) {r.writeHead(404); r.end(); return;} r.writeHead(200, {'Content-Type': f.endsWith('.html') ? 'text/html; charset=utf-8' : 'text/plain'}); r.end(d);});});
(async () => {
  await new Promise(ok => srv.listen(0, ok));
  const url = `http://localhost:${srv.address().port}/index.html`;
  const b = await chromium.launch(), fails = [];
  for (const [w, stage] of [[390, 'handy'], [600, 'handy'], [700, 'mittel'], [800, 'mittel'], [1000, 'breit'], [1200, 'breit'], [1400, 'breit'], [1800, 'breit']]) {
    const p = await b.newPage({viewport: {width: w, height: 900}});
    await p.goto(url); await p.waitForSelector('.stream-entry .ill-wrap', {timeout: 15000}); await p.waitForTimeout(300);
    if (w < 760) await p.click('[data-view=image]');  // schmal: Umschalter Text/Bild
    const r = await p.evaluate(() => {
      const wrap = document.querySelector('.stream-entry .ill-wrap'), tiles = [...wrap.querySelectorAll('svg.ill-tile')].filter(t => t.getBoundingClientRect().width > 0);
      const R = e => e.getBoundingClientRect(), txt = R(wrap.querySelector('.ill-text')), t0 = R(tiles[0]);
      return {side: getComputedStyle(wrap).display === 'grid', aside: getComputedStyle(document.querySelector('aside')).display !== 'none',
        minTile: Math.min(...tiles.map(t => R(t).width)), right: Math.max(...tiles.map(t => R(t).right)), vw: innerWidth,
        scroller: getComputedStyle(wrap.querySelector('.ill-tiles')).overflowX, t0left: t0.left, legLeft: R(wrap.querySelector('[data-legend]')).left,
        imgLeft: t0.left, txtRight: txt.right};});
    const f = m => fails.push(`${w}px (${stage}): ${m}`);
    if (stage === 'handy') {if (r.scroller !== 'auto') f('Kacheln nicht zum Wischen'); if (r.minTile < 280) f(`Kachel nur ${Math.round(r.minTile)} px`);}
    else {if (r.right > r.vw + 1) f(`Bild ragt ${Math.round(r.right - r.vw)} px aus dem Fenster`); if (r.minTile < 220) f(`Kachel nur ${Math.round(r.minTile)} px`);
      if ((stage === 'breit') !== r.side) f(r.side ? 'Bild neben dem Text, erwartet darunter' : 'Bild unter dem Text, erwartet daneben');
      if (r.side && r.imgLeft < r.txtRight) f('Bild überdeckt den Text');
      if (Math.abs(r.legLeft - r.t0left) > 8) f(`Legende nicht bündig unter dem Bild (${Math.round(r.legLeft - r.t0left)} px)`);}
    if (r.aside !== (w >= 1200)) f(r.aside ? 'Seitenleiste unter 1200 px sichtbar' : 'Seitenleiste fehlt ab 1200 px');
    await p.close();
  }
  await b.close(); srv.close();
  if (fails.length) {console.log(fails.map(x => 'FEHLER: ' + x).join('\n')); process.exit(1);}
  console.log('PASS: Anordnung Text/Bild in drei Stufen (Handy wischen, mittel darunter, breit daneben), Mindestbreiten, Legende bündig, Seitenleiste ab 1200 px.');
})();
