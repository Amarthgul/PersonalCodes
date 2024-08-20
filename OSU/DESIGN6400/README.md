# DESIGN 6400 Journal 

Journal for DESIGN 6400 AU24 (Prof. Maria Palazzi). 

## How to Navigate: 

- This page is in constant update as per course update.
- Old versions can be traced back throught the GitHub version history. 
- The most recent update according to the submitted assignment is linked below. 

In-page link to the most recent update: [here](#general)

------------------ 

## General 

Placeholder

## Wavelength Reconstruction 

For each pixel or point in a 3D scene, it emits a light. 

In virtually all software the color of the pixel or the color of the point on the 3D object is expressed by RGB value. However, in reality, the color of the light is determined by the distribution of the wavelength. This is important because refraction is dependent on wavelength, as light of different wavelength will be bent differently when entering another material. 

For some colors, they have no direct correlation with certain wavelength, i.e., can be achieved by mixing different wavelengths with different weight. This in itself deserves a short paper and will be discussed in later chapters. 

For now, the RGB can be treated as 3 Gaussian distributions representing the 3 channels. With the RGB value on each channel representing the intensity of the peak wavelength, acting as a scale factor for the entire distribution. Integrating over all 3 distributions will then yield a spectral representation of the given RGB color, and the same process can be used to translate the wavelength distribution into RGB value. 
For ease of calculation (especially later with Abbe number), it may be fitting to choose the peak wavelength of RGB as: 

$$R = \lambda _{C} = 656.27 \mu m$$

$$G = \lambda _{d} = 587.56 \mu m$$

$$B = \lambda _{F} = 486.13 \mu m$$


