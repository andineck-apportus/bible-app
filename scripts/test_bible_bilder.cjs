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
    await p.click('[data-action=index]');await p.fill('input[type=search]','Joh 2,1');await p.waitForTimeout(300);await p.click('.results button');await p.click('.sheet .nav-open');await p.waitForTimeout(900);
    while(+await p.evaluate(()=>document.querySelector('.app').dataset.level)>5){await p.evaluate(()=>document.querySelector('.immersed')?.classList.remove('immersed'));await p.click('[data-action=up]');await p.click('.sheet .pick-open');await p.waitForTimeout(800);}
    assert(await p.$$eval('.has-ill',x=>x.length)>=3,'Bilder bei den Abschnitten von Johannes 2 (und den geladenen Nachbarn)');
    assert.equal(await p.evaluate(()=>document.querySelector('.app').dataset.show),'both','Text und Bild zusammen als Vorgabe');
    {const tb=p.locator('.has-ill .tile-box[data-tilecap]:visible').first();await tb.click();await p.waitForTimeout(200);  // Legende je Kachel einblenden (Hinweis Andi Neck 2026-10-25)
      assert.equal(await tb.getAttribute('aria-expanded'),'true','Kachel-Legende eingeblendet');assert(await tb.locator('.tile-cap:not([hidden])').count(),'Kachel-Legende sichtbar');
      await tb.click();await p.waitForTimeout(200);assert.equal(await tb.getAttribute('aria-expanded'),'false','Kachel-Legende wieder aus');}
    await p.locator('.has-ill [data-legend]:visible').first().click();await p.waitForTimeout(400);  // ganze Erklärung zum Bild
    // Johannes 2 im Aquarellstil (docs/BILDSTIL.md): gemalte Felder, Worte als Text je Sprache, Belege B/R/I in der Legende
    assert(await p.evaluate(()=>!!document.querySelector('.sheet .legend-img svg.ill-tile[data-scene] image')),'Legende zeigt das Aquarellbild');
    assert(await p.evaluate(()=>document.querySelectorAll('.sheet .legend-ev .ev').length>=6),'Belege B/R/I je Feld');
    assert(await p.evaluate(()=>[...document.querySelectorAll('.sheet .legend-img .lw-de')].some(t=>/Sie haben keinen/.test(t.textContent))),'Worte der Mutter Jesu als Text');
    assert(!await p.$('[data-settings]'),'Legende öffnet nicht das Menü');
    await p.click('.sheet [data-close]');await p.waitForTimeout(300);await p.evaluate(()=>document.querySelector('.immersed')?.classList.remove('immersed'));await p.click('[data-action=menu]');await p.click('[data-figindex]');await p.waitForTimeout(300);
    const nAni=await p.$$eval('.sheet .legend-fig',x=>x.length);assert(nAni>300,'Bildlexikon Anime ('+nAni+')');
    assert(await p.$('.sheet .legend-fig use[href^="#an-"]'),'Anime-Darstellungen im Bildlexikon');
    // Bildlexikon im Aquarellstil (Entscheid Andi Neck 2026-10-28): Einzelporträt (img mit alt) oder Platzhalter «noch nicht gemalt»,
    // Name, Erkennungsmerkmal und «kommt vor in» (antippbar → Stelle)
    await p.click('.sheet [data-figindex-style=aquarell]');await p.waitForTimeout(600);
    const aq=await p.evaluate(()=>{const c=[...document.querySelectorAll('.sheet .legend-fig.fig-paint')];
      return {n:c.length,img:c.filter(x=>x.querySelector('.fig-pic img')).length,alt:c.filter(x=>{const i=x.querySelector('.fig-pic img');return i&&i.alt.length>3&&i.getAttribute("src").startsWith("data:image/");}).length,
        none:c.filter(x=>/noch nicht gemalt/.test(x.querySelector('.fig-none')?.textContent||'')).length,sym:document.querySelectorAll('.sheet .legend-fig use').length,
        name:c.every(x=>x.querySelector('b')?.textContent.trim()),sub:c.every(x=>x.querySelector('.sub')?.textContent.trim()),occ:document.querySelectorAll('.sheet .fig-occ [data-ref-go]').length};});
    {const fs=require('node:fs'),R=path.join(__dirname,'..'),st=JSON.parse(fs.readFileSync(path.join(R,'data/illustrations/styles/ILLSTYLE-AQUARELL.json'),'utf8')).renderings;
      aq.want=Object.keys(st).filter(i=>fs.existsSync(path.join(R,'data/illustrations/lexicon',i+'.json'))).length;
      aq.mitBild=Object.values(st).filter(r=>r.image&&fs.existsSync(path.join(R,r.image))&&(!(r.check||{}).trocken||process.env.BIBLE_TROCKEN_BILDER)).length;}
    assert(aq.n>=40&&aq.n===aq.want,'Bildlexikon Aquarell: alle Einträge ('+aq.n+'/'+aq.want+')');
    assert.equal(aq.sym,0,'im Aquarellstil keine SVG-Zeichen');
    assert.equal(aq.img+aq.none,aq.n,'je Eintrag Bild oder Platzhalter');assert.equal(aq.img,aq.mitBild,'Bilder für alle gemalten Einträge ('+aq.img+')');assert.equal(aq.alt,aq.img,'Bilder mit Bilddaten und alt-Text');
    assert(aq.name&&aq.sub,'Name und Erkennungsmerkmal');assert(aq.occ>=10,'«kommt vor in» mit Stellen ('+aq.occ+')');
    {const r=await p.getAttribute('.sheet .fig-paint[data-fig="FIG-JESUS"] .fig-occ [data-ref-go]','data-ref-go');assert(r,'Jesus kommt in gemalten Stellen vor');
      await p.click('.sheet .fig-paint[data-fig="FIG-JESUS"] .fig-occ [data-ref-go]');await p.waitForTimeout(900);
      assert(!await p.$('.sheet .fig-paint'),'Stelle antippen schliesst das Bildlexikon');
      const [bk,c]=r.split('-')[0].split('.');assert(await p.evaluate(([bk,c])=>{const a=document.querySelector('.app');return a.dataset.level>=4;},[bk,c]),'Stelle geöffnet');}
    // Struktur zuerst: Seligpreisungen mit Liste aller acht Glieder und Strukturbild in einzelnen Kacheln
    if(await p.$('.sheet [data-close]')){await p.click('.sheet [data-close]');await p.waitForTimeout(300);}
    await p.click('[data-action=index]');await p.fill('input[type=search]','Mt 5,3');await p.waitForTimeout(300);await p.click('.results button');await p.click('.sheet .nav-open');await p.waitForTimeout(900);
    while(+await p.evaluate(()=>document.querySelector('.app').dataset.level)>5){await p.evaluate(()=>document.querySelector('.immersed')?.classList.remove('immersed'));await p.click('[data-action=up]');await p.click('.sheet .pick-open');await p.waitForTimeout(500);}
    const nLi=await p.evaluate(()=>{const e=[...document.querySelectorAll('.stream-entry')].find(x=>/Seligpreisungen/.test(x.querySelector('h2')?.textContent||''));return e?e.querySelectorAll('.sum-list li').length:0;});
    assert(nLi>=8,'Seligpreisungen als Liste aller Glieder ('+nLi+')');
    assert(await p.$('.ill-tiles svg.ill-tile'),'Bilder als einzelne Kacheln');
    // Abschnitt ohne Worte (Knopf oben beim Umschalter): Worte verdeckt, Zellen zeigen Zeichen gross; Antippen deckt stufenweise auf
    await p.locator('[data-nowords]:visible').first().click();await p.waitForTimeout(400);
    assert(await p.$('.ill.nowords'),'Abschnittsbild ohne Worte');
    const nw=await p.evaluate(()=>{const c=document.querySelector('.ill.nowords g.dg-cell');return {full:getComputedStyle(c.querySelector('.dg-full')).display,nw:getComputedStyle(c.querySelector('.dg-nw')).display};});
    assert.equal(nw.full,'none','ganze Worte verdeckt');assert(!await p.evaluate(()=>[...document.querySelectorAll('.ill.nowords .dg-nw text')].some(t=>t.getBoundingClientRect().width>0)),'ohne Worte: kein Text, nur Zeichen');assert.equal(nw.nw,'inline','Zeichen gross');
    const cell=p.locator('.ill.nowords g.dg-cell:visible').first();await cell.click();  // nur Zeichen, Antippen zeigt gleich die Worte (keine Anfangsbuchstaben mehr)
    assert.equal(await p.evaluate(()=>getComputedStyle(document.querySelector('.ill.nowords g.dg-cell.r2 .dg-full')).display),'inline','Antippen zeigt die Worte');
    // Antippen wirkt auf dem ganzen Feld (Ecke des Rahmens), nicht nur auf dem Zeichen – für Kästchen und Köpfe/Blasen
    for(const sel of ['.ill.nowords g.dg-cell','.ill.nowords g.dg-sw']){
      const box=await p.evaluate(s=>{const g=[...document.querySelectorAll(s)].find(x=>x.getBoundingClientRect().width>0&&!x.classList.contains('r1')&&!x.classList.contains('r2')&&[...x.querySelectorAll('rect')].some(r=>r.getBoundingClientRect().width>0));if(!g)return null;g.scrollIntoView({block:'center'});const r=[...g.querySelectorAll('rect')].map(x=>x.getBoundingClientRect()).find(x=>x.width>0);g.dataset.t='1';return {x:r.left+4,y:r.top+r.height-4};},sel);
      assert(box,'Feld vorhanden: '+sel);await p.mouse.click(box.x,box.y);
      assert(await p.evaluate(()=>{const g=document.querySelector('[data-t="1"]');const ok=g.classList.contains('r1')||g.classList.contains('r2');delete g.dataset.t;return ok;}),'Antippen der Feldecke deckt auf: '+sel);}
    await p.locator('[data-nowords]:visible').first().click();await p.waitForTimeout(300);assert(!await p.$('.ill.nowords'),'wieder mit Worten');
    // Umschalter Text | Bild (Entscheid Andi Neck 2026-10-27): beide unabhängig, mindestens einer an, gilt für alle Ebenen; auf Versebene
    // stehen die Felder des Abschnittsbilds bei ihren Versen
    await p.evaluate(()=>document.querySelector('.immersed')?.classList.remove('immersed'));
    await p.click('[data-action=index]');await p.fill('input[type=search]','Mt 5,33');await p.waitForTimeout(300);await p.click('.results button');await p.click('.sheet .nav-open');await p.waitForTimeout(900);
    assert(await p.$('.verse-ill svg.ill-tile'),'Feld des Abschnittsbilds beim Vers (Text und Bild)');
    const tog=async k=>{await p.evaluate(()=>document.querySelector('.immersed')?.classList.remove('immersed'));await p.locator(`[data-show-t=${k}]:visible`).first().click();await p.waitForTimeout(500);};
    await tog('img');assert(!await p.$('.verse-ill'),'nur Text: keine Bilder bei den Versen');
    assert(await p.$$eval('button[data-show-t=img]',x=>x.length>0&&x.every(b=>b.getAttribute('aria-pressed')==='false')),'Umschalter gilt für alle Abschnitte');
    await tog('text');assert.equal(await p.evaluate(()=>document.querySelector('.app').dataset.show),'img','letzter Knopf aus: wechselt auf den anderen statt beide aus');
    assert(await p.$('.verse-ill svg.ill-tile'),'nur Bild: Felder sichtbar');
    assert(!await p.evaluate(()=>[...document.querySelectorAll('.stream-entry.verse.in-ill .verse-line')].some(e=>e.getBoundingClientRect().height>0)),'nur Bild: kein Verstext, wo ein Bild steht');
    await tog('text');assert.equal(await p.evaluate(()=>document.querySelector('.app').dataset.show),'both','beide wieder an');
    assert(!await p.$('.set [data-seg=ill] [data-val=off]'),'keine Einstellung «keine Bilder» mehr');
    assert.deepEqual(errs,[],'keine Skriptfehler');
    console.log('PASS: Bilder auf allen Ebenen im Stil Anime, Legende, Bildlexikon (Anime, Aquarell mit Porträts bzw. Platzhaltern), Kacheln, strukturierte Zusammenfassung, Kapitel ohne Worte, Umschalter Text | Bild, Bilder bei den Versen.');
  }finally{await b.close();}})().catch(e=>{console.error(e);process.exit(1);});
