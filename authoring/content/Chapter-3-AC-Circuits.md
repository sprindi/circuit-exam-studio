# Chapter 3 - AC circuits

**Source review:** all six lessons, eight embedded documents, 71 slide pages. This summary follows the course's **sine-wave reference** and uses RMS phasors unless a peak-value phasor is explicitly indicated. A solution labeled **Worked here** completes a question or extends a derivation; it is not an answer quoted from the slides.

## 3.1 Basic concept

*Source: 13 pages, all reviewed.*

The alternator drawings introduce a rotating coil in a magnetic field. As its orientation changes, the induced voltage varies and reverses polarity. AC is voltage that reverses polarity or current that reverses direction over time; a changing magnitude alone is insufficient.

In the waveform-identification question, the bipolar triangular, square, and sinusoidal waveforms are AC. The positive-only pulse train and rectified waveform are unidirectional pulsating signals, not AC in the classification used by this lesson.

### Three defining parameters of a sinusoid

The teacher writes

`i(t)=I_m sin(ωt+ψ)`.

| Symbol | Meaning | Unit |
|---|---|---|
| `i(t)` | Instantaneous current | A |
| `I_m` | Peak amplitude | A |
| `ω` | Angular frequency | rad/s |
| `ψ` | Initial phase | radians or degrees, consistently |
| `f` | Cycles per second | Hz |
| `T` | Period | s |

`T=1/f` and `ω=2πf=2π/T`.

The teacher's waveform example has `f=2 Hz`, `T=0.5 s`, and `ω=4π rad/s`. Frequency, period, and angular frequency express the same repetition rate in different forms.

### Instantaneous, peak, and effective values

The course uses lower-case `e, i, u` for instantaneous values; `E_m, I_m, U_m` for amplitudes; and `E, I, U` for effective or RMS values.

For pure sinusoids:

`I=I_m/√2`, `U=U_m/√2`, `E=E_m/√2`.

RMS represents the equivalent heating effect in a resistor. A complete-cycle signed sine average is zero, but its RMS value and heating effect are not zero. The familiar 220 V and 380 V sinusoidal supply ratings are RMS values. Ordinary AC-meter readings are interpreted as RMS for the intended sinusoidal operating conditions; an oscilloscope shows the instantaneous waveform, from which peak values can be measured.

**Teacher's heater question, worked here as an ideal-resistor calculation:** a constant-resistance heater rated at 300 V would dissipate `(220/300)²≈0.538` of its rated power at 220 V RMS. Comparing only the AC peak with the DC rating gives the wrong heating comparison. This calculation does not establish the suitability of a particular appliance.

### Phase and phase difference

Phase is the full angle `ωt+ψ`; initial phase is its value at `t=0`. A fixed phase difference is meaningful when comparing same-frequency sinusoids expressed with the same sine/cosine reference.

**Teacher examples:**

- `i=10 sin(1000t+30°) A`: initial phase `+30°`.
- `u=311 sin(314t-60°) V`: initial phase `-60°`.
- With `i=100 sin(314t+30°)` and the above voltage, `φ=ψ_u-ψ_i=-60°-30°=-90°`. Voltage lags current by 90°, or current leads voltage by 90°.

Strictly, convert angular terms to a consistent unit when evaluating a waveform numerically; a notation mixing `ωt` and a degree-marked offset is shorthand for that conversion.

For `φ=ψ_u-ψ_i`: positive φ means voltage leads current; negative φ means voltage lags current. Zero means in phase; ±180° means opposite phase.

**Questions present but not answered in the slides:** why supply systems use 50/60 Hz, what frequency an electronic fluorescent ballast uses, and advantages of high-frequency operation. Retain these as discussion topics; no single numerical ballast frequency is supplied in the reviewed material.

## 3.2 Phasor representation

*Sources: rotating-vector/complex-number document, 10 pages; sinusoidal-AC phasor document, 7 pages.*

### From sine wave to phasor

The y-component of an anticlockwise rotating vector produces a sine wave. At one frequency, the relative positions of the vectors stay fixed; representing their magnitudes and initial angles gives phasors that are easier to add and divide than time-varying sine expressions.

A phasor contains magnitude and phase. Its frequency is part of the shared problem context and is not encoded in the phasor alone.

### Four forms of a complex number

`a+jb = M(cosψ+j sinψ) = M e^(jψ) = M∠ψ`, where `j²=-1`.

These are rectangular, trigonometric, exponential, and polar forms. The slide calls the trigonometric form “triangular”; the formulas show what is meant.

`M=√(a²+b²)`, `a=M cosψ`, `b=M sinψ`. Use the correct quadrant when finding ψ; `atan2(b,a)` handles this reliably.

