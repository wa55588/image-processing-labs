import cv2
import numpy as np
import matplotlib.pyplot as plt
o = cv2.imread('tou.jpg',0)
f = np.fft.fft2(o)
fshift = np.fft.fftshift(f)
rows,cols = o.shape
crow,ccol = int(rows/2),int(cols/2)
fshift[crow-30:ccol+30,ccol-30:ccol+30] = 0
ishift = np.fft.ifftshift(fshift)
io = np.fft.ifft2(ishift)
io = np.abs(io)
plt.subplot(121)
plt.imshow(o,cmap='gray')
plt.axis('off')
plt.title('Original')
plt.subplot(122)
plt.imshow(io,cmap='gray')
plt.axis('off')
plt.title('Shifted')
plt.show()