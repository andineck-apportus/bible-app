// Prüfung des Vorlesemodus (app/bible/index.html) mit einer nachgebildeten Sprachausgabe.
// Voraussetzung: python3 scripts/build_bible.py; Playwright (PLAYWRIGHT_MODULE=Pfad oder require('playwright')).
// Fehlt Playwright, wird die Prüfung übersprungen (Exit 0 mit Hinweis). Geprüft wird die Abfolge, nicht die Stimme.
const path=require('node:path'),assert=require('node:assert/strict');
let chromium;try{({chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright'));}catch{console.log('SKIP: Playwright nicht verfügbar');process.exit(0);}
(async()=>{const b=await chromium.launch();
  try{const p=await b.newPage({viewport:{width:390,height:780}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
    await p.addInitScript(()=>{window.__said=[];window.SpeechSynthesisUtterance=class{constructor(t){this.text=t;}};
      Object.defineProperty(window,'speechSynthesis',{value:{cancel(){},speak(u){window.__said.push(u.text);if(u.text)(window.__vol=window.__vol||[]).push(u.volume??1);setTimeout(()=>u.onend&&u.onend(),150);},getVoices(){return [{name:'Test',lang:'de-CH'}];},addEventListener(){}}});});
    await p.goto('file://'+path.join(__dirname,'../app/bible/index.html'));await p.waitForTimeout(800);
    const said=()=>p.evaluate(()=>window.__said.filter(Boolean));const label=()=>p.textContent('.player-label');
    assert(await p.$('.player[hidden]'),'Player zu Beginn verborgen');
    await p.click('[data-action=index]');await p.fill('input[type=search]','Joh 3,1');await p.waitForTimeout(300);await p.click('.results button');await p.waitForTimeout(800);
    assert(await p.$('.chapter-head [data-read]')&&await p.$('.part-head [data-read]'),'Startknöpfe bei Kapitel- und Abschnittstitel');
    await p.click('.part-head [data-read]');await p.waitForTimeout(2600);
    const s=await said();assert.deepEqual(s.slice(0,2),['Johannes 3','Jesus und Nikodemus'],'Kapitel- und Abschnittstitel einzeln, ohne Schlusspunkt (sonst «Johannes dritter»)');assert(s[2].startsWith('Es war aber ein Mensch'),'dann Vers 1: '+s[2]);
    assert(await p.evaluate(()=>window.__vol.slice(0,2).every(v=>v<1)&&window.__vol[2]===1),'Titel leiser gesprochen');
    assert(await p.$('[data-read][data-icon=pause]'),'Startknopf des laufenden Abschnitts zeigt Pause');
    await p.$eval('[data-read][data-icon=pause]',e=>e.click());await p.waitForTimeout(200);assert.equal(await p.$eval('.player [data-ra=toggle]',e=>e.getAttribute('aria-label')),'Weiterlesen','Klick auf den Startknopf pausiert');
    assert(!await p.$('[data-read][data-icon=pause]'),'Startknopf zeigt wieder Play');
    await p.click('.player [data-ra=toggle]');await p.waitForTimeout(400);
    assert(s.length>=3&&/Johannes 3,([2-9]|\d\d)$/.test(await label()),'liest ohne Unterbruch weiter: '+await label());
    assert(await p.$('.stream-entry.reading'),'aktueller Vers markiert');
    await p.click('[data-ra=toggle]');const n=(await said()).length;await p.waitForTimeout(500);assert.equal((await said()).length,n,'Pause hält an');
    const before=await label();await p.click('[data-ra=next]');await p.waitForTimeout(200);assert.notEqual(await label(),before,'Weiter springt zum nächsten Vers');
    await p.click('[data-ra=prev]');await p.waitForTimeout(200);assert.equal(await label(),before,'Zurück springt zurück');
    await p.click('[data-ra=close]');assert(await p.$eval('.player',e=>e.hidden),'im Player schliessbar');assert(!await p.$('.stream-entry.reading'),'Markierung entfernt');
    await p.click('[data-action=up]');await p.waitForTimeout(600);await p.click('.stream-entry h2 [data-read]');await p.waitForTimeout(400);
    assert(!(await p.$eval('.player',e=>e.hidden)),'Start auf Abschnittsebene');
    await p.click('[data-ra=close]');await p.evaluate(()=>document.querySelector('.immersed')?.classList.remove('immersed'));await p.waitForTimeout(300);await p.click('[data-action=index]');await p.fill('input[type=search]','1 Joh 2,1');await p.waitForTimeout(300);await p.click('.results button');await p.waitForTimeout(800);
    await p.evaluate(()=>{window.__said=[];});await p.click('[data-stream="v61-2-1"] .chapter-head [data-read]');await p.waitForTimeout(1500);assert.equal((await said())[0],'Erster Johannes 2','Buchnummer als Ordnungszahl');
    await p.click('[data-ra=close]');await p.evaluate(()=>document.querySelector('.immersed')?.classList.remove('immersed'));await p.waitForTimeout(300);await p.click('[data-action=index]');await p.fill('input[type=search]','Rut 1,1');await p.waitForTimeout(300);await p.click('.results button');await p.waitForTimeout(800);
    await p.evaluate(()=>{window.__said=[];});await p.click('[data-stream="v7-1-1"] .chapter-head [data-read]');await p.waitForTimeout(5000);
    {const t=(await said()).join(' ');assert(t.includes('Jahwe')&&!t.includes('JHWH'),'Gottesname JHWH wird als «Jahwe» vorgelesen');}
    assert.deepEqual(errs,[],'keine Skriptfehler');
    console.log('PASS: Vorlesen ab Titel, fortlaufend, Pause, vor/zurück, Markierung, Schliessen (nachgebildete Sprachausgabe).');
  }finally{await b.close();}})().catch(e=>{console.error(e);process.exit(1);});
