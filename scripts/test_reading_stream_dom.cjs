// Optionale Bedienungsprüfung: npm install --no-save jsdom, dann mit Node ausführen.
const {JSDOM}=require('jsdom'),fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
let model;
const dom=new JSDOM(fs.readFileSync(path.join(__dirname,'../app/reading-stream/index.html'),'utf8'),{runScripts:'dangerously',pretendToBeVisual:true,beforeParse(w){w.__BIBLE_TEST__=x=>model=x;}});
const app=dom.window.document.querySelector('#bible-stream .app');
assert(app,'App fehlt');
const reader=app.querySelector('.reader'),sheetHost=app.querySelector('.sheet-host');
const click=s=>{const el=app.querySelector(s);assert(el,s);el.click();};
const M=()=>model.STUDY;
const mk=v=>M().de['MRK.3.'+v];
const vOf=r=>Number(r.split('.')[2]);
const mkAlts=()=>M().alternatives.filter(a=>a.ref.startsWith('MRK.3.'));

// Voreinstellung: Lesarten, Hintergrund und Urtext sind eingeschaltet; für die folgenden Prüfungen zuerst aus
click('[data-action=menu]');
for(const k of ['inline','bgInline','advanced'])assert.equal(sheetHost.querySelector(`[data-toggle=${k}]`).getAttribute('aria-checked'),'true',k+' standardmässig an');
for(const k of ['inline','bgInline','advanced'])click(`[data-toggle=${k}]`);
click('[data-close]');

// Einstieg über das Menü in den Pilotabschnitt; Studienblatt mit Deutung und Gegenargument
click('[data-action=menu]');click('[data-go="TU-MRK-003-020-021"]');
assert.equal(sheetHost.textContent,'','Menü schliesst nach Navigation');
assert(reader.querySelector('[data-stream="TU-MRK-003-031-035"]'));
click('[data-study="TU-MRK-003-022-030"]');
const counter=M().interpretations.find(i=>['TU-MRK-003-022-030','TU-MRK-003-020-035'].includes(i.subject)&&i.counter.length)?.counter[0];
assert(counter&&sheetHost.textContent.includes(counter.slice(0,40)),'Gegenargument im Studienblatt');
assert(!/[Ͱ-Ͽἀ-῿]/.test(sheetHost.textContent),'Ohne Urtext-Modus kein Griechisch im Studienblatt');
click('[data-close]');

// Vertiefen in die Verse; Rückkehrposition
reader.scrollTop=137;click('[data-deep="TU-MRK-003-022-030"]');
const verse=reader.querySelector('[data-stream="v40-3-29"]');
assert.equal(verse.querySelector('.stream-copy').textContent,mk(29));
assert(!verse.querySelector('[data-alternative]'),'Lesarten standardmässig nicht im Lesestrom');
for(let v=22;v<=30;v++){const want=mkAlts().some(a=>vOf(a.ref)===v)||model.BG.some(b=>!b.wide&&b.chapter==='MRK.3'&&b.from<=v&&v<=b.to);
 assert.equal(!!reader.querySelector(`[data-more="v40-3-${v}"]`),want,`«+» nur bei Lesarten oder Hintergrund (3,${v})`);}

