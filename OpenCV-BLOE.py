import cv2
import numpy as np

img = np.zeros((200,200),np.uint8)
img2 = np.zeros((200,200),np.uint8)

img[1000:120, 100:120] = 200
img2[80:180, 80:170] = 240

#new_img = cv2.bitwise_not(img)
#new_img = cv2.bitwise_and(img,img2)
#new_img = cv2.bitwise_or(img,img2)
new_img = cv2.bitwise_xor(img,img2)
cv2.imshow("test1",new_img)
cv2.imshow("test",img)
cv2.imshow("test2",img2)
cv2.waitKey(0)