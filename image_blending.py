import cv2
import numpy as np
back = cv2.imread("test1.jpg")
small = cv2.imread("test2.jpg")

print(back.shape)
print(small.shape)
small_resized = cv2.resize(small, (back.shape[1], back.shape[0]))


result = cv2.addWeighted(small,0.7,back,0.3,0)
cv2.imshow("jianfa.py",result)
cv2.waitKey(0)