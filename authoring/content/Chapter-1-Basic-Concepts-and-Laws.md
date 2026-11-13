# Chapter 1 - The basic concepts and laws of circuits

**Source review:** all 10 lessons, 159 slide pages. This summary follows the actual embedded course documents. Repeated animation frames are combined; distinct concepts, worked examples, and review tasks are retained. A solution labeled **Worked here** completes a question the slides leave unanswered.

**Notation:** the teacher generally uses `U` for voltage, `V_a` for node potential, `U_s` for source EMF/ideal source voltage, and `R₀` for internal resistance. Keep the indicated voltage polarities and current arrows throughout each solution.

## 1.1 Function and components

*Source: 14 pages, especially pp. 3-14.*

A physical circuit combines electrical devices for a purpose. Its circuit model replaces those devices with ideal elements and their connections. The battery-switch-lamp example illustrates the distinction: the physical battery, bulb, wires, and switch become an ideal source, load, connecting lines, and switch in the model. Closing the switch completes a conducting path; opening it interrupts the path.

### Two functions of circuits

| Type | Main purpose | Example from the slides | Main design emphasis |
|---|---|---|---|
| Power circuit | Generate, transmit, and convert electrical energy | Generator, step-up transformer, transmission line, step-down transformer, lights/heater/motor | Efficient energy delivery |
| Signal circuit | Transmit and process information carried by electrical signals | Microphone, amplifier, processing stages, loudspeaker; telephone, CATV, network, Wi-Fi | Signal quality and the required processing effect |

Both types have voltages, currents, and power. Classify them by their principal purpose. A battery lighting a bulb is a power circuit; the pictured temperature-measuring circuit is a signal circuit.

### Three component groups

- **Source:** supplies electrical energy or an electrical signal. Its actual delivered power depends on the connected load.
- **Load:** receives electrical energy and performs a useful conversion, such as producing light, heat, or motion.
- **Intermediate link:** conductors, switches, control devices, protective components, and other transmission connections.

For the torch example, the battery is the source, the bulb is the load, and the switch and spring contacts belong to the intermediate link.

**“Load increase”** means increased power consumption. At an approximately fixed supply voltage, that requires increased load current. It does not generally mean that the resistance increases.

### Terms to know

The course's introductory DC model has constant current and voltage; AC changes direction or polarity with time. Sinusoidal AC follows a sine wave. A two-terminal network connects to the rest of a circuit through two terminals. In the introductory classification used here, a passive network contains no source, whereas an active network contains a source.

**Review:** distinguish physical circuit/model, power/signal circuit, and passive/active network; identify the three component groups in an everyday circuit.

## 1.2 Basic quantities

*Source: 12 pages, especially pp. 3-12.*

The lesson compares six quantities: current, electric potential, voltage, electromotive force, power, and energy.

| Quantity | Meaning | Course relationship and unit |
|---|---|---|
| Current `I` | Rate of charge flow past a point | For constant current, `I = Q/t`; ampere, A |
| Potential `V_a` | Potential of node a relative to a chosen reference | `V_a = U_a0`; volt, V |
| Voltage `U_ab` | Potential difference from a to b | `U_ab = V_a - V_b`; volt, V |
| EMF `E` or `U_s` | Energy supplied per unit charge by the source's non-electric energy-conversion process | volt, V |
| Power `P` | Rate of delivering or absorbing energy | In the shown DC circuits, `P = UI`; watt, W |
| Energy `W` | Accumulated energy transfer | Constant-power case: `W = Pt`; joule, J |

For varying current, the generalization of the first relationship is `i = dq/dt`. Conventional current follows positive-charge motion.

### Potential depends on the reference; voltage differences do not

**Teacher example:** a 10 V source supplies two 2 Ω series resistors. The current is `10/(2+2) = 2.5 A`, and each resistor drops 5 V.

With the source's negative node c as ground, `V_a = 10 V`, `V_b = 5 V`, and `V_c = 0`. With node a as ground, `V_a = 0`, `V_b = -5 V`, and `V_c = -10 V`. In both choices, `U_ab = 5 V` and `U_bc = 5 V`.

Without specifying a reference, those absolute node potentials cannot be uniquely stated. The voltage differences can still be determined.

### EMF versus terminal voltage

Both are measured in volts. EMF describes the source's energy-conversion action; voltage is a potential difference between specified points. An ideal voltage source has terminal voltage equal to its prescribed source voltage. A practical source may have a lower terminal voltage while delivering current because of its internal resistance.