// Hintergrund damals: Vers, Abschnitt, Hinweise im Text
click('[data-more="v40-3-22"]');
assert(sheetHost.querySelector('[data-bg-note="BG-MRK-0006"]'),'Beelzebul im Versblatt 3,22');
assert(!sheetHost.querySelector('[data-bg-note="BG-MRK-0001"]'),'Abschnittsweiter Hintergrund nicht im Versblatt');
click('[data-close]');
click('[data-background="TU-MRK-003-022-030"]');
for(const b of model.BG.filter(x=>(x.wide&&x.section==='TU-MRK-003-020-035')||x.subject==='TU-MRK-003-022-030'))assert(sheetHost.querySelector(`[data-bg-note="${b.id}"]`),b.id);
assert(sheetHost.textContent.includes('Josephus'),'Quellenangabe sichtbar');
click('[data-close]');
assert(!reader.querySelector('.bg-line'),'Hintergrund standardmässig nicht im Lesestrom');
click('[data-action=menu]');click('[data-toggle=bgInline]');click('[data-close]');
click('.bg-line[data-bg="BG-MRK-0008"]');assert(sheetHost.textContent.includes('Jes 49,24–25'));click('[data-close]');
click('[data-action=menu]');click('[data-toggle=bgInline]');click('[data-close]');

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
for(let v=20;v<=35;v++)assert.equal(reader.querySelector(`[data-stream="v40-3-${v}"] .stream-copy`).textContent,mk(v));
assert(reader.querySelector('[data-stream="v40-4-1"]'));
assert.equal(reader.querySelectorAll('.alt-line[data-alternative]').length,mkAlts().length);
// Bis zur Quelle: jede Alternative führt zu Handschriften, Ausgaben, Wortbedeutungen und Erklärungen
for(const a of mkAlts()){
 const vid=`v40-3-${vOf(a.ref)}`;
 click(`[data-more="${vid}"]`);
 const btn=sheetHost.querySelector(`[data-source="${a.variant}"]`);assert(btn,'Bis zur Quelle '+a.variant);btn.click();
 const txt=sheetHost.textContent;
 assert(txt.includes('Was die alten Handschriften lesen'),'Handschriften '+a.variant);
 assert(sheetHost.querySelectorAll('details.wit').length>=6,'Handschriften und Ausgaben '+a.variant);
 assert(txt.includes('Wie kann der Unterschied entstanden sein?'),'Erklärungen '+a.variant);
 assert(txt.includes('CC BY-SA 4.0'),'Attribution CNTR');
 if(a.variant==='VAR-SBLGNTAPP-MRK-003-029-01'){assert(txt.includes('Codex Alexandrinus')&&txt.includes('eines Gerichts'));assert(/Abweichung:.*Ephraemi/.test(txt),'Arbeitsnotiz-Abweichung Ephraemi');}
 click('[data-close]');
}
let tested=mkAlts().length;


