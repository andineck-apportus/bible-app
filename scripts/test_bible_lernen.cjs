// Prüfung von Merkversen und Lernmodus: Merkvers als Zeichen am Vers (Karte auf Antippen), umschaltbar auf Karte oder aus;
// Menü «Lernen» mit Karteikarten (Leitner), Anfangsbuchstaben, Lückentext, Wörter ordnen, Stellen zuordnen.
// Voraussetzung: python3 scripts/build_bible.py; Playwright (PLAYWRIGHT_MODULE=Pfad oder require('playwright')).
const path=require('node:path'),assert=require('node:assert/strict');
let chromium;try{({chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright'));}catch{console.log('SKIP: Playwright nicht verfügbar');process.exit(0);}
(async()=>{const b=await chromium.launch();
  try{const p=await b.newPage({viewport:{width:390,height:844}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
    await p.goto('file://'+path.join(__dirname,'../app/bible/index.html'));await p.waitForTimeout(800);
    await p.click('[data-action=menu]');await p.fill('input[type=search]','Mt 5,3');await p.waitForTimeout(300);await p.click('.results button');await p.waitForTimeout(1200);
    assert(await p.$('[data-merk="MAT.5.3"]'),'Merkvers-Zeichen am Vers');
    assert.equal(await p.$$eval('.reader .merk',x=>x.length),0,'Standard: keine Karte im Lesefluss');
    await p.click('[data-merk="MAT.5.3"]');await p.waitForTimeout(400);
    assert(await p.$('.sheet .merk .ill-img svg'),'Karte im Blatt');
    assert((await p.$eval('.sheet .merk-text',e=>e.textContent)).includes('Armen'),'Verswortlaut auf der Karte');
    await p.click('.sheet [data-close]');
    await p.click('[data-action=menu]');await p.click('[data-settings]');await p.click('[data-set=merk][data-value=card]');await p.click('.sheet [data-close]');await p.waitForTimeout(400);
    assert(await p.$('.reader .merk'),'Einstellung «Karte»: Karte im Text');
    await p.click('[data-action=menu]');await p.click('[data-settings]');await p.click('[data-set=merk][data-value=off]');await p.click('.sheet [data-close]');await p.waitForTimeout(400);
    assert(!await p.$('.reader .merk')&&!await p.$('[data-merk]'),'Einstellung «Aus»');
    // Lernen
    await p.click('[data-action=menu]');await p.click('[data-learn=menu]');await p.waitForTimeout(300);
    assert.equal(await p.$$eval('.sheet [data-learn^="start:"]',x=>x.length),5,'fünf Lernmethoden');
    await p.click('[data-learn="start:cards"]');await p.waitForTimeout(600);
    assert(await p.$('.sheet .learn-img svg'),'Karteikarte mit Bild');await p.click('[data-learn=reveal]');await p.click('[data-learn="rate:good"]');
    const st=await p.evaluate(()=>JSON.parse(localStorage.getItem('lesestrom-lernen')||'{}'));assert(Object.values(st).some(x=>x.box===1&&x.due>Date.now()),'Leitner: Kasten 1, nächste Wiederholung gesetzt');
    await p.click('[data-learn=menu]');await p.click('[data-learn="start:letters"]');await p.waitForTimeout(400);
    const fl=await p.$eval('.sheet .learn-letters',e=>e.textContent);assert(fl.split(' ').every(w=>w.replace(/[^\p{L}]/gu,'').length<=1),'Anfangsbuchstaben');
    await p.click('[data-learn=menu]');await p.click('[data-learn="start:cloze"]');await p.waitForTimeout(400);
    assert(await p.$('.sheet .cloze .gap'),'Lückentext mit Lücken');await p.click('.sheet .cloze .gap');
    await p.click('[data-learn="stage:4"]');const gaps=await p.$$eval('.sheet .cloze .gap',x=>x.length);assert(gaps>3,'Stufe «alles»: viele Lücken');
    await p.click('[data-learn=menu]');await p.click('[data-learn="start:order"]');await p.waitForTimeout(400);
    for(let k=0;k<80&&await p.$('.order-pool .chip');k++){const ok=await p.evaluate(()=>{const line=document.querySelector('.order-line').textContent.replace(' …','').trim();return line;});
      const chips=await p.$$('.order-pool .chip');for(const c of chips){const before=await p.$$eval('.order-pool .chip',x=>x.length);await c.click();const after=await p.$$eval('.order-pool .chip',x=>x.length);if(after<before)break;}}
    assert(!await p.$('.order-pool .chip'),'Wörter ordnen: alle Wörter gesetzt');
    await p.click('[data-learn=menu]');await p.click('[data-learn="start:quiz"]');await p.waitForTimeout(400);
    assert(await p.$$eval('.sheet [data-learn^="answer:"]',x=>x.length)>=2,'Quiz mit Auswahl');await p.click('.sheet [data-learn^="answer:"]');
    assert(await p.$('.sheet .learn-opts .row.ok'),'Quiz zeigt die richtige Stelle');
    assert.deepEqual(errs,[],'keine Fehler: '+errs.join('; '));
    console.log('PASS: Merkverse als Zeichen/Karte/aus; Lernen mit Karteikarten (Leitner), Anfangsbuchstaben, Lückentext, Wörter ordnen, Stellen zuordnen.');
  }finally{await b.close();}
})().catch(e=>{console.error(e);process.exit(1);});