### Power versus energy

Power measures how fast energy is transferred; energy also depends on duration. For source current leaving the positive terminal, `U_s I` is supplied power. For a load current entering its positive terminal, `U_L I` is absorbed power.

**Teacher questions, worked here:**

- Bulb at 6 V and 1.6 A: `P = 6 × 1.6 = 9.6 W`.
- Bulb at 2 V and 10 mA for 30 minutes: `P = 0.020 W`, `t = 1800 s`, so `W = 36 J`.
- `1 kWh = 1000 W × 3600 s = 3.6 × 10⁶ J`.

Do not confuse kW, a power unit, with kWh, an energy unit.

## 1.3 Circuit conditions

*Source: 7 pages, especially pp. 4-7.*

The slides analyze a source `U_s`, internal resistance `R₀`, and external load `R` in three operating conditions.

| Condition | Current | Terminal voltage | External power |
|---|---|---|---|
| Closed/loaded | `I = U_s/(R₀ + R)` | `U = IR = U_s - IR₀` | `P = UI` |
| Open/no load | `I = 0` | For this source model, `U_oc = U_s` | `P = 0` |
| Shorted terminals | `I_sc = U_s/R₀` | `U = 0` | `P_terminal = 0` |

An open circuit has zero branch current, but its voltage can be nonzero. An ideal short has zero voltage, but its current can be nonzero. The open-circuit voltage and short-circuit current depend on the rest of the network.

**Generated versus delivered power:**

`P_s = U_s I`, `ΔP = I²R₀`, and `P = UI = P_s - ΔP`.

A short's zero external terminal power does not mean the source has stopped converting energy: internal heating can be substantial. The finite `I_sc` formula assumes nonzero internal resistance; an ideal zero-resistance voltage-source short has no finite-current solution.

**Teacher example:** `U_s = 125 V`, `U = 115 V`, `I = 4 A`.

- Generated power: `P_s = 125 × 4 = 500 W`.
- Delivered power: `P = 115 × 4 = 460 W`.
- Internal voltage drop: `125 - 115 = 10 V`.
- Internal resistance: `R₀ = 10/4 = 2.5 Ω`.
- Internal loss: `ΔP = 40 W`, agreeing with `I²R₀`.

**Slide clarification:** the example reuses a drawing with a shorting line, but its nonzero terminal voltage and numerical calculation describe loaded operation.

## 1.4 Reference point and reference direction

*Source: 9 pages, all reviewed.*

Choose a reference node and set its potential to zero. This circuit “ground” is a reference choice; it need not be a connection to physical earth. Then `U_ab = V_a - V_b`, and `U_ba = -U_ab`.

**Teacher example 1:** a 10 V source drives 4 Ω, 3 Ω, and 3 Ω in series. `I = 1 A`. With the bottom source terminal d grounded, `V_a = 10 V`, `V_b = 6 V`, and `V_c = 3 V`. Without a ground choice, only differences are determined.

**Teacher example 2:** two equal series resistors connect between nodes at `V_a = 12 V` and `V_b = -10 V`. Their midpoint has

`V_c = V_b + (V_a - V_b)/2 = -10 + 11 = 1 V`.

### Reference directions

Assign a current arrow and a voltage reference before calculating. A positive answer agrees with the reference; a negative answer indicates the opposite actual direction or polarity.

The teacher represents voltage direction in three equivalent ways: an arrow, `+/-` terminal marks, or ordered subscripts such as `U_AB`. In the course's arrow convention, the voltage arrow points from the referenced positive terminal toward the referenced negative terminal.

For a resistor, `U = RI` when current enters the terminal marked positive. If its current reference is reversed while the voltage reference is retained, use `U = -RI`.

**Exam habit:** never change an arrow halfway through a calculation without also changing the associated signed variable.

## 1.5 Ideal circuit elements

*Source: 16 pages, especially pp. 2-16.*

The course separates passive elements R, L, C from ideal active voltage and current sources.

| Element | Law with passive voltage/current references | Meaning |
|---|---|---|
| Resistor | `u = Ri` | Voltage is proportional to current |
| Inductor | `u_L = L di_L/dt` | Voltage depends on current's rate of change |
| Capacitor | `i_C = dq/dt = C du_C/dt` | Current depends on voltage's rate of change |

