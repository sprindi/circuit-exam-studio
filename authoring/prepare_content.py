from pathlib import Path
import re,json,markdown,html
root=Path(__file__).resolve().parent;dist=root.parent/'public'
chapfiles=['Chapter-1-Basic-Concepts-and-Laws.md','Chapter-2-Transient-Analysis.md','Chapter-3-AC-Circuits.md']
topics=[]
for n,name in enumerate(chapfiles,1):
 s=(root/'content'/name).read_text();matches=list(re.finditer(r'^## ((?:Embedded )?(\d+\.\d+)\b[^\n]*)',s,re.M))
 for j,m in enumerate(matches):
  end=matches[j+1].start() if j+1<len(matches) else len(s)
  text=s[m.end():end];text=re.split(r'^## Chapter \d',text,flags=re.M)[0]
  title=m.group(1).replace('Embedded ','').replace(' - ',' ',1);code=m.group(2);title=title[len(code):].strip()
  rendered=markdown.markdown(text,extensions=['tables'])
  topics.append({'id':code,'chapter':n,'title':title,'html':rendered,'text':html.unescape(re.sub(r'<[^>]+>',' ',rendered)),'minutes':max(2,round(len(text.split())/170))})
assert len(topics)==21
(dist/'content.js').write_text('window.COURSE_TOPICS='+json.dumps(topics,ensure_ascii=False)+';\n')
print('Prepared',len(topics),'complete topics and the reviewed PDF')
