// Optionale Bedienungsprüfung: npm install --no-save jsdom, dann mit Node ausführen.
const {JSDOM}=require('jsdom'),fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
let model;
const dom=new JSDOM(fs.readFileSync(path.join(__dirname,'../app/reading-stream/index.html'),'utf8'),{runScripts:'dangerously',pretendToBeVisual:true,beforeParse(w){w.__BIBLE_TEST__=x=>model=x;}});
const app=dom.window.document.querySelector('#bible-stream .app');
assert(app,'App fehlt');
const reader=app.querySelector('.reader'),sheetHost=app.querySelector('.sheet-host');
const click=s=>{const el=app.querySelector(s);assert(el,s);el.click();};
const M=()=>model.MARKUS;

// Einstieg über das Menü in den Pilotabschnitt; Studienblatt mit Deutung und Gegenargument
click('[data-action=menu]');click('[data-go="TU-MRK-003-020-021"]');
assert.equal(sheetHost.textContent,'','Menü schliesst nach Navigation');
assert(reader.querySelector('[data-stream="TU-MRK-003-031-035"]'));
click('[data-study="TU-MRK-003-022-030"]');
const counter=M().interpretations.find(i=>['TU-MRK-003-022-030',M().section.id].includes(i.subject)&&i.counter.length)?.counter[0];
assert(counter&&sheetHost.textContent.includes(counter.slice(0,40)),'Gegenargument im Studienblatt');
assert(!/[Ͱ-Ͽἀ-῿]/.test(sheetHost.textContent),'Ohne Urtext-Modus kein Griechisch im Studienblatt');
click('[data-close]');

// Vertiefen in die Verse; Rückkehrposition
reader.scrollTop=137;click('[data-deep="TU-MRK-003-022-030"]');
const verse=reader.querySelector('[data-stream="v40-3-29"]');
assert.equal(verse.querySelector('.stream-copy').textContent,M().de[29]);
assert(!verse.querySelector('[data-alternative]'),'Lesarten standardmässig nicht im Lesestrom');
assert(!reader.querySelector('[data-more="v40-3-23"]')||M().alternatives.some(a=>a.verse===23),'«+» nur bei Versen mit Lesarten');

// Versblatt ohne und mit Urtext-Modus
click('[data-more="v40-3-29"]');
assert(sheetHost.querySelector('[data-alternative]'),'Lesarten im Versblatt');
assert(!sheetHost.textContent.includes('MorphGNT'),'Ohne Urtext-Modus keine Wortanalyse');
click('[data-close]');
click('[data-action=menu]');click('[data-toggle=advanced]');click('[data-close]');
click('[data-more="v40-3-29"]');
const details=sheetHost.querySelector('details');details.querySelector('summary').click();assert(details.open);
assert(sheetHost.textContent.includes('Keine Handschriftenzählung'));
assert(sheetHost.textContent.includes('MorphGNT'));
click('[data-close]');
click('[data-action=up]');assert.equal(reader.scrollTop,137,'Rückkehrposition');

// Suche, fortlaufendes Lesen über die Kapitelgrenze, Lesarten im Fliesstext
click('[data-action=menu]');click('[data-toggle=inline]');
const input=sheetHost.querySelector('input[type=search]');input.value='Mk 3,20';input.dispatchEvent(new dom.window.Event('input',{bubbles:true}));
sheetHost.querySelector('.results [data-go]').click();
click('[data-action=load-next]');
for(let v=20;v<=35;v++)assert.equal(reader.querySelector(`[data-stream="v40-3-${v}"] .stream-copy`).textContent,M().de[v]);
assert(reader.querySelector('[data-stream="v40-4-1"]'));
assert.equal(reader.querySelectorAll('.alt-line[data-alternative]').length,M().alternatives.length);
console.log(`PASS: Pilotzugang, Studienblatt ohne Griechisch, Lesarten auf Wunsch (${M().alternatives.length}), Urtext-Modus, Rückkehrposition, Suche, Kapitelgrenze.`);
dom.window.close();
