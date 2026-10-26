#!/usr/bin/env python3
"""Anordnung der Bilder im Browser prüfen (BILDPROZESS.md, Leitlinie 9; Hinweis Andi Neck 2026-10-24):
- Text in einer Zelle eines Strukturbilds ragt nicht über die Zelle hinaus;
- Text und Zeichen in Kästen (Stichwortband, Titelblase, Köpfe, Namensschild) bleiben im Rahmen und überdecken sich nicht;
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
  await p.addStyleTag({content:`.lw{display:none}.lw-${lang}{display:inline}`+(mode?'.dg-full{display:none}.dg-nw{display:inline}g.dg-label,g.ill-name{display:none}':'')});
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
        // Sprechblasen überdecken keine Figur, kein Gotteszeichen und keinen Gegenstand der Szene (Hinweis Andi Neck 2026-10-26:
        // Blase lag über dem Strahlenkranz). Blase = weisse Form mit Strich 1.6; verglichen mit Zeichen und Figuren ausserhalb der Blase.
        if(!mode){const bubs=[...tile.querySelectorAll('[data-box]')].map(b=>{const [x,y,w,h]=b.dataset.box.split(',').map(Number);return {b,g:b.parentNode,B:{left:x,top:y,right:x+w,bottom:y+h,width:w,height:h}};});
          const ov=(a,b)=>Math.max(0,Math.min(a.right,b.right)-Math.max(a.left,b.left))*Math.max(0,Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top));
          const local=e=>{if(e.closest('g[transform]')!==bubs[0]?.b.closest('g[transform]'))return null;const x=+e.getAttribute('x'),y=+e.getAttribute('y'),w=+e.getAttribute('width'),h=+e.getAttribute('height');return w>0?{left:x,top:y,right:x+w,bottom:y+h,width:w,height:h}:null;};
          const others=[...tile.querySelectorAll('use')].filter(e=>!e.closest('.ill-words,.dg-nw,.dg-vis,g.ill-name')&&!bubs.some(x=>x.g.contains(e)));
          for(const {B} of bubs)for(const e of others){const E=local(e);if(!E||E.width*E.height>B.width*B.height)continue;  // grosse Hintergründe dürfen dahinter liegen
            const o=ov(B,E);if(o>0.18*E.width*E.height)res.push(`${id} ${nm} [${lang}]: Sprechblase überdeckt ${e.getAttribute('href')} (${Math.round(100*o/(E.width*E.height))} %)`);}
          for(let i=0;i<bubs.length;i++)for(let j=i+1;j<bubs.length;j++)if(ov(bubs[i].B,bubs[j].B)>4)res.push(`${id} ${nm} [${lang}]: Sprechblasen überlappen`);
          // Spitze einer Blase verläuft nicht hinter einer anderen Blase (Hinweis Prüfung 2026-10-26)
          const seg=(x1,y1,x2,y2,R)=>{for(let k=1;k<20;k++){const t=k/20,x=x1+(x2-x1)*t,y=y1+(y2-y1)*t;if(x>R.left+2&&x<R.right-2&&y>R.top+2&&y<R.bottom-2)return true;}return false;};
          for(const a of bubs){const tl=a.b.dataset.tail;if(!tl)continue;const [tx,ty]=tl.split(',').map(Number);const cx=Math.max(a.B.left,Math.min(a.B.right,tx)),cy=Math.max(a.B.top,Math.min(a.B.bottom,ty));
            for(const c of bubs)if(c!==a&&seg(cx,cy,tx,ty,c.B))res.push(`${id} ${nm} [${lang}]: Spitze einer Sprechblase läuft hinter einer anderen Blase`);}
          // Spitze kurz und steil (Hinweis Andi Neck 2026-10-26: lange, schräge Spitzen quer durchs Bild). Ansatz wie in
          // _bubble.bubble_path (Eckradius 12, halbe Breite 5); Masse in Feldeinheiten (Feld 186 × 140, in der App etwa 1,8 px
          // je Einheit): länger als 36 Einheiten oder, ab 25 Einheiten, flacher als 35° zur Waagrechten ist ein Befund.
          const TMAX=36,TFLAT=25,AMIN=35;
          const tailm=(B,tx,ty)=>{const x=B.left,y=B.top,w=B.width,h=B.height,R=12,H=5;const dx=tx-Math.min(Math.max(tx,x),x+w),dy=ty-Math.min(Math.max(ty,y),y+h);
            const side=Math.abs(dy)>=Math.abs(dx)?(dy>0?'b':'t'):(dx>0?'r':'l');const bx=Math.min(Math.max(tx,x+R+H),x+w-R-H),by=Math.min(Math.max(ty,y+R+H),y+h-R-H);
            const [px,py]={b:[bx,y+h],t:[bx,y],l:[x,by],r:[x+w,by]}[side];const L=Math.hypot(tx-px,ty-py);return {px,py,L,ang:Math.atan2(Math.abs(ty-py),Math.abs(tx-px))*180/Math.PI};};
          for(const a of bubs){const tl=a.b.dataset.tail;if(!tl||a.b.dataset.link)continue;const [tx,ty]=tl.split(',').map(Number);const m=tailm(a.B,tx,ty);
            if(m.L>TMAX)res.push(`${id} ${nm} [${lang}]: Spitze einer Sprechblase zu lang (${m.L.toFixed(0)} Einheiten, höchstens ${TMAX})`);
            else if(m.L>TFLAT&&m.ang<AMIN)res.push(`${id} ${nm} [${lang}]: Spitze einer Sprechblase zu flach (${m.ang.toFixed(0)}° bei ${m.L.toFixed(0)} Einheiten)`);}
          // Wichtige Teile ohne eigenes Zeichen (Kreuzestafel, Gegenstände über Köpfen: class ill-wichtig) verdeckt weder eine Blase
          // noch ihre Spitze (Hinweis Andi Neck 2026-10-26: Blase und Spitze lagen auf der INRI-Tafel); Spitzen laufen auch nicht
          // über Zeichen und Gegenstände (ausser dem, an dem sie enden)
          const wich=[...tile.querySelectorAll('.ill-wichtig')].map(e=>{const E=local(e);return E&&{e,E};}).filter(Boolean);
          for(const {B} of bubs)for(const {e,E} of wich)if(ov(B,E)>1)res.push(`${id} ${nm} [${lang}]: Sprechblase überdeckt ${e.dataset.name||'ein wichtiges Bildteil'}`);
          const segR=(x1,y1,x2,y2,R,m)=>{for(let k=1;k<40;k++){const t=k/40,x=x1+(x2-x1)*t,y=y1+(y2-y1)*t;if(x>R.left+m&&x<R.right-m&&y>R.top+m&&y<R.bottom-m)return true;}return false;};
          for(const a of bubs){const tl=a.b.dataset.tail;if(!tl||a.b.dataset.think)continue;const [tx,ty]=tl.split(',').map(Number);const m=tailm(a.B,tx,ty);
            for(const {e,E} of wich)if(segR(m.px,m.py,tx,ty,E,.5))res.push(`${id} ${nm} [${lang}]: Spitze einer Sprechblase läuft über ${e.dataset.name||'ein wichtiges Bildteil'}`);
            for(const e of others){const E=local(e);if(!E||E.width*E.height>a.B.width*a.B.height)continue;
              if(tx>E.left-3&&tx<E.right+3&&ty>E.top-3&&ty<E.bottom+3)continue;  // Spitze endet an diesem Teil (z. B. Kopfbedeckung des Sprechers)
              if(segR(m.px,m.py,tx,ty,E,Math.min(E.width,E.height)*.18))res.push(`${id} ${nm} [${lang}]: Spitze einer Sprechblase läuft über ${e.getAttribute('href')}`);}}
          // Jede Sprech-Angabe des Bildauftrags ist als Blase gezeichnet (Hinweis Andi Neck 2026-10-26: zweite Blase derselben Figur
          // fehlte). Der Zeichner setzt je Feld <g class="ill-sp" data-n="Anzahl"> und an jede Blase data-speech="Index".
          const want=[...tile.querySelectorAll('g.ill-sp')].reduce((s,g)=>s+Number(g.dataset.n||0),0);
          if(tile.querySelector('g.ill-sp')){const got=new Set([...tile.querySelectorAll('[data-speech]')].map(e=>e.dataset.speech));
            if(got.size!==want)res.push(`${id} ${nm} [${lang}]: ${got.size} von ${want} Sprech-Angaben als Blase gezeichnet`);}}
        // Kästen mit Rahmen (Stichwortband, Titelblase, Spaltenköpfe, Namensschild): Text und Zeichen bleiben im Rahmen und
        // überdecken sich nicht (Hinweis Andi Neck 2026-10-25: Text ragte über das Stichwortband)
        const sv=e=>{const B=e.getBoundingClientRect();return B.width>0&&B.height>0?B:null;};
        const tp=1.5;
        tile.querySelectorAll('g.ill-words, g.dg-sw > g.dg-full, g.dg-sw > g.dg-nw, g.ill-name').forEach(c=>{
          if(c.closest('g.dg-cell'))return;
          const fr=[...c.querySelectorAll(':scope > rect'),...c.parentNode.querySelectorAll(':scope > rect')].map(sv).find(Boolean);if(!fr)return;
          const ts=[...c.querySelectorAll('text')].map(t=>[t,sv(t)]).filter(x=>x[1]);
          const us=[...c.querySelectorAll('use')].map(u=>[u,sv(u)]).filter(x=>x[1]);
          for(const [e,B] of [...ts,...us])if(B.left<fr.left-tp||B.top<fr.top-tp||B.right>fr.right+tp||B.bottom>fr.bottom+tp)
            res.push(`${id} ${nm} [${L}]: ${e.tagName==='use'?'Zeichen':'Text'} ragt über den Kasten «${(e.textContent||e.getAttribute('href')).slice(0,40)}»`);
          for(const [t,B] of ts)for(const [u,U] of us)if(B.left<U.right-tp&&B.right>U.left+tp&&B.top<U.bottom-tp&&B.bottom>U.top+tp)
            res.push(`${id} ${nm} [${L}]: Text überdeckt ein Zeichen «${t.textContent.slice(0,40)}» / ${u.getAttribute('href')}`);});
        if(mode){  // «ohne Worte» gibt es auf allen Bildern (Hinweis Andi Neck 2026-10-25)
          // ohne Worte: kein Feld bleibt leer – jede umschaltbare Gruppe hat Zeichen oder Anfangsbuchstaben, und kein Wort
          // steht ohne Ersatz (es würde verdeckt und hinterliesse eine leere Fläche)
          tile.querySelectorAll('g.dg-sw > g.dg-nw').forEach(g=>{if(!g.querySelector('use,text'))res.push(`${id} ${nm} [${L}]: leeres Feld ohne Worte («${g.parentNode.querySelector('.dg-full').textContent.slice(0,30)}»)`);});
          tile.querySelectorAll('.dg-nw text').forEach(t=>{if(t.getBoundingClientRect().width)res.push(`${id} ${nm} [${L}]: Text in der Fassung ohne Worte «${t.textContent.slice(0,30)}» (nur Zeichen erlaubt)`);});
          tile.querySelectorAll('text').forEach(t=>{if(t.classList.contains("pn-n")||t.closest(".dg-nw,.dg-keep")||!t.getBoundingClientRect().width)return;
            res.push(`${id} ${nm} [${L}]: Wort ohne Ersatz «${t.textContent.slice(0,30)}» <${(t.parentNode.getAttribute("class")||t.parentNode.tagName)}|${t.closest("g.dg-vis")?.dataset.visual||"-"}|${t.getAttribute("font-size")}>`);});
          return;}
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
