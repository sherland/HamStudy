MIT OpenCourseWare <http://ocw.mit.edu>

#### 2.161 Signal Processing: Continuous and Discrete Fall 2008

For information about citing these materials or our Terms of Use, visit: [http://ocw.mit.edu/terms.](http://ocw.mit.edu/terms)

� <sup>y</sup><sup>n</sup> <sup>=</sup> <sup>f</sup>khn−k. <sup>k</sup>=−∞

![](_page_1_Figure_8.jpeg)

#### **1 FFT Convolution for FIR Filters**

# Massachusetts Institute of Technology Department of Mechanical Engineering 2.161 Signal Processing - Continuous and Discrete Fall Term 2008

## **Lecture 18**<sup>1</sup>

#### **Reading:**

- Proakis and Manolakis: 7.3.1, 7.3.2, 10.3
- Oppenheim, Schafer, and Buck: 8.7.3, 7.1

The response of an FIR filter with impulse response {hk} to an input {fk} is given by the linear convolution <sup>∞</sup>

The length of the convolution of two finite sequences of lengths P and Q is N = P + Q − 1. The following figure shows a sequence {fn} of length P = 6, and a sequence {hn} of length Q = 4 reversed and shifted so as to compute the extremes of the convolved sequence y<sup>0</sup> and y8.

The convolution property of the DFT suggests that the FFT might be used to convolve two equal length sequences

y<sup>n</sup> = IDFT {DFT {fn} .DFT {hn}} .

<sup>1</sup>copyright c D.Rowell 2008

However, DFT convolution is a circular convolution, involving periodic extensions of the two sequences. The following figure shows the circular convolution of length 6, on two sequences {fn} of length P = 6 and {hn} of length Q = 4. The periodic extensions cause overlap in the first Q − 1 samples, generating "wrap-around" errors in the DFT convolution.

![](_page_2_Figure_1.jpeg)

![](_page_2_Diagram_2.jpeg)

- DFT convolution of two sequences of length P and Q (P ≥ Q) in DFTs of length P
  - 1. Produces an output sequence of length P, whereas linear convolution produces an output sequence of length P + Q − 1.
- 2. Introduces wrap-around error in the first Q−1 samples of the output sequence. **The solution is to zero-pad both input sequences to a length** N ≥ P +Q−1 **and then to use DFT convolution with the length** N **sequences.**

For example, if {fn} is of length P = 237, and {hn} is of length Q = 125, for error-free convolution we must perform the DFTs in length N ≥ 237 + 125 − 1 = 461. If the available FFT routine is radix-2, we should choose N=512.

**The use of the FFT for Filtering Long Data Sequences:** The DFT convolution method provides an attractive alternative to direct convolution when the length of the data record is very large. The general method is to break the data into manageable sections, then use the FFT to to perform the convolution and then recombine the output sections. Care must be taken, however, to avoid wrap-around errors. There are two basic methods used for convolving long data records. Let the impulse response {hn} have length Q.

**Overlap-Save Method:** (Also known as the overlap-discard,or select-savings method.) In this method the data is divided into blocks of length P samples, but with successive blocks overlapping by Q − 1. The DFT convolution is done on each block with length P, and wrap-around errors are allowed to contaminate the first Q − 1 samples of the output. These initial samples are then discarded, and only the error-free P − (Q − 1) samples are saved in the output record.

� <sup>y</sup>mP (<sup>n</sup> +(<sup>Q</sup> <sup>−</sup> 1)),n =0,...,P <sup>−</sup> (<sup>Q</sup> <sup>−</sup> 1) <sup>y</sup>m(n)= <sup>0</sup>, otherwise.

� ∞ y(n)= ym(n − m(P − Q + 1)). m=0

![](_page_3_Figure_6.jpeg)

With the overlap of the data blocks, in the mth block the samples are

fm(n)= f(n + m(P − (Q − 1))), n =0,...,P − 1,

and after DFT convolution in length P, giving ymP (n), the output is taken as

and the output is formed by concatenating all such records:

**Overlap-Add Method:** In this method the data is divided into blocks of length P, but the DFT convolution is done in zero-padded blocks of length N = P + Q − 1 so that

![](_page_4_Figure_1.jpeg)

� � N M <sup>y</sup><sup>n</sup> <sup>=</sup> <sup>a</sup>kyn−<sup>k</sup> <sup>+</sup> <sup>b</sup>kfn−<sup>k</sup> k=1 k=0

#### **2 The Design of IIR Filters**

wrap-around errors do not occur. In this case the output is identical to the linear convolution of the two blocks, with an initial rise of length Q − 1 samples, and a trailing section also of length Q − 1 samples. It is easy to show that if the trailing section of the mth output block is overlapped with the initial section of the (m + 1)th block, the samples add together to generate the correct output values.

MATLAB's fftfilt() function performs DFT convolution using the overlap-add method.

An IIR filter is characterized by a recursive difference equation

and a rational transfer function of the form

b0z<sup>0</sup> + b1z−<sup>1</sup> + ... + bMz−<sup>M</sup> <sup>H</sup>(z)= <sup>z</sup><sup>0</sup> <sup>+</sup> <sup>a</sup>1z−<sup>1</sup> <sup>+</sup> ... <sup>+</sup> <sup>a</sup><sup>N</sup> <sup>z</sup>−<sup>N</sup>

IIR filters have the advantage that they can give a better cut-off characteristic than a FIR filter of the same order, but have the disadvantage that the phase response cannot be well controlled.

� � <sup>1</sup> − z−<sup>1</sup> <sup>n</sup> <sup>n</sup><sup>s</sup> <sup>→</sup> . <sup>T</sup>

The most common design procedure for digital IIR filters is to design a continuous filter in the s-plane, and then to transform that filter to the z-plane. Because the mapping between the continuous and discrete domains cannot be done exactly, the various design methods are at best approximations.

# **2.1 Design By Approximation of Derivatives:**

Perhaps the simplest method for low-order systems is to use backward-difference approximation to continuous domain derivatives.

## **Example 1**

Suppose we wish to make a discrete-time filter based on a prototype first-order high-pass filter

<sup>s</sup> <sup>H</sup>p(s)= . <sup>s</sup> <sup>+</sup> <sup>a</sup>

The differential equation describing this filter is

<sup>d</sup><sup>y</sup> <sup>d</sup><sup>f</sup> <sup>+</sup> ay <sup>=</sup> <sup>d</sup><sup>t</sup> <sup>d</sup><sup>t</sup>

The backward-difference approximation to a derivative based on samples taken at intervals T apart is

<sup>d</sup><sup>x</sup> <sup>x</sup><sup>n</sup> <sup>−</sup> <sup>x</sup>n−<sup>1</sup> ≈ dt T

and substitution into the differential equation gives

<sup>y</sup><sup>n</sup> <sup>−</sup> <sup>y</sup>n−<sup>1</sup> <sup>f</sup><sup>n</sup> <sup>−</sup> <sup>f</sup>n−<sup>1</sup> <sup>+</sup> ay<sup>n</sup> <sup>=</sup> <sup>T</sup> <sup>T</sup>

or

1 1 <sup>y</sup><sup>n</sup> <sup>=</sup> <sup>y</sup>n−<sup>1</sup> <sup>+</sup> (f<sup>n</sup> <sup>−</sup> <sup>f</sup>n−1) 1+ aT 1+ aT

The transfer function is

<sup>1</sup> <sup>−</sup> <sup>z</sup>−<sup>1</sup> <sup>z</sup> <sup>−</sup> <sup>1</sup> <sup>H</sup>(z)= <sup>=</sup> (1 <sup>+</sup> aT)1 <sup>+</sup> <sup>z</sup>−<sup>1</sup> (1 <sup>+</sup> aT)<sup>z</sup> +1

This example indicates that the method uses the transformation

1 − z−<sup>1</sup> <sup>s</sup> <sup>→</sup> <sup>T</sup>

in Hp(s). For higher order terms

![](_page_6_Figure_12.jpeg)

#### **Example 2**

Convert the continuous low-pass Butterworth filter with Ω<sup>c</sup> = 1 rad/s to a digital filter with a sampling time T =0.5 s. The transfer function is

<sup>1</sup> <sup>H</sup>p(s)= √ . <sup>s</sup><sup>2</sup> <sup>+</sup> <sup>2</sup><sup>s</sup> +1

The discrete-time transfer function is

<sup>1</sup> <sup>H</sup>(z)= � <sup>−</sup><sup>1</sup> �<sup>2</sup> <sup>√</sup> � <sup>−</sup><sup>1</sup> � <sup>1</sup>−<sup>z</sup> <sup>1</sup>−<sup>z</sup> <sup>+</sup> <sup>2</sup> +1 <sup>T</sup> <sup>T</sup> T2 <sup>=</sup> √ √ (1 <sup>+</sup> <sup>2</sup><sup>T</sup> <sup>+</sup> <sup>T</sup><sup>2</sup>) <sup>−</sup> (2 <sup>+</sup> <sup>2</sup>T)z−<sup>1</sup> <sup>+</sup> <sup>z</sup>−<sup>2</sup>

and with T =0.5s,

<sup>0</sup>.<sup>25</sup> <sup>H</sup>(z)= <sup>1</sup>.<sup>9571</sup> <sup>−</sup> <sup>2</sup>.7071z−<sup>1</sup> <sup>+</sup> <sup>z</sup>−<sup>2</sup>

The frequency response of this filter is plotted in Example 4.

In general, the backward-difference does not lead to satisfactory digital filters that mimic the prototype filter characteristics. (See Proakis and Manolakis, Sec. 10.3.1).

#### **2.2 Design by Impulse-Invariance:**

In the impulse-invariant design method the impulse response {hn} of the digital filter is taken to be proportional to the samples of the impulse response hp(t) of the continuous filter Hp(s) with a sampling interval of T seconds. The most common form is

h<sup>n</sup> = Thp(nT).

Then

H(z) = TZ {hp(nT)} = TZ<sup>T</sup> � L<sup>−</sup><sup>1</sup> {Hp(s)} �

since hp(t) = L<sup>−</sup><sup>1</sup> {Hp(s)}, and where Z<sup>T</sup> {} indicates the z-transform of a continuous function with sampling interval T.

#### Example 3

Find the impulse-invariant IIR filter from the prototype continuous filter

<sup>a</sup> <sup>H</sup>p(s) <sup>=</sup> . <sup>s</sup> <sup>+</sup> <sup>a</sup>

Solution: Using Laplace transform tables

hp(t) = L<sup>−</sup><sup>1</sup> � <sup>a</sup> � <sup>=</sup> <sup>a</sup> <sup>e</sup><sup>−</sup>at. <sup>s</sup> <sup>+</sup> <sup>a</sup>

and from z-transform tables

� <sup>a</sup> <sup>a</sup> <sup>e</sup><sup>−</sup>at� <sup>Z</sup><sup>T</sup> <sup>=</sup> . <sup>1</sup> <sup>−</sup> <sup>e</sup><sup>−</sup>aT <sup>z</sup><sup>−</sup><sup>1</sup>

The IIR filter is

� <sup>a</sup> <sup>e</sup><sup>−</sup>at� <sup>=</sup> aT <sup>H</sup>(z) <sup>=</sup> <sup>T</sup>Z<sup>T</sup> <sup>1</sup> <sup>−</sup> <sup>e</sup><sup>−</sup>aT <sup>z</sup><sup>−</sup><sup>1</sup>

and the difference equation is

y<sup>n</sup> = e<sup>−</sup>aT yn−<sup>1</sup> + aTf<sup>n</sup>

For the digital filter <sup>∞</sup> <sup>H</sup>( <sup>e</sup><sup>j</sup> <sup>Ω</sup><sup>T</sup> ) <sup>=</sup> <sup>H</sup>(z)<sup>|</sup> <sup>j</sup> <sup>Ω</sup><sup>T</sup> <sup>=</sup> �<sup>h</sup><sup>k</sup> <sup>e</sup><sup>−</sup><sup>j</sup> <sup>k</sup>Ω<sup>T</sup> z= e k=0

and the DTFT of the samples of the continuous prototype's impulse response is

<sup>∞</sup> <sup>1</sup> <sup>∞</sup> � � <sup>2</sup>πk �� DTFT {hp(nT)} <sup>=</sup> �<sup>h</sup>p(kT) <sup>e</sup><sup>−</sup><sup>j</sup> <sup>k</sup>Ω<sup>T</sup> <sup>=</sup> � <sup>H</sup><sup>p</sup> <sup>j</sup> <sup>Ω</sup> <sup>−</sup> . <sup>T</sup> <sup>T</sup> k=0 k=−∞

Then if h<sup>n</sup> = Thp(nT),

<sup>∞</sup> � � <sup>2</sup>πk �� <sup>H</sup>( <sup>e</sup><sup>j</sup> <sup>Ω</sup><sup>T</sup> ) <sup>=</sup> � <sup>H</sup><sup>p</sup> <sup>j</sup> <sup>Ω</sup> <sup>−</sup> . <sup>T</sup> k=−∞

The discrete-time frequency response is therefore a superposition of shifted replicas of the frequency response of the prototype. As a result, aliasing will be present in H( e<sup>j</sup> <sup>ω</sup>) if the prototype's frequency response |Hp(j Ω)| �= 0 for |Ω| ≥ π/T.

![](_page_8_Figure_0.jpeg)

For this reason the impulse-invariance method is not suitable for the design of high-pass or band-stop filters, which by definition require a prototype Hp(s) with a non-zero frequency response at Ω = π/T.

## Example 4

Design an impulse-invariant filter based on the second-order low-pass Butterworth prototype used in Example 2, with T = 0.5 s.

<sup>1</sup> <sup>H</sup>p(s) <sup>=</sup> <sup>s</sup><sup>2</sup> <sup>+</sup> √2<sup>s</sup> <sup>+</sup> <sup>1</sup>

Solution: From z-transform tables

� � <sup>β</sup> �� <sup>e</sup><sup>−</sup>aT sin(βT)<sup>z</sup> <sup>Z</sup><sup>T</sup> <sup>L</sup><sup>−</sup><sup>1</sup> (<sup>s</sup> <sup>+</sup> <sup>a</sup>)<sup>2</sup> <sup>+</sup> <sup>β</sup><sup>2</sup> <sup>=</sup> <sup>z</sup><sup>2</sup> <sup>+</sup> <sup>2</sup><sup>z</sup> <sup>e</sup><sup>−</sup>aT cos(βT)<sup>z</sup> <sup>+</sup> <sup>e</sup><sup>−</sup>2aT

and Hp(s) may be written in this form

<sup>1</sup> <sup>H</sup>p(s) <sup>=</sup> (<sup>s</sup> <sup>+</sup> <sup>1</sup>/ √2)<sup>2</sup> <sup>+</sup> (1/ √2)<sup>2</sup>

so that a = 1/ √2, and <sup>β</sup> <sup>=</sup> <sup>1</sup>/ √2. Substituting these values,

0.1719z<sup>−</sup><sup>1</sup> H(z) = TZ<sup>T</sup> � L<sup>−</sup><sup>1</sup> {Hp(s)} � <sup>=</sup> <sup>1</sup> <sup>−</sup> <sup>1</sup>.3175z<sup>−</sup><sup>1</sup> <sup>+</sup> <sup>0</sup>.4935z<sup>−</sup><sup>2</sup>

The frequency response of the impulse-invariant, and backward-difference (from Example 2) filters are compared with the prototype below:

![](_page_9_Figure_0.jpeg)

The MATLAB function

[bz, az] = impinvar(bs, as, Fs)

will compute the numerator az, and denominator bz coefficients for an impulse-invariant filter from the continuous prototype coefficients bs and as, with a sampling frequency Fs. The filter in Example 4 can be designed in a single line: [bz, az] = impinvar(1, [1 sqrt(2) 1], 2).