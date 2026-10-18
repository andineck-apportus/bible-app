// Prüfung der Seitenleiste (breite Ansicht): ab Kapitelebene Schritt zum vorherigen/nächsten Elternteil und Titel als Weg nach oben.
// Voraussetzung: python3 scripts/build_bible.py; Playwright (PLAYWRIGHT_MODULE=Pfad oder require('playwright')).
const path=require('node:path'),assert=require('node:assert/strict');
let chromium;try{({chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright'));}catch{console.log('SKIP: Playwright nicht verfügbar');process.exit(0);}
(async()=>{const b=await chromium.launch();
  try{const p=await b.newPage({viewport:{width:1100,height:760}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
    await p.goto('file://'+path.join(__dirname,'../app/bible/index.html'));await p.waitForTimeout(800);
    await p.click('[data-action=index]');await p.fill('input[type=search]','Joh 21,1');await p.waitForTimeout(300);await p.click('.results button');await p.waitForTimeout(900);
    const lvl=()=>p.evaluate(()=>+document.querySelector('.app').dataset.level),loc=()=>p.textContent('.location');
    while(await lvl()>4){await p.evaluate(()=>document.querySelector('.immersed')?.classList.remove('immersed'));await p.click('[data-action=up]');await p.waitForTimeout(800);}
    assert.equal((await p.textContent('aside [data-step=prev]')).trim(),'Lukas 24','Schritt zurück ins vorherige Buch');
    assert.equal((await p.textContent('aside [data-step=next]')).trim(),'Apostelgeschichte 1','Schritt weiter ins nächste Buch');
    await p.click('aside [data-step=next]');await p.waitForTimeout(900);assert.equal((await loc()).trim(),'Apostelgeschichte 1');
    assert.equal((await p.textContent('aside [data-step=prev]')).trim(),'Johannes 21','Seitenleiste zeigt danach das neue Buch');
    await p.click('aside .side-head');await p.waitForTimeout(900);assert.equal(await lvl(),3,'Titel führt eine Ebene hinauf');
    assert.deepEqual(errs,[],'keine Skriptfehler');
    console.log('PASS: Seitenleiste mit Schritt vor/zurück über die Buchgrenze und Titel als Weg nach oben.');
  }finally{await b.close();}})().catch(e=>{console.error(e);process.exit(1);});
