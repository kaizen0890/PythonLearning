import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import math


img = cv2.imread('./images/1.bmp')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## Apply DFT using opencv function
dft = cv2.dft(np.float32(gray),flags = cv2.DFT_COMPLEX_OUTPUT)
## Apply FFT using numpy function
dft_np = np.fft.fft2(img)
## Get image size
height = np.size(img, 0)
width = np.size(img, 1)
## Bring magnitude to center for easy analyze
dft_shift = np.fft.fftshift(dft)
## Get magnitude and phase after FFT
magnitude, angle = cv2.cartToPolar(dft_shift[:,:,0],dft_shift[:,:,1])
## Calculate magnitude spectrum
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
## Calculate magnitude spectrum  
"""
 magnitude = sqrt(real^2 + image^2)
 phase = arctan2 (real, image)
"""
phase = np.arctan2(dft_shift[:,:,0],dft_shift[:,:,1])
## Create matrix which will store complex part after change magnitude/phase
for_ifft = [[] for i in range(height)]
## Change magnitude or phase's value
"""
for i in range(height):
	for j in range(width):
		magnitude[i][j] = 1
"""
## Calculate real and image part from magnitude and phase
"""
real = magnitude*cos(phase)
image = magnitude*sin(phase)
"""
for i in range(height):
	for j in range(width):
		real_part = magnitude[i][j]*math.cos(phase[i][j])
		image_part = magnitude[i][j]*math.sin(phase[i][j])
		for_ifft[i].append(complex(real_part,image_part))

f_ishift = np.fft.ifftshift(for_ifft)
## Extract the real and imaginary part separately 
d_shift = np.array(np.dstack([f_ishift.real,f_ishift.imag]))
img_back = cv2.idft(d_shift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

## Display result on matplot
plt.subplot(121),plt.imshow(gray, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Output Image'), plt.xticks([]), plt.yticks([])
plt.show()

