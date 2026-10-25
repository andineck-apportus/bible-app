#!/usr/bin/env python3
"""Anordnung der Bilder im Browser prüfen (BILDPROZESS.md, Leitlinie 9; Hinweis Andi Neck 2026-10-24):
- Text in einer Zelle eines Strukturbilds ragt nicht über die Zelle hinaus;
- Beschriftungen von Pfeilen und Zweigen überdecken keine Zelle und keine andere Beschriftung;
- Inhalt der Strukturbilder hält Abstand zum Kachelrahmen;
- Pfeile zwischen Zellen beginnen und enden an einer Zelle (nicht daneben, nicht darin);
- keine Zeile eines Rasters oder einer Pfeilkette lässt grossen Leerraum (eine Zelle ohne Nachbarn füllt die Breite);
Geprüft wird je Sprache (de, gsw), mit der echten Schrift im Browser.

    python3 scripts/authoring/pruefe_bilder.py [PRÄFIX …]     # z. B. RUT MAT-005; ohne Präfix alle Anime-Bilder

Ausgabe: je Befund eine Zeile; Schluss PASS oder FEHLER mit Anzahl (Exit 1 bei Befunden).
"""
import json
import os
import pathlib
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[2]
ANI = ROOT / "data/illustrations/anime"

JS = r"""
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:900,height:900}});
const out=[];
for(const mode of ['','nw'])for(const lang of ['de','gsw']){
  await p.goto('file://'+process.argv[2]+'?'+lang);
  await p.addStyleTag({content:`.lw{display:none}.lw-${lang}{display:inline}`+(mode?'.dg-full{display:none}.dg-nw{display:inline}':'')});
  await p.waitForTimeout(200);
  const r=await p.evaluate(([lang,mode])=>{
    const res=[];const tol=.8;
    const inter=(a,b)=>a.x<b.x+b.width-tol&&a.x+a.width>b.x+tol&&a.y<b.y+b.height-tol&&a.y+a.height>b.y+tol;
    const vis=t=>{const cs=getComputedStyle(t);return cs.display!=='none'&&t.getBBox().width>0;};
    for(const fig of document.querySelectorAll('div.ill')){
      const id=fig.dataset.id;
      fig.querySelectorAll('svg.ill-tile').forEach((tile,ti)=>{
        const nm=tile.classList.contains('ill-narrow')?'schmal':'Kachel '+(ti+1);
        // Text in Zellen
        const L=lang+(mode?', ohne Worte':'');
        tile.querySelectorAll('g.dg-cell').forEach(c=>{const R=c.querySelector('rect').getBBox();
          c.querySelectorAll(mode?'.dg-nw text, .dg-nw use':'.dg-full text, :scope > text').forEach(t=>{if(!vis(t))return;const B=t.getBBox();
            if(B.x<R.x-tol||B.y<R.y-tol||B.x+B.width>R.x+R.width+tol||B.y+B.height>R.y+R.height+tol)
              res.push(`${id} ${nm} [${L}]: ${t.tagName==='use'?'Zeichen':'Text'} ragt über die Zelle: «${t.textContent.slice(0,50)}»${mode?` (${[B.x,B.y,B.width,B.height,R.x,R.y,R.width,R.height].map(v=>v.toFixed(1))})`:""}`);});});
        if(mode)return;
        // Leerraum: in Raster, Pfeilkette, Kette und Spalten füllt jede Zeile die Breite (Hinweis Andi Neck 2026-10-24)
        tile.querySelectorAll('g.dg-vis').forEach(g=>{if(!['grid','arrows','tree','columns'].includes(g.dataset.visual))return;
          const rs=[...g.querySelectorAll(':scope > g.dg-cell > rect, :scope g.dg-cell > rect')].map(r=>r.getBBox());if(!rs.length)return;
          const full=Math.max(...rs.map(b=>b.x+b.width))-Math.min(...rs.map(b=>b.x));const rows={};
          rs.forEach(b=>{const k=Math.round(b.y);(rows[k]=rows[k]||[]).push(b);});
          Object.values(rows).forEach(r=>{const span=Math.max(...r.map(b=>b.x+b.width))-Math.min(...r.map(b=>b.x));
            if(span<full*.8)res.push(`${id} ${nm} [${lang}]: Leerraum – Zeile mit ${r.length} Zelle(n) füllt nur ${Math.round(100*span/full)} % der Breite (${g.dataset.visual})`);});});
        // Verbindungen: Anfang und Ende sitzen an einer Zelle (höchstens 3 Einheiten Abstand, Hinweis Andi Neck 2026-10-24)
        const crs=[...tile.querySelectorAll('g.dg-cell>rect')].map(r=>r.getBBox());
        const dist=(x,y,R)=>{const dx=Math.max(R.x-x,0,x-(R.x+R.width)),dy=Math.max(R.y-y,0,y-(R.y+R.height));return Math.hypot(dx,dy);};
        tile.querySelectorAll('g.dg-link').forEach(L=>{for(const k of ['a','b']){const [x,y]=L.dataset[k].split(',').map(Number);
          const dmin=Math.min(...crs.map(R=>dist(x,y,R)));if(!(dmin<=3))res.push(`${id} ${nm} [${lang}]: Pfeil-${k==='a'?'Anfang':'Ende'} nicht an einer Zelle (Abstand ${dmin.toFixed(1)})`);
          if(crs.some(R=>x>R.x+2&&x<R.x+R.width-2&&y>R.y+2&&y<R.y+R.height-2))res.push(`${id} ${nm} [${lang}]: Pfeil-${k==='a'?'Anfang':'Ende'} liegt in einer Zelle`);}});
        // Abstand zum Rahmen: Inhalt hält mindestens 3 Einheiten Abstand zur Innenkante des Kachelrahmens
        const fr=tile.querySelector('polygon.pn-frame');
        if(fr){const F=fr.getBoundingClientRect(),sc=tile.getBoundingClientRect().width/tile.viewBox.baseVal.width,m=(1.1+2.5)*sc;
          tile.querySelectorAll('g.dg-cell>rect, g.dg-label>rect, rect[rx="7"]').forEach(r=>{const B=r.getBoundingClientRect();
            if(B.left<F.left+m||B.top<F.top+m||B.right>F.right-m||B.bottom>F.bottom-m)res.push(`${id} ${nm} [${lang}]: Inhalt zu nahe am Rahmen («${r.parentNode.textContent.slice(0,25)}»)`);});}
        // Beschriftungen
        const cells=[...tile.querySelectorAll('g.dg-cell>rect')].map(r=>r.getBBox());
        const labs=[...tile.querySelectorAll('g.dg-label')].map(g=>({g,B:g.querySelector('rect').getBBox()}));
        labs.forEach((L,i)=>{if(cells.some(C=>inter(L.B,C)))res.push(`${id} ${nm} [${lang}]: Beschriftung überdeckt eine Zelle: «${L.g.textContent.slice(0,30)}»`);
          labs.slice(i+1).forEach(M=>{if(inter(L.B,M.B))res.push(`${id} ${nm} [${lang}]: Beschriftungen überlappen: «${L.g.textContent.slice(0,20)}» / «${M.g.textContent.slice(0,20)}»`);});
          L.g.querySelectorAll('text').forEach(t=>{if(!vis(t))return;const B=t.getBBox();if(B.width>L.B.width+tol)res.push(`${id} ${nm} [${lang}]: Beschriftung breiter als ihr Schild «${t.textContent}»`);});});
      });
    }
    return res;},[lang,mode]);
  out.push(...r);
}
console.log(JSON.stringify(out));await b.close();})();
"""


