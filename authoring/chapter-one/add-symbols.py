import json
from pathlib import Path
V='voltage / potential difference, measured in volts (V)'
I='current: charge flowing each second, measured in amperes (A)'
R='resistance, measured in ohms (Ω)'
S={
'Us':'source EMF: energy supplied per coulomb, in volts (V); also written E or Uₛ',
'U':'terminal voltage: potential difference across the output a–b, in volts (V)',
'R0':'internal resistance inside the source, in ohms (Ω); subscript 0 identifies the internal part',
'R':'external load resistance, in ohms (Ω)',
'I':I,'P':'power: energy transferred each second, measured in watts (W)',
'W':'energy transferred, measured in joules (J); here W is a quantity, not the watt unit',
't':'elapsed time, measured in seconds (s)',
'Q':'charge crossing the chosen section, measured in coulombs (C)',
'Ua':'voltage of a relative to b: Uₐᵦ = Vₐ − Vᵦ, in volts (V)',
'Va':'potential of point a relative to the chosen ground, in volts (V)',
'Vb':'potential of point b relative to the same ground, in volts (V)',
'IL':'current through the external load, in amperes (A); subscript L means load',
'Is':'current set by the ideal current source, in amperes (A)',
'Rth':'resistance of the equivalent network seen from the load terminals, in ohms (Ω)',
'Uth':'Thévenin equivalent source voltage, in volts (V)',
'RL':'external load resistance, in ohms (Ω); subscript L means load',
}
labels={'Us':'Uₛ (Us, E)','U':'U','R0':'R₀ (R0)','R':'R','I':'I','P':'P','W':'W','t':'t','Q':'Q','Ua':'Uₐᵦ','Va':'Vₐ','Vb':'Vᵦ','IL':'IL','Is':'Iₛ (Is)','Rth':'Rth','Uth':'Uth','RL':'RL'}
def key(*names):return [[labels[n],S[n]] for n in names]
def entries(*items):return list(items)
D={
'1.1':[
entries(['Source','supplies electrical energy, such as the battery'],['Link','wires and switch that connect the source to the load'],['Load','uses electrical energy, such as the lamp']),
entries(['Power circuit','main purpose: deliver and convert energy'],['Signal circuit','main purpose: transmit or process information']),
entries(['Ideal element','a simplified model with an exact electrical relationship'],['Active network','contains a source in this course’s classification'],['Passive network','contains no source in this course’s classification']),
key('P','I')+[['U',V],['R',R],['∥','parallel connection: both elements connect across the same two nodes']]],
'1.2':[
key('P')+[['U','voltage across the bulb, in volts (V)'],['I',I]],
key('W','P','t')+[['mA','milliampere: 1 mA = 0.001 A']],
key('Ua','Va','Vb')+[['Ground','chosen reference point assigned 0 V']],
key('I','Q','t')+[['i = dq/dt','instantaneous current: the rate at which charge crosses the section']],
key('Us','U','R0','I','R')],
'1.3':[
key('Us','R0','R','I')+[['Rtotal','total series resistance: R₀ + R']],
key('Us','U','I','R0')+[['Pload','power delivered to the disconnected load, in watts (W)']],
key('Us','R0','R','U')+[['Ishort','current with the output terminals directly connected, in amperes (A)'],['Pinternal','power converted to heat inside the source, in watts (W)']],
key('Us','U','I','R0')+[['Generated power','UₛI: power supplied by the source action, in watts (W)'],['Delivered power','UI: power reaching the external load, in watts (W)'],['Internal loss','I²R₀: heat produced inside the source, in watts (W)']]],
'1.4':[
entries(['Vₐ, Vᵦ, V꜀, Vᵈ','node potentials relative to the selected ground, in volts (V)'],['Ground','reference node assigned 0 V; moving it changes the potential labels'],['Voltage difference','potential at the first point minus potential at the second point']),
key('Ua')+[['Uᵦₐ','voltage of b relative to a, in volts (V); the opposite order to Uₐᵦ'],['R',R],['I',I]],
[['U','voltage measured with the marked + and − references, in volts (V)'],['R',R],['I','signed current relative to the chosen arrow, in amperes (A)'],['Negative I','actual current flows opposite to that arrow']],
entries(['Vmid','midpoint potential relative to ground, in volts (V)'],['+12 V, −10 V','end-point potentials measured against the same ground'],['Equal resistors','two series resistors with the same resistance; the midpoint has no extra load'])],
'1.5':[
[['u',V],['i',I],['R',R]]+key('P'),
entries(['C','capacitance: charge stored per volt, measured in farads (F)'],['uC','voltage across the capacitor, in volts (V)'],['iC','current entering its positive terminal, in amperes (A)'],['duC/dt','how fast capacitor voltage changes, in volts per second (V/s)'],['WC','energy stored in the capacitor, in joules (J)'],['µF, ms','1 µF = 10⁻⁶ F; 1 ms = 0.001 s']),
entries(['L','inductance, measured in henries (H)'],['iL','current through the inductor, in amperes (A)'],['uL','inductor voltage with passive references, in volts (V)'],['diL/dt','how fast inductor current changes, in amperes per second (A/s)'],['WL','energy stored in the inductor, in joules (J)']),
[['U','fixed ideal-source voltage, in volts (V)'],['I',I],['Isource','total current delivered by the source to all load branches, in amperes (A)'],['R',R]],
[['I','fixed ideal-source current, in amperes (A)'],['U','voltage across the source and its load, in volts (V)'],['R',R]],
entries(['pabs','power absorbed by the device, in watts (W); positive means energy enters it'],['u','voltage with the marked positive and negative terminals, in volts (V)'],['i','current defined entering the positive terminal, in amperes (A)'])],
'1.6':[
key('Us','Is','IL')+[['R','source resistance: series in the voltage form, parallel in the current form, in ohms (Ω)']],
key('Us','Is','IL')+[['R','source resistance: parallel in the current form, series in the voltage form, in ohms (Ω)']],
key('IL')+[['∥','parallel connection; R₁ ∥ R₂ = R₁R₂ / (R₁ + R₂)'],['30 A','sum of the two compatible source currents'],['1 Ω','equivalent parallel source resistance']],
entries(['Ideal voltage source','holds its specified voltage across its terminals'],['Ideal current source','holds its specified current through its branch'],['External equivalence','the load sees the same voltage/current relationship; internal power can differ'])],
'1.7':[
[['I','unknown outgoing current, in amperes (A)'],['KCL','Kirchhoff’s current law: charge does not accumulate at an ideal circuit node'],['Node','connected junction where the branch currents meet']],
[['I','common current through the series path, in amperes (A)'],['RI','resistor voltage drop, in volts (V)'],['KVL','Kirchhoff’s voltage law: signed voltage changes around a closed loop add to zero']],
entries(['n','number of nodes used in the connected circuit graph'],['b','number of branches in that graph'],['n − 1','number of independent node-current equations'],['b − n + 1','number of independent loop-voltage equations']),
entries(['I₁, I₂','currents entering the boundary, in amperes (A)'],['Iout','current leaving the boundary, in amperes (A)'],['Σ','add all the indicated signed currents'],['Boundary','imagined closed line enclosing part of the circuit']),
key('Us','U','I')+[['R','series resistance in this two-terminal branch, in ohms (Ω)'],['∓','use − when current leaves the positive output; use + when it enters']]],
'1.8':[
entries(['I₁ … I₅','five branch currents, each signed relative to its chosen arrow, in amperes (A)'],['Subscripts 1 … 5','identify branches; they are labels, not multiplication'],['KCL','Kirchhoff’s current law: signed currents at each node sum to zero']),
entries(['I₁ … I₅','signed currents in branches 1 to 5, in amperes (A)'],['R₁ … R₅','resistances in branches 1 to 5, in ohms (Ω)'],['Us₁, Us₂','EMFs of the two voltage sources, in volts (V)'],['IₖRₖ','voltage drop across branch k’s resistor, in volts (V)'],['KVL','Kirchhoff’s voltage law: signed changes around a closed loop sum to zero']),
[['I','signed current relative to the upward arrow, in amperes (A)'],['−2 A','actual current is 2 A opposite to the chosen arrow'],['5 Ω','resistor’s resistance'],['10 V','marked voltage drop across that resistor']]],
'1.9':[
key('IL')+[['IL′','load current due to the first source acting alone, in amperes (A)'],['Vnode','potential of the load’s upper node relative to the bottom node, in volts (V)'],['Inactive source','independent source set to zero for this one contribution']],
key('IL')+[['Inactive source','independent source set to zero for this one contribution'],['Open','disconnected path: no current crosses the inactive ideal current source']],
key('IL')+[['IL′','load current from the first source alone, in amperes (A)'],['IL″','load current from the second source alone, in amperes (A)'],['′ and ″','labels for separate contributions; they do not mean derivatives here']],
key('I','P')+[['R','resistance of the resistor whose power is wanted, in ohms (Ω)'],['I²','square of the total signed current, after adding the contributions']]],
'1.10':[
key('Uth')+[['Uoc','open-circuit voltage across the chosen terminals, in volts (V)'],['Vₐ, Vᵦ','potentials of a and b relative to the common reference, in volts (V)'],['Uₐᵦ','Vₐ − Vᵦ: voltage of a relative to b, in volts (V)']],
key('Rth')+[['∥','parallel combination: R₁R₂ / (R₁ + R₂)'],['Independent sources suppressed','ideal voltage sources shorted; ideal current sources opened']],
key('IL','Uth','Rth','RL')+[['UL','voltage across the reconnected load, in volts (V)']],
[['IN','Norton equivalent source current, in amperes (A)']]+key('Uth','Rth','IL','RL')]
}
Path('work/chapter-one/symbols.json').write_text(json.dumps(D,ensure_ascii=False,indent=2))
