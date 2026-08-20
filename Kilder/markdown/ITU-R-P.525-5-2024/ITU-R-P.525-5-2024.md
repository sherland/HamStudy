# **Recommendation ITU-R P.525-5**

**(11/2024)**

P Series: Radiowave propagation

# **Calculation of free-space attenuation**

#### **Foreword**

The role of the Radiocommunication Sector is to ensure the rational, equitable, efficient and economical use of the radiofrequency spectrum by all radiocommunication services, including satellite services, and carry out studies without limit of frequency range on the basis of which Recommendations are adopted.

The regulatory and policy functions of the Radiocommunication Sector are performed by World and Regional Radiocommunication Conferences and Radiocommunication Assemblies supported by Study Groups.

# **Policy on Intellectual Property Right (IPR)**

ITU-R policy on IPR is described in the Common Patent Policy for ITU-T/ITU-R/ISO/IEC referenced in Resolution ITU-R 1. Forms to be used for the submission of patent statements and licensing declarations by patent holders are available from<http://www.itu.int/ITU-R/go/patents/en> where the Guidelines for Implementation of the Common Patent Policy for ITU-T/ITU-R/ISO/IEC and the ITU-R patent information database can also be found.

|        | Series of ITU-R Recommendations                                                      |
|--------|--------------------------------------------------------------------------------------|
|        | (Also available online at https://www.itu.int/publ/R-REC/en)                         |
| Series | Title                                                                                |
| BO     | Satellite delivery                                                                   |
| BR     | Recording for production, archival and play-out; film for television                 |
| BS     | Broadcasting service (sound)                                                         |
| BT     | Broadcasting service (television)                                                    |
| F      | Fixed service                                                                        |
| M      | Mobile, radiodetermination, amateur and related satellite services                   |
| P      | Radiowave propagation                                                                |
| RA     | Radio astronomy                                                                      |
| RS     | Remote sensing systems                                                               |
| S      | Fixed-satellite service                                                              |
| SA     | Space applications and meteorology                                                   |
| SF     | Frequency sharing and coordination between fixed-satellite and fixed service systems |
| SM     | Spectrum management                                                                  |
| SNG    | Satellite news gathering                                                             |
| TF     | Time signals and frequency standards emissions                                       |
| V      | Vocabulary and related subjects                                                      |

*Note*: *This ITU-R Recommendation was approved in English under the procedure detailed in Resolution ITU-R 1.*

*Electronic Publication* Geneva, 2024

# RECOMMENDATION ITU-R P.525-5

# **Calculation of free-space attenuation**

(1978-1982-1994-2016-2019-2024)

#### **Scope**

This Recommendation provides methods to calculate the attenuation in free space.

#### **Keywords**

Free space, attenuation, telecommunication links

# **Related ITU Recommendations**

Recommendation [ITU-R P.341](https://www.itu.int/rec/R-REC-P.341/en)

Recommendation [ITU-R P.368](https://www.itu.int/rec/R-REC-P.368/en)

NOTE – In every case the latest edition of the Recommendation in force should be used.

The ITU Radiocommunication Assembly,

*considering*

that free-space propagation is a fundamental reference for radio-engineering,

*recommends*

that the methods in the Annex should be used for the calculation of attenuation in free space.

# **Annex**

## **1 Introduction**

For the purposes of radiocommunication, free space is defined as a perfect vacuum which may be considered of infinite extent in all directions, so that free space propagation is the propagation of a radio wave radiating in free space[1](#page-2-0).

As free-space propagation is often used as a reference in other texts, this Annex presents relevant formulae.

<span id="page-2-0"></span><sup>1</sup> The International Standards Organisation in its electrotechnical vocabulary (electropedia) has a more general definition:

Free space propagation: propagation of an electromagnetic wave in a homogeneous ideal dielectric medium which may be considered of infinite extent in all directions

NOTE – For propagation in free space, the magnitude of each vector of the electromagnetic field in any given direction from the source is proportional to the reciprocal of the distance from the source beyond a distance determined by the size of the source and the wavelength.

#### **2 Basic formulae for telecommunication links**

Free-space propagation may be calculated in different ways, each of which is adapted to a particular type of service.

### **2.1 Point-to-area links**

If there is a transmitter serving several randomly-distributed receivers (broadcasting, mobile service), the electric field is calculated at a point located at some appropriate distance from the transmitter by the expression:

�� = √30�� �� (1)

where:

*e* : r.m.s. field strength (V/m) (see Note 1) *p*: equivalent isotropically radiated power (e.i.r.p.) of the transmitter in the direction of the point in question (W) (see Note 2) *d*: distance from the transmitter to the point in question (m).

Equation (1) is often replaced by equation (2) which uses practical units:

��mV/m <sup>=</sup> <sup>173</sup> √��kW ��km (2)

where:

*e*mV/m : r.m.s field strength (mV/m)

*p*kW : equivalent isotropically radiated power (e.i.r.p.) of the transmitter in the direction of the point in question (kW)

*d*km : distance from the transmitter to the point in question (km).

For antennas operating in free-space conditions the cymomotive force may be obtained by multiplying together *e* and *d* in equation (1). Its dimension is volts.

NOTE 1 – If the wave is elliptically polarized and not linear, and if the electric field components along two orthogonal axes are expressed by *e<sup>x</sup>* and *e<sup>y</sup>* , the left-hand term of equation (1) should be replaced by *e e <sup>x</sup> y* <sup>2</sup> <sup>2</sup> <sup>+</sup> . *e<sup>x</sup>* and *e<sup>y</sup>* can be deduced only if the axial ratio is known. *e* should be replaced by *e* 2 in the case of circular polarization.

NOTE 2 – In the case of antennas located at ground level (typically at relatively low frequencies) with vertical polarization, radiation is generally considered only in the upper half-space. When the ground is assumed to be plane and perfectly conducting, the power flux-density for a given radiated power is doubled, as compared with an antenna in free space. (Alternatively, when considering field strengths, the field strength is similarly increased by 3 dB.) This should be taken into account in determining the radiated power (and is already included in Recommendation [ITU-R P.368](https://www.itu.int/rec/R-REC-P.368/en) and in Annex 3 to Recommendation [ITU-R P.341\)](https://www.itu.int/rec/R-REC-P.341/en).

# **2.2 Relations between the characteristics of a plane wave**

There are also relations between the characteristics of a plane wave (or a wave which can be treated as a plane wave) at a point:

�� = �� 2 120π = 30�� 120π��<sup>2</sup> <sup>=</sup> �� <sup>×</sup> 1 4π��2 (3)

where:

*s*: power flux-density (W/m<sup>2</sup> ) *e* : r.m.s. field strength (V/m)

*p*: equivalent isotropically radiated power (e.i.r.p.) of the transmitter in the direction of the point in question (W).

#### **2.3 Point-to-point links**

For a point-to-point link between isotropic antennas, it is necessary to consider the power at the output of the receiving isotropic antenna ���� at the point in question:

���� = �� × �� = �� 4π��<sup>2</sup> <sup>×</sup> λ 2 4π , (4)

where:

��: effective aperture of a receiving isotropic antenna (m<sup>2</sup> ).

Introducing free-space attenuation between isotropic antennas, also known as the free-space basic transmission loss (symbols: *Lbf* or *Abf*), it can be calculated as follows (see Recommendation [ITU-R](https://www.itu.int/rec/R-REC-P.341/en) P.341):

������ <sup>=</sup> −10 log<sup>10</sup> ( 1 4π��<sup>2</sup> <sup>×</sup> λ 2 4π ) <sup>=</sup> <sup>20</sup> log<sup>10</sup> ( 4π�� λ ) dB (5)

where:

*Lbf* : free-space basic transmission loss (dB) *d*: distance : wavelength, and

*d* and are expressed in the same unit.

Equation (5) can also be written using the frequency instead of the wavelength.

������ = 32.4 + 20 log<sup>10</sup> �� + 20 log<sup>10</sup> �� dB (6)

where:

*f*: frequency (MHz) *d*: distance (km).

# **3 The free-space basic transmission loss for a radar system** (symbols: *Lbr* or *Abr*)

Radar systems represent a special case because the signal is subjected to a loss while propagating both from the transmitter to the target and from the target to the receiver. For radars using a common antenna for both transmitter and receiver, a radar free-space basic transmission loss, *Lbr*, can be written as follows:

������ = 103.4 + 20 log<sup>10</sup> �� + 40 log<sup>10</sup> �� − 10 log<sup>10</sup> σ dB (7)

where:

: radar target cross-section (m<sup>2</sup> ) *d*: distance from the radar to the target (km) *f*: frequency of the system (MHz).

The radar target cross-section of an object is the ratio of the total isotropically equivalent scattered power to the incident power density.

#### **4 Conversion formulae**

On the basis of free-space propagation, the following conversion formulae may be used.

Field strength for a given isotropically transmitted power:

�� = ���� − 20 log<sup>10</sup> �� + 74.8 (8)

Available power received through a conjugately matched isotropic receiving antenna for a given field strength:

���� = �� − 20 log<sup>10</sup> �� − 167.2 (9)

Free-space basic transmission loss for a given isotropically transmitted power and field strength:

������ = ���� − �� + 20 log<sup>10</sup> �� + 167.2 dB (10)

Power flux-density for a given field strength:

�� = �� − 145.8 (11)

where:

*Pt* : isotropically transmitted power (dB(W)) *Pr* : available power received through a conjugately matched antenna (dB(W)) *E*: electric field strength (dB(V/m)) *f*: frequency (GHz) *d*: radio path length (km) *Lbf* : free-space basic transmission loss (dB) *S*: power flux-density (dB(W/m<sup>2</sup> )).

Note that equations (8) and (10) can be used to derive equation (6).