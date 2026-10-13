// Prüfung der aufgeteilten Fassung (build/reading-stream): Kern lädt Buch- und Sprachpakete erst bei Bedarf nach.
// Voraussetzung: python3 scripts/build_reading_stream.py; Playwright (PLAYWRIGHT_MODULE=Pfad oder require('playwright')).
// Fehlt Playwright, wird die Prüfung übersprungen (Exit 0 mit Hinweis).
const http=require('node:http'),fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
let chromium;try{({chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright'));}catch{console.log('SKIP: Playwright nicht verfügbar');process.exit(0);}
const root=path.join(__dirname,'../build',process.argv[2]||'reading-stream');
const server=http.createServer((q,r)=>{const f=path.join(root,decodeURIComponent(q.url.split('?')[0]));if(!f.startsWith(root)||!fs.existsSync(f)||fs.statSync(f).isDirectory()){r.writeHead(404);r.end();return;}
  r.writeHead(200,{'Content-Type':f.endsWith('.html')?'text/html; charset=utf-8':f.endsWith('.gz')?'application/gzip':f.endsWith('.txt')?'text/plain':'application/json'});fs.createReadStream(f).pipe(r);});
server.listen(0,async()=>{const url=`http://localhost:${server.address().port}/index.html`;const b=await chromium.launch();
  try{const p=await b.newPage({viewport:{width:390,height:800}});const reqs=[],errs=[];
    p.on('request',r=>{if(/\.(json\.gz|gz\.txt)$/.test(r.url()))reqs.push(r.url().split('/').slice(-3).join('/').replace(/^.*?\/(b|l)\//,'$1/').replace(/\.(json\.gz|gz\.txt)$/,''));});p.on('pageerror',e=>errs.push(e.message));
    const ev=f=>p.evaluate(f);const wait=()=>p.waitForTimeout(400);
    await p.goto(url);await wait();
    assert.deepEqual(reqs,['b/_overview'],'auf Bibelebene nur der Hintergrund der oberen Ebenen');
    await ev(()=>document.querySelector('[data-overview="all"]').click());await wait();
    const ov=await ev(()=>document.querySelector('.sheet').innerText);
    assert(ov.includes('Eine Bibliothek aus rund tausend Jahren')&&!ov.includes('[['),'Hintergrund der Bibel');
    await ev(()=>document.querySelector('[data-close]').click());
    await ev(()=>document.querySelector('[data-action=menu]').click());await ev(()=>document.querySelector('.sheet [data-go^="TU-MAT-006"]').click());await wait();
    assert(reqs.includes('b/MAT')&&reqs.includes('l/de/MAT')&&!reqs.some(x=>x.includes('gsw')),'nur Matthäus und Hochdeutsch geladen');
    await ev(()=>document.querySelector('[data-action=down]').click());await wait();
    assert.equal(await ev(()=>document.querySelector('[data-stream="v39-6-11"] .stream-copy').textContent),'Unser tägliches Brot gib uns heute.');
    await ev(()=>document.querySelector('[data-action=menu]').click());await ev(()=>document.querySelector('[data-set="text"][data-value="gsw"]').click());await wait();await ev(()=>document.querySelector('[data-close]').click());
    assert(reqs.includes('l/gsw/MAT')&&reqs.includes('l/gsw/common'),'Mundart-Pakete nachgeladen');
    assert.equal(await ev(()=>document.querySelector('[data-stream="v39-6-11"] .stream-copy').textContent),'Öises täglich Broot gib üs hüt.');
    await ev(()=>document.querySelector('[data-more="v39-6-11"]').click());await ev(()=>document.querySelector('.sheet-tools [data-background="TU-MAT-006-009-013"]').click());await wait();
    const sheet=await ev(()=>document.querySelector('.sheet').innerText);
    assert(!sheet.includes('[[')&&sheet.includes('Vatterunser'),'Hintergrund in Mundart, Stellen als Anzeige');
    await ev(()=>document.querySelector('[data-close]').click());await ev(()=>document.querySelector('[data-action=home]')?.click());await wait();
    await ev(()=>document.querySelector('[data-action=down]').click());await wait();await ev(()=>document.querySelector('[data-action=down]').click());await wait();
    await ev(()=>document.querySelector('[data-overview="g5"]').click());await wait();
    assert((await ev(()=>document.querySelector('.sheet').innerText)).includes('Vier Verzellige vom Jesus'),'Hintergrund der Buchgruppe in Mundart');
    assert.deepEqual(errs,[],'keine Skriptfehler');
    console.log(`PASS: aufgeteilte Fassung lädt nach Bedarf (${process.argv[2]||'reading-stream'}, ${reqs.length} Pakete: ${reqs.join(', ')}).`);
  }finally{await b.close();server.close();}});
