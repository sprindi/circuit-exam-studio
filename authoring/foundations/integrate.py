from pathlib import Path
import re,json,shutil,hashlib,sys
root=Path(__file__).resolve().parent
live=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else root.parents[1]/'dist'
assert (live/'index.html').exists(), 'Pass the existing website dist directory as the first argument.'
p=live/'chapter-one.js';s=p.read_text()
fixture=root/'exercise-function.sha256'
practice=s[s.index('function drawPractice()'):s.index('\nwindow.ChapterOne=')]
if not fixture.exists():fixture.write_text(hashlib.sha256(practice.encode()).hexdigest())
assert fixture.read_text()==hashlib.sha256(practice.encode()).hexdigest(),'Exercise function changed'
if 'id="c1-teaching-root"' not in s:
 s=s.replace('function stop(){audioToken++;','function stop(){window.CircuitFoundation?.stop();audioToken++;')
 old='<div id="c1-case-list" class="c1-case-list" role="tablist" aria-label="Cases in this topic"></div><div id="c1-workspace"></div>'
 new='${window.CircuitFoundation?.supports(t.id)?\'<div id="c1-teaching-root"></div>\':\'<div id="c1-case-list" class="c1-case-list" role="tablist" aria-label="Cases in this topic"></div><div id="c1-workspace"></div>\'}'
 assert old in s;s=s.replace(old,new)
 s=s.replace("!$('#c1-workspace')","(!$('#c1-workspace')&&!$('#c1-teaching-root'))")
 s=s.replace('active.p.seen[active.d.cases[active.p.case].id]=true;save();',"if(!$('#c1-teaching-root')){active.p.seen[active.d.cases[active.p.case].id]=true;save();}")
 s=s.replace('save();drawPractice();if(active.p.practiceOpen)', 'save();drawPractice();window.CircuitFoundation?.setPracticeOpen(active.p.practiceOpen);if(active.p.practiceOpen)')
 s=s.replace('};draw();drawPractice();}',"};if($('#c1-teaching-root')){window.CircuitFoundation.mount($('#c1-teaching-root'),id,()=>{if(!active.p.practiceOpen)$('#c1-practise').click();else $('#c1-practice-panel').scrollIntoView({block:'start'});});window.CircuitFoundation.setPracticeOpen(active.p.practiceOpen);}else draw();drawPractice();}")
 s=s.replace('The short cases above are guided study aids.','The explanations above are guided study aids.')
 a=s.index('function overview()');b=s.index('\nfunction page(',a)
 s=s[:a]+'''function overview(){return `<section class="c1"><div class="c1-breadcrumb"><a href="#chapters">← All chapters</a><span>CHAPTER 01</span></div><div class="c1-overview-head"><span class="c1-eyebrow">BASIC CONCEPTS & LAWS</span><h1>Understand the circuit.<br>Then choose the rule.</h1><p>Start with what charge and energy do. Learn to label a circuit, then use its laws to find an unknown.</p></div><section class="cf-roadmap"><div><span class="c1-eyebrow">YOUR ROUTE THROUGH THE CHAPTER</span><h2>From a physical idea to a useful calculation.</h2><ol><li><b>Build the meaning · 1.1–1.3</b><span>Source, load, current, voltage, EMF and connection conditions.</span></li><li><b>Choose and read references · 1.4–1.5</b><span>Signs, potential, element behavior and absorbed or supplied power.</span></li><li><b>Find a simpler route to the unknown · 1.6–1.10</b><span>Transform sources, identify topology, apply circuit laws and use equivalent circuits.</span></li></ol></div><aside><h3>Before you begin</h3><p>You need basic algebra and unit conversions. New quantities are explained where you meet them.</p><h3>What success looks like</h3><p>You can explain a symbol, state when a rule applies, read its diagram and check whether the result makes physical sense.</p><a href="#topic/1.1">Start with the foundations →</a></aside></section><div class="c1-overview-grid">${topics().map(t=>`<a class="c1-topic-card" href="#topic/${t.id}"><span class="c1-topic-id">${t.id}</span><h2>${data[t.id].title}</h2><p>${data[t.id].goal}</p><span class="c1-card-footer">${['1.1','1.2','1.3'].includes(t.id)?'New guided foundation':data[t.id].cases.length+' existing cases'} <span>Open topic ↗</span></span></a>`).join('')}</div><p class="c1-source-note">All 10 taught topics and complete teacher references remain available. The new teaching experience currently covers 1.1–1.3; the remaining topics retain their existing explanations. Reviewed marks and reflection checks record your actions, not proof of mastery.</p></section>`;}''' +s[b:]
 p.write_text(s)
# Keep video help attached to old-reader topics without changing practice code.
p=live/'chapter-one.js';s=p.read_text()
marker='${window.CircuitFoundation?.supports(t.id)?'
if "CircuitVideos?.renderTopic(t.id)" not in s:
 s=s.replace(marker,"${window.CircuitFoundation?.supports(t.id)?'':window.CircuitVideos?.renderTopic(t.id)||''}"+marker)
if 'a[data-circuit-video]' not in s:
 s=s.replace("window.ChapterOne={page,overview,mount,stop};", "window.ChapterOne={page,overview,mount,stop};document.addEventListener('click',e=>{if(e.target.closest('a[data-circuit-video]'))stop();});")