| Operation | Convenient form | Rule |
|---|---|---|
| Add/subtract | Rectangular | Combine real and imaginary parts separately |
| Multiply | Polar | Multiply magnitudes; add angles |
| Divide | Polar | Divide magnitudes; subtract angles |

**Teacher examples:**

- `1+j=√2∠45°`; `j=1∠90°`.
- `(1+j)+(5+j6)=6+j7`.
- `(1+j)/(√3/2+j/2)=√2∠15°`.
- `(1+j)(1/2+j√3/2)/(√3/2+j/2)=√2∠75°`.

Multiplication by `j=e^(j90°)` rotates a phasor anticlockwise by 90°. Multiplication by `-j=e^(−j90°)` rotates it clockwise by 90°. Neither changes magnitude.

### RMS versus peak phasors

Using the course's sine reference:

`i(t)=√2 I sin(ωt+ψ)` corresponds to RMS phasor `Ĩ=I∠ψ`.

For example, `20√2 sin(1000t+30°)` has RMS phasor `20∠30° A` and peak phasor `20√2∠30° A`. In contrast, `20 sin(1000t+30°)` has RMS phasor `(20/√2)∠30° A`.

The teacher marks the attempted conversion from `Ĩ=20∠30°` directly to `20 sin(1000t+30°)` as wrong: the RMS/peak factor is missing, and the phasor alone did not specify 1000 rad/s. If ω is supplied elsewhere, the correct waveform is `20√2 sin(ωt+30°)`.

### Teacher's current-addition example

`i₁=12.7√2 sin(314t+30°) A`

`i₂=11√2 sin(314t-60°) A`.

Convert to RMS phasors:

`Ĩ₁=12.7∠30°`, `Ĩ₂=11∠-60°`.

Add in rectangular form:

`Ĩ≈(11.00+j6.35)+(5.50-j9.526)=16.499-j3.176 A`.

Therefore

`Ĩ≈16.8∠-10.9° A`

`i(t)≈16.8√2 sin(314t-10.9°) A`.

The RMS current is about 16.8 A, not 23.7 A. These two phasors can be added directly because their frequency is the same.

## 3.3 Single parameter AC circuit

*Source: 6 pages, all reviewed.*

The lesson compares time waveforms, phasor diagrams, effective-value relationships, and phasor equations for ideal R, L, and C.

| Element | RMS magnitude relation | Phasor equation | Phase relationship |
|---|---|---|---|
| Resistor | `U=RI` | `Ũ=RĨ` | Voltage and current in phase |
| Inductor | `U=X_L I`, `X_L=ωL=2πfL` | `Ũ=jX_LĨ` | Voltage leads current by 90° |
| Capacitor | `U=X_C I`, `X_C=1/(ωC)=1/(2πfC)` | `Ũ=-jX_CĨ` | Current leads voltage by 90° |

With `i=I_m sinωt`, the inductor law gives `u_L=ωLI_m cosωt`, explaining the voltage lead. With `u_C=U_m sinωt`, the capacitor law gives `i_C=ωCU_m cosωt`, explaining the current lead.

Inductive reactance grows with frequency. Capacitive reactance magnitude decreases with frequency. `X_C` in this table is a positive magnitude; the capacitor impedance is negative imaginary.

**Corrections to the actual slides:** the capacitor caption incorrectly says voltage leads current; its waveform and phasor diagram show current leading. Its phasor equation, repeated in the summary, also prints `X_L` instead of `X_C`. Use `Ũ=-jX_CĨ`.

## 3.4 Series AC circuit

*Sources: series RLC, 11 pages; series impedance, 4 pages.*

### Series RLC

The same current passes through all series elements. KVL holds for instantaneous voltages and for their corresponding phasors:

`Ũ=Ũ_R+Ũ_L+Ũ_C=[R+j(X_L-X_C)]Ĩ`.

Define

`Z=R+jX`, with `X=X_L-X_C`.

`|Z|=√(R²+X²)`, `φ=argZ`, and `Ĩ=Ũ/Z`.

For positive R, `φ=arctan(X/R)`. For general complex numbers, retain the correct quadrant.

**Phasor versus magnitude:** `Ũ=ZĨ` contains magnitude and phase; `U=|Z|I` contains magnitudes only. Do not write a complex impedance in a scalar-magnitude equation as though it were a real resistance.

### The opening 1 V example

The slides ask for total voltage when each element has RMS magnitude `U_R=U_L=U_C=1 V`. Refer current to 0°:

`Ũ_R=1`, `Ũ_L=j`, `Ũ_C=-j`.

Thus `Ũ=1+j-j=1 V`. The total is **1 V, not 3 V**. Inductive and capacitive voltage phasors cancel.

### Circuit classification and impedance triangle

| Condition | Net impedance | Behavior |
|---|---|---|
| `X_L>X_C` | Positive imaginary part | Inductive; current lags voltage |
| `X_L<X_C` | Negative imaginary part | Capacitive; current leads voltage |
| `X_L=X_C` | `Z=R` | Resistive terminal behavior; voltage/current in phase |

