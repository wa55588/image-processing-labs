import cv2
import numpy as np

tou = cv2.imread("tou.jpg")

logo = np.zeros((200,200,3),np.uint8)
mask = np.zeros((200,200),np.uint8)

logo[20:120, 20:120] = [0,0,255]
logo[80:180, 80:180] = [0,255,0]

mask[20:120, 20:120] = 255
mask[80:180, 80:180] = 255
m = cv2.bitwise_not(mask)

roi = tou[0:200, 0:200]
tmp = cv2.bitwise_and(roi,roi,mask = m)
cv2.imshow("test1",tmp)
cv2.imshow("test2",m)
cv2.imshow("test",roi)
cv2.imshow("logo",logo)
cv2.waitKey(0)