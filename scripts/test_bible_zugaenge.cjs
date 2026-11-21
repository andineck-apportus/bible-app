// Prüfung der weiteren Zugänge auf der Ebene Bibel (Entscheid Andi Neck 2026-11-21): Umschalter «Zoom · Bibliothek · Geschichte ·
// Zeit · Ort», Zoom vorgewählt, Wahl gemerkt; je Zugang ein Element antippen → Buch bzw. Stelle offen; Beschriftung ohne Überlappung
// und mit Abstand zum Rand (360 und 1280 px, hell und dunkel); Züritüütsch-Beschriftung bei Lesesprache gsw.
// Voraussetzung: python3 scripts/build_bible.py; Playwright (PLAYWRIGHT_MODULE=Pfad oder require('playwright')).
const path=require('node:path'),assert=require('node:assert/strict');
let chromium;try{({chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright'));}catch{console.log('SKIP: Playwright nicht verfügbar');process.exit(0);}
const URL='file://'+path.join(__dirname,'../app/bible/index.html');
// Überlappungen: Rechtecke der sichtbaren Beschriftungen je Zugang paarweise, und Text innerhalb seiner Karte bzw. Karte (Rand ≥ 2 px)
const LAYOUT=()=>{const r=[],vis=e=>{const b=e.getBoundingClientRect();return b.width>0&&b.height>0&&!e.closest('[hidden]');};
  const box=e=>e.getBoundingClientRect(),ov=(a,b,m=0.5)=>a.left+m<b.right&&b.left+m<a.right&&a.top+m<b.bottom&&b.top+m<a.bottom;
  const zg=document.querySelector('.zg');if(!zg)return ['kein Zugang sichtbar'];
  // Karte: Ortsnamen, Gewässer und Punkte
  for(const m of zg.querySelectorAll('.zg-map-in')){const mb=box(m);
    const L=[...m.querySelectorAll('.zg-lbl,.zg-water')].filter(vis),D=[...m.querySelectorAll('.zg-dot')];
    for(let i=0;i<L.length;i++){const a=box(L[i]);
      if(a.left<mb.left+2||a.right>mb.right-2||a.top<mb.top+2||a.bottom>mb.bottom-2)r.push('Karte: am Rand «'+L[i].textContent+'»');
      for(let j=i+1;j<L.length;j++)if(ov(a,box(L[j])))r.push('Karte: überlappt «'+L[i].textContent+'» / «'+L[j].textContent+'»');
      for(const d of D){if(d.dataset.zplace===L[i].dataset.zplace)continue;const c=box(d),k={left:c.left+5,right:c.right-5,top:c.top+5,bottom:c.bottom-5};if(ov(a,k))r.push('Karte: «'+L[i].textContent+'» über Punkt '+d.dataset.zplace);}}
    const shown=m.querySelectorAll('.zg-lbl:not([hidden])').length;if(shown<D.length*0.8)r.push(`Karte ${m.dataset.map}: nur ${shown}/${D.length} Ortsnamen`);}
  // Texte innerhalb ihrer Karte/Buchrücken; Buchrücken und Karten untereinander ohne Überlappung
  for(const s of zg.querySelectorAll('.zg-plate span')){const a=box(s),b=box(s.closest('.zg-spine'));if(a.left<b.left||a.right>b.right||a.top<b.top)r.push('Buchrücken: Kürzel zu breit '+s.textContent);}
  const cards=[...zg.querySelectorAll('.zg-card,.zg-spine,.zg-grp-h,.zg-h,.zg-when,.zg-evt')].filter(vis);
  for(let i=0;i<cards.length;i++)for(let j=i+1;j<cards.length;j++){const a=cards[i],b=cards[j];if(a.contains(b)||b.contains(a))continue;if(ov(box(a),box(b),1))r.push('überlappt: '+a.className+' / '+b.className+' «'+(a.textContent||'').trim().slice(0,30)+'»');}
  for(const t of zg.querySelectorAll('.zg-card b,.zg-card .zg-st-x,.zg-st-r,.zg-chip')){if(!vis(t))continue;const c=t.closest('.zg-card');if(!c||c===t)continue;const a=box(t),b=box(c);
    if(a.left<b.left+2||a.right>b.right-2||a.bottom>b.bottom-2)r.push('Text am Kartenrand: «'+t.textContent.trim().slice(0,30)+'»');}
  const sw=document.querySelector('.zg-switch');if(sw.scrollWidth>sw.clientWidth+1)r.push('Umschalter zu breit ('+sw.scrollWidth+'/'+sw.clientWidth+')');
  const z=box(zg);if(z.right>document.documentElement.clientWidth+1)r.push('Zugang breiter als die Seite');
  return r;};
(async()=>{const b=await chromium.launch();let n=0;
  try{
    // 1 Umschalter, Vorgabe Zoom, je Zugang antippen → Buch offen
    const p=await b.newPage({viewport:{width:390,height:844}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
    await p.goto(URL);await p.waitForTimeout(900);
    assert.equal(await p.$$eval('.zg-switch button',x=>x.length),5,'Umschalter mit fünf Zugängen');
    assert.equal(await p.getAttribute('[data-zugang=zoom]','aria-pressed'),'true','Zoom vorgewählt');
    assert(await p.$('.has-ill .ill-img'),'Zoom zeigt das Bild der Ebene Bibel wie bisher');
    const open=async(sel,code,what)=>{await p.click(sel);await p.waitForTimeout(800);
      const st=await p.evaluate(()=>({lvl:+document.querySelector('.app').dataset.level,h:location.hash}));
      assert(st.lvl>=3&&st.h.startsWith('#/'+code),`${what}: ${code} geöffnet (Ebene ${st.lvl}, ${st.h})`);
      await p.evaluate(()=>{history.replaceState(null,'','#/');});await p.click('[data-action=home]');await p.waitForTimeout(700);n++;};
    await p.click('[data-zugang=lib]');await p.waitForTimeout(300);
    assert.equal(await p.$$eval('.zg-spine',x=>x.length),66,'Bibliothek: 66 Buchrücken');
    assert.equal(await p.$$eval('.zg-grp',x=>x.length),10,'Bibliothek: 10 Buchgruppen');
    assert(/Jona, 48 Verse/.test(await p.getAttribute('.zg-spine[data-zbook=JON]','aria-label')),'Buchrücken mit Name und Versen');
    await open('.zg-spine[data-zbook=JON]','JON','Bibliothek');
    assert.equal(await p.getAttribute('[data-zugang=lib]','aria-pressed'),'true','Wahl bleibt nach dem Zurückkehren');
    assert.equal(await p.evaluate(()=>JSON.parse(localStorage.getItem('bible:settings')).zugang),'lib','Wahl gespeichert');
    await p.click('[data-zugang=story]');await p.waitForTimeout(300);
    assert.equal(await p.$$eval('.zg-st',x=>x.length),8,'Geschichte: acht Stationen');
    assert.equal(await p.$$eval('.zg-st img',x=>x.filter(i=>i.naturalWidth>0).length),8,'Geschichte: acht Bilder');
    await open('.zg-st[data-zref="EXO.14"]','EXO.14','Geschichte');
    await p.click('[data-zugang=time]');await p.waitForTimeout(300);
    const codes=await p.$$eval('.zg-time [data-zbook]',x=>new Set(x.map(e=>e.dataset.zbook)).size);assert.equal(codes,66,'Zeitleiste: alle 66 Bücher');
    assert(/um 1050–930 v\. Chr\./.test(await p.textContent('.zg-tl-dated')),'Jahre als ungefähr gekennzeichnet');
    assert(!/\d/.test(await p.$$eval('.zg-tl-seq .zg-ep b',x=>x.map(e=>e.textContent).join(''))),'Folge ohne Jahreszahlen');
    await open('.zg-time .zg-chip[data-zbook=DAN]','DAN','Zeit');
    await p.click('[data-zugang=map]');await p.waitForTimeout(500);
    assert.match(await p.textContent('.zg-panel'),/Ort antippen/,'Karte: Hinweis vor der Wahl');
    await p.click('.zg-all .zg-chip[data-zplace=ninive]');await p.waitForTimeout(300);
    assert.match(await p.textContent('.zg-panel'),/Ninive[\s\S]*Jona/,'Ort zeigt seine Bücher');
    assert(await p.$('.zg-dot.on[data-zplace=ninive]'),'Ort auf der Karte hervorgehoben');
    await p.locator('.zg-dot[data-zplace=korinth]').click({force:true});await p.waitForTimeout(300);assert.match(await p.textContent('.zg-panel'),/1\. Korinther/,'Punkt antippen');
    await open('.zg-panel [data-zbook="1CO"]','1CO','Ort');
    await p.click('[data-zugang=zoom]');await p.waitForTimeout(300);assert(await p.$('.has-ill .ill-img')&&!await p.$('.zg'),'zurück zum Zoom');
    assert.deepEqual(errs,[],'keine Skriptfehler');await p.close();
    // 2 Züritüütsch
    const g=await b.newPage({viewport:{width:390,height:844}});await g.addInitScript(()=>localStorage.setItem('bible:settings',JSON.stringify({v:3,text:'gsw',zugang:'story'})));
    await g.goto(URL);await g.waitForTimeout(900);
    assert.equal(await g.textContent('[data-zugang=time]'),'Ziit','Umschalter auf Züritüütsch');
    assert.match(await g.textContent('.zg-story'),/Schöpfig[\s\S]*Chrüüz/,'Stationen auf Züritüütsch');await g.close();n++;
    // 3 Layout: 360 und 1280 px, hell und dunkel, de und gsw
    for(const [w,h] of [[360,780],[1280,900]])for(const theme of ['light','dark'])for(const text of ['de','gsw']){
      const q=await b.newPage({viewport:{width:w,height:h}});await q.addInitScript(([th,tx])=>localStorage.setItem('bible:settings',JSON.stringify({v:3,theme:th,text:tx})),[theme,text]);
      await q.goto(URL);await q.waitForTimeout(800);
      for(const v of ['lib','story','time','map']){await q.click(`[data-zugang=${v}]`);await q.waitForTimeout(350);
        if(v==='map'){await q.click('.zg-all .zg-chip[data-zplace=jerusalem]');await q.waitForTimeout(200);}
        const r=await q.evaluate(LAYOUT);assert.deepEqual(r,[],`${v} ${w}px ${theme} ${text}: ${r.slice(0,5).join('; ')}`);n++;}
      await q.close();}
    console.log(`PASS: Zugänge der Ebene Bibel (${n} Prüfungen: Umschalter, Bibliothek, Geschichte, Zeit, Ort; Layout 360/1280 px, hell/dunkel, de/gsw)`);
  }finally{await b.close();}})().catch(e=>{console.error('FAIL:',e.message);process.exit(1);});