The inductor diagram also shows its induced EMF `e`, with `u_L = -e`; the opposing EMF is consistent with Lenz's law.

### Ideal sources

An independent ideal voltage source fixes its prescribed voltage; the external circuit determines its current. An independent ideal current source fixes its prescribed current; the external circuit determines its voltage. The examples use constant sources, though prescribed sources can also vary with time.

**Teacher voltage-source example:** a 10 V source supplies one 2 Ω resistor at 5 A. Adding a second 2 Ω resistor in parallel makes the total current 10 A; the source voltage remains 10 V.

**Teacher current-source example:** a 1 A source gives 1 V across 1 Ω and 10 V across 10 Ω. The source current remains 1 A.

### A source can absorb power

Use the passive convention for **absorbed** power: `p_abs = ui` when the referenced current enters the positive voltage terminal. Negative absorbed power means delivery. Identify actual direction or use signed variables consistently; the word “source” alone does not determine the power sign.

The teacher's five power questions are completed below. Each uses an upward 3 A current source and a voltage source with 3 V, positive at the top.

| Circuit in the slide | Resistor absorption | Voltage-source absorption | Current-source delivery |
|---|---:|---:|---:|
| Only the two sources, connected in one loop | - | 9 W | 9 W |
| Add a 1 Ω resistor in parallel | 9 W | 0 W | 9 W |
| Add a 0.5 Ω resistor in parallel | 18 W | -9 W, so it supplies 9 W | 9 W |
| Add a 2 Ω resistor in parallel | 4.5 W | 4.5 W | 9 W |
| Put a 1 Ω resistor in series along the top connection | 9 W | 9 W | 18 W |

**Worked here:** the parallel cases follow `I_R = 3/R`; the voltage-source downward current is `3 - I_R`. In the series case the resistor drops 3 V, so the current source sustains 6 V and supplies 18 W. Every row satisfies power conservation.

## 1.6 Practical sources and source transformation

*Source: 18 pages, including the worked example and final review.*

A practical voltage source has an ideal voltage source in series with resistance:

`U = U_s - IR`.

Its terminal voltage falls as delivered current increases. A practical current source has an ideal current source in parallel with resistance:

`I_out = I_s - U/R`.

The two descriptions have the same external terminal behavior when

`I_s = U_s/R`, `U_s = I_s R`, and the resistance is unchanged.

The current-source arrow points toward the voltage source's positive terminal. For finite nonzero R, change series resistance into parallel resistance, or the reverse.

**Conditions emphasized in the slides:** transform practical source combinations, not isolated ideal sources into finite equivalents. Equivalence is external: internal currents, powers, and component behavior can differ.

**Teacher example:** a 10 V source in series with 2 Ω becomes a 5 A source in parallel with 2 Ω. Connecting a 3 Ω load gives `I_L = 10/(2+3) = 2 A` in either representation. In the current-source version, current division gives the same result.

For two parallel resistors carrying total current I:

`I₁ = [R₂/(R₁+R₂)]I`, `I₂ = [R₁/(R₁+R₂)]I`.

### Main course example

The slides show a 5 V source, a 2 kΩ resistor feeding a central node, a 1 kΩ shunt, a 2 mA source injecting into the node, and a series path of 1 kΩ plus the 2 kΩ load. There is also a 2 kΩ resistor directly across the ideal voltage source and a 2 kΩ resistor in series with the ideal current source.

For the external load calculation, the last two resistors can be omitted: a parallel resistor cannot change an ideal voltage source's imposed terminal voltage, and a series resistor cannot change an ideal current source's imposed current. This simplification does not preserve their internal power.

1. Transform `5 V + series 2 kΩ` into `2.5 mA || 2 kΩ`.
2. Combine the same-direction current sources: `2.5 + 2 = 4.5 mA`.
3. Combine the shunts: `2 kΩ || 1 kΩ = 2/3 kΩ`.
4. The external branch is `1 + 2 = 3 kΩ`.
5. Current division gives `I_load = 4.5 × (2/3)/(3+2/3) = 9/11 mA ≈ 0.818 mA`, downward.

**Final review circuit, worked here:** a `40 V + 2 Ω` branch and a `20 V + 2 Ω` branch supply a 4 Ω load in parallel. Transform them into 20 A and 10 A sources; combine to `30 A || 1 Ω`. The load current is `30 × 1/(1+4) = 6 A`, downward, with 24 V across the load.

