import json,concurrent.futures,time
from pathlib import Path
from gtts import gTTS
r=Path('/home/soufiane/Documents/Codex/2026-11-11/ope/work/circuit-exam-studio/dist');(r/'audio').mkdir(exist_ok=True)
d=json.loads(Path('work/chapter-one/cases.json').read_text());jobs=[s for t in d.values()for c in t['cases']for s in c['steps']]
def run(s):
 p=r/s['audio']
 if p.exists()and p.stat().st_size>500:return None
 for i in range(3):
  try:gTTS(s['label']+'. '+s['why'],lang='en',timeout=25).save(str(p));return None
  except Exception as e:
   if i==2:return(s['audio'],str(e))
   time.sleep(1)
with concurrent.futures.ThreadPoolExecutor(max_workers=4)as pool:
 errors=[]
 for i,error in enumerate(pool.map(run,jobs),1):
  if error:errors.append(error)
  if i%30==0:print(i,'/',len(jobs),'ready',flush=True)
print('Finished. Errors:',errors,flush=True)
if errors:raise SystemExit(1)
