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
