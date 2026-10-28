#!/usr/bin/env node
// Navigation per Tastatur, Zuletzt gelesen, Adressen (Hash-Router) und Laden mit Abbrechen (Hinweise Andi Neck 2026-10-28).
// Voraussetzung: python3 scripts/build_bible.py (aufgeteilte Fassung in build/bible); Playwright.
//   node scripts/test_bible_navigation.cjs
const http=require('http'),fs=require('fs'),path=require('path'),assert=require('node:assert/strict');
let chromium;try{({chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright'));}catch{console.log('SKIP: Playwright nicht verfügbar');process.exit(0);}
const ROOT=path.join(__dirname,'..','build','bible');
const srv=http.createServer((q,r)=>{const f=path.join(ROOT,decodeURIComponent(q.url.split('?')[0].split('#')[0]).replace(/^\/$/,'/index.html'));
  fs.readFile(f,(e,d)=>{if(e){r.writeHead(404);r.end();return;}r.writeHead(200,{'Content-Type':f.endsWith('.html')?'text/html; charset=utf-8':f.endsWith('.json')?'application/json':'application/octet-stream'});r.end(d);});});
(async()=>{await new Promise(ok=>srv.listen(0,ok));const url=`http://localhost:${srv.address().port}/index.html`;
  const b=await chromium.launch();
  try{const p=await b.newPage({viewport:{width:1300,height:900}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
    const S=()=>p.evaluate(()=>({level:document.querySelector('.app').dataset.level,loc:document.querySelector('.loc-text')?.textContent,hash:location.hash}));
    const focus=()=>p.evaluate(()=>{const a=document.activeElement;return {cls:a.className,go:a.dataset.go||'',nav:a.dataset.nav||''};});
    const search=async q=>{await p.evaluate(()=>document.querySelector('.immersed')?.classList.remove('immersed'));await p.click('[data-action=index]');await p.fill('input[type=search]',q);await p.waitForTimeout(250);};
    await p.goto(url);await p.evaluate(()=>localStorage.clear());await p.reload();await p.waitForTimeout(600);
    // 1 Suchtreffer Kapitel: Fokus auf «Johannes 1 öffnen», Enter öffnet
    await search('joh 1');await p.click('.results button[data-pick^="c"]');await p.waitForTimeout(200);
    let f=await focus();assert.equal(f.go,'c42-1','Fokus auf «Johannes 1 öffnen»');assert.match(f.cls,/nav-open/);assert(await p.$('.sheet'),'Auswahl öffnet noch nicht');
    await p.keyboard.press('Enter');await p.waitForTimeout(900);let s=await S();
    assert.equal(s.level,'4');assert.equal(s.loc,'Johannes 1');assert.equal(s.hash,'#/JHN.1','Adresse des Kapitels');
    assert.equal(JSON.parse(await p.evaluate(()=>localStorage.getItem('bible:recent')))[0].id,'c42-1','Kapitel unter Zuletzt gelesen');
    // 2 Suchtreffer Buch: Fokus auf «Johannes öffnen»
    await search('johannes');await p.click('.results button[data-pick^="b"]');await p.waitForTimeout(200);
    f=await focus();assert.match(f.go,/^b\d+$/,'Fokus auf «Buch öffnen»');await p.keyboard.press('Enter');await p.waitForTimeout(700);s=await S();
    assert.equal(s.level,'3');assert.match(s.hash,/^#\/[1-3]?[A-Z]+$/,'Adresse des Buchs');
    assert.equal(JSON.parse(await p.evaluate(()=>localStorage.getItem('bible:recent')))[0].id.startsWith('b'),true,'Buch unter Zuletzt gelesen');
    // 3 Abschnitt: Fokus auf dem Abschnitt, Enter öffnet
    await search('joh 2,1-12');await p.click('.results button[data-pick^="TU-"]');await p.waitForTimeout(200);
    f=await focus();assert.equal(f.go,'TU-JHN-002-001-012','Fokus auf «… öffnen» des Abschnitts');await p.keyboard.press('Enter');await p.waitForTimeout(700);s=await S();
    assert.equal(s.level,'5');assert.equal(s.hash,'#/JHN.2.1-12','Adresse des Abschnitts');
    // 4 Auswahl im Navigator per Knopf: Kapitel wählen → Fokus auf «… öffnen»
    await p.evaluate(()=>document.querySelector('.immersed')?.classList.remove('immersed'));await p.click('[data-action=index]');await p.waitForTimeout(200);
    await p.click('.sheet .grid.nums [data-nav="c:3"]');await p.waitForTimeout(200);f=await focus();assert.equal(f.go,'c42-3','nach Kapitelwahl Fokus auf «Johannes 3 öffnen»');
    await p.click('.sheet .grid.nums [data-nav="v:7"]');await p.waitForTimeout(150);f=await focus();assert.equal(f.go,'v42-3-7','Vers gewählt: Fokus auf «Johannes 3,7 öffnen»');assert(await p.$('.sheet'),'Vers wird erst ausgewählt');
    await p.keyboard.press('Escape');await p.waitForTimeout(200);
    // 4b Pfad unten: Glied antippen zeigt die Auswahl, springt nicht; erst «… öffnen» springt und schliesst
    await p.evaluate(()=>document.querySelector('.immersed')?.classList.remove('immersed'));const before=(await S()).loc;
    await p.click('.dock .path [data-pickat^="b"]');await p.waitForTimeout(200);assert.equal((await S()).loc,before,'Glied angetippt: noch am selben Ort');
    assert(await p.$('.sheet .pick-list, .sheet .grid.nums'),'Ebene darunter angezeigt');await p.click('.sheet .grid.nums [data-pickat]');await p.waitForTimeout(150);
    assert(await p.$('.sheet .pick-sel .crumbs [aria-current=true]'),'Auswahl als Pfad');assert.equal((await S()).loc,before,'nach der Auswahl noch nicht gesprungen');
    await p.keyboard.press('Enter');await p.waitForTimeout(700);assert(!await p.$('.sheet'),'nach «öffnen» geschlossen');assert.equal((await S()).loc,'Johannes 1','zum gewählten Kapitel gesprungen');
    // 5 Adresse öffnen und Zurück im Browser
    await p.goto(url+'#/JHN.2.5');await p.waitForTimeout(1200);s=await S();assert.equal(s.level,'6','Vers über die Adresse');assert.equal(s.loc,'Johannes 2,5');
    await p.goto(url+'#/MAT.5');await p.waitForTimeout(1200);s=await S();assert.equal(s.loc,'Matthäus 5');
    await search('mk 1');await p.click('.results button[data-pick^="c"]');await p.waitForTimeout(200);await p.keyboard.press('Enter');await p.waitForTimeout(900);
    assert.equal((await S()).hash,'#/MRK.1');await p.goBack();await p.waitForTimeout(1000);s=await S();assert.equal(s.hash,'#/MAT.5','Zurück im Browser');assert.equal(s.loc,'Matthäus 5');
    // 6 Laden verzögert: Spinner, gesperrt, Abbrechen kehrt zurück; danach normal laden
    let hold=true;await p.route('**/b/LUK.json.gz*',async r=>{while(hold)await new Promise(ok=>setTimeout(ok,100));await r.continue();});
    await search('lk 3');await p.click('.results button[data-pick^="c"]');await p.waitForTimeout(200);await p.keyboard.press('Enter');await p.waitForTimeout(600);
    assert(await p.$('.loading .spinner'),'Spinner beim Nachladen');assert(await p.evaluate(()=>document.querySelector('.reader').inert),'Bedienung gesperrt');
    assert.equal((await focus()).cls,'link soft','Fokus auf «Abbrechen»');
    await p.click('.loading [data-action=load-cancel]');await p.waitForTimeout(300);s=await S();
    assert(!await p.$('.loading'),'Spinner weg');assert.equal(s.loc,'Matthäus 5','zurück am vorherigen Ort');assert.equal(s.hash,'#/MAT.5');assert(!await p.evaluate(()=>document.querySelector('.reader').inert),'Bedienung frei');
    hold=false;await search('lk 3');await p.click('.results button[data-pick^="c"]');await p.waitForTimeout(200);await p.keyboard.press('Enter');await p.waitForTimeout(1500);
    s=await S();assert.equal(s.loc,'Lukas 3','nach dem Abbrechen normal geladen');assert(!await p.$('.loading'));
    assert.deepEqual(errs,[],'keine Skriptfehler');
    console.log('PASS: Auswahl zuerst, Fokus auf «… öffnen» (Suche, Navigator, Pfad unten), Zuletzt gelesen beim Öffnen, Adressen (#/JHN.2.5) mit Zurück im Browser, Laden mit Spinner, Sperre und Abbrechen.');
  }finally{await b.close();srv.close();}})().catch(e=>{console.error(e);srv.close();process.exit(1);});
