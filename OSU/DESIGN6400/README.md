# DESIGN 6400 Journal 

Journal for DESIGN 6400 AU24 (Prof. Maria Palazzi). 

## How to Navigate: 

- Use the table of content to quickly jump to different chapters. 
- The most recent update according to the submitted assignment is linked below. 

In-page link to **the most recent update**: [here](#sufrace-iteration). 

Please note that the same chapter may be modified over time with the project progresses. To inspect the older versions, use the GitHub version history feature. 

#### Table of content:

- [1 - General](#1---general) 
- [2 - Wavelength Reconstruction](#2---wavelength-reconstruction)
  - [2.1 - Selecting the Distribution](#21---selecting-the-distribution)
- [3 - Ray Propagation](#3---ray-propagation)
  - [3.1 - Explore Ray Transfer Matrix](#31---explore-ray-transfer-matrix)
  - [3.2 - Sufrace Iteration](#32---sufrace-iteration)
  - [3.3 - Aspherical Surface](#33---aspherical-surface)
  - [3.4 - Aperture Stop](#34---aperture-stop)
- [4 - Imager](#4---imager)
------------------ 

## 1 - General 

Placeholder

## 2 - Wavelength Reconstruction 

For each pixel or point in a 3D scene, it emits a light. 

In virtually all software the color of the pixel or the color of the point on the 3D object is expressed by RGB value. However, in reality, the color of the light is determined by the distribution of the wavelength. This is important because refraction is dependent on wavelength, as light of different wavelength will be bent differently when entering another material. 

For some colors, they have no direct correlation with certain wavelength, i.e., can be achieved by mixing different wavelengths with different weight. This in itself deserves a short paper and will be discussed in later chapters. 

For now, the RGB can be treated as 3 Gaussian distributions representing the 3 channels. With the RGB value on each channel representing the intensity of the peak wavelength, acting as a scale factor for the entire distribution. Integrating over all 3 distributions will then yield a spectral representation of the given RGB color, and the same process can be used to translate the wavelength distribution into RGB value. 
For ease of calculation (especially later with Abbe number), it may be fitting to choose the peak wavelength of RGB as: 

$$R = \lambda _{C} = 656.27 \mu m$$

$$G = \lambda _{d} = 587.56 \mu m$$

$$B = \lambda _{F} = 486.13 \mu m$$

### 2.1 - Selecting the Distribution 

Placeholder

## 3 - Ray Propagation 

With the color of the ray fixed, the refraction index will also become determinsitic. Now it is possible to propagate rays through different surfaces. 

### 3.1 - Explore Ray Transfer Matrix

In geometric optics, under the paraxial approximation, a ray can be described by:

$$\binom{h_2}{\gamma _2}$$

$$h_2$$ is the height of the light, and $$\gamma _2$$ its angle. As such, the ray propagatiion can be expressed as a matrix operation: 

$$\binom{h_2}{\gamma _2}=\begin{bmatrix}
 \mathbb{A}& \mathbb{B} \\
\mathbb{C} & \mathbb{D} \\
\end{bmatrix}\cdot \binom{h_1}{\gamma _1}$$

Where the different components of the matrix can be configured differently to represent translation and refraction. Typically, the translation matrix will be denoted as $$\mathbf{T}$$ and refration matrix as $$\mathbf{R}$$. Then, a ray going through a lens can be represented as: 


$$\binom{h_3}{\gamma _3}= \mathbf{M} _L \binom{h_1}{\gamma _1} \quad with \quad \mathbf{M} _L= \mathbf{R} _2 \mathbf{T} _{12} \mathbf{R} _1$$


### 3.2 - Sufrace Iteration 

Placeholder 

### 3.3 - Aspherical Surface 

Placeholder 

### 3.4 - Aperture Stop 

Placeholder 

## 4 - Imager

Placeholder 

