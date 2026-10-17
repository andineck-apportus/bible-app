// Prüfung der Bilder im Lesestrom: Bilder auf allen Ebenen über den Versen, Stil-Umschalter beim Bild und in der Legende.
// Voraussetzung: python3 scripts/build_reading_stream.py; Playwright (PLAYWRIGHT_MODULE=Pfad oder require('playwright')).
const path=require('node:path'),assert=require('node:assert/strict');
let chromium;try{({chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright'));}catch{console.log('SKIP: Playwright nicht verfügbar');process.exit(0);}
(async()=>{const b=await chromium.launch();
  try{const p=await b.newPage({viewport:{width:390,height:844}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
    await p.goto('file://'+path.join(__dirname,'../app/reading-stream/index.html'));await p.waitForTimeout(800);
    assert(await p.$('.has-ill .ill-img svg'),'Bild auf der Ebene Bibel');
    assert.equal(await p.$$eval('.ill-styles',x=>x.length),0,'kein Stil-Umschalter, wo es nur einen Stil gibt');
    await p.click('[data-action=menu]');await p.fill('input[type=search]','Joh 2,1');await p.waitForTimeout(300);await p.click('.results button');await p.waitForTimeout(900);
    while(+await p.evaluate(()=>document.querySelector('.app').dataset.level)>5){await p.evaluate(()=>document.querySelector('.immersed')?.classList.remove('immersed'));await p.click('[data-action=up]');await p.waitForTimeout(800);}
    assert.equal(await p.$$eval('.has-ill .ill-styles',x=>x.length),3,'Stil-Umschalter bei den drei Abschnitten von Johannes 2');
    assert.equal(await p.$eval('.has-ill .ill-styles button',e=>e.dataset.illStyle),'symbol','Symbol zuerst');
    await p.evaluate(()=>{const b=document.querySelector('.has-ill [data-view=image]');b&&b.click();});
    await p.click('.has-ill [data-ill-style=anime]');await p.waitForTimeout(500);
    assert(await p.evaluate(()=>!!document.querySelector('.has-ill .ill-img use[href^="#an-"]')),'Anime-Bild nach dem Umschalten');
    await p.click('.has-ill [data-legend]');await p.waitForTimeout(400);await p.click('.sheet [data-ill-style=symbol]');await p.waitForTimeout(400);
    assert(await p.evaluate(()=>!!document.querySelector('.sheet .legend-img use[href^="#ill-"]')),'Legende wechselt den Stil');
    assert(!await p.$('[data-settings]'),'Umschalten öffnet nicht das Menü');
    await p.click('.sheet [data-close]');await p.waitForTimeout(300);await p.click('[data-action=menu]');await p.click('[data-figindex]');await p.waitForTimeout(300);
    const nSym=await p.$$eval('.sheet .legend-fig',x=>x.length);await p.click('[data-figindex-style=anime]');await p.waitForTimeout(300);
    const nAni=await p.$$eval('.sheet .legend-fig',x=>x.length);assert(nSym>nAni&&nAni>10,'Bildlexikon je Stil ('+nSym+' Symbol, '+nAni+' Anime)');
    assert(await p.$('.sheet .legend-fig use[href^="#an-"]'),'Anime-Darstellungen im Bildlexikon');
    assert.deepEqual(errs,[],'keine Skriptfehler');
    console.log('PASS: Bilder auf allen Ebenen, Stil-Umschalter beim Bild und in der Legende, Bildlexikon je Stil (Symbol/Anime).');
  }finally{await b.close();}})().catch(e=>{console.error(e);process.exit(1);});
