// Structural tests for the standalone prototype. Run with Node.js >= 18.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const html = fs.readFileSync(path.join(__dirname, '../app/reading-stream/index.html'), 'utf8');
let model;
const sandbox = {
  document: { getElementById: () => ({ querySelectorAll: () => [] }) },
  __BIBLE_TEST__: result => { model = result; },
};
for (const match of html.matchAll(/<script>([\s\S]*?)<\/script>/g)) vm.runInNewContext(match[1], sandbox);
assert(model);
assert.deepEqual(Array.from(model.streams, entries => entries.length), [1, 2, 10, 66, 1189, 6471, 31102]);
assert.equal(model.BOOK_SUMMARIES.length, 66);
for (const n of model.nodes.values()) {
  if (n.level < 6) assert(n.children.length > 0, n.id);
  for (const id of n.children) assert.equal(model.nodes.get(id).parent, n.id);
  if (n.level === 6) assert.match(n.canonicalRef, /^[A-Z0-9]{3}\.\d+\.\d+$/);
}
for (const [query, ref] of [['Mk 3,24', 'MRK.3.24'], ['Ps 119,176', 'PSA.119.176'], ['Offb 22,21', 'REV.22.21'], ['1. Mose 1,1', 'GEN.1.1']]) {
  assert.equal(model.search(query)[0]?.canonicalRef, ref, query);
}
assert.equal(model.search('Markus 99,1').length, 0);
assert.equal(model.sibling('v0-1-31', 1), 'v0-2-1');
assert.equal(model.sibling('v65-22-21', 1), null);
assert.equal(model.sibling('v0-1-1', -1), null);
assert(!html.includes('globalThis.lucide'));
assert(!/src=["']https?:/.test(html));
assert(html.includes('ill-p-jesus')&&html.includes('ILL-SYM-JHN-002-001-012'),'Bildsprache: Bibliothek und Bilder eingebettet');
assert(['ILL-SYM-BIBLE','ILL-SYM-OT','ILL-SYM-NT','ILL-SYM-GROUP-01','ILL-SYM-GROUP-10','ILL-SYM-JHN'].every(id=>html.includes(id))&&html.includes('ill-gott')&&html.includes('ILL-ANI-JHN-002-001-012')&&html.includes('ILL-ANI-JHN-002-013-022')&&html.includes('ILL-ANI-JHN-002-023-025')&&html.includes('ILL-ANI-BIBLE')&&html.includes('ILL-ANI-GROUP-10')&&html.includes('an-gott')&&html.includes('an-p-jesus'),'Bildsprache auf allen Ebenen (inkl. Anime-Pilot) über den Versen (Bibel, Testamente, Buchgruppen, Buch)');
console.log('PASS: complete streams, summaries, parent links, canonical refs, search, boundaries, standalone dependencies.');

const S = model.STUDY;
assert.equal(S.sections.map(x => x.id).join(), 'TU-RUT-001-001-022,TU-RUT-002-001-023,TU-RUT-003-001-018,TU-RUT-004-001-022,TU-OBA-001-001-021,TU-JON-001-001-017,TU-JON-002-001-010,TU-JON-003-001-010,TU-JON-004-001-011,TU-MAT-001-001-025,TU-MAT-002-001-023,TU-MAT-003-001-017,TU-MAT-004-001-025,TU-MAT-005-001-048,TU-MAT-006-001-034,TU-MAT-007-001-029,TU-MAT-008-001-034,TU-MAT-009-001-038,TU-MAT-010-001-042,TU-MAT-011-001-030,TU-MAT-012-001-050,TU-MAT-013-001-058,TU-MAT-014-001-036,TU-MAT-015-001-039,TU-MAT-016-001-028,TU-MAT-017-001-027,TU-MAT-018-001-035,TU-MAT-019-001-030,TU-MAT-020-001-034,TU-MAT-021-001-046,TU-MAT-022-001-046,TU-MAT-023-001-039,TU-MAT-024-001-051,TU-MAT-025-001-046,TU-MAT-026-001-075,TU-MAT-027-001-066,TU-MAT-028-001-020,TU-MRK-001-001-045,TU-MRK-002-001-028,TU-MRK-003-001-019,TU-MRK-003-020-035,TU-MRK-004-001-041,TU-MRK-005-001-043,TU-MRK-006-001-056,TU-MRK-007-001-037,TU-MRK-008-001-038,TU-MRK-009-001-050,TU-MRK-010-001-052,TU-MRK-011-001-033,TU-MRK-012-001-044,TU-MRK-013-001-037,TU-MRK-014-001-072,TU-MRK-015-001-047,TU-MRK-016-001-020,TU-LUK-011-001-004,TU-JHN-001-001-051,TU-JHN-002-001-025,TU-JHN-003-001-036,TU-JHN-004-001-054,TU-JHN-005-001-047,TU-JHN-006-001-071,TU-JHN-007-001-053,TU-JHN-008-001-059,TU-JHN-009-001-041,TU-JHN-010-001-042,TU-JHN-011-001-057,TU-JHN-012-001-050,TU-JHN-013-001-038,TU-JHN-014-001-031,TU-JHN-015-001-027,TU-JHN-016-001-033,TU-JHN-017-001-026,TU-JHN-018-001-040,TU-JHN-019-001-042,TU-JHN-020-001-031,TU-JHN-021-001-025,TU-PHP-001-001-030,TU-PHP-002-001-030,TU-PHP-003-001-021,TU-PHP-004-001-023,TU-TIT-001-001-016,TU-TIT-002-001-015,TU-TIT-003-001-015,TU-1JN-001-001-010,TU-1JN-002-001-029,TU-1JN-003-001-024,TU-1JN-004-001-021,TU-1JN-005-001-021,TU-2JN-001-001-013,TU-3JN-001-001-014');
assert.equal(S.words.filter(w => w.ref.startsWith('OBA.') && w.lang === 'he').length, 435, 'Obadja: Morphem-Tokens');
assert.equal(S.words.filter(w => w.ref.startsWith('TIT.')).length, 659, 'Titus: Wörter');
assert.equal(Object.keys(S.de).filter(r => r.startsWith('TIT.') || r.startsWith('OBA.')).length, 67, 'Titus und Obadja übersetzt');
assert.equal(S.words.filter(w => w.ref.startsWith('RUT.') && w.lang === 'he').length, 2026, 'Rut: Morphem-Tokens');
assert.equal(S.words.filter(w => w.ref.startsWith('PHP.')).length, 1626, 'Philipper: Wörter');
assert.equal(Object.keys(S.de).filter(r => r.startsWith('RUT.') || r.startsWith('PHP.')).length, 189, 'Rut und Philipper übersetzt');
assert.equal(S.de['PHP.4.13'], 'Alles vermag ich durch den, der mich stark macht.');
assert(S.de['RUT.1.16'].includes('dein Gott ist mein Gott'));
assert.equal(S.alternatives.filter(a => a.ref.startsWith('MRK.3.')).length, 9);
assert.equal(S.words.filter(w => w.ref.startsWith('MRK.3.')).length, 535);
assert.equal(S.variants.filter(v => v.ref.startsWith('MRK.3.')).length, 55);
for (const [code, b, c, n] of [['MRK', 40, 3, 35], ['MAT', 39, 6, 34], ['LUK', 41, 11, 54], ['TIT', 55, 1, 16], ['TIT', 55, 2, 15], ['TIT', 55, 3, 15], ['OBA', 30, 1, 21], ['RUT', 7, 1, 22], ['RUT', 7, 4, 22], ['PHP', 49, 2, 30], ['PHP', 49, 4, 23]]) {
  const chapter = model.nodes.get(`c${b}-${c}`);
  assert.deepEqual(Array.from(chapter.children).flatMap(id => Array.from(model.nodes.get(id).children)), Array.from({length:n}, (_,i)=>`v${b}-${c}-${i+1}`), code);
}
for (const sec of S.sections) for (const part of sec.parts) {
  const node = model.nodes.get(part.id);
  assert(node, part.id);
  assert.equal(node.part.summary, part.summary);
  // Verse ohne Wörter im Grundtext (z. B. Mk 7,16 fehlt im SBLGNT) haben keine Übersetzung
  for (const v of node.children) { const r = model.nodes.get(v).canonicalRef; if (S.words.some(w => w.ref === r)) assert(S.de[r], v + ' ohne Übersetzung'); }
}
assert.equal(model.nodes.get('v40-3-29').parent, 'TU-MRK-003-022-030');
assert.equal(model.nodes.get('v39-6-11').parent, 'TU-MAT-006-009-013');
assert.equal(model.nodes.get('v41-11-3').parent, 'TU-LUK-011-001-004');
assert.equal(model.sibling('v40-3-35',1), 'v40-4-1');
assert.equal(model.sibling('TU-MRK-003-020-021',1), 'TU-MRK-003-022-030');
assert.equal(model.sibling('TU-MAT-006-009-013',1), 'TU-MAT-006-014-015');
for (const [g, l] of [['πονηροῦ', 'ponēroú'], ['Πάτερ ἡμῶν ὁ ἐν τοῖς οὐρανοῖς', 'Páter hēmṓn ho en toís ouranoís'], ['ῥῦσαι', 'rhýsai'], ['ἀγγέλους', 'angélous'], ['υἱοῖς', 'huioís'], ['Ἰησοῦς', 'Iēsoús']]) assert.equal(model.translit(g), l, g);
assert.equal(model.translit('Vater'), '');
// Wörterbuch (UBS, STEPBible), Ausgaben je Wort (TAGNT), Ketiv/Qere (TAHOT) – nur in den Buchpaketen
const kathos = S.words.find(w => w.id === 'TOK-SBLGNT-MRK-001-002-001');
assert(kathos.lx && S.lexicon[kathos.lx.u] && S.lexicon[kathos.lx.u].src === 'ubs-grc' && S.lexicon[kathos.lx.u].s.length, 'UBS-Eintrag zu καθώς');
assert.equal(JSON.stringify(kathos.ed.alt.map(a => [a.grc, a.eds])), '[["Ὡς",["TR","Byz"]]]', 'TR/Byz lesen Ὡς');
assert.equal(Array.from(kathos.ed.eds).join(), 'NA28,NA27,Tyn,SBL,WH,Treg');
const grc = S.words.filter(w => w.lang !== 'he');
assert(grc.filter(w => w.lx).length / grc.length > 0.99, 'fast jedes griechische Wort hat einen Wörterbuch-Eintrag');
assert(S.ed_extra['MRK.1.1'].some(x => x.grc === 'υἱοῦ' && !x.eds.includes('SBL')), 'υἱοῦ θεοῦ (Mk 1,1) fehlt im SBLGNT');
const cons = x => x.replace(/[^\u05D0-\u05EA]/g, '');
assert.equal(cons(S.ketiv['TOK-WLC-OBA-001-011-016'].ketiv), 'שערו', 'Ketiv Obd 1,11 (Qere שעריו)');
assert.equal(cons(S.ketiv['TOK-WLC-OBA-001-011-016'].qere), 'שעריו');
assert.equal(cons(S.ketiv_only['RUT.3.12'][0].ketiv), 'אם', 'Ketiv ohne Qere Rut 3,12');
assert(S.words.filter(w => w.lang === 'he' && w.lx && w.lx.u).length > 2000, 'hebräische Wörter mit UBS-Eintrag');
for (const w of S.words) for (const k of Object.values(w.lx || {})) if (typeof k === 'string') assert(S.lexicon[k], 'Wörterbuch-Schlüssel ' + k);
console.log(`PASS: study projection (${S.sections.length} worked passages, ${Object.keys(S.de).length} translated verses, ${S.alternatives.length} alternatives, ${S.words.length} words, ${S.variants.length} variants), real sections, continuous coverage, transliteration.`);
