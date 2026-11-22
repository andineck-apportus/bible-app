// Merkbilder (Entscheid Andi Neck 2026-11-22): Kapitelleiste auf Buchebene, Übung «Kapitel und Bild», und Strukturbilder in der
// App vollständig (Kacheln mit verschachtelten <svg> nicht abgeschnitten, Fehler vom 2026-11-22).
// Voraussetzung: python3 scripts/build_bible.py; Playwright (PLAYWRIGHT_MODULE=Pfad oder require('playwright')).
const path=require('node:path'),assert=require('node:assert/strict');
let chromium;try{({chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright'));}catch{console.log('SKIP: Playwright nicht verfügbar');process.exit(0);}
async function buch(p,ref){await p.click('[data-action=index]');await p.fill('input[type=search]',ref);await p.waitForTimeout(400);await p.click('.results button');await p.click('.sheet .nav-open');await p.waitForTimeout(900);
  for(let i=0;i<8;i++){const lv=+await p.evaluate(()=>document.querySelector('.app').dataset.level);if(lv<=3)break;await p.evaluate(()=>document.querySelector('.immersed')?.classList.remove('immersed'));await p.click('[data-action=up]');await p.click('.sheet .pick-open').catch(()=>{});await p.waitForTimeout(800);}}
(async()=>{const b=await chromium.launch();
  try{const p=await b.newPage({viewport:{width:390,height:844}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
    await p.goto('file://'+path.join(__dirname,'../app/bible/index.html'));await p.waitForTimeout(800);
    // Strukturbild auf Buchebene vollständig: Psalmen «Zwei Wege» hat zehn Felder mit Text
    await buch(p,'Ps 1');
    const n=await p.evaluate(()=>{const s=document.querySelector('.has-ill .ill-img svg.ill-tile');return s?s.querySelectorAll('text').length:0;});
    assert(n>=20,'Strukturbild vollständig (Texte in der ersten Kachel: '+n+')');
    // Kapitelleiste Jona
    await p.evaluate(()=>document.querySelector('.sheet [data-close]')?.click());await buch(p,'Jona 1');
    const k=await p.$$eval('.kap-leiste .kap-item',x=>x.map(e=>({img:e.querySelector('img')?.getAttribute('src')||'',nr:e.querySelector('.kap-nr')?.textContent,band:e.querySelector('.kap-band')?.textContent,go:e.dataset.go})));
    assert(k.length>=2,'Kapitelleiste mit Merkbildern ('+k.length+')');
    assert(k.every(x=>x.img.startsWith('data:image/webp')&&x.nr&&x.band&&/^c\d+-\d+$/.test(x.go)),'je Kapitel Bild, Nummer, Stichwort und Ziel');
    // Übung «Kapitel und Bild»
    await p.click('.kap-ueben');await p.waitForTimeout(400);
    assert(await p.$('.sheet .kap-strip img'),'Übung zeigt die Felder des Kapitels');
    await p.click('.sheet [data-learn^="kapans:"]');await p.waitForTimeout(300);
    assert(await p.$('.sheet .learn-opts .ok'),'nach der Antwort ist die richtige Wahl markiert');
    const ls=await p.evaluate(()=>Object.keys(JSON.parse(localStorage.getItem('bible:learn')||'{}')).filter(k=>k.startsWith('kap:')).length);
    assert(ls>=1,'Lernstand je Kapitel gespeichert');
    await p.click('.sheet [data-learn="next"]');await p.waitForTimeout(300);
    assert(await p.$('.sheet .kap-opt')||await p.$('.sheet .kap-strip'),'zweite Frage (Bild zum Kapitel oder Kapitel zum Bild)');
    // Kapitel öffnen aus der Leiste
    await p.click('.sheet [data-close]');await p.waitForTimeout(300);await p.click('.kap-leiste .kap-item');await p.waitForTimeout(900);
    assert.equal(await p.evaluate(()=>document.querySelector('.app').dataset.level),'4','Antippen öffnet das Kapitel');
    assert.deepEqual(errs,[],'keine Skriptfehler');
    console.log('PASS: Merkbilder – Kapitelleiste ('+k.length+' Kapitel), Übung «Kapitel und Bild», Strukturbild vollständig ('+n+' Texte)');
  }finally{await b.close();}})().catch(e=>{console.error(e);process.exit(1);});