def main():
    pre = sys.argv[1:]
    lib = (ANI / "_bibliothek.svg").read_text(encoding="utf-8")
    files = sorted(ANI.glob("ILL-ANI-*.svg"))
    sel = [f for f in files if not pre or any(f.stem[8:] == x or f.stem[8:].startswith(x + "-") for x in pre)]
    body = "".join(f'<div class="ill" data-id="{f.stem[8:]}">{f.read_text(encoding="utf-8")}</div>' for f in sel)
    with tempfile.TemporaryDirectory() as td:
        h = pathlib.Path(td) / "p.html"
        h.write_text(f'<html><head><meta charset="utf-8"></head><body><div style="display:none">{lib}</div>{body}</body></html>', encoding="utf-8")
        j = pathlib.Path(td) / "c.cjs"
        j.write_text(JS, encoding="utf-8")
        env = {**os.environ, "PLAYWRIGHT_MODULE": os.environ.get("PLAYWRIGHT_MODULE", "/opt/npm-tools/node_modules/playwright")}
        r = subprocess.run(["node", str(j), str(h)], capture_output=True, text=True, env=env, check=True)
    res = json.loads(r.stdout.strip().splitlines()[-1])
    for x in res:
        print("FEHLER:", x)
    if res:
        print(f"FEHLER: {len(res)} Befunde in {len(sel)} Bildern")
        sys.exit(1)
    print(f"PASS: Anordnung von {len(sel)} Bildern geprüft (Text in Zellen, auch ohne Worte; Beschriftungen; de und gsw)")


if __name__ == "__main__":
    sys.path.insert(0, str(ROOT / "scripts"))
    sys.path.insert(0, str(ROOT / "scripts/authoring"))
    main()