The impedance triangle has horizontal side R, signed vertical side X, and hypotenuse `|Z|`. It lets you connect resistance, reactance, magnitude, and angle.

The slide's special cases are R alone, L alone, C alone, RL, RC, and LC. Their impedances follow by omitting absent elements:

`R`, `jX_L`, `-jX_C`, `R+jX_L`, `R-jX_C`, and `j(X_L-X_C)`.

### Teacher's impedance exercises, worked here

| Given | Derived R and X |
|---|---|
| `Z=300+j500 Ω` | `R=300 Ω`, `X=500 Ω` |
| `Ũ=50∠30° V`, `Ĩ=2∠30° A` | `Z=25 Ω`, so `R=25 Ω`, `X=0` |
| `Ũ=100∠-30° V`, `Ĩ=4∠40° A` | `Z=25∠-70° Ω`, so `R≈8.55 Ω`, `X≈-23.49 Ω` |

### General series impedances

Group an RL section as `Z₁=R₁+jX_L` and an RC section as `Z₂=R₂-jX_C`. Then

`Z_total=Z₁+Z₂`, `Ĩ=Ũ/(Z₁+Z₂)`.

The phasor voltage-divider relationships are

`Ũ₁=[Z₁/(Z₁+Z₂)]Ũ`

`Ũ₂=[Z₂/(Z₁+Z₂)]Ũ`.

**Teacher example, worked here:** `Ũ_s=10∠0° V`, `Z₁=3+j2 Ω`, `Z₂=2+j3 Ω`.

`Z_total=5+j5 Ω`, so `Ĩ=10/(5+j5)=1-j1=√2∠-45° A`.

The section voltages are `Ũ₁=5-j1 V` and `Ũ₂=5+j1 V`; their sum is the supplied 10 V. Their magnitudes should not be added arithmetically.

## 3.5 Parallel AC circuits

*Source: 10 pages, including two impedance examples.*

All parallel branches share the same voltage. Apply KCL to **current phasors**:

`Ĩ=Ĩ_R+Ĩ_L+Ĩ_C`.

With voltage chosen at 0°, resistor current lies on the real axis, inductor current points at -90°, and capacitor current points at +90°.

### Teacher's three 5 A examples

![Original course slide, lesson 3.5, page 4: the three current-addition examples.](assets/parallel-current-examples.png)

*Original course slide, lesson 3.5, page 4: the three current-addition examples.*

| Parallel branches, each taking 5 A | Total phasor | Supply RMS current |
|---|---|---:|
| R, L, and C | `5-j5+j5` | 5 A |
| L and C only | `-j5+j5` | 0 A in the ideal cancellation case |
| R and C only | `5+j5` | `5√2≈7.07 A` |

In the zero-total case, individual reactive branch currents still flow and exchange energy. It is the supply's net reactive current that cancels.

### General parallel impedances

For two branches:

`Z_eq=Z₁Z₂/(Z₁+Z₂)`

`Ĩ=Ũ/Z_eq`

`Ĩ₁=[Z₂/(Z₁+Z₂)]Ĩ`, `Ĩ₂=[Z₁/(Z₁+Z₂)]Ĩ`.

Current division uses the **opposite branch's impedance** in the numerator. Use complex arithmetic; do not substitute only magnitudes.

**Teacher E1, worked here:** `Ĩ_s=5∠0° A`, `Z₁=2+j2 Ω`, `Z₂=3+j3 Ω`.

Because both impedances have the same angle, their current-divider ratios are real: `Ĩ₁=3∠0° A`, `Ĩ₂=2∠0° A`. The equivalent is `1.2+j1.2 Ω`, so the common voltage is `Ũ=6+j6 V`.

### Teacher E2: solve in two ways

Given `U=220 V`, the left branch is `Z₁=20-j114 Ω` and the right branch is `Z₂=40+j157 Ω`. Choose `Ũ=220∠0° V`.

**Method 1 - branch currents:**

`Ĩ₁=220/(20-j114)=0.32846+j1.87220 A`

`Ĩ₂=220/(40+j157)=0.33525-j1.31586 A`.

Add them:

`Ĩ=0.66371+j0.55634≈0.8660∠39.97° A`.

**Method 2 - total impedance:**

`Z_eq=Z₁Z₂/(Z₁+Z₂)≈194.682-j163.188 Ω`

`Z_eq≈254.03∠-39.97° Ω`.

Dividing 220 V by this equivalent gives the same current. The load is net capacitive, so current leads the supply voltage.

**Slide rounding:** the teacher rounds branch polar forms early and reports approximately `0.862∠39.6° A` and `255∠-39.6° Ω`. The values above retain the stated component values until the end; the small numerical difference comes from intermediate rounding.

