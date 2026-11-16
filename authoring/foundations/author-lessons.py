from pathlib import Path
import json
D={}
def lesson(id,title,question,prep,goals,finish,prereq=None):
 D[id]={'title':title,'question':question,'preparation':prep,'goals':[{'id':f'g{i+1}','text':t}for i,t in enumerate(goals)],'scenes':[],'finish':finish}
 if prereq:D[id]['prerequisite']={'topic':prereq[0],'label':prereq[1]}
def scene(topic,id,title,purpose,visual,paragraphs,takeaway,voice,rule=None,phases=None,condition=None,note=None):
 d={'id':id,'title':title,'purpose':purpose,'visual':visual,'paragraphs':paragraphs,'takeaway':takeaway,'voice':voice,'source':'Course lesson '+topic+' · original reviewed material below'}
 if rule:d['rule']={'formula':rule[0],'when':rule[1],'symbols':rule[2]}
 if phases:d['phases']=[{'title':a,'equation':b,'why':c,'voice':e}for a,b,c,e in phases]
 if condition:d['condition']=condition
 if note:d['note']=note
 D[topic]['scenes'].append(d)
lesson('1.1','See what a circuit does','What makes the lamp light—and where does its energy come from?',[
'No previous circuit formulas are required. Start with an ordinary battery, switch and lamp.','An arrow will have a named meaning. Energy conversion and charge flow are different ideas.'
],[
'Identify the source, connecting parts and load in a physical circuit.','Explain the difference between a real device and its ideal circuit model.','Distinguish energy-delivery circuits from signal-processing circuits.','Explain what “more load” means and recognise the basic network terms.'
],'You now have a picture to attach the quantities to: a connected path, circulating charge, and energy converted by the source and the load.')
scene('1.1','source-link-load','A connected path makes useful conversion possible','Recognise the job of each part before naming symbols.','physical',[
'A battery converts chemical energy into electrical energy. The switch and wires connect it to the lamp. The lamp converts electrical energy into light and heat. These are the source, intermediate link and load.',
'Closing the switch completes a conducting path. In this simple circuit, opening it stops the sustained current and the lamp goes out. The battery does not create charge for the lamp to use up: charge circulates; energy is transferred and converted.'
],'Source → electrical energy transfer → load conversion. This energy account is not a picture of electrons carrying glowing parcels.',
'Begin with the jobs. The battery is the source, the lamp is the load, and the wires and switch connect them. Closing the switch completes a conducting path. Charge is not used up in the lamp. Energy is converted into light and heat. Use the switch to compare the two conditions.')
scene('1.1','physical-to-model','The drawing is a model of the real parts','Know what a schematic keeps—and what it leaves out.','network',[
'A circuit model replaces a real battery, wire or lamp by ideal elements and their connections. It keeps the electrical relationships needed to answer the question, rather than the exact shape of the objects.',
'For example, an ideal voltage-source symbol prescribes a voltage. A real battery may also need internal resistance in its model. A lamp can be approximated as a resistance for a stated operating point; a real filament is not always a constant resistor.'
],'Read the connections, element type and references. A neat symbol is not a promise that the real device is ideal.',
'The schematic is a model, not a photograph. Follow which terminals are connected. An ideal source fixes its prescribed voltage; a practical battery may need an extra internal resistance. Treat a lamp as a resistor only under the stated approximation. The model must suit the question.')
scene('1.1','power-or-signal','Two purposes, both using electricity','Classify by the main job, not simply by whether energy is consumed.','purposes',[
'A power circuit is mainly designed to generate, transmit or convert electrical energy. A generator, transmission system and motor are examples. In a torch, the useful result is light.',
'A signal circuit mainly transmits or processes information. A microphone–amplifier–speaker chain or a temperature-measuring circuit is an example. Signal circuits also need energy: their main purpose is what distinguishes them.'
],'Ask “What is the intended output: energy conversion or information processing?”',
'A circuit may mainly deliver energy or mainly process information. The power circuit supplies a useful energy conversion. The signal circuit carries and processes information, such as sound or temperature. Both consume energy, so consumption alone does not decide the type.')
scene('1.1','load-and-language','“More load” does not mean “more resistance”','Connect the words in a question to the physical effect.','load',[
'In the course, an increase in load means more power consumption. If the supply voltage is held fixed, the source must provide more current. Connecting a second identical resistive load in parallel is a useful example: the voltage stays the same, but another branch takes current.',
'A two-terminal network connects to the rest of a circuit at two terminals. In this course’s introductory classification, an active network contains a source and a passive network contains no source.',
'The course’s introductory DC examples use constant voltage and current. AC reverses polarity or direction with time; sinusoidal AC follows a sine wave. A quantity changing in size without reversing is not automatically AC.'
],'Use the extra-load control: more delivered power here means more source current and a smaller equivalent load resistance.',
'At a fixed voltage, adding another parallel load increases total current and power consumption. It reduces the equivalent resistance. That is why more load does not mean more resistance. Keep the other terms separate too: active and passive describe sources in this introductory classification; AC involves reversal, not just any change in size.',
('P = UI','For the fixed-voltage resistive loads shown.',[['P','Total load power, in watts (W).'],['U','Voltage across each parallel load, in volts (V).'],['I','Total current supplied to the load branches, in amperes (A).']]))
lesson('1.2','Give the quantities a physical meaning','What is flowing, what is being transferred, and what does a voltmeter measure?',[
'Know the source, connecting path and load. Revisit 1.1 if those jobs are unclear.','Use division and multiplication with units. A basic resistance relation is introduced where needed; its full element treatment is in 1.5.','A volt is a joule per coulomb. An ampere is a coulomb per second. These unit meanings connect the lesson.'
],[
'Explain current as a rate of charge flow, not electron speed.','Distinguish a node potential from a voltage between two points.','Explain EMF, its direction through the source, and why terminal voltage can differ.','Distinguish power from energy and carry out the course calculations with consistent units.'
],'The six quantities now fit together: charge per second is current; energy per charge is measured in volts; energy per second is power; power accumulated over time gives energy.',('1.1','Source, load and a complete circuit'))
scene('1.2','charge-current','Current counts charge crossing a section','Understand an ampere before using it in another formula.','charge',[
'Imagine a counting section across a wire. Current tells you how much charge crosses that section in a time interval. It does not tell you the speed of one electron, or how much charge is simply present in the wire.',
'If 6 coulombs cross in 3 seconds at a steady rate, 2 coulombs cross each second. That rate is 2 amperes. Conventional current is defined in the direction of positive-charge motion; electrons in a metal drift the other way.'
],'The charge is not consumed at the counting section or at the load. In a steady series path, the same current enters and leaves each part.',
'Put an imaginary counting line across the wire. Six coulombs cross it in three seconds. Divide charge by time: two coulombs each second, or two amperes. The moving markers represent amounts of charge, not individual electrons. The arrow is conventional current, and it is not an electron-speed scale.',
('I = Q / t = 6 C / 3 s = 2 A','For steady current. Q/t is an average if the current changes; instantaneous current is i = dq/dt.',[['I','Current: charge crossing each second, measured in amperes (A).'],['Q','Charge crossing the section, in coulombs (C).'],['t','Elapsed time, in seconds (s).']]))
scene('1.2','potential-and-voltage','Potential needs a reference; voltage needs two points','See why changing “zero” cannot change a measured difference.','potential',[
'A node potential is its electrical potential relative to a chosen reference node. Voltage between a and b is the ordered difference Va − Vb. The order matters: Uab and Uba have opposite signs.',
'In the teacher’s circuit, 10 V drives two equal 2 Ω resistors. Their current is 10/(2+2) = 2.5 A, so each resistor drops 5 V. With c as zero, a is 10 V and b is 5 V. Move zero to a: b becomes −5 V and c becomes −10 V.',
'The resistor still has the same 5 V difference. The circuit has not changed. “Ground” here means the selected zero reference; it does not necessarily mean a physical connection to earth.'
],'Try moving the reference. The three potential labels shift together; the difference across the first resistor remains 5 V.',
'A voltage is a difference between two specified points. A potential is relative to your chosen zero. Move the reference in this diagram and watch every potential shift by the same amount. The voltage across each resistor stays the same. Negative potential does not mean the circuit has stopped working.',
('Uab = Va − Vb','Use potentials measured against the same reference. Keep the physical node names fixed.',[['Uab','Voltage of a relative to b, in volts (V).'],['Va, Vb','Node potentials relative to the selected zero, in volts (V).'],['a, b, c','Fixed physical nodes; moving the reference does not rename them.']]))
scene('1.2','emf-action','The source raises energy per charge','Explain EMF as a source action, then account for every drop.','emf',[
'A battery’s chemical processes maintain a separation of charge. Its electromotive force, written Us in this course and also E, describes energy supplied per coulomb by that non-electric source action. Despite its name, EMF is not a mechanical force in newtons.',
'The EMF arrow points through the ideal source from − toward +: the source action raises electrical energy per positive charge. Conventional current then leaves the positive output and goes through the external load toward the negative output.',
'Terminal voltage is what a voltmeter measures between the battery’s output terminals. In a practical battery, some of the source’s energy per charge is converted into heat internally before energy is delivered to the external load. Use the four stage controls to connect these ideas.'
],'The source action, current direction and energy accounting need separate labels. The diagram is a lumped circuit model, not a simulation of microscopic energy transport.',
'EMF tells us the energy supplied per coulomb by the source action. In a battery, chemical processes do that job. The arrow through the ideal source points from negative toward positive. Terminal voltage is a measurement across the output. Follow the energy stages to see why that measured voltage can be lower than the EMF.',
('U = Us − IR₀','For this source model while current leaves the positive output terminal.',[['Us or E','Source EMF: energy supplied per charge, in volts (J/C).'],['U','Terminal voltage measured from a to b, in volts (V).'],['R₀','Resistance inside the source, in ohms (Ω); subscript 0 identifies the internal part.'],['I','Delivered current, in amperes (A).']]),[
('Source action','Us = 12 V = 12 J/C','The ideal source conversion adds 12 joules per coulomb. The upward EMF arrow shows the rise through the source, from − toward +.','The source action adds twelve joules per coulomb. Watch the upward arrow through the ideal source and the rise on the energy-per-charge trace. This is energy conversion, not the creation of charge.'),
('Internal drop','I = 12 / (2 + 4) = 2 A; IR₀ = 4 V','The two resistances share one series current. At 2 A, the internal 2 Ω converts 4 joules per coulomb into heat.','The internal resistance carries the same series current as the load. With two amperes through two ohms, the internal drop is four volts. That means four joules per coulomb becomes heat inside the battery.'),
('At the terminals','U = 12 − 4 = 8 V','Eight joules per coulomb is available between a and b. That is the terminal voltage; the external 4 Ω load accounts for the remaining drop.','The output terminals are after the internal drop. The voltmeter reads eight volts, corresponding to eight joules per coulomb delivered to the external load. The EMF is still twelve volts.'),
('Close the energy account','12 J/C supplied = 4 J/C internal + 8 J/C external','The trace returns to its starting level around the loop. Charge continues around the circuit; energy has been converted.','The energy account balances: twelve joules per coulomb supplied, four converted to heat internally, and eight delivered outside. The trace returns to its starting level. The charge has not been used up.')
])
scene('1.2','emf-limits','When does terminal voltage equal EMF?','Separate the source property from the current-dependent internal drop.','conditions',[
'Use the same 12 V source and internal 2 Ω resistance. With the output open, no current flows: IR₀ is zero, so the terminal voltage equals 12 V. A nonzero voltage can exist without current or delivered load power.',
'For an ideal voltage-source model, R₀ is zero. Its terminal voltage equals the prescribed EMF even when it delivers current. “Only with no current” would therefore be an incomplete statement.',
'The subtraction rule above assumes the source is delivering current out of its positive terminal. If an external circuit pushes current into that terminal, the internal drop changes the terminal relation. The reference and power lessons will examine that receiving/charging case.'
],'Compare the open and loaded connections. The source EMF stays 12 V; the internal drop depends on current.',
'An open circuit has no current, so this practical source has no internal drop and its terminal voltage equals its EMF. An ideal voltage source also has equality, even under load, because its internal resistance is zero. Always state the source model and current reference before using the subtraction rule.',
('U = Us − IR₀','The equal-voltage cases are I = 0 or R₀ = 0 in this model.',[['Us','The source EMF, in volts (V).'],['U','Measured output voltage, in volts (V).'],['IR₀','Current-dependent internal voltage drop, in volts (V).']]),condition='open')
scene('1.2','power-rate','Power is energy transferred each second','Connect voltage and current instead of memorising their product.','power',[
'Voltage gives energy per coulomb; current gives coulombs per second. Their product gives joules per second, which is power. The coulombs cancel in the units: (J/C) × (C/s) = J/s = W.',
'The teacher’s bulb takes 1.6 A at 6 V, so it receives 9.6 joules each second: 9.6 W. This is an operating-point calculation. It does not mean its energy consumption is 9.6 joules for every duration.',
'For a load, current entering its marked positive terminal gives positive absorbed power. For the source delivering the current, energy is supplied. Later you will use signed references to recognise a source that is absorbing power instead.'
],'Power describes the rate, not the accumulated total. The voltage and current references decide the sign of absorbed power.',
'Six volts means six joules per coulomb, and one point six amperes means one point six coulombs per second. Multiply them to get nine point six joules each second, or nine point six watts. This is a rate of energy transfer, not the total energy for an unspecified time.',
('P = UI = 6 × 1.6 = 9.6 W','For the DC load at the stated operating point, with current entering its + terminal.',[['P','Power absorbed by the bulb, in watts (W = J/s).'],['U','Voltage across the bulb, in volts (V = J/C).'],['I','Current through it, in amperes (A = C/s).']]))
scene('1.2','energy-duration','Energy also depends on how long','Read energy as area under a constant-power graph.','energy',[
'Two devices can use the same power for different times and consume different amounts of energy. At constant power, the energy is the rectangular area P × t under the power–time graph.',
'The course example gives 2 V, 10 mA and 30 minutes. First convert 10 mA to 0.010 A, giving P = 0.020 W. Convert 30 minutes to 1800 seconds. At the end, W = 0.020 × 1800 = 36 J.',
'The symbol W here names an energy quantity measured in joules; the unit W after a number means watts. Likewise, kW is power but kWh is energy: 1 kWh = 1000 W × 3600 s = 3.6 million joules.'
],'Move the elapsed-time control: the height of the power graph stays fixed, while the accumulated area and energy grow.',
'Power is a rate. Energy adds the effect of duration. In this course example, convert milliamperes to amperes and minutes to seconds before multiplying. Move the elapsed-time control: the power stays constant and the shaded area grows. At thirty minutes the total is thirty-six joules.',
('W = Pt','For constant power. The graph shows elapsed time within the 30-minute course example.',[['W','Energy accumulated, measured in joules (J). Not the watt unit in this formula.'],['P','Constant power: 0.020 watts (W).'],['t','Elapsed time in seconds (s), converted from minutes.']]))
scene('1.2','quantity-map','Six quantities, three important distinctions','Connect the meanings before moving to circuit conditions.','quantities',[
'Current answers “how much charge per second?” Potential needs a selected zero; voltage compares two specified points. EMF describes the energy-conversion action of a source.',
'Power answers “how much energy per second?” Energy answers “how much altogether over this duration?” Sharing a unit does not make potential, voltage and EMF interchangeable concepts.',
'You can now explain the three comparisons the original lesson asks for: voltage versus potential, EMF versus terminal voltage, and power versus energy. Return to the corresponding section if a distinction still feels like only a definition.'
],'Use the goal check at the end to decide which explanation to revisit. “Viewed” or “reviewed” alone is not a test of understanding.',
'The six quantities describe different things. Current is charge per second. Potential uses a reference; voltage uses two points. EMF describes the source action. Power is energy per second, and energy also includes time. Before continuing, check that you can explain the three distinctions in the course goals, not just repeat their units.')
lesson('1.3','Read the connection before calculating','What changes when the same source is loaded, open or shorted?',[
'Know current, terminal voltage and source EMF from 1.2.','Identify Us, internal resistance R₀ and the external load R.','Use the series resistance relation and power P = UI with the marked references.'
],[
'Identify loaded, open and shorted outputs without confusing their zero quantities.','Calculate source current and terminal voltage for the stated source model.','Account for delivered power and internal heating, including a short circuit.','Use the teacher’s measured values to infer internal resistance and verify power balance.'
],'The connection selects the model you calculate. An open fixes branch current to zero; an ideal short fixes terminal voltage to zero. Neither statement by itself says that every voltage, current or power in the circuit is zero.',('1.2','Current, EMF, terminal voltage and power'))
scene('1.3','three-connections','One source, three different output conditions','Change the connection; keep the source, node names and references fixed.','conditions',[
'Loaded means a finite resistive load connects the output terminals. Open means that external conducting path is broken. A short directly connects the output terminals with an ideal conducting path.',
'Use the comparison controls to change just that external condition. The source EMF remains 12 V and its internal resistance remains 2 Ω. Notice which quantity becomes zero: current for the open, terminal voltage for the short.',
'These are ideal circuit models. The short-current calculation needs a nonzero internal resistance. Do not replace a shorted zero-resistance ideal voltage source by an arbitrary finite current.'
],'A disconnected path and a wire connection are different constraints. Read the drawing first, then choose the relationship.',
'Keep the same source and change only the output connection. An open path gives zero current; a short gives zero voltage between its terminals. They are not the same condition. The internal resistance remains inside this source model and matters especially for the short.',condition='loaded')
scene('1.3','loaded-operation','Loaded: the internal and external resistances share current','Find the current first, then distinguish source EMF from output voltage.','conditions',[
'With a 4 Ω load and internal 2 Ω resistance, the complete path has 6 Ω. One series current flows through both: I = 12/6 = 2 A.',
'The load voltage is IR = 8 V. Equivalently, subtract the internal 4 V drop from the 12 V source EMF. These two calculations describe the same terminal voltage, not two different kinds of voltage.',
'The source conversion provides 24 W. Of that, 8 W becomes heat internally and 16 W is delivered to the external load. The power account is 24 = 8 + 16 W.'
],'Check both voltage balance and power balance. The measured output voltage belongs across a–b, after the internal resistance.',
'In the loaded condition, add the two series resistances before finding current. The same current then gives the internal drop and the load voltage. The source power splits between internal heating and delivered load power; the totals must balance.',
('I = Us / (R₀ + R); U = IR = Us − IR₀','For the finite resistive load shown, while current leaves the positive output terminal.',[['Us','Source EMF, in volts (V).'],['R₀','Internal source resistance, in ohms (Ω).'],['R','External load resistance, in ohms (Ω).'],['I','Common series current, in amperes (A).'],['U','Output voltage from a to b, in volts (V).']]),condition='loaded')
scene('1.3','open-operation','Open: zero current does not mean zero voltage','Follow the consequence of breaking the external path.','conditions',[
'With the external path broken, no steady current crosses it: I = 0. The internal resistor therefore has no IR₀ drop. In this source model, the output voltage is the full 12 V EMF.',
'No load power is delivered, because U × I = 12 × 0 = 0 W. The voltage can exist while the power transfer is zero. With no current in this model, internal I²R₀ heating is also zero.'
],'An ideal voltmeter can indicate an open-circuit voltage without making the open behave like the 4 Ω load.',
'The open path prevents steady current. With no current, the internal resistor drops no voltage, so the output can still have twelve volts across it. The load receives zero power because the current is zero. Zero current and zero voltage are different statements.',
('I = 0; Uoc = Us; Pload = 0','For the disconnected output of this idealised practical source.',[['I','Current through the broken output path, in amperes (A).'],['Uoc','Open-circuit voltage across a–b, in volts (V).'],['Us','Source EMF, in volts (V).'],['Pload','Power transferred to the external load, in watts (W).']]),condition='open')
scene('1.3','short-operation','Short: zero output voltage can accompany large heating','Keep the source’s internal resistance in the calculation.','conditions',[
'The ideal short connects a directly to b, so their voltage difference is zero. The external resistance is zero, but the internal 2 Ω remains. The short current is therefore 12/2 = 6 A.',
'The shorted external terminals deliver U × I = 0 W. Yet the source conversion provides 12 × 6 = 72 W, and I²R₀ = 6² × 2 = 72 W is converted into heat internally. The zero terminal power does not mean that energy conversion stopped.',
'If R₀ were also zero, an ideal nonzero voltage source and an ideal short would impose incompatible constraints. This model would have no finite-current solution. A real short must be analysed with the relevant physical impedances and limits.'
],'Zero terminal voltage does not imply zero source current or zero internal heating.',
'The short fixes the terminal voltage to zero. It does not remove the internal resistance. This source model gives six amperes, and all seventy-two watts of source conversion becomes internal heat. A zero-resistance ideal voltage source short has no finite-current solution; do not invent a current for that different model.',
('Isc = Us / R₀; U = 0; Pinternal = Isc²R₀','The finite short-current relation requires R₀ > 0.',[['Isc','Short-circuit current, in amperes (A).'],['Us','Source EMF, in volts (V).'],['R₀','Nonzero internal resistance, in ohms (Ω).'],['U','Voltage across the ideal short, in volts (V).'],['Pinternal','Heating inside the source, in watts (W).']]),condition='short')
scene('1.3','teacher-power-balance','Use the measured values to reconstruct the source','Work from terminal measurements back to internal resistance and energy loss.','balance',[
'The teacher gives Us = 125 V, terminal U = 115 V and current I = 4 A. A nonzero terminal voltage means this numerical example describes loaded operation, not an ideal short.',
'The internal drop is 125 − 115 = 10 V. Divide that drop by 4 A to find R₀ = 2.5 Ω. The external load at this operating point is U/I = 28.75 Ω.',
'The source conversion provides 125 × 4 = 500 W. The load receives 115 × 4 = 460 W. Their difference, 40 W, is the internal loss; independently, 4² × 2.5 = 40 W. Both ways agree.'
],'Generated, delivered and internally dissipated power describe different places in the same energy account: 500 W = 460 W + 40 W.',
'The teacher gives the source EMF, measured terminal voltage and current. Their voltage difference is the internal drop. Dividing by current gives the internal resistance. Then compare source power with delivered power and check the difference using current squared times internal resistance. The same loss must emerge both ways.',
('R₀ = (Us − U) / I; Psource = Pload + Pinternal','For the supplying source at the given loaded operating point.',[['Us','125 V: source EMF.'],['U','115 V: measured output voltage.'],['I','4 A: delivered current.'],['R₀','Inferred internal resistance, in ohms (Ω).']]),note='Source clarification: the original numerical slide reuses a drawing with a shorting line. Its 115 V output and calculations describe a loaded source. This diagram follows the numerical conditions.')
# Keep explicit symbol definitions and reuse recordings whose narration is unchanged.
_symbol_overrides = {'charge-current': [['I', 'Current: charge crossing each second, measured in amperes (A).'], ['Q', 'Charge crossing the section, in coulombs (C).'], ['t', 'Elapsed time, in seconds (s).'], ['i(t), q(t)', 'Instantaneous current in amperes and charge in coulombs as functions of time.'], ['dq/dt', 'The rate at which charge changes with time: the slope of a charge–time graph, in C/s.']], 'emf-limits': [['Us', 'The source EMF, in volts (V).'], ['U', 'Measured output voltage, in volts (V).'], ['IR₀', 'Current-dependent internal voltage drop, in volts (V).'], ['I', 'Delivered current, in amperes (A).'], ['R₀', 'Internal source resistance, in ohms (Ω); 0 labels the internal part.']], 'teacher-power-balance': [['Us', '125 V: source EMF.'], ['U', '115 V: measured output voltage.'], ['I', '4 A: delivered current.'], ['R₀', 'Inferred internal resistance, in ohms (Ω).'], ['Psource', 'Power converted by the supplying source: Us × I, in watts (W).'], ['Pload', 'Power delivered to the external load: U × I, in watts (W).'], ['Pinternal', 'Power converted to heat internally: I²R₀, in watts (W).']]}
_existing_path=Path('src/lessons.json')
_existing=json.loads(_existing_path.read_text()) if _existing_path.exists() else {}
_audio={item['voice']:item['audio'] for t in _existing.values() for sc in t['scenes'] for item in [sc,*sc.get('phases',[])] if item.get('audio')}
for t in D.values():
 for sc in t['scenes']:
  if sc['id'] in _symbol_overrides:sc['rule']['symbols']=_symbol_overrides[sc['id']]
  for item in [sc,*sc.get('phases',[])]:
   if item['voice'] in _audio:item['audio']=_audio[item['voice']]
Path('src/lessons.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
print(sum(len(l['scenes'])for l in D.values()),'scenes; depths:',{k:len(l['scenes'])for k,l in D.items()})
