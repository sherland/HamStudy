6.002 Fall 2000 Lecture 3

**6.002 CIRCUITS AND**

**ELECTRONICS**

Superposition, Thévenin and Norton

∑ = 0 *loop Vi* z Circuit composition rules z Node method – the workhorse of 6.002 KCL at nodes using *V* 's referenced from ground (KVL implicit in " ") ( )*ji* <sup>−</sup> *ee <sup>G</sup>* z KVL: KCL: ∑ = 0 *node i I* VI

# **Review**

## Circuit Analysis Methods

6.002 Fall 2000 Lecture 3

Consider

# **Linearity**

Write node equations –

![](_page_2_Diagram_1.jpeg)

0 21 =−+ <sup>−</sup> *<sup>I</sup> R e R e V*

![](_page_2_Figure_5.jpeg)

6.002 Fall 2000 Lecture 3

Consider

# **Linearity**

Write node equations --

Rearrange --

![](_page_3_Diagram_1.jpeg)

0 21 =−+ <sup>−</sup> *<sup>I</sup> R e R e V* linear in *e V*,, *I*

*I*

*R*

*V*

*e*

*RR*

+= ⎥

⎦

<sup>⎤</sup> <sup>⎢</sup>

⎣

⎡

+

1 2 1

11

*G e* = *S*

conductance

matrix

node

voltages

linear sum

of sources

6.002 Fall 2000 Lecture 3

# **Linearity**

or *I RR <sup>R</sup> <sup>R</sup> <sup>V</sup> RR R e* 21 21 21 2 + + + =

*ae V* += *a V*<sup>2211</sup> +…+ *b I* + *b I*<sup>2211</sup> +…

Write node equations --

Rearrange --

0 21 =−+ <sup>−</sup> *<sup>I</sup> R e R e V* linear in *e V*,, *I*

*I R V e RR* += ⎥ ⎦ <sup>⎤</sup> <sup>⎢</sup> ⎣ ⎡ + 1 2 1 11

*G e* = *S*

conductance matrix

node

voltages

linear sum

of sources

Linear!

6.002 Fall 2000 Lecture 3

Linearity Homogeneity ⇒ Superposition

![](_page_5_Picture_1.jpeg)

6.002 Fall 2000 Lecture 3

### Linearity Homogeneity Superposition

#### Homogeneity

![](_page_6_Diagram_5.jpeg)

![](_page_6_Picture_2.jpeg)

6.002 Fall 2000 Lecture 3

### Linearity Homogeneity Superposition

#### Superposition

![](_page_7_Diagram_4.jpeg)

![](_page_7_Picture_1.jpeg)

6.002 Fall 2000 Lecture 3

### Linearity Homogeneity Superposition

## Specific superposition example:

![](_page_8_Diagram_5.jpeg)

![](_page_8_Diagram_6.jpeg)

![](_page_8_Picture_1.jpeg)

## Method 4: Superposition method

The output of a circuit is determined by summing the responses to each source acting alone.

![](_page_9_Picture_2.jpeg)

independent sources only

6.002 Fall 2000 Lecture 3

![](_page_10_Diagram_0.jpeg)

![](_page_10_Diagram_1.jpeg)

6.002 Fall 2000 Lecture 3

## **Back to the example** Use superposition method

![](_page_11_Diagram_1.jpeg)

6.002 Fall 2000 Lecture 3

## **Back to the example** Use superposition method

## *V* acting alone

![](_page_12_Diagram_2.jpeg)

## *I* acting alone

![](_page_12_Diagram_5.jpeg)

*I RR <sup>R</sup> <sup>R</sup> <sup>V</sup> RR R eee IV* 21 21 21 2 + + + =+=

## sum superposition

**Voilà !**

6.002 Fall 2000 Lecture 3

![](_page_13_Diagram_0.jpeg)

## Consider **Yet another method…**

![](_page_14_Diagram_2.jpeg)

no

units

By setting

0

,0

=

=∀

*i*

*Inn*

0

,0

=

∀ =

*i*

*Vmm*

All

0

,0

=∀

∀ =

*mm*

*nn V*

*I*

Arbitrary network **<sup>N</sup>**

## By superposition

*v V I Ri <sup>n</sup>*

*n m n*

*m*

= <sup>α</sup> *<sup>m</sup>* + ∑∑ <sup>β</sup> +

resistance

units

independent of external excitation and behaves like a voltage " " *TH v*

also independent of external excitement & behaves like a resistor

Or

*vv R i* = *TH* + *TH*

As far as the external world is concerned (for the purpose of I-V relation), "Arbitrary network N" is indistinguishable from:

![](_page_15_Diagram_3.jpeg)

*RTH TH v* open circuit voltage at terminal pair (a.k.a. port) resistance of network seen from port ( 's, 's set to 0) *Vm <sup>n</sup> I*

6.002 Fall 2000 Lecture 3

## Method 4: The Thévenin Method

Replace network N with its Thévenin equivalent, then solve external network E.

![](_page_16_Diagram_1.jpeg)

Thévenin equivalent

![](_page_16_Diagram_3.jpeg)

6.002 Fall 2000 Lecture 3

# Example:

![](_page_17_Diagram_1.jpeg)

![](_page_17_Diagram_2.jpeg)

*TH TH RR <sup>V</sup> <sup>V</sup> <sup>i</sup>* + <sup>−</sup> <sup>=</sup> 1 1

# Example:

: *RTH RTH* = *R*<sup>2</sup> + - *RTH R*2

: *VTH* 2 *TH* = *IRV* + - *VTH R*2 J*I*

6.002 Fall 2000 Lecture 3

#### Graphically, *vv <sup>R</sup> <sup>i</sup>* <sup>=</sup> *TH* + *TH*

![](_page_19_Figure_1.jpeg)

Open circuit () *i* ≡ 0 *TH* = *vv VOC*

Short circuit () *v* ≡ 0 *TH TH R <sup>v</sup> <sup>i</sup>* <sup>−</sup> <sup>=</sup> *SC* − *I*

6.002 Fall 2000 Lecture 3

Method 5:

# The Norton Method

in recitation, see text

![](_page_20_Diagram_3.jpeg)

Norton equivalent

*TH TH <sup>N</sup> R <sup>V</sup> <sup>I</sup>* =

6.002 Fall 2000 Lecture 3

# Summary

![](_page_21_Figure_5.jpeg)

#### Discretize matter

LMD LCA Physics EE

 R, I, V Linear networks Analysis methods (linear) KVL, KCL, I — V Combination rules Node method Superposition Thévenin Norton Next Nonlinear analysis Discretize voltage