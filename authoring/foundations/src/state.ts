import type {Lesson} from './content';
export interface LessonState {version:1;scene:string;visited:string[];goals:string[];groundTop:boolean;loads:1|2;emfPhase:number;condition:'loaded'|'open'|'short';minutes:number;audio:Record<string,number>}
export function restoreState(raw:unknown,lesson:Lesson):LessonState{
 const x=(raw&&typeof raw==='object'?raw:{})as Partial<LessonState>;const sceneIds=lesson.scenes.map(s=>s.id),goalIds=lesson.goals.map(g=>g.id);
 const audio:Record<string,number>={};if(x.audio&&typeof x.audio==='object')for(const [key,time]of Object.entries(x.audio))if(typeof time==='number'&&Number.isFinite(time)&&time>=0&&time<3600&&lesson.scenes.some(s=>key===s.id||s.phases?.some((_,i)=>key===s.id+':'+i)))audio[key]=time;
 return {version:1,scene:typeof x.scene==='string'&&['intro','finish',...sceneIds].includes(x.scene)?x.scene:'intro',visited:Array.isArray(x.visited)?[...new Set(x.visited.filter(s=>sceneIds.includes(s)))]:[],goals:Array.isArray(x.goals)?[...new Set(x.goals.filter(g=>goalIds.includes(g)))]:[],groundTop:x.groundTop===true,loads:x.loads===2?2:1,emfPhase:typeof x.emfPhase==='number'&&Number.isFinite(x.emfPhase)?Math.max(0,Math.min(3,Math.trunc(x.emfPhase))):0,condition:['loaded','open','short'].includes(x.condition??'')?x.condition!:'loaded',minutes:typeof x.minutes==='number'&&Number.isFinite(x.minutes)?Math.max(0,Math.min(30,x.minutes)):30,audio};
}
export type Action={type:'scene';id:string}|{type:'goal';id:string}|{type:'control';patch:Partial<Pick<LessonState,'groundTop'|'loads'|'emfPhase'|'condition'|'minutes'>>}|{type:'audio';key:string;time:number};
export function reducer(state:LessonState,action:Action):LessonState{
 if(action.type==='scene')return {...state,scene:action.id,visited:['intro','finish'].includes(action.id)?state.visited:[...new Set([...state.visited,action.id])]};
 if(action.type==='goal')return {...state,goals:state.goals.includes(action.id)?state.goals.filter(g=>g!==action.id):[...state.goals,action.id]};
 if(action.type==='control')return {...state,...action.patch};
 return {...state,audio:{...state.audio,[action.key]:action.time}};
}
