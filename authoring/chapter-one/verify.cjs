const fs=require('fs'),vm=require('vm'),assert=require('assert'),path=require('path');
const root='/home/soufiane/Documents/Codex/2026-11-11/ope/work/circuit-exam-studio/dist';
const box={window:{addEventListener(){}},document:{addEventListener(){}}};vm.createContext(box);
for(const f of ['content.js','chapter-one-data.js','chapter-one-figures.js','chapter-one.js'])vm.runInContext(fs.readFileSync(path.join(root,f),'utf8'),box);
const w=box.window;let count=0,audios=0;
for(const t of w.COURSE_TOPICS.filter(t=>t.chapter===1)){
 const d=w.CHAPTER_ONE[t.id];assert(d);assert(w.ChapterOne.page(t,false).includes(t.html));
 for(const c of d.cases){assert(c.symbols?.length>0);for(const pair of c.symbols){assert.equal(pair.length,2);assert(pair.every(x=>typeof x==='string'&&x.length));}count++;assert.equal(c.steps.length,3);
  for(let i=0;i<3;i++){const svg=w.ChapterOneFigure.render(c.figure,i);assert(svg.includes('<svg')||svg.includes('<img'));assert(!/undefined|NaN/.test(svg));const a=path.join(root,c.steps[i].audio);assert(fs.statSync(a).size>1000);audios++;}
 }
}
assert.equal(count,43);assert.equal(audios,129);
const sw=fs.readFileSync(path.join(root,'sw.js'),'utf8');
const files=vm.runInNewContext(sw.match(/const FILES\s*=\s*(\[[\s\S]*?\]);/)[1]);
for(const f of files){if(f==='./'||f==='/')continue;assert(fs.existsSync(path.join(root,f.replace(/^\.\//,''))),f);}
console.log('PASS: all 10 topics retain complete reference, 43 cases render at all 129 steps, audio assets and offline cache files exist.');
