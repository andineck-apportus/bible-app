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
assert.deepEqual(Array.from(model.streams, entries => entries.length), [1, 2, 10, 66, 1189, 6705, 31102]);
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
console.log('PASS: complete streams, summaries, parent links, canonical refs, search, boundaries, standalone dependencies.');

const S = model.STUDY;
assert.equal(S.sections.map(x => x.id).join(), 'TU-MAT-006-005-015,TU-MRK-003-020-035,TU-LUK-011-001-004');
assert.equal(S.alternatives.filter(a => a.ref.startsWith('MRK.3.')).length, 6);
assert.equal(S.words.filter(w => w.ref.startsWith('MRK.3.')).length, 249);
assert.equal(S.variants.filter(v => v.ref.startsWith('MRK.3.')).length, 28);
for (const [code, b, c, n] of [['MRK', 40, 3, 35], ['MAT', 39, 6, 34], ['LUK', 41, 11, 54]]) {
  const chapter = model.nodes.get(`c${b}-${c}`);
  assert.deepEqual(Array.from(chapter.children).flatMap(id => Array.from(model.nodes.get(id).children)), Array.from({length:n}, (_,i)=>`v${b}-${c}-${i+1}`), code);
}
for (const sec of S.sections) for (const part of sec.parts) {
  const node = model.nodes.get(part.id);
  assert(node, part.id);
  assert.equal(node.part.summary, part.summary);
  for (const v of node.children) assert(S.de[model.nodes.get(v).canonicalRef], v + ' ohne Übersetzung');
}
assert.equal(model.nodes.get('v40-3-29').parent, 'TU-MRK-003-022-030');
assert.equal(model.nodes.get('v39-6-11').parent, 'TU-MAT-006-009-013');
assert.equal(model.nodes.get('v41-11-3').parent, 'TU-LUK-011-001-004');
assert.equal(model.sibling('v40-3-35',1), 'v40-4-1');
assert.equal(model.sibling('TU-MRK-003-020-021',1), 'TU-MRK-003-022-030');
assert.equal(model.sibling('TU-MAT-006-009-013',1), 'TU-MAT-006-014-015');
console.log(`PASS: study projection (${S.sections.length} worked passages, ${Object.keys(S.de).length} translated verses, ${S.alternatives.length} alternatives, ${S.words.length} words, ${S.variants.length} variants), real sections, continuous coverage.`);