## 1.7 Kirchhoff's Laws

*Source: 31 pages, including topology exercises, generalized nodes, and generalized loops.*

KCL and KVL apply to the usual lumped DC and AC models, including nonlinear elements. Linearity is a requirement of superposition, not a requirement for these conservation laws.

### Topology vocabulary

The teacher uses **node** for an essential junction where three or more elements meet and **branch** for the current path between such nodes; a branch can contain several series elements. A loop is any closed path. The slide calls a mesh an independent loop; in standard planar-circuit terminology, a mesh is a loop with no smaller loop inside it. A suitable set of meshes provides independent loop equations.

The four counting examples give:

| Slide example | Essential nodes | Branches | Closed loops | Meshes |
|---|---:|---:|---:|---:|
| Three parallel paths | 2 | 3 | 3 | 2 |
| Four parallel paths | 2 | 4 | 6 | 3 |
| Bridge network | 4 | 6 | 7 | 3 |
| Five-branch network used again in 1.8 | 3 | 5 | 6 | 3 |

Count connected conductors as one node. Distinguish all possible loops from an independent equation set.

### KCL: current balance

The algebraic sum of currents at a node is zero: `Σi = 0`. With entering currents positive, the teacher's five-current example gives

`I₁ + I₃ - I₂ - I₄ - I₅ = 0`, or `I₁ + I₃ = I₂ + I₄ + I₅`.

**Generalized node:** draw a closed boundary around several components. Internal currents cancel; the currents crossing its boundary still balance. The transistor and triangular-network examples give `I₁ + I₂ = I₃`. In the final two-junction example, `I₁ + I₂ = I₃ = I₄ + I₅`.

### KVL: voltage balance

The algebraic sum of voltage changes around a closed path is zero: `Σu = 0`. Choose a traversal direction and apply the polarity signs consistently. For the four-voltage rectangle in the slides:

`U₁ - U₂ + U₃ - U₄ = 0`.

For the opposing-source/resistor example, the chosen traversal gives

`U_s2 + R₂I₂ + R₁I₁ - U_s1 = 0`.

Reversing the traversal reverses every sign and gives an equivalent equation.

**Generalized loop:** an imaginary closing path can include the terminal voltage between two points. A branch consisting of a positive-at-top source and a series resistor has `U = U_s + RI` if I enters its top terminal, and `U = U_s - RI` if I leaves its top terminal. The difference comes from the current reference, not from changing the source itself.

## 1.8 Branch Current Analysis

*Source: 11 pages, all reviewed.*

The purpose is to find the current in each branch of a complex network using KCL, KVL, and element laws.

1. Assign branch-current references and loop traversal directions.
2. Write KCL at independent nodes.
3. Write KVL around independent loops or meshes.
4. Solve the simultaneous equations and interpret the signs.

For a connected graph with n nodes and b branches, there are `n-1` independent KCL equations and `b-n+1` independent loop equations. Apply these counts consistently with the graph/branch definition.

### Teacher's five-branch example

![Original course slide, lesson 1.8, page 8: assigned branch-current references.](assets/branch-current-references.png)

*Original course slide, lesson 1.8, page 8: assigned branch-current references.*

The bottom node is common. At left top node a, `I₁` arrives upward through `U_s1, R₁`, `I₃` leaves downward through `R₃`, and `I₅` crosses `R₅` to right top node b. At b, `I₂` arrives upward through `U_s2, R₂`, and `I₄` leaves downward through `R₄`.

Use these two independent node equations:

`I₁ - I₃ - I₅ = 0`

`I₅ + I₂ - I₄ = 0`.

The bottom-node equation `I₃ + I₄ - I₁ - I₂ = 0` follows from them and adds no independent information.

The three loop equations are:

`I₃R₃ + I₁R₁ - U_s1 = 0`

`I₅R₅ + I₄R₄ - I₃R₃ = 0`

`U_s2 - I₂R₂ - I₄R₄ = 0`.

There are five independent equations for five branch currents. The slides give symbolic component values, so the intended result is the equation system, not a particular numerical current.

## 1.9 Superposition theorem

*Source: 15 pages, including five examples.*

In a linear network, a branch voltage or current is the algebraic sum of the responses produced by the independent sources acting separately. The purpose is to simplify calculation.

