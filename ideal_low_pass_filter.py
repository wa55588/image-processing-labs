import matplotlib.pyplot as plt
import numpy as np
import cv2
o = cv2.imread('tou.jpg',0)
dft = cv2.dft(np.float32(o),flags = cv2.DFT_COMPLEX_OUTPUT)
dshift = np.fft.fftshift(dft)
rs,cs = o.shape
cr,cc = int(rs/2),int(cs/2)
mask = np.zeros((rs,cs,2),np.uint8)
mask[cr-30:cr+30,cc-30:cc+30]=1
md = dshift*mask
imd = np.fft.fftshift(md)
io = cv2.idft(imd)
io = cv2.magnitude(io[:,:,0],io[:,:,1])
plt.subplot(121),plt.imshow(o,cmap='gray')
plt.axis('off')
plt.title('Original')
plt.subplot(122),plt.imshow(io,cmap='gray')
plt.axis('off')
plt.title('result')
plt.show()