# Chapter 2 - Transient analysis

**Source review:** all four indexed lessons, six embedded documents, 100 slide pages. The 2.4 document also contains **2.5 Transient Analysis for RL Circuit**, which is included below. A solution labeled **Worked here** completes an unanswered slide question. Equations use passive voltage/current references unless stated otherwise.

## 2.1 Basic concept

*Source: 25 pages, all reviewed.*

A transient is the interval during which a circuit changes from one operating state to another. For the DC circuits in this lesson, a steady state has constant currents and voltages after the effects of switching have settled. In AC, steady state may instead be periodic; “steady” does not universally mean constant.

Switching can change the circuit's connections, component parameters, or power supply. A nontrivial transient occurs when the change requires stored energy to redistribute over time.

### The three-lamp demonstration

| Branch | Observation after the switch closes | Explanation |
|---|---|---|
| Resistor and lamp | Lamp lights immediately and remains steady | The ideal resistor stores no field energy |
| Inductor and lamp | Lamp gradually becomes bright | Inductor current builds continuously |
| Capacitor and lamp | Lamp initially flashes, then fades | Charging current decreases as capacitor voltage rises |

For an initially unenergized simple RC circuit, capacitor voltage rises from 0 toward `U_s`. For a simple RL circuit, inductor current rises from 0 toward `U_s/R`. A purely resistive ideal circuit can move immediately to its new algebraic operating point.

### Why the capacitor voltage and inductor current matter

A capacitor stores electric-field energy:

`W_e = ½ C u_C²`.

An inductor stores magnetic-field energy:

`W_m = ½ L i_L²`.

For ordinary finite excitation, these state variables cannot jump instantaneously. A capacitor voltage jump would require an impulsive current; an inductor current jump would require an impulsive voltage. That is why the chapter focuses on `u_C` and `i_L`.

### Applications included in the actual slides

- **RC time delay:** the capacitor takes time to reach a chosen voltage threshold.
- **Inductive spark generator:** closing the circuit builds magnetic energy; interrupting its current produces a high induced voltage that can form a spark.
- **Fluorescent-lamp starting:** the starter and inductive ballast use a transient to help initiate discharge.
- **Equipment behavior:** transients can create large voltages or currents. Studying them allows useful effects to be designed and unwanted stresses to be controlled.

The idealized “energy cannot change suddenly” explanation presumes an ordinary switching event with finite excitation, not a deliberately imposed ideal impulse.

## 2.2 Switching law

*Source: 9 pages, including three example circuits.*

Set the switching event to `t = 0`. Use `0⁻` for immediately before it and `0⁺` for immediately after it.

`u_C(0⁺) = u_C(0⁻)`

`i_L(0⁺) = i_L(0⁻)`.

Continuity at one instant does not mean the quantity never changes afterward. Capacitor current and inductor voltage are not subject to these continuity constraints and can jump.

### DC steady-state replacements

Once a DC steady state is established:

- Capacitor: open circuit, because `du_C/dt = 0` gives `i_C = 0`.
- Inductor: short circuit, because `di_L/dt = 0` gives `u_L = 0`.

These are **steady-state** replacements. At `0⁺`, retain the storage state instead of automatically replacing an inductor with a short or a capacitor with an open.

### Course examples

**E1: combined steady-state circuit.** A 6 V source feeds a 2 Ω resistor, followed by three parallel branches: 2 Ω, 2 Ω plus L, and C. In DC steady state, L shorts and C opens. The two remaining branches give `2 Ω || 2 Ω = 1 Ω`, so total current is `6/(2+1) = 2 A`. Each conducting branch carries 1 A, capacitor current is zero, capacitor voltage is 2 V, and inductor voltage is zero.

**E2: bypassing a source-side resistor.** A 6 V source initially supplies a 2 kΩ feed resistor and two branches: `2 kΩ + L` and `1 kΩ + C`. In the pre-switch steady state, `i_L = 1.5 mA` and `u_C = 3 V`. The switch then bypasses the feed resistor. At the instant afterward, the same inductor current and capacitor voltage remain. Other variables are recalculated in the new topology; the expanded solution appears in 2.3 below.

**E3: initially disconnected network.** A source connects through R to parallel branches `R₁`, `R₂ + L`, and C. With the passive network initially unenergized, `u_C(0⁺)=0` and `i_L(0⁺)=0`. **Worked here:** the capacitor clamps the parallel-node voltage to zero at that instant, giving `i_R1(0⁺)=0`, `u_L(0⁺)=0`, and source/capacitor current `6/R`. These conclusions depend on the stated unenergized initial condition.

## 2.3 Three-element method for first order circuit

*Source: three documents: overview, 14 pages; initial value, 16 pages; final value and time constant, 22 pages. All reviewed.*

A first-order circuit has one independent energy-storage state, or an equivalent single storage element, and a first-order differential equation. The classical method solves that equation. The three-element method obtains the same response from three quantities:

1. Initial value `f(0⁺)`.
2. Final steady-state value `f(∞)`.
3. Time constant `τ`.

For a stable first-order linear circuit with constant post-switch excitation and fixed topology:

`f(t) = f(∞) + [f(0⁺) - f(∞)]e^(−t/τ)`, for `t ≥ 0`.

The final value is the destination; the exponential term describes the remaining difference from that destination. Use the formula separately for each interval if switching occurs again.

### Why the formula works

For a series RC circuit, KVL and the capacitor law give

`U = Ri + u_C`, `i = C du_C/dt`.

Therefore `RC du_C/dt + u_C = U`, with solution

`u_C(t) = U + (U₀ - U)e^(−t/RC)`.

For a series RL circuit:

`U = Ri_L + L di_L/dt`,

so

`i_L(t) = U/R + (I₀ - U/R)e^(−tR/L)`.

The teacher then applies Thévenin/Norton equivalence to reduce more complex first-order networks to a simple RC or RL circuit. This is the bridge between Chapters 1 and 2.

### A. Finding initial values

Analyze the **pre-switch** circuit to find `u_C(0⁻)` and `i_L(0⁻)`. Use the switching laws to obtain their `0⁺` values. Then analyze the **post-switch** circuit to determine the other initial currents and voltages.

At `0⁺`, a capacitor with a known voltage can be represented momentarily by that voltage constraint, and an inductor with a known current by that current constraint. These are tools for the instant-specific calculation, not replacements valid for all later times.

The initial-value document contains six examples:

| Example | Circuit situation | Initial result |
|---|---|---|
| E1 | 6 V source and 2 kΩ feed, an inductor, and a switched 2 kΩ shunt | **Worked here:** if initially in DC steady state, `i_L(0⁺) = 3 mA`; the shunt does not change that instantly |
| E2 | 10 V source newly connected through 1 kΩ and L to a parallel 10 kΩ resistor and capacitor, with `u_C(0⁻)=0` | **Worked here:** initially unenergized L has `i_L(0⁺)=0`, and KCL gives capacitor current zero at that instant |
| E3 | 1 A source initially feeding `2 kΩ + L`; a 1 kΩ parallel branch closes | `i_L(0⁻)=i_L(0⁺)=1 A`; new branch current is initially zero |
| E4 | 6 V source, bypassed 2 kΩ feed, `2 kΩ + L` and `1 kΩ + C` branches | `u_C(0⁺)=3 V`, `i_L(0⁺)=1.5 mA`, `i_C(0⁺)=3 mA`, source current `4.5 mA`, and `u_L(0⁺)=3 V` |
| E5 | Initially unenergized 1 H inductor connected through 1 kΩ to 20 V | `i_L(0⁺)=0`; `u_L(0⁺)=20 V` |
| E6 | Steady 20 V, 1 kΩ, 1 H circuit interrupted, leaving a 500 kΩ voltmeter in its discharge path | Current initially remains `20 mA`; meter-voltage magnitude is `0.020 × 500,000 = 10,000 V` |

**E4 reasoning:** before switching, the capacitor branch is open and the inductor is a short, giving `6 V/(2k+2k)=1.5 mA` and a 3 V node. After bypassing the feed resistor, the node jumps to 6 V while the capacitor stays at 3 V. Thus `i_C=(6-3)/1k=3 mA`; the 2 kΩ inductor branch still carries 1.5 mA and drops 3 V across its resistor, leaving 3 V across L.

**E6 polarity clarification:** the slide prints 10 kV as a positive value. With its downward meter-voltage reference retained, the inductor's continuing discharge current actually makes the top meter terminal negative, so the signed meter reading is `−10 kV`. The magnitude is 10 kV. The lesson lists wire-explosion spraying, spot welding, electronic ignition, and flash lamps as related transient applications.

**Scope caution:** some initial-value examples contain both L and C. Their switching laws remain valid, but that does not make the complete two-storage-element response a single first-order exponential.

### B. Finding final values

Use the **post-switch** topology. For its final DC steady state, open capacitors and short inductors, then solve the resulting resistive network.

**Teacher E1:** a 4 mA source feeds two identical conducting 3 Ω branches after the inductor shorts. The inductor-branch final current is `2 mA`.

**Teacher E2:** two 4 kΩ resistors connect in parallel between the 10 V source's top node and the capacitor node; a 3 kΩ resistor connects that node to the bottom rail. The capacitor opens at infinity, giving

`u_C(∞) = 10 × 3/(4||4 + 3) = 10 × 3/5 = 6 V`.

### C. Finding time constants

`τ_RC = R_seen C`, `τ_RL = L/R_seen`.

Find `R_seen` looking into the storage element's terminals in the **post-switch** circuit. Suppress independent sources: voltage sources become shorts and current sources become opens. Keep the circuit's relevant resistances.

A larger τ means a slower response. At one τ, a charging waveform has completed 63.2% of its initial-to-final change; the remaining error is 36.8%.

| Time | Remaining initial-to-final difference |
|---|---:|
| `τ` | 36.8% |
| `2τ` | 13.5% |
| `3τ` | 5.0% |
| `4τ` | 1.8% |
| `5τ` | 0.67% |

The slides call `t ≥ 3τ` approximately settled. That corresponds to accepting about 5% remaining error; 5τ is a stricter approximation. Neither is an exact endpoint.