To analyze one source's contribution, replace every other independent ideal voltage source with a short and every other independent ideal current source with an open. Preserve internal resistances. If dependent sources occur in another problem, retain them; the course examples use independent sources.

Repeat for the remaining sources and add signed currents or voltages using the same references. Sources may also be divided into groups; each contribution need not contain exactly one source.

**Power cannot be superposed:** `R(I₁+I₂)²` is not generally `RI₁² + RI₂²`.

### Course examples

| Example | Essential setup | Result |
|---|---|---|
| E1 | Two voltage-source branches and a central resistor | Add each branch's two signed contributions separately |
| E2 | Upward 4 A source with a series 10 Ω branch; central 10 Ω; right 10 Ω and a 20 V source positive at the bottom | Central downward current `2 A + (-1 A) = 1 A` |
| E3 | 7 A source, 35 V source, and 1 Ω, 2 Ω, 3 Ω, 4 Ω network | Marked rightward 4 Ω current `3 A + 5 A = 8 A` |
| E4 | 3 A upward left source, 5 A downward right source, 10 V bottom source, 2 Ω and 3 Ω middle paths, 4 Ω upper path | **Worked here:** marked bottom leftward current `6.2 A` |
| E5 | 18 V + 1 Ω and 9 V + 1 Ω branches in parallel with a 4 Ω load | **Worked here:** downward load current `2 A + 1 A = 3 A` |

**E4 check:** set the right bottom node to 0 V and the left bottom node to 10 V. KCL at the top requires 2 A from the middle node upward through 4 Ω. The middle-node equation is `(V_m-10)/2 + V_m/3 + 2 = 0`, giving `V_m = 3.6 V`. The left node supplies `3 A + (10-3.6)/2 = 6.2 A`, matching the indicated bottom return-current direction.

**E5 check:** with only 18 V active, the other 1 Ω branch remains after its source is shorted. The top node is 8 V and the load gets 2 A. With only 9 V active, the node is 4 V and the load gets 1 A. Together it is 12 V and 3 A.

## 1.10 Equivalent Source Theorem

*Source: 26 pages, including Thévenin and Norton treatments of the same circuit.*

Replace an active linear two-terminal network by a simpler network that has the same terminal voltage-current relationship.

| Equivalent | Source value | Resistance connection |
|---|---|---|
| Thévenin | `U_th = U_oc`, the open-circuit voltage at the selected port | `R₀` in series |
| Norton | `I_N = I_sc`, the short-circuit current at that port | The same `R₀` in parallel |

Find `R₀` by suppressing independent sources and looking into the port. When the values are finite and the ratio is defined, `R₀ = U_oc/I_sc`. In networks containing dependent sources, a test source may be needed; do not suppress dependent sources.

Remove **only the external load** before calculating the equivalent. The selected port can lie between two nodes neither of which is the ground node.

### Teacher's 8 Ω bridge-load example

![Original course slide, lesson 1.10, page 6: the selected port after removing the 8 Ω load.](assets/thevenin-load-port.png)

*Original course slide, lesson 1.10, page 6: the selected port after removing the 8 Ω load.*

The 8 Ω load connects nodes a and b. On the left, an 8 V source with series 2 Ω is in parallel with another 2 Ω. On the right, a downward 3 A source is in parallel with a 5 V source and series 5 Ω. The bottom connection stays in place when the 8 Ω load is removed.

1. **Open-circuit voltage:** the left divider gives `V_a = 4 V`. The right node has `V_b = -10 V`. Therefore `U_ab = 4 - (-10) = 14 V`.
2. **Equivalent resistance:** short both ideal voltage sources and open the ideal current source. Looking from a to b gives `R₀ = (2 Ω || 2 Ω) + 5 Ω = 6 Ω`.
3. **Thévenin load current:** `I = 14/(6+8) = 1 A`, from a to b.
4. **Norton equivalent:** `I_N = 14/6 A`, in parallel with 6 Ω. Current division through the 8 Ω load again gives 1 A.

The two methods describe the same external behavior. Choose whichever source representation makes the load calculation simpler.

## Chapter 1 revision checklist

You should be able to identify circuit function and component roles; distinguish reference-dependent potential from voltage difference; calculate internal source loss; interpret current/voltage signs; explain when a source absorbs power; transform practical sources; count essential nodes and independent loops; write the five-branch equation system; suppress sources correctly for superposition; and derive Thévenin/Norton equivalents at the chosen load port.