// Vaterunser: Matthäus und Lukas
click('[data-action=menu]');
assert.equal(sheetHost.querySelectorAll('[data-go^="TU-"]').length,M().sections.length,'Ausgearbeitete Stellen im Menü');
click('.sheet [data-go="TU-MAT-006-005-008"]');
click('[data-deep="TU-MAT-006-009-013"]');
const mtv=v=>reader.querySelector(`[data-stream="v39-6-${v}"] .stream-copy`);
for(let v=9;v<=13;v++)assert.equal(mtv(v).textContent,M().de['MAT.6.'+v]);
click('[data-study="TU-MAT-006-009-013"]');
assert(sheetHost.textContent.includes('Brot für den kommenden Tag'),'Deutungen zu epiousios');
assert(sheetHost.textContent.includes('Was kann es heute bedeuten?'),'Anwendung Vaterunser');
click('[data-close]');
assert(reader.querySelector('.part-head [data-study="TU-MAT-006-009-013"]')&&reader.querySelector('.part-head [data-background="TU-MAT-006-009-013"]'),'Werkzeuge am Abschnittstitel');
assert(!reader.querySelector('.part-end'),'keine Links am Abschnittsende');
assert(reader.querySelector('button.vno[data-more="v39-6-11"]'),'Versnummer öffnet Details');
const decBtn=reader.querySelector('[data-ref="MAT.6.11"] button.dec');assert(decBtn&&decBtn.textContent==='tägliches','tägliches markiert');decBtn.click();
let ptx=sheetHost.textContent;
assert(ptx.includes('Brot für den kommenden Tag')&&ptx.includes('Das zum Leben nötige Brot'),'Deutungen im Wort-Blatt');
assert(ptx.includes('Unser täglich Brot gib uns heute')&&ptx.includes('Unser nötiges Brot gib uns heute'),'ältere Übersetzungen im Wort-Blatt');
assert(sheetHost.querySelector('.play[data-speak="τὸν ἐπιούσιον"]'),'Griechisch anhörbar');
click('[data-close]');
click('[data-more="v39-6-11"]');
assert(sheetHost.querySelector('.sheet-tools [data-study="TU-MAT-006-009-013"] svg')&&sheetHost.querySelector('.sheet-tools [data-background="TU-MAT-006-009-013"] svg'),'Symbole Verstehen/Geschichte im Versblatt');
assert(!sheetHost.textContent.includes('Diesen Abschnitt verstehen'),'keine alten Links im Versblatt');
click('[data-close]');
click('[data-more="v39-6-13"]');
let dtx=sheetHost.textContent;
assert(dtx.includes('Wie ist übersetzt?')&&dtx.includes('folgt der vertrauten Wiedergabe'),'Übersetzungsentscheidungen');
assert(dtx.includes('«durch» wäre διά'),'Hinweis zu «führe uns durch»');
assert(dtx.includes('Lutherbibel, revidierte Fassung 1912')&&dtx.includes('erlöse uns von dem Übel'),'Vergleich Luther 1912');
assert(dtx.includes('errette uns von dem Bösen'),'Vergleich Elberfelder 1905');
click('[data-close]');
click('[data-more="v39-6-13"]');click('.sheet [data-source="VAR-SBLGNTAPP-MAT-006-013-01"]');
let txt=sheetHost.textContent;
assert(txt.includes('Codex Sinaiticus')&&txt.includes('Codex Washingtonianus')&&txt.includes('P. Oxyrhynchus 60.4010'),'Zeugen zur Doxologie');
assert(txt.includes('Didache'),'Erklärung Doxologie');
assert(sheetHost.querySelector('.word-row .play[data-speak]'),'Anhören-Knopf bei den Wörtern');
assert(txt.includes('ponēroú'),'Umschrift sichtbar');
const det=sheetHost.querySelector('details.wit');const pb=det.querySelector('.play');if(pb){pb.click();assert(!det.open,'Anhören klappt nicht auf');}
sheetHost.querySelector('.word-row .play').click();assert(app.querySelector('.live').textContent.length>0,'Rückmeldung ohne Sprachausgabe');
tested++;click('[data-close]');
click('[data-action=menu]');assert(sheetHost.textContent.includes('Aussprache'),'Aussprache-Einstellung');click('[data-toggle=translit]');click('[data-close]');
click('[data-more="v39-6-13"]');click('.sheet [data-source="VAR-SBLGNTAPP-MAT-006-013-01"]');assert(!sheetHost.querySelector('.tr'),'Umschrift abschaltbar');click('[data-close]');
click('[data-action=menu]');click('[data-toggle=translit]');click('[data-close]');
for(const a of M().alternatives.filter(a=>a.ref.startsWith('MAT.6.'))){const v=vOf(a.ref);if(!reader.querySelector(`[data-more="v39-6-${v}"]`)){continue;}click(`[data-more="v39-6-${v}"]`);sheetHost.querySelector(`[data-source="${a.variant}"]`).click();assert(sheetHost.textContent.includes('Was die gedruckten Ausgaben haben'),a.variant);click('[data-close]');tested++;}
click('[data-action=menu]');const inp=sheetHost.querySelector('input[type=search]');inp.value='Lk 11,2';inp.dispatchEvent(new dom.window.Event('input',{bubbles:true}));sheetHost.querySelector('.results [data-go]').click();
assert.equal(reader.querySelector('[data-stream="v41-11-2"] .stream-copy').textContent,M().de['LUK.11.2']);
click('[data-more="v41-11-2"]');click('.sheet [data-source="VAR-SBLGNTAPP-LUK-011-002-01"]');
txt=sheetHost.textContent;assert(txt.includes('Papyrus 75')&&txt.includes('Codex Vaticanus'),'P75 zu Lk 11,2');tested++;click('[data-close]');
console.log(`PASS: Pilotzugang, Studienblatt ohne Griechisch, Lesarten auf Wunsch (${M().alternatives.length}), Hintergrund damals (${model.BG.length}), Bis zur Quelle (${tested}), Urtext-Modus, Rückkehrposition, Suche, Kapitelgrenze, Vaterunser Mt/Lk, Übersetzungsentscheidungen und Vergleich, Wort-Blatt, Umschrift und Anhören.`);
dom.window.close();