## 3.6 Power in AC circuits

*Source: 10 pages, including pure-element power, general power, units, addition, and the power triangle.*

Instantaneous power is `p(t)=u(t)i(t)`. Positive absorbed power transfers energy into an element; negative absorbed power returns energy to the circuit. Average power is the cycle average:

`P=(1/T)∫₀ᵀ p(t)dt`.

### Pure resistor

For `u=√2 U sinωt` and `i=√2 I sinωt`:

`p=2UI sin²ωt=UI(1-cos2ωt)`.

Power is never negative and oscillates at twice the electrical frequency. Its average is

`P=UI=I²R=U²/R`, with `Q=0`.

**Slide correction:** the last line of the instantaneous-power derivation prints `1-cos²ωt`; the correct identity is `1-cos(2ωt)`.

### Pure inductor

Choose `i=√2 I sinωt`. Voltage leads by 90°, so `u=√2 U cosωt` and

`p=UI sin2ωt`.

It alternates between storage and return of magnetic energy. Its cycle average is `P=0`. With the usual signed reactive-power convention:

`Q_L=+UI=I²X_L=U²/X_L`.

**Slide correction:** the pure-inductor page accidentally repeats the resistor's instantaneous and average-power formulas. The plotted alternating power, the text about energy exchange, and the final summary table correctly imply zero average real power for an ideal inductor.

### Pure capacitor

Choose `u=√2 U sinωt`; then `i=√2 I cosωt`, giving `p=UI sin2ωt` for that chosen time reference. Energy alternates between storage in the electric field and return to the circuit; again `P=0`.

The reactive-power **magnitude** is `UI=I²X_C=U²/X_C`. The standard signed value is

`Q_C=-UI`.

The slide prints a positive capacitor Q as a magnitude. When adding inductive and capacitive reactive powers, use opposite signs. Instantaneous-power expressions must be compared using the same waveform reference; choosing a different reference changes the displayed sine's sign or phase, not the physical energy exchange.

### General circuit power

Define `φ=ψ_u-ψ_i`. Using RMS U and I:

| Quantity | Formula | Unit |
|---|---|---|
| Active, real, or average power | `P=UI cosφ` | W, kW |
| Signed reactive power | `Q=UI sinφ` | var, kvar |
| Apparent power | `S=UI=√(P²+Q²)` | VA, kVA |
| Power factor | `PF=P/S=cosφ` | Dimensionless |

For a passive load, positive Q is inductive and negative Q is capacitive. State **lagging** or **leading** as well as the numerical power factor, because the cosine alone cannot distinguish them.

The teacher resolves current into an in-phase active component of magnitude `I_P=I cosφ` and a quadrature component associated with `I sinφ`. With voltage at 0°, the consistent rectangular expression is

`Ĩ=I cosφ-jI sinφ`.

Thus `P=U I_P`, while the sign of Q distinguishes the quadrature direction. Some slide drawings show a leading-current arrow while using an unsigned angle; use the explicit `φ=ψ_u-ψ_i` definition to avoid sign ambiguity.

### Power addition and triangle

For components or branches at the same frequency:

`P_total=ΣP_k`, `Q_total=ΣQ_k`.

Then `S_total=√(P_total²+Q_total²)`. Apparent-power magnitudes do **not** generally add: `S_total≠ΣS_k`.

The power triangle places P horizontally, signed Q vertically, and S on the hypotenuse. Consequently `cosφ=P/S` and `tanφ=Q/P` when the ratio is defined.

**Worked here to illustrate the slide's addition rule:** an ideal resistor absorbing 300 W and an ideal inductor taking 400 var have total apparent power `√(300²+400²)=500 VA`, not 700 VA. Adding an ideal capacitor with `Q=-400 var` cancels the net reactive power, leaving 300 VA for that ideal combined load.

### What this document covers

The reviewed power document teaches instantaneous, average, reactive, and apparent power and their combination. It does not contain a separate capacitor-sizing or power-factor-correction procedure. Such a procedure in the earlier outline-based guide was extra material, not a summary of these slides.

## Chapter 3 problem-solving sequence

Establish the shared frequency and sine reference. Convert waveform amplitudes to RMS phasors. Replace R, L, and C by `R`, `jωL`, and `1/(jωC)`. Combine series impedances or parallel current phasors using complex arithmetic. Keep the phase until the end. Convert a result back to a waveform with the `√2` peak factor. For power, use RMS values, define `φ=ψ_u-ψ_i`, and retain the sign of reactive power.

**Common mistakes:** calling every varying waveform AC; mixing peak and RMS values; assigning a frequency from a phasor alone; adding polar magnitudes; dropping the capacitor's minus-j sign; using the wrong impedance in current division; summing apparent powers arithmetically; or copying the identified slide typos without checking their diagrams and element laws.
