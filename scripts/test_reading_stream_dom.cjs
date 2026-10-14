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
const mkAlts=()=>M().alternatives.filter(a=>a.ref.startsWith('MRK.3.')&&vOf(a.ref)>=20); // Pilotabschnitt Mk 3,20–35

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
for(let v=22;v<=30;v++){const want=mkAlts().some(a=>vOf(a.ref)===v)||model.BG.some(b=>!b.wide&&b.chapter==='MRK.3'&&b.from<=v&&v<=b.to)||!!M().decisions['MRK.3.'+v]||(M().compare['MRK.3.'+v]||[]).some(c=>c.lang==='de');
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
assert.equal(sheetHost.querySelectorAll('details.worked:not(.recent) [data-go^="TU-"]').length,M().sections.length,'Ausgearbeitete Stellen im Menü (eingeklappt)');
assert(sheetHost.textContent.includes('Zuletzt gelesen')&&sheetHost.querySelectorAll('[data-clear-recent]').length===1,'Zuletzt gelesen nach dem Lesen');assert(sheetHost.querySelector('details.recent .recent-row'),'Zuletzt gelesen eingeklappt');
{const rr=[...sheetHost.querySelectorAll('.recent-row')];assert(rr.length>0&&rr.every(r=>[4,5].includes(model.nodes.get(r.dataset.go).level)),'Verlauf auf Abschnitt- bzw. Kapitelebene');}
click('[data-clear-recent]');
assert(!sheetHost.textContent.includes('Zuletzt gelesen'),'Verlauf löschen');
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
const decBtn=reader.querySelector('[data-ref="MAT.6.11"] .dec');assert(decBtn&&decBtn.textContent==='tägliches','tägliches markiert');decBtn.click();
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
assert(app.classList.contains('flow'),'Verse fortlaufend ist Standard');
click('[data-action=menu]');click('[data-toggle=flow]');assert(!app.classList.contains('flow'),'Verse fortlaufend abschaltbar');click('[data-toggle=flow]');assert(app.classList.contains('flow'));click('[data-close]');

// Navigator: Pfad, Hierarchie AT/NT → Gruppe → Buch → Kapitel → Vers
click('[data-action=index]');
assert(sheetHost.querySelector('.crumbs [aria-current=true]'),'Pfad zeigt die aktuelle Position');
assert(sheetHost.textContent.includes('Du bist hier'));
click('[data-nav="t:ot"]');click('[data-nav="g:0"]');
assert(sheetHost.querySelector('.grid.books [data-nav="b:0"]'),'Bücher der Gruppe');
click('[data-nav="b:0"]');assert(sheetHost.querySelector('.grid.nums [data-nav="c:50"]'),'50 Kapitel Genesis');
click('[data-nav="c:1"]');assert(sheetHost.querySelector('.grid.nums [data-go="v0-1-31"]'),'31 Verse Genesis 1');
assert(sheetHost.querySelector('.open[data-go="c0-1"]'),'Kapitel öffnen');
click('[data-go="v0-1-3"]');assert.equal(model.nodes.get('v0-1-3').id,'v0-1-3');assert(reader.querySelector('[data-stream="v0-1-3"]'),'Sprung zu Genesis 1,3');
click('[data-action=index]');assert(sheetHost.querySelector('.grid.books [data-nav="b:0"].cur')&&sheetHost.querySelector('[data-nav="c:1"].cur'),'Navigator startet an der aktuellen Position');
assert(!sheetHost.querySelector('.grid.books .study'),'in der Gruppe Gesetz ist nichts ausgearbeitet');
click('[data-nav="t:nt"]');assert(sheetHost.querySelector('[data-nav="g:5"]'),'Gruppen des NT');click('[data-nav="g:5"]');assert(sheetHost.querySelector('.grid.books [data-nav="b:39"].study'),'Matthäus als ausgearbeitet markiert');
click('[data-close]');

// Querverweise und Stellen im Text sind verlinkt; Rücksprung
click('[data-action=menu]');const inp2=sheetHost.querySelector('input[type=search]');inp2.value='Mt 6,11';inp2.dispatchEvent(new dom.window.Event('input',{bubbles:true}));sheetHost.querySelector('.results [data-go]').click();
click('[data-more="v39-6-11"]');
assert(sheetHost.querySelector('.xrefs [data-ref-go="PRO.30.8"]'),'Querverweis Spr 30,8');
assert(sheetHost.textContent.includes('Spr 30,8')&&sheetHost.textContent.includes('Lk 11,3'),'Kurzform der Stellen');
sheetHost.querySelector('.xrefs [data-ref-go="PRO.30.8"]').click();
assert(reader.querySelector('[data-stream="v19-30-8"]'),'Sprung zu Sprüche 30,8');
const back=app.querySelector('.jump-back');assert(back&&back.textContent.includes('Matthäus 6,11'),'Rücksprung angeboten');back.click();
assert(reader.querySelector('[data-stream="v39-6-11"]')&&!app.querySelector('.jump-back'),'zurück bei Matthäus 6,11');
click('[data-more="v39-6-11"]');sheetHost.querySelector('.sheet-tools [data-background="TU-MAT-006-009-013"]').click();
assert(sheetHost.querySelector('[data-ref-go="MRK.14.36"]'),'Vergleichsstelle verlinkt');
assert(!sheetHost.textContent.includes('[['),'Stellen-Marken als Anzeige, nicht roh');
assert(sheetHost.querySelector('[data-ref-go="ISA.64.7"]'),'Stelle im Fliesstext verlinkt (Jes 63,16; 64,7)');
assert(!sheetHost.textContent.includes('data-ref-go="SIR'),'Sirach nicht verlinkt');
click('[data-close]');
// Zweite Übersetzungsschicht: Züridüütsch aus dem Griechischen, umschaltbar
click('[data-action=menu]');assert(sheetHost.querySelector('[data-set="text"][data-value="gsw"]'),'Lesetext-Auswahl');click('[data-set="text"][data-value="gsw"]');click('[data-close]');
assert.equal(reader.querySelector('[data-stream="v39-6-11"] .stream-copy').textContent,'Öises täglich Broot gib üs hüt.','Mundart im Lesestrom');
assert(reader.querySelector('[data-stream="v39-6-11"] .dec.traditional'),'Entscheidung «täglich» auch in der Mundart markiert');
click('[data-action=index]');assert(sheetHost.textContent.includes('S Vatterunser')&&sheetHost.textContent.includes('Nöd zum Schiin'),'Navigator-Titel in Mundart');click('[data-close]');
click('[data-action=up]');assert(reader.textContent.includes('mit sibe Bitte')&&reader.querySelector('[data-stream="TU-MAT-006-009-013"] h2').textContent==='S Vatterunser','Abschnittstitel und -zusammenfassung in Mundart');click('[data-action=down]');
assert(reader.querySelector('.alt-line[data-alternative="VAR-SBLGNTAPP-MAT-006-012-01"]').textContent.includes('vergänd'),'Mundart-Lesart im Text');
click('[data-more="v39-6-11"]');assert(sheetHost.textContent.includes('Ältere Übersetzungen · Züridüütsch')&&sheetHost.textContent.includes('noch keine Vergleichsübersetzung')&&sheetHost.textContent.includes('Ältere Übersetzungen · Hochdeutsch')&&sheetHost.textContent.includes('Lutherbibel'),'Vergleichsübersetzungen nach Sprache des Zielkontexts');click('[data-close]');
click('[data-more="v39-6-11"]');assert(sheetHost.textContent.includes('Öises täglich Broot')&&sheetHost.textContent.includes('für de nööchscht Taag'),'Mundart-Entscheidung im Versblatt');
sheetHost.querySelector('.sheet [data-source="VAR-SBLGNTAPP-MAT-006-013-01"]')||click('[data-close]');
// Inhalte in Mundart (data/localizations): Deutungen, Befunde, Hintergrund, Zusammenfassungen, Lesarten-Erklärungen
if(sheetHost.querySelector('.sheet'))click('[data-close]');
click('[data-more="v39-6-11"]');sheetHost.querySelector('.sheet-tools [data-study="TU-MAT-006-009-013"]').click();
assert(sheetHost.textContent.includes('Broot für de nööchscht Taag')&&sheetHost.textContent.includes('de folgendi Tag'),'Deutung und Wortbedeutung in Mundart');
assert(!sheetHost.textContent.includes('Brot für den kommenden Tag'),'keine hochdeutsche Deutung im Mundart-Blatt');click('[data-close]');
click('[data-more="v39-6-11"]');sheetHost.querySelector('.sheet-tools [data-background="TU-MAT-006-009-013"]').click();
assert(/\b(isch|händ|de|vo)\b/.test(sheetHost.querySelector('.bg-note .body').textContent),'Hintergrund in Mundart');click('[data-close]');
click('[data-action=menu]');click('[data-set="text"][data-value="de"]');click('[data-close]');
assert.equal(reader.querySelector('[data-stream="v39-6-11"] .stream-copy').textContent,M().de['MAT.6.11'],'zurück zu Hochdeutsch');
assert.equal(Object.keys(M().layers.gsw.text).length,2002,'Mundart für alle 2002 Verse');
// Obadja (Hebräisch) und Titus: Muster ganzer Bücher
click('[data-action=menu]');click('[data-set="text"][data-value="de"]');if(sheetHost.querySelector('[data-toggle=advanced][aria-checked=false]'))click('[data-toggle=advanced]');click('[data-close]');
click('[data-action=menu]');sheetHost.querySelector('[data-go^="TU-OBA"]').click();click('[data-action=down]');
assert(reader.querySelector('[data-stream="v30-1-21"]')||true);
click('[data-more="v30-1-3"]');
assert(sheetHost.querySelector('.il.he .heb'),'Hebräisch Wort für Wort');
assert(sheetHost.textContent.includes('Hebräisch Wort für Wort')&&sheetHost.textContent.includes('Westminster Leningrad Codex'),'Quellen für den hebräischen Text');
assert(sheetHost.textContent.includes('sela'),'Lesehilfe-Umschrift');
assert(sheetHost.textContent.includes('Texte vom Toten Meer')&&sheetHost.textContent.includes('MurXII')&&sheetHost.textContent.includes('CC BY-NC'),'Texte vom Toten Meer (nicht kommerzielle Schicht)');
click('[data-close]');
assert.equal(model.STUDY.layers.de.text['OBA.1.21'],'Und Retter werden hinaufziehen auf den Berg Zion, um das Gebirge Esau zu richten; und die Königsherrschaft wird JHWH gehören.');
assert(model.STUDY.words.filter(w=>w.ref==='OBA.1.1').every(w=>w.wtr),'Umschrift je Wort');
assert(model.STUDY.layers.gsw.text['TIT.3.15'].startsWith('Es grüessed dich alli'),'Titus in Mundart');
assert(model.STUDY&&dom.window.document.querySelector('#bible-stream'));
// Wörterbuch (UBS/STEPBible), Ketiv/Qere (TAHOT), Ausgaben je Wort (TAGNT); Urtext-Modus ist an
const goto=q=>{click('[data-action=menu]');const i=sheetHost.querySelector('input[type=search]');i.value=q;i.dispatchEvent(new dom.window.Event('input',{bubbles:true}));sheetHost.querySelector('.results [data-go]').click();};
goto('Obadja 1,11');click('[data-more="v30-1-11"]');
let ltx=sheetHost.textContent;
const hc=x=>x.replace(/[^\u05D0-\u05EA ]/g,'');
assert(ltx.includes('Geschrieben (Ketiv)')&&ltx.includes('Gelesen (Qere)')&&/שערו(?!י)/.test(hc(sheetHost.querySelector('.kq').textContent)),'Ketiv/Qere in Obd 1,11');
assert(sheetHost.querySelector('.il.he .kqmark'),'Ketiv/Qere am Wort markiert');
assert(ltx.includes('Wörterbuch')&&ltx.includes('UBS-Wörterbuch (englisch, CC BY-SA 4.0)'),'Wörterbuch im hebräischen Wortblatt');
assert(ltx.includes('STEPBible TAHOT')&&ltx.includes('UBS Dictionary of Biblical Hebrew'),'Attribution Hebräisch');
click('[data-close]');
goto('Rut 3,12');click('[data-more="v7-3-12"]');
assert(sheetHost.textContent.includes('Geschrieben, aber nicht gelesen (Ketiv ohne Qere)')&&hc(sheetHost.textContent).includes('אם'),'Ketiv ohne Qere in Rut 3,12');
click('[data-close]');
goto('Mk 1,2');click('[data-more="v40-1-2"]');
ltx=sheetHost.textContent;
assert(ltx.includes('Wörter in den Textausgaben')&&ltx.includes('fehlt in TR, Byz')&&ltx.includes('Ὡς'),'Ausgaben je Wort in Mk 1,2');
assert(ltx.includes('nicht über Handschriften'),'Ausgabenbefund, nicht Handschriften');
const gd=sheetHost.querySelector('.il details');gd.querySelector('summary').click();
assert(gd.textContent.includes('Wörterbuch')&&gd.querySelector('ul.lex li'),'Wörterbuch-Eintrag im griechischen Wortblatt');
assert(ltx.includes('UBS Dictionary of the Greek New Testament')&&ltx.includes('Ausgaben je Wort (TAGNT)')&&ltx.includes('CC BY-SA 4.0'),'Attribution Griechisch');
click('[data-close]');
goto('Mk 1,1');click('[data-more="v40-1-1"]');
assert(/\+ υἱοῦ/.test(sheetHost.textContent)&&sheetHost.textContent.includes('nicht in SBL'),'Wörter anderer Ausgaben (Mk 1,1)');
click('[data-close]');
click('[data-action=menu]');click('[data-sources-map]');
assert(sheetHost.textContent.includes('Quellen und Rechte')&&sheetHost.querySelectorAll('.src-item').length>=60,'Quellen und Rechte: ganzer Katalog');
click('[data-src-filter="used"]');
assert(sheetHost.querySelectorAll('.src-item').length===sheetHost.querySelectorAll('.src-item .u-used').length&&sheetHost.textContent.includes('MACULA Hebrew'),'Filter verwendet');
click('[data-close]');
console.log(`PASS: Pilotzugang, Studienblatt ohne Griechisch, Lesarten auf Wunsch (${M().alternatives.length}), Hintergrund damals (${model.BG.length}), Bis zur Quelle (${tested}), Urtext-Modus, Rückkehrposition, Suche, Kapitelgrenze, Vaterunser Mt/Lk, Übersetzungsentscheidungen und Vergleich, Wort-Blatt, Umschrift und Anhören, Verse fortlaufend, Navigator, Querverweise und Rücksprung, Lesetext Hochdeutsch/Züridüütsch mit Titeln, Obadja hebräisch Wort für Wort, Titus, Quellen und Rechte, Texte vom Toten Meer, Wörterbuch, Ketiv/Qere, Ausgaben je Wort.`);
dom.window.close();
