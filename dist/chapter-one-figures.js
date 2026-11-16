(()=>{'use strict';
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const line=(d,cls='wire')=>`<path class="${cls}" d="${d}"/>`,txt=(x,y,s,cls='')=>`<text x="${x}" y="${y}" class="${cls}">${esc(s)}</text>`,dot=(x,y)=>`<circle class="node" cx="${x}" cy="${y}" r="4"/>`;
function R(x,y,label,vertical=false,hot=false){return `<g transform="translate(${x} ${y}) ${vertical?'rotate(90)':''}" class="${hot?'hot':''}">${line('M0 0h16l8 -12 12 24 12 -24 12 24 12 -24 8 12h20','part')}${vertical?`<text transform="translate(52 -42) rotate(-90)" text-anchor="middle">${esc(label)}</text>`:txt(50,-25,label,'center')}</g>`;}
function source(x,y,label,kind='voltage',r=28){return `<circle class="part" cx="${x}" cy="${y}" r="${r}"/>`+(kind==='current'?line(`M${x} ${y+15}v-30m-7 9 7 -9 7 9`,'arrow'):txt(x,y-5,'+','center')+txt(x,y+18,'−','center'))+txt(x-42,y-r-14,label,'source-label');}
function arrow(x,y,dir,label){return line(`M${x} ${y}h${dir*50}m${-dir*9} -6 ${dir*9} 6 ${-dir*9} 6`,'arrow')+txt(x+dir*25,y-16,label,'center');}
const frame=(p,caption)=>`<svg viewBox="0 0 640 390" role="img" aria-label="${esc(caption)}">${p}</svg>`;
function loop({v='12 V',r0='2 Ω',load='4 Ω',i='2 A',u='8 V',state='loaded',kind='voltage',reverse=false,flip=false,lamp=false,cap='a',bottom='b'}){let p=line('M90 172V90H190M290 90H480V140M480 240V320H90V228')+source(90,200,v,kind);
 p+=r0?R(190,90,r0,false,true):line('M190 90H290');
 if(state==='open')p+=`<circle class="terminal" cx="480" cy="140" r="5"/><circle class="terminal" cx="480" cy="240" r="5"/>`+txt(435,195,'OPEN','center accent');
 else if(state==='short')p+=line('M480 140V240','short')+txt(520,205,'SHORT','accent');
 else if(lamp)p+=line('M480 140v22m0 56v22')+`<circle class="lamp" cx="480" cy="190" r="28"/>`+line('M462 172l36 36m0 -36 -36 36','part')+txt(525,198,'Lamp');
 else p+=R(480,140,load,true,true);
 p+=(lamp?arrow(345,90,1,'Closed path'):arrow(reverse?405:345,90,reverse?-1:1,`I${reverse?'ref':''} = ${i}`))+dot(480,115)+dot(480,270)+txt(496,120,cap)+txt(496,282,bottom)+txt(560,170,flip?'−':'+','center')+txt(560,235,flip?'+':'−','center')+txt(570,205,u,'center accent');
 return p;}
function parallel({v='10 V',kind='voltage',branches=['2 Ω','2 Ω'],note='Both branches share the same voltage',openMiddle=false}){let p=line('M90 172V80H510M90 228V320H510')+source(90,200,v,kind);const xs=branches.length===1?[510]:[300,510];for(let j=0;j<branches.length;j++){const x=xs[j];p+=line(`M${x} 80V140M${x} 240V320`)+R(x,140,branches[j],true,true);}p+=txt(320,365,note,'center caption');return p;}
function norton(current,r,load,u,i){return parallel({v:current,kind:'current',branches:[r,load],note:`Load: ${u}, ${i}`});}
function twoSources(A,B,res,load,zero=-1,extraCurrent=false){let p=line('M120 70H530M120 340H530');for(const [j,x]of[120,320].entries()){
 if(j===1&&extraCurrent){p+=line('M320 70V155M320 235V340')+`<circle class="terminal" cx="320" cy="155" r="5"/><circle class="terminal" cx="320" cy="235" r="5"/>`+txt(320,195,'OPEN','center accent')+txt(320,222,'Is = 0','center caption');continue;}
 p+=line(`M${x} 70V110M${x} 210V240M${x} 280V340`)+R(x,110,res,true,j===zero);
 p+=j===zero?line(`M${x} 240V280`,'short')+txt(x+30,270,'0 V → short','caption'):source(x,260,(j?B:A)+' V','voltage',20);
 }p+=line('M530 70V150M530 250V340')+R(530,150,load,true,true)+dot(530,70)+dot(530,340);return p;}
function bridge(zero){let p=line('M80 80H220M420 80H560M80 340H560');p+=line('M80 80V110M80 210V248M80 292V340')+R(80,110,'2 Ω',true,zero)+line('M220 80V140M220 240V340')+R(220,140,'2 Ω',true,zero);
 p+=line('M420 80V215M420 265V340M560 80V110M560 210V248M560 292V340')+R(560,110,'5 Ω',true,zero);
 p+=zero?line('M80 248V292M560 248V292','short')+`<circle class="terminal" cx="420" cy="215" r="4"/><circle class="terminal" cx="420" cy="265" r="4"/>`+txt(420,245,'OPEN','center caption'):source(80,270,'8 V','voltage',22)+source(560,270,'5 V','voltage',22)+`<circle class="part" cx="420" cy="240" r="25"/>`+line('M420 225v30m-7 -9 7 9 7 -9','arrow')+txt(452,238,'3 A');
 p+=`<circle class="terminal" cx="220" cy="80" r="5"/><circle class="terminal" cx="420" cy="80" r="5"/>`+txt(220,50,zero?'a':'a · 4 V','center accent')+txt(420,50,zero?'b':'b · −10 V','center accent')+line('M230 80H280M360 80H410','port')+txt(320,94,'Load removed','center caption')+txt(320,373,zero?'Seen from a to b: (2 ∥ 2) + 5 = 6 Ω':'Uab = 4 − (−10) = 14 V','center accent');return p;}
function ground(three,shift){let p;if(!three){p=loop({v:'10 V',r0:'2 Ω',load:'2 Ω',i:'2.5 A',u:'5 V'});p+=txt(100,50,shift?'a = 0 V':'a = 10 V')+txt(380,50,shift?'b = −5 V':'b = 5 V')+txt(285,355,shift?'c = −10 V':'c = 0 V');}
 else{p=line('M90 172V90H190M290 90H480V140M480 240V320H290M190 320H90V228')+source(90,200,'10 V')+R(190,90,'4 Ω')+R(480,140,'3 Ω',true)+R(190,320,'3 Ω');p+=txt(90,50,shift?'a = 0 V':'a = 10 V')+txt(390,50,shift?'b = −4 V':'b = 6 V')+txt(420,365,shift?'c = −7 V':'c = 3 V')+txt(45,365,shift?'d = −10 V':'d = 0 V');}return p;}
function slope(kind){const cap=kind==='capacitor-law';let p='';p+=cap?line('M35 185H115m0 -32v64m24 -64v64m0 -32h85','part')+txt(125,125,'C = 10 µF','center'):line('M35 185h35q0 -25 15 -25t15 25q0 -25 15 -25t15 25q0 -25 15 -25t15 25h40','part')+txt(125,125,'L = 0.5 H','center');
 p+=arrow(40,245,1,cap?'iC = 2 mA':'uL = 2 V')+line('M320 65V290H600')+line('M320 290L570 100','slope')+line('M320 100H570V290','guide')+txt(315,40,cap?'uC (V)':'iL (A)')+txt(292,110,cap?'2 V':'2 A')+txt(510,325,cap?'10 ms':'0.5 s')+txt(322,320,'0')+txt(330,370,cap?'Specified voltage ramp: 200 V/s':'Specified current ramp: 4 A/s','center caption');return p;}
function node(boundary,phase){if(boundary)return `<rect class="boundary" x="160" y="100" width="300" height="180" rx="20"/>`+line('M60 200H540M260 40V200')+dot(260,200)+dot(380,200)+arrow(80,200,1,'2 A')+arrow(480,200,1,phase?'5 A':'Iout')+line('M260 45V125m-6 -9 6 9 6 -9','arrow')+txt(278,70,'3 A')+txt(315,320,'Internal currents cancel','center caption');return line('M60 195H570M320 195V325')+dot(320,195)+arrow(105,195,1,'5 A')+arrow(465,195,1,'2 A')+line('M320 235v50m-6 -9 6 9 6 -9','arrow')+txt(350,270,phase?'3 A':'I')+txt(320,80,'Incoming = outgoing','center caption');}
function blocks(phase){const labels=phase===0?['Battery','Lamp','Light + heat']:['Microphone','Amplifier','Speaker'];let p='';labels.forEach((s,i)=>{const x=25+i*210;p+=`<rect class="block ${i===phase?'chosen':''}" x="${x}" y="125" width="170" height="105" rx="14"/>`+txt(x+85,185,s,'center');if(i<2)p+=arrow(x+180,175,1,'');});p+=txt(320,300,phase===0?'Power circuit · energy conversion':'Signal circuit · information processing','center caption');return p;}
function figure(key,phase){let p='',caption='';switch(key){
 case'lamp':p=loop({v:'Battery',r0:'',load:'',i:phase?'Path closed':'Reference',u:'',lamp:true});caption='Source, connecting path and lamp load';break;
 case'blocks':p=blocks(phase);caption='Compare circuit purposes';break;
 case'power':p=loop({v:'6 V',r0:'',load:'3.75 Ω',i:'1.6 A',u:'6 V'});caption='Bulb operating point: 6 volts and 1.6 amperes';break;
 case'energy':p=loop({v:'2 V',r0:'',load:'200 Ω',i:'10 mA',u:'2 V'})+txt(320,375,'Duration: 30 min = 1800 s','center caption');caption='Constant-power energy example';break;
 case'charge':{
 const emphasis=phase===0?'6 C crosses here':phase===1?'Time interval: 3 s':'2 C each second = 2 A';
 p=txt(320,45,'Count charge crossing one section','center')+`<defs><clipPath id="c1-flow-clip"><rect x="45" y="110" width="550" height="80" rx="30"/></clipPath></defs><rect class="block" x="45" y="110" width="550" height="80" rx="30"/><g clip-path="url(#c1-flow-clip)"><g class="c1-charge-flow">`;
 for(let x=-20;x<=700;x+=90)p+=`<circle class="charge-packet" cx="${x}" cy="150" r="15"/>`+txt(x,157,'+','center');
 p+='</g></g>'+line('M320 82V215','boundary')+arrow(450,85,1,'I')+txt(320,245,emphasis,'center accent');
 for(let j=0;j<3;j++){const x=60+j*180;p+=`<rect class="block" x="${x}" y="270" width="160" height="65" rx="9"/>`+txt(x+80,295,'Second '+(j+1),'center caption')+txt(x+80,322,'2 C crosses','center');}
 p+=txt(320,374,'6 C in 3 s · charge markers are schematic','center caption');caption='Current: charge per second through the dashed counting section';break;}
 case'emf-terminal':{
 p=loop({v:'E = 12 V',r0:'R₀ = 2 Ω',load:'4 Ω',i:'2 A',u:'8 V'});
 p+=line('M25 300V40H310V115H145V300Z','boundary')+txt(180,24,'INSIDE THE BATTERY','center caption')+txt(325,350,phase===0?'EMF: 12 J/C supplied':phase===1?'Internal drop: 4 J/C becomes heat':'Output: 8 J/C reaches the load','center accent');
 caption='Battery supplying current: 12 V EMF − 4 V internal drop = 8 V at terminals a–b';break;}
 case'loaded':p=loop({});caption='12 V source with internal 2 ohms and external 4 ohms';break;
 case'open':p=loop({state:'open',i:'0 A',u:'12 V'});caption='Open terminals: zero current, nonzero voltage';break;
 case'short':p=loop({state:'short',load:'0 Ω',i:'6 A',u:'0 V'});caption='Shorted output: internal resistance limits current';break;
 case'source-balance':p=loop({v:'125 V',r0:'2.5 Ω',load:'28.75 Ω',i:'4 A',u:'115 V'});caption='Source EMF, terminal voltage and internal drop';break;
 case'ground-two':p=ground(false,phase>0);caption='Changing the zero reference preserves voltage differences';break;
 case'ground-three':p=ground(true,phase>0);caption='Node potentials before and after moving the reference';break;
 case'polarity':p=loop({v:'10 V',r0:'',load:'5 Ω',i:'2 A',u:phase?'−10 V':'10 V',flip:phase>0,cap:'a',bottom:'b'});caption='Same circuit; opposite ordered voltage reference';break;
 case'negative-current':p=loop({v:'10 V',r0:'',load:'5 Ω',i:'−2 A',u:'10 V',reverse:true})+txt(320,375,'Actual current: 2 A downward through R','center caption');caption='Negative current relative to the upward branch reference';break;
 case'midpoint':p=line('M100 172V60H320V90M320 190V210M320 310V340H100V228')+source(100,200,'22 V')+R(320,90,'Equal R',true)+R(320,210,'Equal R',true)+dot(320,200)+txt(360,65,'a = +12 V')+txt(360,205,'mid = +1 V','accent')+txt(360,340,'b = −10 V');caption='Midpoint of equal unloaded series resistors';break;
 case'resistor-law':p=loop({v:'16 V',r0:'',load:'8 Ω',i:'2 A',u:'16 V'});caption='Ohm law with passive references';break;
 case'capacitor-law':case'inductor-law':p=slope(key);caption=key==='capacitor-law'?'Capacitor current follows voltage slope':'Inductor voltage follows current slope';break;
 case'load-change':p=parallel({branches:phase?['2 Ω','2 Ω']:['2 Ω'],note:phase?'Total source current: 10 A':'Source current: 5 A'});caption='An ideal voltage source maintains 10 V as loads change';break;
 case'current-source':p=parallel({v:'1 A',kind:'current',branches:[phase?'10 Ω':'1 Ω'],note:phase?'Load voltage: 10 V':'Load voltage: 1 V'});caption='An ideal current source maintains 1 A as resistance changes';break;
 case'source-absorbs':p=line('M100 172V80H500V172M500 228V320H100V228')+source(100,200,'3 A','current')+source(500,200,'3 V')+arrow(285,80,1,'3 A')+txt(320,365,'Current enters the + terminal: 9 W absorbed','center caption');caption='A voltage source absorbing power from a current source';break;
 case'transform':case'transform-reverse':{const n=key==='transform'?phase>0:phase===0;p=n?norton('5 A','2 Ω','3 Ω','6 V','2 A'):loop({v:'10 V',r0:'2 Ω',load:'3 Ω',i:'2 A',u:'6 V'});caption=n?'Equivalent current-source form':'Equivalent voltage-source form';break;}
 case'combine':p=phase? norton('30 A','1 Ω','4 Ω','24 V','6 A'):twoSources(40,20,'2 Ω','4 Ω');caption='Two practical sources supplying one load';break;
 case'irrelevant':p=phase?loop({v:'1 A',kind:'current',r0:'3 Ω',load:'5 Ω',i:'1 A',u:'5 V'}):parallel({branches:['2 Ω','5 Ω'],note:'Ideal 10 V source: the 5 Ω load always takes 2 A'});caption=phase?'A series resistor cannot change ideal source current':'A shunt resistor cannot change ideal source voltage';break;
 case'kcl':p=node(false,phase);caption='One node, three current references';break;
 case'boundary':p=node(true,phase);caption='KCL applied to a boundary around multiple nodes';break;
 case'kvl':p=loop({v:'12 V',r0:'2 Ω',load:'4 Ω',i:'2 A',u:'8 V'})+txt(320,375,'12 − 4 − 8 = 0','center caption');caption='Voltage rises and drops in one loop';break;
 case'branches':return `<figure class="c1-course-figure"><img src="assets/branch-current-references.png" alt="Original teacher five-branch circuit with assigned branch current references"><figcaption>Teacher’s circuit · 3 essential nodes · 5 branches <a href="assets/branch-current-references.png" target="_blank" rel="noopener">Enlarge ↗</a></figcaption></figure>`;
 case'terminal':p=line('M90 172V90H190M290 90H500M90 228V320H500')+source(90,200,'10 V')+R(190,90,'2 Ω',false,true)+dot(500,90)+dot(500,320)+arrow(phase?420:350,90,phase?-1:1,'2 A')+txt(520,100,'a')+txt(520,320,'b')+txt(440,205,phase?'Uab = 14 V':'Uab = 6 V','center accent')+txt(320,375,'External circuit sets the current','center caption');caption='Terminal voltage depends on the assigned current direction';break;
 case'super-voltage':p=twoSources(18,9,'1 Ω','4 Ω',1)+txt(320,375,'18 V alone: IL = +2 A','center caption');caption='Inactive voltage source is a short; its resistor remains';break;
 case'super-current':p=twoSources(12,0,'2 Ω','4 Ω',-1,true)+txt(320,375,'Active voltage source: IL = +2 A','center caption');caption='Inactive current-source branch is open';break;
 case'super-add':p=twoSources(18,9,'1 Ω','4 Ω',phase===0?1:phase===1?0:-1)+txt(320,375,phase===0?'18 V alone: IL = 2 A':phase===1?'9 V alone: IL = 1 A':'Both active: IL = 3 A','center caption');caption='Source contributions use the same load-current reference';break;
 case'power-warning':p=loop({v:'4 V',r0:'',load:'4 Ω',i:'1 A',u:'4 V'})+txt(320,375,'Target branch after adding currents: P = 4 W','center caption');caption='Calculate resistor power from the total branch current';break;
 case'bridge-open':p=bridge(false);caption='Original teacher bridge network with only the load removed';break;
 case'bridge-resistance':p=bridge(true);caption='Same port, independent sources zeroed, resistances retained';break;
 case'thevenin':p=loop({v:'14 V',r0:'6 Ω',load:'8 Ω',i:'1 A',u:'8 V'});caption='Thévenin equivalent with the 8 ohm load reconnected';break;
 case'norton':p=norton('7/3 A','6 Ω','8 Ω','8 V','1 A');caption='Norton equivalent with the same 8 ohm load';break;
 default:throw Error('Missing chapter-one figure '+key);
 }return `<figure>${frame(p,caption)}<figcaption>${esc(caption)}</figcaption></figure>`;}
window.ChapterOneFigure={render:figure};
})();