**RL time-constant example:** opening the suppressed current source removes its series 2 Ω feed branch from the resistance seen by the inductor. The two remaining 3 Ω resistors form 6 Ω in the discharge path. With `L = 1 H`, `τ = 1/6 s`.

**RC time-constant example:** suppressing the 10 V source makes two upper 6 kΩ resistors and the lower 3 kΩ resistor all appear in parallel from the capacitor terminals. Thus

`R_seen = 6k || 6k || 3k = 1.5 kΩ`, and `τ = 1500 C` seconds when C is in farads.

**Slide correction:** the printed answer says 1.5 Ω, but the resistor labels require **1.5 kΩ**. No numerical capacitance is provided in that example.

**Final bridge review, worked here:** an 18 V supply feeds two dividers: `3 kΩ over 6 kΩ` on the left and `6 kΩ over 3 kΩ` on the right, with C between their midpoints. At infinity, the midpoint voltages are 12 V and 6 V, so capacitor voltage is 6 V with the left plate positive. With the source shorted, `R_seen = (3k||6k) + (6k||3k) = 4 kΩ`, so `τ = 4000 C` seconds.

**Units:** `1 F = 10⁶ µF = 10¹² pF`; `kΩ × µF = ms`.

## 2.4 Transient Analysis for RC Circuit

*Source: 14 pages; pp. 1-10 cover RC response types, and pp. 11-14 contain the embedded RL material.*

### Zero-state response

There is no initial stored energy; the source creates the response. For an initially uncharged capacitor connected through R to `U_s`:

`u_C(0⁺)=0`, `i_C(0⁺)=U_s/R`, `u_C(∞)=U_s`, `i_C(∞)=0`, `τ=RC`.

Therefore

`u_C(t) = U_s(1-e^(−t/RC))`

`i_C(t) = (U_s/R)e^(−t/RC)`.

Voltage rises continuously; current starts at its maximum and decays. The current formula also follows by differentiating the voltage: `i_C=C du_C/dt`.

### Zero-input response

Disconnect the source and allow an initially charged capacitor of voltage `U₀` to discharge through R:

`u_C(t) = U₀e^(−t/RC)`.

For current referenced **into the capacitor's positive terminal**:

`i_C(t) = -(U₀/R)e^(−t/RC)`.

The negative sign means actual discharge current leaves the positive plate. The voltage and stored energy decrease, while energy is dissipated in R.

### Complete response

The source and initial stored energy both contribute. The slides switch a capacitor, initially settled at `U_s1`, to a second source `U_s2` through R:

`u_C(t) = U_s2 + (U_s1-U_s2)e^(−t/RC)`

`i_C(t) = [(U_s2-U_s1)/R]e^(−t/RC)`.

If `U_s2 > U_s1`, voltage rises; if `U_s2 < U_s1`, it falls. The same formula covers either case.

**Slide correction:** the small initial/final-value table beside the complete-response example repeats values from the zero-state example. The displayed main equation correctly requires `u_C(0⁺)=U_s1` and `i_C(0⁺)=(U_s2-U_s1)/R`.

**Useful consequence, worked here:** to find the time to reach a target strictly between the initial and final values, rearrange the exponential:

`t = -τ ln[(u_target-u_final)/(u_initial-u_final)]`.

Check that the ratio is positive and the target lies on the waveform's path.

## Embedded 2.5 - Transient Analysis for RL Circuit

![Original course slide, lesson 2.4 document, page 14: the embedded RL decay example.](assets/rl-decay-example.png)

*Original course slide, lesson 2.4 document, page 14: the embedded RL decay example.*

This material is in the 2.4 document and is part of the reviewed theory coverage even though it has no separate course-index entry.

**Teacher example:** a 3 A source initially feeds a 2 Ω series resistor and then parallel branches of 2 Ω and `1 Ω + 1 H`. At pre-switch DC steady state, the inductor shorts. Current division gives `i_L(0⁻)=2 A`.

The switch then disconnects the current source and grounds the left end of the feed resistor, leaving a discharge network.

- Initial current: `i_L(0⁺)=2 A`.
- Final current: `i_L(∞)=0`.
- Resistance seen by L: `R_seen=1+(2||2)=2 Ω`.
- Time constant: `τ=1/2=0.5 s`.

Hence

`i_L(t)=2e^(−2t) A`.

The inductor voltage, with the marked downward passive reference, is

`u_L(t)=L di_L/dt=-4e^(−2t) V`.

The current remains positive while its derivative and voltage are negative: the inductor releases its stored energy into the resistors.

## Chapter 2 problem-solving sequence

Draw separate pre-switch and post-switch circuits. Determine the stored state before switching. Carry only the correct state variables through `0⁺`. Use the new topology for other initial quantities, final values, and resistance seen by the storage element. Substitute into the first-order formula, then verify its value at zero, its limit at infinity, its units, and its direction of change.

**Common mistakes:** assuming every capacitor starts at zero; using the old topology for τ; forcing capacitor current or inductor voltage to remain continuous; losing the discharge-current sign; treating 3τ as exact settling; or applying a single exponential to a circuit with two independent storage states.
