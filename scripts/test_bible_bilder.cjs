// Prüfung der Bilder in der App: Bilder auf allen Ebenen im Stil Anime (Symbol eingestellt 2026-10-23), Legende, Bildlexikon.
// Voraussetzung: python3 scripts/build_bible.py; Playwright (PLAYWRIGHT_MODULE=Pfad oder require('playwright')).
const path=require('node:path'),assert=require('node:assert/strict');
let chromium;try{({chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright'));}catch{console.log('SKIP: Playwright nicht verfügbar');process.exit(0);}
(async()=>{const b=await chromium.launch();
  try{const p=await b.newPage({viewport:{width:390,height:844}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
    await p.goto('file://'+path.join(__dirname,'../app/bible/index.html'));await p.waitForTimeout(800);
    assert(await p.$('.has-ill .ill-img svg'),'Bild auf der Ebene Bibel');
    assert.equal(await p.$$eval('.ill-styles',x=>x.length),0,'nur ein Bildstil (Anime), kein Umschalter');
    assert(await p.evaluate(()=>!!document.querySelector('.has-ill .ill-img use[href^="#an-"]')),'Anime-Bild auf der Ebene Bibel');
    await p.click('[data-action=index]');await p.fill('input[type=search]','Joh 2,1');await p.waitForTimeout(300);await p.click('.results button');await p.waitForTimeout(900);
    while(+await p.evaluate(()=>document.querySelector('.app').dataset.level)>5){await p.evaluate(()=>document.querySelector('.immersed')?.classList.remove('immersed'));await p.click('[data-action=up]');await p.waitForTimeout(800);}
    assert(await p.$$eval('.has-ill',x=>x.length)>=3,'Bilder bei den Abschnitten von Johannes 2 (und den geladenen Nachbarn)');
    await p.evaluate(()=>{const b=document.querySelector('.has-ill [data-view=image]');b&&b.click();});
    await p.click('.has-ill [data-legend]');await p.waitForTimeout(400);
    assert(await p.evaluate(()=>!!document.querySelector('.sheet .legend-img use[href^="#an-"]')),'Legende im Stil Anime');
    assert(!await p.$('[data-settings]'),'Legende öffnet nicht das Menü');
    await p.click('.sheet [data-close]');await p.waitForTimeout(300);await p.click('[data-action=menu]');await p.click('[data-figindex]');await p.waitForTimeout(300);
    const nAni=await p.$$eval('.sheet .legend-fig',x=>x.length);assert(nAni>300,'Bildlexikon Anime ('+nAni+')');
    assert(await p.$('.sheet .legend-fig use[href^="#an-"]'),'Anime-Darstellungen im Bildlexikon');
    // Struktur zuerst: Seligpreisungen mit Liste aller acht Glieder und Strukturbild in einzelnen Kacheln
    await p.click('.sheet [data-close]');await p.waitForTimeout(300);
    await p.click('[data-action=index]');await p.fill('input[type=search]','Mt 5,3');await p.waitForTimeout(300);await p.click('.results button');await p.waitForTimeout(900);
    while(+await p.evaluate(()=>document.querySelector('.app').dataset.level)>5){await p.evaluate(()=>document.querySelector('.immersed')?.classList.remove('immersed'));await p.click('[data-action=up]');await p.waitForTimeout(500);}
    await p.evaluate(()=>{const b=document.querySelector('.has-ill [data-view=text]');b&&b.click();});
    const nLi=await p.evaluate(()=>{const e=[...document.querySelectorAll('.stream-entry')].find(x=>/Seligpreisungen/.test(x.querySelector('h2')?.textContent||''));return e?e.querySelectorAll('.sum-list li').length:0;});
    assert(nLi>=8,'Seligpreisungen als Liste aller Glieder ('+nLi+')');
    assert(await p.$('.ill-tiles svg.ill-tile'),'Bilder als einzelne Kacheln');
    // Kapitel ohne Worte: Worte verdeckt, Zellen zeigen Zeichen gross; Antippen deckt stufenweise auf (Hinweis Andi Neck 2026-10-25)
    while(+await p.evaluate(()=>document.querySelector('.app').dataset.level)>4){await p.evaluate(()=>document.querySelector('.immersed')?.classList.remove('immersed'));await p.click('[data-action=up]');await p.waitForTimeout(500);}
    await p.evaluate(()=>{const b=document.querySelector('.has-ill [data-view=image]');b&&b.click();});
    await p.locator('[data-nowords]:visible').first().click();await p.waitForTimeout(400);
    assert(await p.$('.ill.nowords'),'Kapitelbild ohne Worte');
    const nw=await p.evaluate(()=>{const c=document.querySelector('.ill.nowords g.dg-cell');return {full:getComputedStyle(c.querySelector('.dg-full')).display,nw:getComputedStyle(c.querySelector('.dg-nw')).display};});
    assert.equal(nw.full,'none','ganze Worte verdeckt');assert.equal(nw.nw,'inline','Zeichen gross');
    const cell=p.locator('.ill.nowords g.dg-cell:visible').first();await cell.click();await cell.click();
    assert.equal(await p.evaluate(()=>getComputedStyle(document.querySelector('.ill.nowords g.dg-cell.r2 .dg-full')).display),'inline','zweimal Antippen zeigt die Worte');
    await p.locator('[data-nowords]:visible').first().click();await p.waitForTimeout(300);assert(!await p.$('.ill.nowords'),'wieder mit Worten');
    // Bilder bei den Versen (Einstellung)
    await p.evaluate(()=>{const s=JSON.parse(localStorage.getItem('bible:settings')||'{}');s.vill='on';localStorage.setItem('bible:settings',JSON.stringify(s));});
    await p.reload();await p.waitForTimeout(800);
    await p.click('[data-action=index]');await p.fill('input[type=search]','Mt 5,33');await p.waitForTimeout(300);await p.click('.results button');await p.waitForTimeout(900);
    assert(await p.$('[data-stream$="MAT.5.33"] .verse-ill svg.ill-tile, .verse-ill svg.ill-tile'),'Feld des Abschnittsbilds beim Vers');
    assert.deepEqual(errs,[],'keine Skriptfehler');
    console.log('PASS: Bilder auf allen Ebenen im Stil Anime, Legende, Bildlexikon, Kacheln, strukturierte Zusammenfassung, Kapitel ohne Worte, Bilder bei den Versen.');
  }finally{await b.close();}})().catch(e=>{console.error(e);process.exit(1);});
