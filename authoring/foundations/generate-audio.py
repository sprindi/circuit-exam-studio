import json,hashlib,concurrent.futures,time
from pathlib import Path
from gtts import gTTS
root=Path(__file__).parent
p=root/'src/lessons.json';data=json.loads(p.read_text())
out=root/'audio';out.mkdir(exist_ok=True)
jobs=[]
for lesson in data.values():
 for s in lesson['scenes']:
  for item in [s,*s.get('phases',[])]:
   text=item['voice'];name='f-'+hashlib.sha256(text.encode()).hexdigest()[:16]+'.mp3';item['audio']='foundation/audio/'+name;jobs.append((text,out/name))
def run(job):
 text,path=job
 if path.exists() and path.stat().st_size>500:return
 for attempt in range(3):
  try:gTTS(text,lang='en',timeout=25).save(str(path));return
  except Exception:
   if attempt==2:raise
   time.sleep(1)
with concurrent.futures.ThreadPoolExecutor(max_workers=4)as pool:
 for i,_ in enumerate(pool.map(run,jobs),1):print(i,'/',len(jobs),'recordings ready',flush=True)
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
