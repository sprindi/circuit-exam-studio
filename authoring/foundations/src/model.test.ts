import {describe,it,expect} from 'vitest';
import {sourceModel,energyModel,shiftPotentials,parallelLoad} from './model';
import {restoreState,reducer} from './state';
import {lessons} from './content';
const source=(condition:'loaded'|'open'|'short',emf=12,internal=2,load=4)=>sourceModel({emf,internal,load,condition});
describe('one source model drives current, voltage and power',()=>{
 it.each([['loaded',2,8,24,8,16],['open',0,12,0,0,0],['short',6,0,72,72,0]] as const)('%s condition', (condition,current,terminal,sp,ip,lp)=>{const m=source(condition);expect(m.kind).toBe('finite');if(m.kind==='finite'){expect(m.current).toBe(current);expect(m.terminal).toBe(terminal);expect(m.sourcePower).toBe(sp);expect(m.internalPower).toBe(ip);expect(m.loadPower).toBe(lp);expect(m.sourcePower).toBeCloseTo(m.internalPower+m.loadPower);expect(m.levels).toEqual([0,12,terminal,0]);}});
 it('reproduces the teacher example without rounded intermediate values',()=>{const m=source('loaded',125,2.5,28.75);if(m.kind!=='finite')throw Error();expect([m.current,m.terminal,m.sourcePower,m.internalPower,m.loadPower]).toEqual([4,115,500,40,460]);});
 it('distinguishes a practical short from inconsistent ideal constraints',()=>{expect(source('short',12,0).kind).toBe('undefined');expect(source('short',0,0).kind).toBe('undefined');const m=source('loaded',12,0);expect(m.kind==='finite'&&m.terminal).toBe(12);expect(m.kind==='finite'&&m.current).toBe(3);});
 it('preserves differences when the zero reference moves',()=>{const shifted=shiftPotentials([10,5,0],10);expect(shifted).toEqual([0,-5,-10]);expect(shifted[0]!-shifted[1]!).toBe(5);});
 it('converts mA and minutes before integrating energy',()=>{expect(energyModel(2,10,30)).toEqual({amperes:.01,seconds:1800,power:.02,energy:36});expect(energyModel(2,10,0).energy).toBe(0);});
 it('adds parallel branch current without changing ideal supply voltage',()=>{expect(parallelLoad(10,2,1).totalCurrent).toBe(5);expect(parallelLoad(10,2,2)).toEqual({branchCurrent:5,totalCurrent:10,totalPower:100});});
 it('rejects invalid input rather than drawing NaN',()=>{expect(()=>source('loaded',12,-2)).toThrow();expect(()=>source('loaded',NaN)).toThrow();expect(()=>energyModel(2,10,-1)).toThrow();});
});
describe('saved learning state',()=>{
 it('normalizes damaged or old storage without accepting nonexistent sections',()=>{const s=restoreState({scene:'bogus',visited:['charge-current','bogus','charge-current'],goals:['bogus'],minutes:Infinity,emfPhase:100,audio:{'charge-current':20,'unknown':2,'power-rate':NaN}},lessons['1.2']!);expect(s.scene).toBe('intro');expect(s.visited).toEqual(['charge-current']);expect(s.goals).toEqual([]);expect(s.minutes).toBe(30);expect(s.emfPhase).toBe(3);expect(s.audio).toEqual({'charge-current':20});});
 it('keeps section, controls, reflection and audio distinct',()=>{let s=restoreState(null,lessons['1.2']!);s=reducer(s,{type:'scene',id:'emf-action'});s=reducer(s,{type:'control',patch:{emfPhase:2}});s=reducer(s,{type:'audio',key:'emf-action:2',time:12});const restored=restoreState(JSON.parse(JSON.stringify(s)),lessons['1.2']!);expect(restored).toEqual(s);expect(s.goals).toEqual([]);});
});
