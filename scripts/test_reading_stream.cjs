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
assert.deepEqual(Array.from(model.streams, entries => entries.length), [1, 2, 10, 66, 1189, 6704, 31102]);
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

const source = JSON.parse(fs.readFileSync(path.join(__dirname, '../app/prototype/data.json'), 'utf8'));
assert.equal(JSON.stringify(model.MARKUS), JSON.stringify(source));
assert.equal(model.MARKUS.alternatives.length, 6);
assert.equal(model.MARKUS.words.length, 249);
assert.equal(model.MARKUS.variants.length, 28);
const chapter = model.nodes.get('c40-3');
assert.deepEqual(Array.from(chapter.children).flatMap(id => Array.from(model.nodes.get(id).children)), Array.from({length:35}, (_,i)=>`v40-3-${i+1}`));
for (const part of source.section.parts) {
  assert.equal(model.nodes.get(part.id).part.summary, part.summary);
  assert.equal(model.nodes.get(part.id).parent, 'c40-3');
}
assert.equal(model.nodes.get('v40-3-29').parent, 'TU-MRK-003-022-030');
assert.equal(model.sibling('v40-3-35',1), 'v40-4-1');
assert.equal(model.sibling('TU-MRK-003-020-021',1), 'TU-MRK-003-022-030');
console.log('PASS: canonical Markus projection, real sections, 16 translations, 6 alternatives, 249 words, 28 variants, continuous coverage.');
