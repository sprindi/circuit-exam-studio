export type Condition = 'loaded'|'open'|'short';
export interface SourceInput { emf:number; internal:number; load:number; condition:Condition }
export function sourceModel(x:SourceInput){
 if(![x.emf,x.internal,x.load].every(Number.isFinite)||x.internal<0||x.load<0)throw new Error('Use finite, non-negative resistances.');
 if(x.condition==='short'&&x.internal===0)return {kind:'undefined' as const,reason:x.emf===0?'Two ideal zero-voltage constraints do not determine a unique current.':'An ideal nonzero voltage source cannot have a finite current through an ideal short.'};
 const effective=x.condition==='short'?0:x.load;
 if(x.condition==='loaded'&&x.internal+effective===0)return {kind:'undefined' as const,reason:'Zero total resistance does not give a finite source current.'};
 const current=x.condition==='open'?0:x.emf/(x.internal+effective);
 const internalDrop=current*x.internal,terminal=x.emf-internalDrop;
 return {kind:'finite' as const,current,internalDrop,terminal,sourcePower:x.emf*current,internalPower:current*current*x.internal,loadPower:terminal*current,levels:[0,x.emf,terminal,0]};
}
export function shiftPotentials(values:number[],reference:number){return values.map(v=>v-reference);}
export function energyModel(voltage:number,milliamps:number,minutes:number){
 if(![voltage,milliamps,minutes].every(Number.isFinite)||minutes<0)throw new Error('Use finite quantities and non-negative elapsed time.');
 const amperes=milliamps/1000,seconds=minutes*60,power=voltage*amperes;return {amperes,seconds,power,energy:power*seconds};
}
export function parallelLoad(voltage:number,resistance:number,count:1|2){const branchCurrent=voltage/resistance;return {branchCurrent,totalCurrent:count*branchCurrent,totalPower:count*voltage*branchCurrent};}
export const fmt=(v:number,digits=2)=>Number(v.toFixed(digits)).toString();
