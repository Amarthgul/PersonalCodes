# DESIGN 6400 Journal & Documentation 

Journal for DESIGN 6400 AU24 (Prof. Maria Palazzi). 

## How to Navigate: 

- Use the table of content to quickly jump to different chapters.
- **The journal that summarizes each week's progress can be found at the end** [(**or click here**)](#journals). 
- Use `History` on top right to inspect past versions or make comparasions. 

The most recent updated section can be found [here](#32---sufrace-iteration). Note that this is the section that received the most amount of progress with respect to the project, not the course. As such, this may not be the same as the journal content of the corresponding week. 

#### Table of content:

- [1 - General](#1---general)
  - [1.1 - Back Focal Distance and Telecentricity](#11---back-focal-distance-and-telecentricity)
  - [1.2 - Eesurgence in Film and Vintage Lenses](#12---resurgence-in-film-and-vintage-lenses)
- [2 - Wavelength Reconstruction](#2---wavelength-reconstruction)
  - [2.1 - Selecting the Distribution](#21---selecting-the-distribution)
- [3 - Ray Propagation](#3---ray-propagation)
  - [3.1 - Explore Ray Transfer Matrix](#31---explore-ray-transfer-matrix)
  - [3.2 - Sufrace Iteration](#32---sufrace-iteration)
    - [3.2.1 - Object to 1st Surface](#321---object-to-1st-surface)
    - [3.2.2 - Internal Surfaces](322---internal-surfaces)
    - [3.2.3 - Image Plane](#323---image-plane)
  - [3.3 - Aspherical Surface](#33---aspherical-surface)
    - [3.3.1 - Even Aspheric](#331---even-aspheric)
    - [3.3.2 - Cylindrical](#332---cylindrical)
  - [3.4 - Aperture Stop](#34---aperture-stop)
- [4 - Imager](#4---imager)
  - [4.1 - Tilt and Shift](#41---tilt-and-shift)
  - [4.2 - OLPF and UVIR Cut](#42---olpf-and-uvir-cut)
  - [4.3 - Film](#43---film)
- [5 - Diffraction](#5---diffraction)
- [Journals](#journals)
- [References](#references)


------------------ 

<br />

## 1 - General 

This project aims to establish a way with which a physical lens can be digitized and used in virtual productions, such as for digital animations and TV/movies post VFX, to emulate the optical characteristics of the physical optics in a virtual setting. 

Vintage lenses are (by definition) no longer in production, there will be a day when those lenses become inaccessible for the people that wish to use them. This project thus holds a certain level of time sensitivity and will need to reach some degree of completion before vintage lenses become antique and eventually history. 

<br />

### 1.1 - Back Focal Distance and Telecentricity  

In optics, the distance between the last surface of the lens and the image plane is referred to as the `Back Focal Distance` (**BFD** for short, sometimes it is also referred to interchangeably as `Back Focal Length`). 

While BFD may seem to be a free space, in many cases it is rather constrained. For a single lens reflex (SLR) camera, the mirror is placed between the lens and the image plane, reflecting the light up into the prism and then into the viewfinder. This means the BFD must be long enough to accommodate the mirror chamber and the shutter mechanism in front of the image plane. This is the direct reason why 135 format SLRs all have a flange distance of about 40mm. 

For lens design, BFD indriectly ties in with telecentricity. Below is the layout/crossection of the lens Jupiter-12 35mm f/2.8, it has a very shoty BFD and the rays exit lens at a large angle: 

<div align="center">
	<img src="resources/Jupiter12Layoutinf.png" width="512">
  <p align="center">Figure 1.1. Jupiter-12 35mm f/2.8</p>
</div>

In comparison, longer BFD tend to force the exiting rays to be more telecentric, as demonstrated below: 

<div align="center">
	<img src="resources/Canon85LayoutInf.png" width="512">
  <p align="center">Figure 1.2. Canon 85mm f/1.2</p>
</div>

Note that for the Canon lens in figure 1.2, the last surface is relatively far away from the image plane (long BFD), and the exiting ray at the top have a smaller oblique angle compare to the Jupiter lens. For a pure telecentirc lens, all the exiting rays will be parallel to the optical axis. 

While high telecentricity can be very desirable for some scenarios, such as industrial applications, it also adds difficulty to lens design, especially wide angle lenses with a relatively large image circle. This makes designing wide angle lenses for SLR cameras rather difficult, designers have to resort to the inverse telephoto paradigm, straightening the existing ray for them to reach the image plane. For this reason, most wide angle lenses in the SLR era are bigger and heavier. 

In comparison, rangefinder lenses can have their elements “sink” into the camera and get really close to the image plane, such as the Jupiter-12 example in figure 1.1. More extreme examples can be seen at Zeiss Hologon 16mm f/8, which achieved 16mm wide angle with an astonishingly small body, also with highly non-telecentric design. For those lenses, even if the camera flange distance allows adaptation, the protruding rear element may also be in the way and prevents the camera from taking a picture. 

With the advancement of technology, there are less and less reasons to keep the mirror for digital cameras. Eventually the mirror was removed and digital imaging fully embraced mirrorless cameras. For mirrorless cameras, there is nothing in between the lens and the image plane (aside from some filter glasses like OLPF and UV IR cut, see [chapter 4.2](#42---olpf-and-uvir-cut)). This literated BFD in lens design, allowing lens designers to come up with optics that fully utilizes this space. 

<div align="center">
	<img src="resources/FlangeChart.png" width="960">
  <p align="center">Figure 1.3. Flange distance for different camera mounts. Showing only the main streams (there were a lot of main streams historically), some of the more proprietary and scarce mounts are omitted to save space</p>
</div>

The liberation of BFD also means that older lenses designed for rangefinder cameras, which tend to have a short BFD and consequently shorter flange distance, can now also be adapted and mounted onto mirrorless cameras. Due to the lack of mirror, even if a lens was originally designed for a system with even shorter flange distance, it can still be adapted onto new mirrorless cameras, such as putting an M42 lens onto a PL mount camera. From the technical aspect, this ensured that a vintage lens can be adapted onto almost any modern camera and is one of the driving forces for the resurgence. 

<br />

### 1.2 - Resurgence in Film and Vintage Lenses 

Placeholder 

<br />

## 2 - Wavelength Reconstruction 

For this application, a pixel on an image or a point in a 3D scene can both be viewed as a light source emiting light.  

In virtually all software the color of the pixel or the color of the point on the 3D object is expressed by RGB value (although underlaying implementations may vary). However, in reality, the color of the light is determined by the distribution and the intensity of every wavelength. This is important because refraction is dependent on wavelength, as light of different wavelength will be bent differently when entering another material with a different refraction index. 

RGB can be treated as 3 Gaussian distributions of wavelengths. With the RGB value on each channel representing the intensity of the peak wavelength, acting as a scale factor for the entire distribution. Integrating over all 3 distributions will then yield a spectral representation of the given RGB color, and the same process can be used to translate the wavelength distribution into RGB value. 
For ease of calculation (especially later with Abbe number), it may be fitting to choose the peak wavelength of RGB as: 

$$R = \lambda _{C} = 656.27 \mu m$$

$$G = \lambda _{d} = 587.56 \mu m$$

$$B = \lambda _{F} = 486.13 \mu m$$

<br />

### 2.1 - Selecting the Distribution 

Although integrating the 3 Gaussian distribution can be more accurate in calculating the color shift and tint in an optical system, it faces some challenges at the end of the system. Consider the case of an orthochromatic film:

<div align="center">
	<img src="resources/OrthoPlusSp.png" width="360">
  <p align="center">Figure 2.1. Ilford Ortho Plus Spectral Sensitivity</p>
</div>

The image above showed the spectral sensitivity of [Ilford Ortho Plus](https://www.ilfordphoto.com/amfile/file/download/file/1948/product/1658) film. As can be seen, this type of film is sensitive to blue and green but not to red, red objects will appear black when shot on this film. 

The integrated spectral distribution will be clipped by the spectral sensitivity of the orthochromatic film, and the red side of the spectrum will become zero. However, due to the red channel is a Guassian distribution, there will still be part of the red channel that overlaps with the the green section, making reconstruction difficult. In this situation, it could be hard to find the RGB color using 3 Guassian distributions whose $\mu$ is still the same as the original. 

Another significant influencer is **Metamerism**, while two colors may be perceived the same, the actual composition of wavelengths and their intensities may be different. This is particularly true for colors that look warm due to the large overlapping wavelength for human green and red cod cells. On the flip side, blue rod cells caps at around 470 nm, making wavelengths shorter than that rather deterministic (also the reason why wavelengths at the shorter end in the CIE 1931 chart are located on a near straight line). 

<br />

## 3 - Ray Propagation 

With the color of the ray fixed, the refraction index will also become determinsitic. Now it is possible to propagate rays through different surfaces. 

### 3.1 - Explore Ray Transfer Matrix

In geometric optics, a ray can be described by:

$$\binom{h_2}{\gamma _2}$$

$h_2$ is the height of the light (from the optical axis), and $\gamma _2$ its angle. As such, the ray propagatiion can be expressed as a matrix operation: 

$$\binom{h_2}{\gamma _2}=\begin{bmatrix}
 \mathbb{A}& \mathbb{B} \\
\mathbb{C} & \mathbb{D} \\
\end{bmatrix}\cdot \binom{h_1}{\gamma _1}$$

Where the different components of the matrix can be configured differently to represent translation and refraction. This is very similar to 2D transformation matrix, the only difference is that $\gamma$ represents the radian and thus the "rotation" is based on the Snell's law, as defnied by: 

$$n_1 \sin \theta _1 = n_2 \sin \theta _2$$

Typically, the translation matrix will be denoted as $\mathbf{T}$ and refration matrix as $\mathbf{R}$. Under the paraxial assumption, it can be derived that: 

$$\mathbf{T}=\begin{bmatrix}
1 & -l \\
0 & 1 \\
\end{bmatrix}$$

$$\mathbf{R}=\begin{bmatrix}
1 & 0 \\
\frac{n_2 - n_1}{n_2 \cdot r} & \frac{n_1}{n_2} \\
\end{bmatrix}$$

Where $l$ is the traveled length, $r$ is the surface radius, $n_1$ and $n_2$ are the RI of each medium. 
Then, a ray going through a lens can be represented as: 

$$\binom{h_3}{\gamma _3}= \mathbf{M} _L \binom{h_1}{\gamma _1} \quad with \quad \mathbf{M} _L= \mathbf{R} _2 \mathbf{T} _{12} \mathbf{R} _1$$

The translation and refraction matrix can then be pre-multiplied and thus represent the lens with one single matrix. For a lens with multiple elements, this process is still applicable, allowing the ray transfer to be condensed into simple matrix multiplications. 

This approach, however, does not fit here. On one hand, the ray transfer matrix is established under paraxial approximation, which assumes the oblique angle of the incident light $\theta$ to be small enough that it equals $\sin \theta$. On the other hand, the ray transfer applies only on a 2D plane or an axisymmetric lens, which is not the case here. Additionally, the ray transfer matrix is also sequential, as it ignores reflection at each surface and the scattering during ray propagation. 

For this application, the lens can be non-axisymmetric due to the inclusion of cylindrical and conical elements. And to emulate veiling glares and some types of flares, reflection also needs to be modeled, which makes this process non-sequential. To put it simply, it is closer to a 3D ray tracer application. 

For 3D, representing an angle in degrees or radians can be difficult, as Euler angles are susceptible to gimbal lock. Quaternions are free from these sufferings but are rather questionable to be used to calculate reflections and refractions, due to the need of being translated into Euler angle, perform reflection and refractions, then translate back to quaternions again. 

One way to work around that might be to use vectors to represent the ray direction, this also avoids the gimbal lock and rotation hierarchy problem. With 3D vectors, it can be proved that when the incident vector $\mathbf{I}$ in a medium with RI $n_1$ enters a different medium with RI $n_2$, given the normal at the point of incident to be $\mathbf{N}$, then the refracted vector $\mathbf{R}$ can be expressed as:  

$$ \mathbf{R}=\frac{n_1}{n_2}\left ( \mathbf{I} - \left ( \mathbf{I} \cdot \mathbf{N} \right ) \mathbf{N} \right ) - \mathbf{N} \sqrt{ 1 - \left ( \frac{n_1}{n_2} \right ) ^{2} \left ( 1 -  \left( \mathbf{I} \cdot \mathbf{N} \right )^{2} \right ) }$$

In a similar way, the reflection vector can be defined as: 

$$\mathbf{R}=\mathbf{I}-2 \left ( \mathbf{I} \cdot \mathbf{N} \right ) \mathbf{N}$$

To use these vector equations in the same way as the ray transfer matrix, there need to be a matrix $\mathbf{M}$ such that: 

$$\mathbf{R} = \mathbf{M} \cdot \mathbf{I}$$

Take the refraction equation as an example. Use $$\sigma = \frac{n_ 1}{n_ 2}$$ to substitute the corresponding terms, and disassemble the vectors as:

$$\mathbf{R} = \begin{pmatrix} 
R_x \\
R_y \\   
R_z \\
\end{pmatrix}$$

$$\mathbf{N} = \begin{pmatrix} 
N_x \\
N_y \\   
N_z \\
\end{pmatrix}$$

$$\mathbf{I} = \begin{pmatrix} 
I_x \\
I_y \\   
I_z \\
\end{pmatrix}$$

The vector refraction formula can then be written as: 

$$\mathbf{R} = \begin{pmatrix}  
R_x \\ 
R_y \\  
R_z \\
\end{pmatrix}=\begin{pmatrix}  
I_x \left( \sigma - \sigma N_x^2\right) - I_y \left( \sigma N_y N_x \right) - I_z \left( \sigma N_z N_x \right) \\ 
I_y \left( \sigma N_x N_y \right) - I_y \left( \sigma - \sigma N_y^2 \right) - I_z \left( \sigma N_z N_y \right) \\  
I_z \left( \sigma N_x N_z \right) - I_y \left( \sigma N_y N_z \right) - I_z \left( \sigma - \sigma N_Z^2 \right) \\
\end{pmatrix} - \begin{pmatrix} 
N_x \\
N_y \\   
N_z \\
\end{pmatrix} S
$$

Where $S$ is a scalar defined by $\mathbf{I}$ and $\mathbf{N}$:

$$S = \sqrt{ 1 - \sigma^2 + \sigma^2 I_x^2 N_x^2 + \sigma^2 I_y^2 N_y^2 + \sigma^2 I_z^2 N_z^2 + 2 \sigma ^2 I_x I_y N_x N_y + 2 \sigma ^2 I_x I_y N_x N_y +2 \sigma ^2 I_z I_x N_z N_x }$$

This turned out to be troublesome, terms like $\sigma ^2 I_x I_y N_x N_y$ makes it very hard to rearrange $S$ such that there exists a matrix $M$ that satisfies $\mathbf{R} = \mathbf{M} \cdot \mathbf{I}$. This also indicates that the different terms in the incident vector in 3D are not independent from each other upon refraction, which makes sense. To summarize, **in a 3D setting without the paraxial approximation, the ray transfer matrix may not work**. 

Luckily, this is not the end of the story. Not being able to obtain a matrix multiplication form of refraction simply means that the program may have to iterate through every surface instead of aggregate all the surfaces together, it will take more time, but still doable. 

<br />

### 3.2 - Sufrace Iteration 

Before feeding a ray into the lens, the surfaces must be defined. A typical spherical surface in this application has 4 attributes:

- **Radius** $r$. The surface curvature. 

- **Material**. A material attribute is used instead of $n_D$ and $v_D$ since refraction and reflectance vary by wavelength, using material could ensure that refractive index can be freely calculated depending on the wavelength. This attribute is presented in the form of a `string` like `LASFN1`, a look-up table is used to retrive the parameters of the material. 

- **Clear semi-diameter** $d$. The name “semi-diameter” is borrowed from Zemax, it essentially describes the working radius of the surface, calculated by height from the optical axis. Radius larger than that will be treated as a flat plane perpendicular to the axis. This value is non-negative, and for a lens group with 2 or more surfaces (such as a doublet), the clear semi-diameter of the first surface will be used for the rest of surfaces as well. 

- **Edge chamfer** $c$. At the edge of the clear semi-diameter, a 45 degree chamfer can be applied. The positive chamfer value points to the positive $z$ direction, which means this value should be either 0 or having the opposite sign of $r$.  For a lens group with 2 or more surfaces, only the first and last sufrace's chamfer will be calculated. 

<div align="center">
	<img src="resources/SurfaceNotes.png" width="512">
  <p align="center">Figure 3.1. Notations for surfaces, negative values are noted in red.</p>
</div>

Aside from the chamfer, the rest are the same as most optical simulation software, like Zemax and CODEX. 

It is also worth noting that here we defined the origin to be the vertex of the first surface. The coordinate system is a right hand system with the positive $y$ axis pointing up, The $z$ axis is the optical axis for the lens and its positive direction points to the direction of the image plane, as shown in the figure below. 


<div align="center">
	<img src="resources/systemNote.png" width="320">
  <p align="center">Figure 3.2. The coordinate system used.</p>
</div>

Readers may notice this coordinate seems to contradict the surface radius direction. The sign of the surface radius is set to conform to the lens design tradition, with positive being convex and negative being concave when viewing from the front. 

<br />

#### 3.2.1 - Object to 1st Surface 

For an object point $P$ not located at infinity, ignoring indirect reflections for now, all the light reflected from this point that can be gathered by the lens forms a cone. If the object point is not directly on the optical axis, then this cone becomes an oblique cone. 

The next task is to sample the lights in this oblique cone evenly. The most obvious way may be to subdivide the circle formed by the clear semi-diameter $d$, but as we will show later in the case of extreme oblique angle, this sampling method will introduce unevenness when the surface radius gets large. A better way is to sample from the projection of $d$ from the direction of the object point $P$. 

<div align="center">
	<img src="resources/OffAxisCone.png" width="500">
  <p align="center">Figure 3.3. Cross section of an oblique cone.</p>
</div>

The figure above shows the cross section of the oblique cone on the plane that contains its apex, the figure below shows the cone in a more 3D enviroment: 

<div align="center">
	<img src="resources/Cone3dDiagram.png" width="500">
  <p align="center">Figure 3.4. The cone in 3D.</p>
</div>

Let the location of the point $P$ to be:

$$P = \left( p_x, p_y, p_z \right) ^ T$$

Then, the position of point $A$ and $C$ can be accquired by timing the clear semi-diamater $d$ with the normalized $xy$ directional vector: 

$$A = d \frac{\left( p_x, p_y, 0 \right) ^ T}{\left|  \left( p_x, p_y, 0 \right) ^ T \right|} =
\begin{pmatrix} 
d p_x / \sqrt{p_x ^ 2 + p_y ^ 2} \\ 
d p_y / \sqrt{p_x ^ 2 + p_y ^ 2} \\
0 \\
\end{pmatrix}$$

and:

$$C = d \frac{\left( -p_x, -p_y, 0 \right) ^ T}{\left|  \left( -p_x, -p_y, 0 \right) ^ T \right|} =
\begin{pmatrix} 
-d p_x / \sqrt{p_x ^ 2 + p_y ^ 2} \\ 
-d p_y / \sqrt{p_x ^ 2 + p_y ^ 2} \\
0 \\
\end{pmatrix}$$

This makes it possible to calculate $\vec{PA}$ and $\vec{PC}$. Let $\mathbf{\hat{a}}$ and $\mathbf{\hat{c}}$ to denote the normalized $\vec{PA}$ and $\vec{PC}$, then the direction of vector $\vec{PD}$ can be accquired by simply averging them: 

$$\vec{n} = \frac{ \mathbf{\hat{a}} + \mathbf{\hat{c}} }{2}=\begin{pmatrix} 
n_x \\ 
n_y \\
n_z \\
\end{pmatrix}$$

Note that $\vec{n}$ is also the normal vector the the projected conical area we are trying to get, as such, the plane passing through point $A$, in which the conical area resides in, can be defined as: 

$$n_x \left( x - \frac{d p_x}{ \sqrt{p_x ^ 2 + p_y ^ 2} }  \right) + 
n_y \left( y - \frac{d p_y}{  \sqrt{p_x ^ 2 + p_y ^ 2} } \right) + n_z z = 0$$

For the typical plane equation $Ax + By + Cz + D = 0$, this gives us: 

$$\begin{empheq}{align}
 A &= n_x\\
 B &= n_y\\
 C &= n_z\\
 D &= -\frac{d p _x n _x + d p _y n _y}{ \sqrt{p _x ^2 + p _y ^2} }
\end{empheq}$$

This then allows us to find the position of point $B$:

$$p_B=\begin{pmatrix} 
p_x + t \left( - \frac{dp_x}{\sqrt{p _x ^2 + p _y ^2}}  - p _x  \right)  \\ 
p_y + t \left( - \frac{dp_y}{\sqrt{p _x ^2 + p _y ^2}}  - p _y \right)  \\
p_z + t \left(  - P _z \right)  \\
\end{pmatrix}$$

With $t$ being: 

$$t=\frac{-n _x p _x - n _y p _y - n _z p _z + \frac{d p _x n _x + d p _y n _y}{ \sqrt{p _x ^2 + p _y ^2} } }
{n _x \left( - \frac{dp_x}{\sqrt{p _x ^2 + p _x ^2}}  - p _y \right) + n _ y \left( - \frac{dp_y}{\sqrt{p _x ^2 + p _y ^2}}  - p _y \right) + n _z \left( - p _z \right)}$$

This then allows us to derive the equation for the eclipse perpendicular to plane $PAC$ and passing through $AB$, illustrated in the figure below as the pink ellipse: 

<div align="center">
	<img src="resources/3.2.1VerticalConical.png" width="360">
  <p align="center">Figure 3.5.</p>
</div>

As a 2D shape, the ellipse can be described as: 

$$\frac{x ^ 2}{a ^ 2} + \frac{y ^ 2}{b ^ 2} = 1$$

Where: 

$$a = \frac{AB}{2}$$

$$b = \frac{ \sqrt{B B\' \cdot AC} }{ 2 }$$

Apparently, $AB$ can be accquired by subtracting the postion of the two points, and $BB\'$ can be calculated by exploiting the similarity between $PBB\'$ and $PCA$, it is also quite convenient since $AC$ is the clear diameter, i.e., $AC = 2d$. 

<br />

#### 3.2.2 - Internal Surfaces

Placeholder 

<br />

#### 3.2.3 - Image Plane 

Placeholder

<br />

### 3.3 - Aspherical Surface 

Placeholder 

<br />

#### 3.3.1 - Even Aspheric 

Standard ASPH elements, which can be seen as early as the FD 55mm f/1.2 Asph. 

<br />

#### 3.3.2 - Cylindrical 

For anamorphic lenses. 

<br />

### 3.4 - Aperture Stop 

Placeholder 

<br />

## 4 - Imager

In [chapter 3.2.3](#323---image-plane) it is already discussed how to intersect a simple imager with rays, this chapter will focus on the more complex effects of the imager, such as tilt shift, halation, and spectral response. 

<br />

### 4.1 - Tilt and Shift

Placeholder 

<br />

### 4.2 - OLPF and UVIR Cut 

Placeholder 

<br />

### 4.3 - Film

Placeholder 

<br />

## 5 - Diffraction 

Up till this point, the project has been operating under the realm of geometric optics, i.e., treating lights as beams and particles. However, geometric optics cannot replicate one of the most famous optical artifacts used in movies, TVs, and video games: **flares**. 

<br />

## Journals

- [Week 2 (Aug 26th)](#week-2)
- [Week 1 (Aug 19th)](#week-1)

### Week 2

(Week of Aug 26th)

Attempting to disassemble the ray transfer matrix in 3D revealed that this approach may not work, documented in chapter [3.1](#31---explore-ray-transfer-matrix). 

<br />

### Week 1

(Week of Aug 19th)

This week was mostly spent on setting up this markdown document and some initialization work for the course. The table of content was drafted according to my estimation and will hopefully provide a directional guide in the rest of the semester. In this documentation I have been working on the first several chapters, particularly the first introductory chapter, preparing it for the next research proposal assignment.  

For now, I intend to spend the first 5 weeks on the math part, establishing a theoretical foundation for the later implementation (paper prototype, one can say). Although some degree of implementation may be attempted. 

<br />

## References 

Placeholder 
