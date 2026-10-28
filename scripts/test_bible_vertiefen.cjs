#!/usr/bin/env node
// Vertiefen (docs/LESEN-UND-VERTIEFEN.md, Entscheid Andi Neck 2026-10-28): ein Knopf mit Punkt, Blatt mit zwei Reitern, Pfad,
// Kapitel sammelt aus den Abschnitten, Gliederung führt Blatt zu Blatt, Buch mit Türen nach unten, Versblatt-Reihenfolge,
// Anwendungen nur mit Einstellung. Handybreite 390.
// Voraussetzung: python3 scripts/build_bible.py (aufgeteilte Fassung in build/bible); Playwright.
//   node scripts/test_bible_vertiefen.cjs
const http=require('http'),fs=require('fs'),path=require('path'),assert=require('node:assert/strict');
let chromium;try{({chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright'));}catch{console.log('SKIP: Playwright nicht verfügbar');process.exit(0);}
const ROOT=path.join(__dirname,'..','build','bible');
const srv=http.createServer((q,r)=>{const f=path.join(ROOT,decodeURIComponent(q.url.split('?')[0].split('#')[0]).replace(/^\/$/,'/index.html'));
  fs.readFile(f,(e,d)=>{if(e){r.writeHead(404);r.end();return;}r.writeHead(200,{'Content-Type':f.endsWith('.html')?'text/html; charset=utf-8':'application/octet-stream'});r.end(d);});});
(async()=>{await new Promise(ok=>srv.listen(0,ok));const url=`http://localhost:${srv.address().port}/index.html`;
  const b=await chromium.launch();
  try{const p=await b.newPage({viewport:{width:390,height:844}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
    const ev=(f,a)=>p.evaluate(f,a),wait=(ms=500)=>p.waitForTimeout(ms);
    const click=async s=>{await p.locator(s).first().click();await wait(350);};
    const txt=s=>ev(s=>[...document.querySelectorAll(s)].map(x=>x.textContent).join(' | '),s);
    await p.goto(url);await ev(()=>localStorage.clear());
    // 1 Lesetext: ein Knopf «Vertiefen» mit Punkt, nichts Zusätzliches am Abschnittsende
    await p.goto(url+'#/LUK.15.11-32');await wait(1500);
    const btn='[data-stream="TU-LUK-015-011-032"] [data-vertiefen="TU-LUK-015-011-032"]';
    assert(await p.$(btn),'Knopf «Vertiefen» am Abschnittstitel');
    assert(await p.$(btn+' .deep-dot'),'Punkt: es gibt etwas');
    assert.equal(await ev(s=>document.querySelector(s).textContent.trim(),btn),'Vertiefen','keine Zahl am Knopf');
    assert(!(await p.$('.reader [data-study],.reader [data-background]')),'keine alten Knöpfe «Verstehen» und «Damals → Heute»');
    const box=await p.locator(btn).boundingBox();assert(box.height>=44,'Touch-Ziel ≥ 44 px');
    assert(!(await p.$('.reader .deep-teaser,.reader .dq-q')),'keine Frage im Lesetext');
    // 2 Blatt: zwei Reiter, Verstehen zuerst; Kernaussage, Was auffällt, Zeilen
    await click(btn);
    assert.equal(await ev(()=>document.querySelectorAll('.sheet [role=tablist] [role=tab]').length),2,'zwei Reiter');
    assert.equal(await ev(()=>document.querySelector('#deep-tab-u').getAttribute('aria-selected')),'true','Verstehen ausgewählt');
    assert.equal(await ev(()=>document.activeElement&&document.activeElement.classList.contains('deep-title')),true,'Fokus im Blatt beim Öffnen');
    assert.equal(await txt('.sheet .deep-gist'),'Der Vater läuft dem jüngeren Sohn entgegen – und geht auch zum älteren hinaus.','Kernaussage in einem Satz');
    const pts=await ev(()=>document.querySelectorAll('.sheet .deep-points li').length);assert(pts>=1&&pts<=3,'Was auffällt: bis drei Punkte');
    const rows=await ev(()=>[...document.querySelectorAll('#deep-panel-u .deep-row .dr-t')].map(x=>x.textContent));
    assert.deepEqual(rows,['Umfeld damals','Wie man es verstehen kann','Ähnliche Stellen'],'Zeilen unter Verstehen');
    assert((await txt('#deep-panel-u .deep-row .dr-a')).includes('Erbteil'),'Anriss Umfeld damals');
    assert(!(await ev(()=>/\b\d+\b/.test([...document.querySelectorAll('.sheet [role=tab]')].map(x=>x.textContent).join('')))),'keine Zahlen an Reitern');
    assert.equal(await txt('.sheet .deep-path [aria-current]'),'15,11–32','Pfad');
    // Reiter wechseln (Tastatur: Pfeil rechts)
    await p.focus('#deep-tab-u');await p.keyboard.press('ArrowRight');await wait(200);
    assert.equal(await ev(()=>document.querySelector('#deep-tab-w').getAttribute('aria-selected')),'true','Pfeiltaste wechselt den Reiter');
    assert(await ev(()=>document.querySelector('#deep-panel-u').hidden),'Verstehen ausgeblendet');
    assert.equal(await txt('#deep-panel-w .dq:not([hidden]) .dq-q'),'Geht der ältere Sohn hinein?','grosse Frage');
    await click('#deep-panel-w [data-next-q]');
    assert.equal(await txt('#deep-panel-w .dq:not([hidden]) .dq-q'),'Warum lässt der Vater den Sohn seine Rede nicht zu Ende sagen?','Nächste Frage');
    const wrows=await ev(()=>[...document.querySelectorAll('#deep-panel-w .deep-row .dr-t')].map(x=>x.textContent));
    assert.deepEqual(wrows,['Was das Gleichnis zeigt','Wie man es gelesen hat','Weitere Fragen'],'Brücke nach Textart (Gleichnis), Rezeption, weitere Fragen');
    assert((await txt('#deep-panel-w .deep-row')).includes('Rembrandt'),'Wie man es gelesen hat');
    assert(!(await p.$('.sheet [data-app]'))&&(await txt('.sheet .deep-apps-off')).includes('ausgeblendet'),'Anwendungen standardmässig ausgeblendet');
    await click('#deep-tab-u');assert.equal(await ev(()=>document.querySelector('#deep-tab-u').getAttribute('aria-selected')),'true','zurück zu Verstehen');
    // Grundsatz bei allen Abschnitten, aus denen er abgeleitet ist (PRIN-LUK-0505)
    for(const id of ['TU-LUK-015-001-007','TU-LUK-015-011-032']){  // derived_from: Befund zu 15,1–7, Befund und Deutung zu 15,11–32
      await ev(id=>{const b=document.createElement('button');b.dataset.vertiefen=id;b.dataset.tab='w';document.querySelector('.app').appendChild(b);b.click();b.remove();},id);await wait();
      assert((await txt('#deep-panel-w')).includes('Gott sucht die Verlorenen'),'Grundsatz bei '+id);}
    // 3 Pfad: eine Ebene höher zum Kapitel; Kapitel sammelt aus den Abschnitten
    await click('.sheet .deep-path button[data-vertiefen^="c"]');
    assert.equal(await txt('.sheet .deep-title'),'Lukas 15','Kapitelblatt über den Pfad');
    assert.equal(await ev(()=>document.querySelector('#deep-tab-u').getAttribute('aria-selected')),'false','Reiter bleibt beim Wechsel über den Pfad');
    await click('#deep-tab-u');
    const outline=await ev(()=>[...document.querySelectorAll('#deep-panel-u .deep-outline [data-vertiefen]')].map(x=>x.dataset.vertiefen));
    assert.deepEqual(outline,['TU-LUK-015-001-007','TU-LUK-015-008-010','TU-LUK-015-011-032'],'Gliederung mit allen Abschnitten');
    const cu=await txt('#deep-panel-u');
    assert(cu.includes('Hauptfigur des Gleichnisses ist der Vater')&&cu.includes('Die Drachme')&&cu.includes('Erbteil'),'Kapitel zeigt Deutungen und Hintergrund der Abschnitte');
    assert((await txt('#deep-panel-u .deep-row .tag')).includes('Lukas 15,11–32'),'mit Stelle');
    const cw=await txt('#deep-panel-w');
    assert(cw.includes('Dreimal verloren und gefunden')&&cw.includes('Rembrandt')&&cw.includes('Gregor'),'Kapitel: eigene Frage, Rezeption gesammelt');
    assert.equal(await ev(()=>document.querySelectorAll('#deep-panel-w .deep-outline [data-vertiefen][data-tab=w]').length),3,'In den Abschnitten weiterdenken: je Abschnitt eine Tür');
    // Gliederung öffnet direkt das Blatt des Abschnitts (Blatt zu Blatt), Pfad führt zurück
    await click('#deep-panel-u .deep-outline [data-vertiefen="TU-LUK-015-008-010"]');
    assert.equal(await txt('.sheet .deep-title'),'Die verlorene Drachme','Blatt zu Blatt');
    await click('.sheet .deep-path button');assert.equal(await txt('.sheet .deep-title'),'Lukas 15','Pfad zurück zum Kapitel');
    // 4 Buch: Kernanalyse im neuen Aufbau; Türen nach unten
    await click('.sheet .deep-path button');assert.equal(await txt('.sheet .deep-title'),'Lukas','Buchblatt');
    const bu=await ev(()=>[...document.querySelectorAll('#deep-panel-u .deep-row .dr-t')].map(x=>x.textContent));
    assert(bu[0]==='Wozu geschrieben'&&bu.includes('Worum es geht'),'Buch: Wozu geschrieben, Worum es geht');
    await click('#deep-tab-w');
    assert((await txt('#deep-panel-w .deep-label')).includes('In den Kapiteln weiterdenken')&&await p.$('#deep-panel-w [data-vertiefen="c41-15"][data-tab=w]'),'Buch: Wegweiser in die Kapitel');
    await click('#deep-panel-w [data-vertiefen="c41-15"]');assert.equal(await ev(()=>document.querySelector('#deep-tab-w').getAttribute('aria-selected')),'true','Tür öffnet Weiterdenken des Kapitels');
    await click('.sheet .close');
    // Bibel: nie nur «noch nicht erarbeitet», sondern Wege nach unten
    await ev(()=>{const b=document.createElement('button');b.dataset.vertiefen='all';document.querySelector('.app').appendChild(b);b.click();b.remove();});await wait();
    assert(await p.$('#deep-panel-u .deep-outline [data-vertiefen="nt"]'),'Bibel: Weg nach unten');
    await click('#deep-tab-w');assert(await p.$('#deep-panel-w .deep-outline [data-vertiefen="nt"][data-tab=w]'),'Bibel: Tür ins Neue Testament');
    await click('.sheet .close');
    // 5 Versblatt: Vers, Kästen, «Mehr zu diesem Vers» in fester Reihenfolge, «Abschnitt vertiefen»
    await p.goto(url+'#/LUK.15.21');await wait(1500);await ev(()=>document.querySelector('[data-more="v41-15-21"]').click());await wait();
    const order=await ev(()=>{const s=document.querySelector('.sheet');const pos=x=>x?[...s.querySelectorAll('*')].indexOf(x):-1;
      return {text:pos(s.querySelector('.vs-text')),box:pos(s.querySelector('.vbox[data-alternative]')),more:pos(s.querySelector('.vmore')),
        rows:[...s.querySelectorAll('.vmore .deep-row .dr-t')].map(x=>x.textContent)};});
    assert(order.text<order.box&&order.box<order.more,'Vers, dann Kasten, dann Mehr zu diesem Vers');
    assert.deepEqual(order.rows,['Textausgaben im Vergleich','Querverweise','Griechisch Wort für Wort','Bis zu den Handschriften','Stand dieser Stelle'],'Reihenfolge der Zeilen');
    assert((await txt('.sheet .vbox')).includes('Anders überliefert')&&(await txt('.sheet .vbox')).includes('Tagelöhner'),'Kasten «Anders überliefert»');
    assert((await txt('.sheet .vbox .vbox-s')).includes('Textausgaben'),'Belegung als Satz');
    await click('.sheet .vs-up [data-vertiefen]');assert.equal(await txt('.sheet .deep-title'),'Der Vater und seine zwei Söhne','Abschnitt vertiefen aus dem Versblatt');
    await click('.sheet .close');
    // 6 Anwendungen nur mit Einstellung
    await click('[data-action=menu]');await click('[data-settings]');assert.equal(await ev(()=>document.querySelector('[data-toggle=apps]').getAttribute('aria-checked')),'false','Standard aus');
    await click('[data-toggle=apps]');await click('.sheet .close');
    await ev(()=>{const b=document.createElement('button');b.dataset.vertiefen='TU-LUK-015-011-032';b.dataset.tab='w';document.querySelector('.app').appendChild(b);b.click();b.remove();});await wait();
    assert(await p.$('#deep-panel-w [data-app="APP-LUK-0505"]'),'Anwendung mit Einstellung sichtbar');
    assert((await txt('#deep-panel-w .deep-row')).includes('Grenze:'),'mit Grenze');
    assert(!(await p.$('.sheet .deep-apps-off')),'Hinweis «ausgeblendet» verschwindet');
    assert.deepEqual(errs.filter(e=>!/attribute d: Expected number/.test(e)),[],'keine Skriptfehler');
    console.log('PASS: Vertiefen – ein Knopf mit Punkt, zwei Reiter (Tastatur), Pfad, Kapitel sammelt aus den Abschnitten, Gliederung Blatt zu Blatt, Buch und Bibel mit Türen nach unten, Versblatt-Reihenfolge, Anwendungen nur mit Einstellung.');
  }finally{await b.close();srv.close();}})();