p.write_text(s)
# Local video lifecycle: pause on navigation and bind old-reader players.
p=live/'chapter-one.js';s=p.read_text()
s=s.replace('function stop(){window.CircuitFoundation?.stop();','function stop(){window.CircuitVideos?.stop();window.CircuitFoundation?.stop();')
s=s.replace('else draw();drawPractice();}',"else draw();drawPractice();window.CircuitVideos?.mount($('#c1-page'));}")
p.write_text(s)
p=live/'app.js';s=p.read_text();s=s.replace('window.ChapterOne?.stop();document.documentElement','window.ChapterOne?.stop();window.CircuitFoundation?.unmount();document.documentElement');s=s.replace('window.CircuitFoundation?.unmount();document.documentElement','window.CircuitFoundation?.unmount();window.CircuitVideos?.unmount();document.documentElement');p.write_text(s)
p=live/'chapter-one-figures.js';s=p.read_text();s=s.replace("cap:phase?'b':'a',bottom:phase?'a':'b'","cap:'a',bottom:'b'");p.write_text(s)
# Canonical video-first lesson shell; retain the original optional teaching and practice implementation.
p=live/'chapter-one.js';s=p.read_text()
a=s.index('function page(');b=s.index('\nfunction mount(',a);s=s[:a]+(root/'chapter-one-page.txt').read_text().rstrip()+s[b:]
a=s.index('function mount(');b=s.index('\nfunction draw()',a);s=s[:a]+(root/'chapter-one-mount.txt').read_text().rstrip()+s[b:]
s=s.replace('function overview(){return',"function overview(){const finished=new Set(window.CircuitStore?.get('app')?.reviewed||[]);return")
s=s.replace('New guided foundation', 'Video + cheat sheet')
s=s.replace("${['1.1','1.2','1.3'].includes(t.id)?'Video + cheat sheet':data[t.id].cases.length+' existing cases'}","${window.CircuitVideos?.count(t.id)||0} full video${window.CircuitVideos?.count(t.id)===1?'':'s'} + cheat sheets")
s=s.replace('<span class="c1-topic-id">${t.id}</span>', '<div class="c1-topic-card-top"><span class="c1-topic-id">${t.id}</span><span class="c1-completion ${finished.has(t.id)?\'is-finished\':\'\'}">${finished.has(t.id)?\'✓ Finished\':\'Not marked finished\'}</span></div>')
s=s.replace('<h1>Understand the circuit.<br>Then choose the rule.</h1>','<h1>Watch. Keep the rules.<br>Then practise.</h1><p class="c1-chapter-completion">${topics().filter(t=>finished.has(t.id)).length} of 10 lessons marked finished</p>')
s=s.replace('All 10 taught topics and complete teacher references remain available. The new teaching experience currently covers 1.1–1.3; the remaining topics retain their existing explanations. Reviewed marks and reflection checks record your actions, not proof of mastery.','Each full video belongs to one lesson. Its cheat sheet sits directly below it; exercises open separately. All original teaching and teacher references remain available. Completion is your own mark, separate from watching progress and exercise scores.')
p.write_text(s)
p=live/'app.js';s=p.read_text()
if 'C1_PRACTICE_RETURN_START' not in s:
 s=s.replace("function bindStudyState(){\n const main=$('#main');","function bindStudyState(){\n const main=$('#main');"+(root/'practice-return.txt').read_text().strip())
p.write_text(s)
assets=[]
for source in (root/'build').iterdir():
 if source.suffix in ['.js','.css']:
  path=live/'foundation'/source.name;path.parent.mkdir(exist_ok=True);shutil.copy2(source,path);assets.append(path.relative_to(live).as_posix())
for source in (root/'audio').glob('*.mp3'):
 path=live/'foundation/audio'/source.name;path.parent.mkdir(exist_ok=True);shutil.copy2(source,path);assets.append(path.relative_to(live).as_posix())
assert len(assets)>=22,'Build audio first'
for old in (live/'foundation').glob('lesson-*'):
 if old.relative_to(live).as_posix() not in assets:old.unlink()
for video in json.loads((root/'src/video-catalog.json').read_text())['videos'].values():
 assert (live/video['local']).is_file(), 'Missing downloaded video: '+video['local']
 assert (live/video['poster']).is_file(), 'Missing local poster: '+video['poster']
p=live/'index.html';s=p.read_text();s=re.sub(r'<link rel="stylesheet" href="foundation/[^"]+">','',s);s=re.sub(r'<script src="foundation/[^"]+"></script>','',s)
s=s.replace('</head>','<link rel="stylesheet" href="'+next(x for x in assets if x.endswith('.css'))+'"></head>')
s=s.replace('<script src="chapter-one.js">','<script src="'+next(x for x in assets if x.endswith('.js'))+'"></script><script src="chapter-one.js">');p.write_text(s)
p=live/'sw.js';s=p.read_text();s=re.sub(r"const CACHE='[^']+';","const CACHE='circuit-studio-foundations-"+hashlib.sha256(''.join(assets).encode()).hexdigest()[:10]+"';",s)
a=s.index('const FILES=');b=s.index(';',a)
# Existing list is JS strings with both quote styles, but no escaping or computed members.
files=re.findall(r'''["']([^"']+)["']''',s[a:b]);files=list(dict.fromkeys([x for x in files if not x.startswith('foundation/')]+assets))
for name in files:assert (live/name).exists(),name
s=s[:a]+'const FILES='+json.dumps(files)+s[b:]
s=s.replace("if(event.request.method!=='GET'||","if(new URL(event.request.url).pathname.includes('/videos/')||event.request.method!=='GET'||") if "pathname.includes('/videos/')" not in s else s
p.write_text(s)
print('Integrated',len(assets),'foundation assets. Existing exercise function unchanged.')
