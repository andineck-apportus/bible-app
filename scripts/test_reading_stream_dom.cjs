// Optional interaction checks: npm install --no-save jsdom, then run with Node.
const {JSDOM}=require('jsdom'),fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
let model;const dom=new JSDOM(fs.readFileSync(path.join(__dirname,'../app/reading-stream/index.html'),'utf8'),{runScripts:'dangerously',pretendToBeVisual:true,beforeParse(w){w.__BIBLE_TEST__=x=>model=x;}});
for(const app of dom.window.document.querySelectorAll('.app')){
 const reader=app.querySelector('.reader');
 const click=s=>{const el=app.querySelector(s);assert(el,s);el.click();};
 click('[data-action=menu]');click('[data-go="TU-MRK-003-020-021"]');
 assert(reader.querySelector('[data-stream="TU-MRK-003-031-035"]'));
 assert(reader.textContent.includes(model.MARKUS.interpretations[2].counter[0]));
 reader.scrollTop=137;click('[data-deep="TU-MRK-003-022-030"]');
 const verse=reader.querySelector('[data-stream="v40-3-29"]');
 assert.equal(verse.querySelector('.stream-copy').textContent,model.MARKUS.de[29]);
 assert(verse.querySelector('[data-alternative]'));
 const details=verse.querySelector('details');details.querySelector('summary').click();assert(details.open);
 assert(verse.textContent.includes('Keine Handschriftenzählung'));
 assert(verse.textContent.includes('MorphGNT'));
 click('[data-action=up]');assert.equal(reader.scrollTop,137);
 click('[data-action=menu]');const input=reader.querySelector('input');input.value='Mk 3,20';input.dispatchEvent(new dom.window.Event('input',{bubbles:true}));click('.results [data-go]');
 click('[data-action=load-next]');
 for(let v=20;v<=35;v++)assert.equal(reader.querySelector(`[data-stream="v40-3-${v}"] .stream-copy`).textContent,model.MARKUS.de[v]);
 assert(reader.querySelector('[data-stream="v40-4-1"]'));
 assert.equal(reader.querySelectorAll('[data-alternative]').length,6);
}
console.log('PASS: both devices, pilot entry, source text, alternatives, word details, source caveats, disclosure interaction, return position, continuous chapter boundary.');dom.window.close();
