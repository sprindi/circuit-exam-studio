from pathlib import Path
import re,json,shutil,hashlib,sys
author=Path(__file__).resolve().parent
live=Path(sys.argv[1]).resolve()
assert (live/'index.html').exists(), 'Pass the existing website dist directory.'
p=live/'app.js';s=p.read_text()
s=s.replace("(route==='topic'&&(topic(id)||topics[0]).chapter===1)||(route==='chapter'&&Number(id)===1)","(route==='topic')||(route==='chapter'&&[1,2,3].includes(Number(id)))")
s=s.replace("}else main.innerHTML=library(id);$('#review-topic')", "}else if(window.CourseLessons?.supports(selected.id)){state.lastTopic=selected.id;save();main.innerHTML=window.CourseLessons.page(selected,state.reviewed.includes(selected.id));}else main.innerHTML=library(id);$('#review-topic')")
s=s.replace("window.ChapterOne.overview():chapterPage(id)","window.ChapterOne.overview():window.CourseLessons?.overview(Number(id))||chapterPage(id)")
s=s.replace("if(document.documentElement.classList.contains('chapter-one-reading')){window.ChapterOne.mount", "if(document.querySelector('#course-lesson')){window.CourseLessons.mount();window.CircuitGuided?.mount();}else if(document.documentElement.classList.contains('chapter-one-reading')){window.ChapterOne.mount")
s=s.replace("/^#practice\\/topic\\/(1\\.(?:10|[1-9]))$/", "/^#practice\\/topic\\/([123]\\.(?:10|[1-9]))$/")
p.write_text(s)
p=live/'guided.js';s=p.read_text();s=s.replace("$('.article').before(host);draw();", "const slot=$('#course-guided-slot');if(slot)slot.append(host);else $('.article').before(host);draw();");p.write_text(s)
assets=[]
for p in (author/'build').iterdir():
 if p.suffix in ['.js','.css']:
  shutil.copy2(p,live/'foundation'/p.name);assets.append('foundation/'+p.name)
for p in (live/'foundation/audio').glob('*.mp3'):assets.append(p.relative_to(live).as_posix())
p=live/'index.html';s=p.read_text();s=re.sub(r'foundation/lesson-[^"\s]+\.css',next(x for x in assets if x.endswith('.css')),s);s=re.sub(r'foundation/lesson-[^"\s]+\.js',next(x for x in assets if x.endswith('.js')),s);p.write_text(s)
p=live/'sw.js';s=p.read_text();a=s.index('const FILES=')+12;b=s.index(';',a);files=json.loads(s[a:b]);files=[x for x in files if not x.startswith('foundation/')]+assets;s=s[:a]+json.dumps(files)+s[b:];s=re.sub(r"const CACHE='[^']+';","const CACHE='circuit-studio-course-"+hashlib.sha256((live/'app.js').read_bytes()+''.join(assets).encode()).hexdigest()[:12]+"';",s);p.write_text(s)
# Keep prior content-hashed files temporarily: existing open pages can still request them.
print('Installed shared lesson bundle, updated offline cache; Chapter 1 source and exercises untouched.')
