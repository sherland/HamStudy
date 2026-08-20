MIT OpenCourseWare <http://ocw.mit.edu>

#### 2.161 Signal Processing: Continuous and Discrete Fall 2008

For information about citing these materials or our Terms of Use, visit: [http://ocw.mit.edu/terms.](http://ocw.mit.edu/terms)

![](_page_1_Diagram_8.jpeg)

#### **1 Introduction to Time-Domain Digital Signal Processing**

# Massachusetts Institute of Technology Department of Mechanical Engineering 2.161 Signal Processing - Continuous and Discrete Fall Term 2008

# **Lecture 13**<sup>1</sup>

### **Reading:**

- Proakis & Manolakis, Chapter 3 (The z-transform)
- Oppenheim, Schafer & Buck, Chapter 3 (The z-transform)

Consider a continuous-time filter

*-*

such as simple first-order RC high-pass filter:

described by a transfer function

<sup>H</sup>(s)= RCs RCs +1.

The ODE describing the system is

τ dy <sup>d</sup><sup>t</sup> <sup>+</sup> <sup>y</sup> <sup>=</sup> <sup>τ</sup> df dt

where τ = RC is the time constant.

Our task is to derive a simple discrete-time equivalent of this prototype filter based on samples of the input f(t) taken at intervals ΔT.

![](_page_1_Diagram_15.jpeg)

<sup>1</sup>copyright c D.Rowell 2008

� � N M <sup>y</sup><sup>n</sup> <sup>=</sup> <sup>a</sup>iyn−<sup>i</sup> <sup>+</sup> <sup>b</sup>ifn−<sup>i</sup> i=1 i=0

� N <sup>y</sup><sup>n</sup> <sup>=</sup> <sup>a</sup>iyn−<sup>i</sup> <sup>+</sup> <sup>b</sup>0f<sup>n</sup> i=0

If we use a backwards-difference numerical approximation to the derivatives, that is

<sup>d</sup><sup>x</sup> (x(nΔT) <sup>−</sup> <sup>x</sup>((<sup>n</sup> <sup>−</sup> 1)ΔT) <sup>≈</sup> dt ΔT

and adopt the notation y<sup>n</sup> = y(nΔT), and let a = τ/ΔT,

<sup>a</sup>(y<sup>n</sup> <sup>−</sup> <sup>y</sup>n−1)+ <sup>y</sup><sup>n</sup> <sup>=</sup> <sup>a</sup>(f<sup>n</sup> <sup>−</sup> <sup>f</sup>n−1)

and solving for y<sup>n</sup>

a a a <sup>y</sup><sup>n</sup> <sup>=</sup> <sup>y</sup>n−<sup>1</sup> <sup>+</sup> <sup>f</sup><sup>n</sup> <sup>−</sup> <sup>f</sup>n−<sup>1</sup> 1+ <sup>a</sup> 1+ <sup>a</sup> 1+ <sup>a</sup>

which is a first-order difference equation, and is the computational formula for a sampleby-sample implementation of digital high-pass filter derived from the continuous prototype above. Note that

- The "fidelity" of the approximation depends on ΔT, and becomes more accurate when ΔT τ .
- At each step the output is a linear combination of the present and/or past samples of the output and input. This is a recursive system because the computation of the current output depends on prior values of the output.

In general, regardless of the design method used, a LTI digital filter implementation will be of a similar form, that is

where the a<sup>i</sup> and b<sup>i</sup> are constant coefficients. Then as in the simple example above, the current output is a weighted combination of past values of the output, and current and past values of the input.

- If a<sup>i</sup> ≡ 0 for i =1 ...N, so that

� M <sup>y</sup><sup>n</sup> <sup>=</sup> <sup>b</sup>ifn−<sup>i</sup> i=0

The output is simply a weighted sum of the current and prior inputs. Such a filter is a non-recursive filter with a finite-impulse-response (FIR), and is known as a moving average (MA) filter, or an all-zero filter.

- If b<sup>i</sup> ≡ 0 for i =1 ...M, so that

only the current input value is used. This filter is a recursive filter with an infiniteimpulse-response (IIR), and is known as an auto-regressive (AR) filter, or an all-pole filter.

� � N M <sup>y</sup><sup>n</sup> <sup>=</sup> <sup>a</sup>iyn−<sup>i</sup> <sup>+</sup> <sup>b</sup>ifn−<sup>i</sup> i=1 i=0

� <sup>1</sup> <sup>n</sup> =0 <sup>δ</sup><sup>n</sup> <sup>=</sup> <sup>0</sup> otherwise. - *-*

� ∞ <sup>f</sup><sup>n</sup> <sup>=</sup> <sup>f</sup>kδn−<sup>k</sup> <sup>k</sup>=−∞

� ∞ <sup>y</sup><sup>n</sup> <sup>=</sup> <sup>f</sup>khn−<sup>k</sup> <sup>k</sup>=−∞

#### **2 The Discrete-time Convolution Sum**

- With the full difference equation

the filter is a recursive filter with an infinite-impulse response (IIR), and is known as an auto-regressive moving-average (ARMA) filter.

For a continuous system

*-*

the output y(t), in response to an input f(t), is given by the convolution integral:

� ∞ y(t)= f(τ )h(t − τ )dτ 0

where h(t) is the system impulse response.

For a LTI discrete-time system, such as defined by a difference equation, we define the pulse response sequence {h(n)} as the response to a unit-pulse input sequence {δn}, where

If the input sequence {fn} is written as a sum of weighted and shifted pulses, that is

then by superposition the output will be a sequence of similarly weighted and shifted pulse responses

which defines the convolution sum, which is analogous to the convolution integral of the continuous system.

#### **The** z**-Transform 3**

The z-transform in discrete-time system analysis and design serves the same role as the Laplace transform in continuous systems. We begin here with a parallel development of both the z and Laplace transforms from the Fourier transforms.

� ∞ F∗ (jΩ) = fne−jnΩΔ<sup>T</sup> n=0

� � {wn} = fnr−<sup>n</sup>

� ∞ W∗ (jΩ) = F˜∗ (jΩ|r)= � fnr−n� e−jnΩΔ<sup>T</sup> n=0 ∞ <sup>=</sup> �<sup>f</sup><sup>n</sup> � rejΩΔ<sup>T</sup> �<sup>−</sup><sup>n</sup> n=0

� ∞ F(z)= F˜∗ (jΩ|r)= fnz−<sup>n</sup> n=0

#### **The Laplace Transform**

**(1)** We begin with causal f(t) and find its Fourier transform (Note that because f(t)is causal, the integral has limits of 0 and ∞):

� ∞ F(jΩ) = f(t)e−jΩ<sup>t</sup> dt 0

**(2)** We note that for some functions f(t) (for example the unit step function), the Fourier integral does not converge.

**(3)** We introduce a weighted function

w(t)= f(t)e−σt

and note

lim <sup>w</sup>(t)= <sup>f</sup>(t) <sup>σ</sup>→<sup>0</sup>

The effect of the exponential weighting by e−σt is to allow convergence of the integral for a much broader range of functions f(t).

**(4)** We take the Fourier transform of w(t)

� ∞ <sup>W</sup>(jΩ) <sup>=</sup> <sup>F</sup>˜(jΩ|σ)= � f(t)e−σt� e−jΩ<sup>t</sup> dt 0 � ∞ = f(t)e−(σ+jΩ)dt 0

and define the complex variable s = σ + jΩso that we can write

� ∞ F(s)= F˜(jω|σ)= f(t)e−stdt 0

F(s) is the one-sided Laplace Transform. Note that the Laplace variable s = σ + jΩ is expressed in Cartesian form.

#### **The Z transform**

**(1)** We sample f(t) at intervals ΔT to produce f ∗(t). We take its Fourier transform (and use the sifting property of δ(t)) to produce

**(2)** We note that for some sequences f<sup>n</sup> (for example the unit step sequence), the summation does not converge.

**(3)** We introduce a weighted sequence

and note

lim {wn} <sup>=</sup> {fn} <sup>r</sup>→<sup>1</sup>

The effect of the exponential weighting by r−<sup>n</sup> is to allow convergence of the summation for a much broader range of sequences fn.

**(4)** We take the Fourier transform of w<sup>n</sup>

and define the complex variable z = rejΩΔ<sup>T</sup> so that we can write

F(z) is the one-sided Z-transform. Note that z = rejΩΔ<sup>T</sup> is expressed in polar form.

![](_page_5_Picture_4.jpeg)

![](_page_5_Picture_5.jpeg)

![](_page_5_Diagram_6.jpeg)

� ∞ <sup>Z</sup> {fn}⊗{gn} <sup>=</sup> <sup>f</sup>mgn−<sup>m</sup> ⇐⇒ <sup>F</sup>(z)G(z) <sup>m</sup>=−∞

� ∞ F(z)= fnz−<sup>n</sup> <sup>n</sup>=−∞

#### **The Laplace Transform** (contd.)

**(5)** For a causal function f(t), the region of convergence (ROC) includes the s-plane to the right of all poles of F(jΩ).

**(6)** If the ROC includes the imaginary axis, the FT of f(t)is F(jΩ):

F(jΩ) = F(s)|s=j<sup>Ω</sup>

**(7)** The convolution theorem states

� <sup>∞</sup> <sup>L</sup> <sup>f</sup>(t)⊗g(t)= <sup>f</sup>(<sup>τ</sup> )g(t−<sup>τ</sup> )dτ ⇐⇒ <sup>F</sup>(s)G(s) −∞

**(8)** For an LTI system with transfer function H(s), the frequency response is

H(s)|s=j<sup>Ω</sup> = H(jΩ)

if the ROC includes the imaginary axis.

### **The Z transform** (contd.)

**(5)** For a right-sided (causal) sequence {fn} the region of convergence (ROC) includes the z-plane at a radius greater than all of the poles of F(z).

**(6)** If the ROC includes the unit circle, the DFT of {fn}, n =0, 1,...,N − 1. is {Fm} where

F<sup>m</sup> = F(z)|z=ejωm = F(ejωm),

where ω<sup>m</sup> =2πm/N for m =0, 1,...,N − 1. **(7)** The convolution theorem states

**(8)** For a discrete LSI system with transfer function H(z), the frequency response is

H(z)|z=ejω = H(ejω) |ω|≤ π

if the ROC includes the unit circle.

From the above derivation, the Z-transform of a sequence {fn} is

where z = r e<sup>j</sup> <sup>ω</sup> is a complex variable. For a causal sequence f<sup>n</sup> = 0 for n< 0, the transform

� can be written <sup>∞</sup> F(z)= fnz−<sup>n</sup> n=0

� � � ∞ �<sup>f</sup>nr−<sup>n</sup>� <sup>&</sup>lt; <sup>∞</sup> <sup>n</sup>=−∞

� 0 n< 0 <sup>u</sup><sup>n</sup> <sup>=</sup> <sup>1</sup> <sup>n</sup> <sup>≥</sup> <sup>0</sup>

**Example:** The finite sequence {f0,...,f3} = {5, 3, −1, 4} has the z-transform

F(z)=5z<sup>0</sup> +3z−<sup>1</sup> − z−<sup>2</sup> +4z−<sup>3</sup>

**The Region of Convergence:** For a given sequence, the region of the z-plane in which the sum converges is defined as the region of convergence (ROC). In general, within the ROC

and the ROC is in general an annular region of the z-plane:

![](_page_6_Figure_7.jpeg)

- **(a)** The ROC is a ring or disk in the z-plane.
- **(b)** The ROC cannot contain any poles of F(z).
- **(c)** For a finite sequence, the ROC is the entire z-plane (with the possible exception of z =0 and z = ∞.
- **(d)** For a causal sequence, the ROC extends outward from the outermost pole.
- **(e)** for a left-sided sequence, the ROC is a disk, with radius defined by the innermost pole.
- **(f)** For a two sided sequence the ROC is a disk bounded by two poles, but not containing any poles.
- **(g)** The ROC is a connected region.

z**-Transform Examples:** In the following examples {un} is the unit step sequence,

and is used to force a causal sequence.

(1) {fn} = {δn} (the digital pulse sequence) From the definition of F(z):

F(z) = 1z<sup>0</sup> = 1 for all z.

(2) {fn} = {a<sup>n</sup>un}

� <sup>n</sup>z<sup>−</sup><sup>n</sup> � <sup>F</sup>(z) <sup>=</sup> ∞ a = ∞ � az<sup>−</sup><sup>1</sup> �n n=0 n=0

<sup>n</sup> <sup>Z</sup> <sup>F</sup>(z) <sup>=</sup> <sup>1</sup> <sup>=</sup> <sup>z</sup> {<sup>a</sup> } ←→ for <sup>z</sup> <sup>&</sup>gt; a. <sup>1</sup> <sup>−</sup> az<sup>−</sup><sup>1</sup> <sup>z</sup> <sup>−</sup> <sup>a</sup> <sup>|</sup> <sup>|</sup>

since

<sup>∞</sup> <sup>1</sup> � <sup>n</sup> <sup>x</sup> <sup>=</sup> for <sup>x</sup> <sup>&</sup>lt; <sup>1</sup>. <sup>1</sup> <sup>−</sup> <sup>x</sup> <sup>n</sup>=0

(3) {fn} = {un} (the unit step sequence).

<sup>∞</sup> <sup>1</sup> <sup>z</sup> <sup>F</sup>(z) <sup>=</sup> �z<sup>−</sup><sup>n</sup> <sup>=</sup> <sup>=</sup> for <sup>z</sup> <sup>&</sup>lt; <sup>1</sup> <sup>1</sup> <sup>−</sup> <sup>z</sup><sup>−</sup><sup>1</sup> <sup>z</sup> <sup>−</sup> <sup>1</sup> <sup>|</sup> <sup>|</sup> n=0

from (2) with a = 1.

(4) {fn} <sup>=</sup> � e<sup>−</sup>bnu<sup>n</sup> � .

∞ ∞ <sup>F</sup>(z) <sup>=</sup> � <sup>e</sup><sup>−</sup>bnz<sup>−</sup><sup>n</sup> <sup>=</sup> �� e<sup>−</sup><sup>b</sup> z<sup>−</sup><sup>1</sup> �n n=0 n=0

� <sup>e</sup><sup>−</sup>bn� <sup>Z</sup> <sup>1</sup> <sup>z</sup> <sup>F</sup>(z) <sup>=</sup> <sup>=</sup> for <sup>z</sup> <sup>&</sup>gt; <sup>e</sup><sup>−</sup><sup>b</sup> . <sup>z</sup><sup>−</sup><sup>1</sup> <sup>z</sup> <sup>−</sup> <sup>e</sup> ←→ <sup>−</sup>bn <sup>1</sup> <sup>−</sup> <sup>e</sup><sup>−</sup><sup>b</sup> <sup>|</sup> <sup>|</sup>

from (2) with a = e<sup>−</sup><sup>b</sup> .

<sup>n</sup> (5) {fn} <sup>=</sup> � e<sup>−</sup>b<sup>|</sup> <sup>|</sup> � .

0 ∞ <sup>F</sup>(z) <sup>=</sup> � � e<sup>−</sup><sup>b</sup> z �<sup>−</sup><sup>n</sup> <sup>+</sup>�� e<sup>−</sup><sup>b</sup> z<sup>−</sup><sup>1</sup> �<sup>n</sup> <sup>−</sup> <sup>1</sup> n=−∞ n=0 1 1 <sup>=</sup> <sup>1</sup> <sup>−</sup> <sup>e</sup><sup>−</sup><sup>b</sup><sup>z</sup> <sup>+</sup> <sup>1</sup> <sup>−</sup> <sup>e</sup><sup>−</sup><sup>b</sup>z<sup>−</sup><sup>1</sup> <sup>−</sup> <sup>1</sup>

Note that the item f<sup>0</sup> = 1 appears in each sum, therefore it is necessary to subtract 1.

<sup>n</sup> <sup>b</sup> � e<sup>−</sup>b<sup>|</sup> <sup>|</sup> � <sup>Z</sup> <sup>F</sup>(z) <sup>=</sup> <sup>1</sup> <sup>−</sup> <sup>e</sup><sup>−</sup>2<sup>b</sup> for <sup>e</sup><sup>−</sup><sup>b</sup> ←→ <sup>&</sup>lt; <sup>z</sup> <sup>&</sup>lt; <sup>e</sup> . (1 <sup>−</sup> <sup>e</sup><sup>−</sup><sup>b</sup>z)(1 <sup>−</sup> <sup>e</sup><sup>−</sup><sup>b</sup>z<sup>−</sup><sup>1</sup>) <sup>|</sup> <sup>|</sup>

![](_page_8_Picture_0.jpeg)

![](_page_8_Figure_1.jpeg)

(6) {fn} = { e<sup>−</sup>jω0<sup>n</sup>un} = {cos(ω0n)un} − j {sin(ω0n)un} . F(z) = Z {cos(ω0n)un} − jZ {sin(ω0n)un}

From (1)

1 <sup>F</sup>(z) <sup>=</sup> <sup>1</sup> <sup>−</sup> <sup>e</sup><sup>−</sup>jω<sup>0</sup> <sup>z</sup><sup>−</sup><sup>1</sup> for <sup>|</sup>z<sup>|</sup> <sup>&</sup>gt; <sup>1</sup> <sup>1</sup> <sup>−</sup> cos(ω0)z<sup>−</sup><sup>1</sup> <sup>−</sup> <sup>j</sup> sin(ω0) <sup>=</sup> <sup>1</sup> <sup>−</sup> <sup>2</sup> cos(ω0)z∗−<sup>1</sup> <sup>+</sup> <sup>z</sup><sup>−</sup><sup>2</sup> z<sup>2</sup> − cos(ω0)z − j sin(ω0)z<sup>2</sup> <sup>=</sup> <sup>z</sup><sup>2</sup> <sup>−</sup> <sup>2</sup> cos(ω0)<sup>z</sup> <sup>+</sup> <sup>1</sup>

and therefore

<sup>z</sup><sup>2</sup> <sup>−</sup> cos(ω0)<sup>z</sup> <sup>Z</sup> {cos(ω0n)un} <sup>=</sup> for <sup>z</sup> <sup>&</sup>gt; <sup>1</sup> <sup>2</sup> <sup>z</sup> <sup>−</sup> <sup>2</sup> cos(ω0)<sup>z</sup> <sup>+</sup> <sup>1</sup> <sup>|</sup> <sup>|</sup> sin(ω0)z<sup>2</sup> <sup>Z</sup> {sin(ω0n)un} <sup>=</sup> for <sup>z</sup> <sup>&</sup>gt; <sup>1</sup> <sup>2</sup> <sup>z</sup> <sup>−</sup> <sup>2</sup> cos(ω0)<sup>z</sup> <sup>+</sup> <sup>1</sup> <sup>|</sup> <sup>|</sup>

Properties of the z-Transform: Refer to the texts for a full description. We simply summarize some of the more important properties here.

### (a) Linearity:

Z a {fn} + b {gn} ←→ aF(z) + bG(z) ROC: Intersection of ROC<sup>f</sup> and ROCg.

# (b) Time Shift:

Z z<sup>−</sup><sup>m</sup> {fn−m} ←→ F(z) ROC: ROC<sup>f</sup> except for z = 0 if k < 0, or z = ∞ if k > 0.

If g<sup>n</sup> = fn−m,

∞ ∞ <sup>f</sup>kz<sup>−</sup>(k+m) <sup>G</sup>(z) <sup>=</sup> � <sup>f</sup>n−mz<sup>−</sup><sup>n</sup> <sup>=</sup> � <sup>=</sup> <sup>z</sup><sup>−</sup><sup>m</sup>F(z). n=−∞ k=−∞

This is an important property in the analysis and design of discrete-time systems. We will often have recourse to a unit-delay block:

*f y = f <sup>n</sup> <sup>n</sup> z n - 1 - 1* U n i t D e l a y

#### (c) Convolution:

<sup>Z</sup> {fn} ⊗ {gn} ←→ <sup>F</sup>(z)G(z) ROC: Intersection of ROC<sup>f</sup> and ROCg.

∞ where {fn} <sup>⊗</sup> {gn} <sup>=</sup> � <sup>f</sup>kgn−<sup>k</sup> is the convolution sum. k=−∞

Let

<sup>∞</sup> <sup>∞</sup> � <sup>∞</sup> � <sup>Y</sup> (z) <sup>=</sup> � <sup>y</sup>nz<sup>−</sup><sup>n</sup> <sup>=</sup> � � <sup>f</sup>kgn−<sup>k</sup> <sup>z</sup><sup>−</sup><sup>n</sup> n=−∞ n=−∞ k=−∞ <sup>∞</sup> � <sup>∞</sup> � <sup>∞</sup> <sup>∞</sup> <sup>=</sup> � <sup>f</sup><sup>k</sup> � <sup>g</sup>n−kz<sup>−</sup>(n−k) <sup>z</sup><sup>−</sup><sup>k</sup> <sup>=</sup> � <sup>f</sup>kz<sup>−</sup><sup>k</sup> � <sup>g</sup>mz<sup>−</sup><sup>m</sup> k=−∞ n=−∞ k=−∞ m=−∞ = F(z)G(z)

# (d) Conjugation of a complex sequence:

� fn � <sup>Z</sup>←→ <sup>F</sup>(z) ROC: ROC<sup>f</sup>

### (e) Time reversal:

<sup>Z</sup> <sup>F</sup>(1/z) ROC: <sup>1</sup> < z < <sup>1</sup> {f<sup>−</sup>n} ←→ <sup>r</sup><sup>1</sup> <sup>|</sup> <sup>|</sup> <sup>r</sup><sup>2</sup>

where the ROC of F(z) lies between r<sup>1</sup> and r2.

# (e) Scaling in the z-domain:

<sup>Z</sup> <sup>F</sup>(a<sup>−</sup><sup>1</sup> {a<sup>n</sup>fn} ←→ <sup>z</sup>) ROC: |a| <sup>r</sup><sup>1</sup> <sup>&</sup>lt; |z| <sup>&</sup>lt; |a| <sup>r</sup><sup>2</sup>

where the ROC of F(z) lies between r<sup>1</sup> and r2.

### (e) Differentiation in the z-domain:

{nfn} <sup>Z</sup> <sup>d</sup>F(z) ←→ <sup>−</sup><sup>z</sup> ROC: <sup>r</sup><sup>2</sup> <sup>&</sup>lt; <sup>z</sup> <sup>&</sup>lt; <sup>r</sup><sup>1</sup> <sup>d</sup><sup>z</sup> <sup>|</sup> <sup>|</sup>

where the ROC of F(z) lies between r<sup>1</sup> and r2.