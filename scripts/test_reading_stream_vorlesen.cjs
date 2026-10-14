// Prüfung des Vorlesemodus (app/reading-stream/index.html) mit einer nachgebildeten Sprachausgabe.
// Voraussetzung: python3 scripts/build_reading_stream.py; Playwright (PLAYWRIGHT_MODULE=Pfad oder require('playwright')).
// Fehlt Playwright, wird die Prüfung übersprungen (Exit 0 mit Hinweis). Geprüft wird die Abfolge, nicht die Stimme.
const path=require('node:path'),assert=require('node:assert/strict');
let chromium;try{({chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright'));}catch{console.log('SKIP: Playwright nicht verfügbar');process.exit(0);}
(async()=>{const b=await chromium.launch();
  try{const p=await b.newPage({viewport:{width:390,height:780}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
    await p.addInitScript(()=>{window.__said=[];window.SpeechSynthesisUtterance=class{constructor(t){this.text=t;}};
      Object.defineProperty(window,'speechSynthesis',{value:{cancel(){},speak(u){window.__said.push(u.text);setTimeout(()=>u.onend&&u.onend(),150);},getVoices(){return [{name:'Test',lang:'de-CH'}];},addEventListener(){}}});});
    await p.goto('file://'+path.join(__dirname,'../app/reading-stream/index.html'));await p.waitForTimeout(800);
    const said=()=>p.evaluate(()=>window.__said.filter(Boolean));const label=()=>p.textContent('.player-label');
    assert(await p.$('.player[hidden]'),'Player zu Beginn verborgen');
    await p.click('[data-action=menu]');await p.fill('input[type=search]','Joh 3,1');await p.waitForTimeout(300);await p.click('.results button');await p.waitForTimeout(800);
    assert(await p.$('.chapter-head [data-read]')&&await p.$('.part-head [data-read]'),'Startknöpfe bei Kapitel- und Abschnittstitel');
    await p.click('.part-head [data-read]');await p.waitForTimeout(1200);
    const s=await said();assert(s[0].startsWith('Johannes 3. Jesus und Nikodemus. Es war aber ein Mensch'),'beginnt mit Kapitel, Abschnittstitel und Vers 1: '+s[0]);
    assert(s.length>=3&&/Johannes 3,[2-9]/.test(await label()),'liest ohne Unterbruch weiter: '+await label());
    assert(await p.$('.stream-entry.reading'),'aktueller Vers markiert');
    await p.click('[data-ra=toggle]');const n=(await said()).length;await p.waitForTimeout(500);assert.equal((await said()).length,n,'Pause hält an');
    const before=await label();await p.click('[data-ra=next]');await p.waitForTimeout(200);assert.notEqual(await label(),before,'Weiter springt zum nächsten Vers');
    await p.click('[data-ra=prev]');await p.waitForTimeout(200);assert.equal(await label(),before,'Zurück springt zurück');
    await p.click('[data-ra=close]');assert(await p.$eval('.player',e=>e.hidden),'im Player schliessbar');assert(!await p.$('.stream-entry.reading'),'Markierung entfernt');
    await p.click('[data-action=up]');await p.waitForTimeout(600);await p.click('.stream-entry h2 [data-read]');await p.waitForTimeout(400);
    assert(!(await p.$eval('.player',e=>e.hidden)),'Start auf Abschnittsebene');
    assert.deepEqual(errs,[],'keine Skriptfehler');
    console.log('PASS: Vorlesen ab Titel, fortlaufend, Pause, vor/zurück, Markierung, Schliessen (nachgebildete Sprachausgabe).');
  }finally{await b.close();}})().catch(e=>{console.error(e);process.exit(1);});
