import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
# img[200:300,400:500] = 255,0,0

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),40)
cv2.rectangle(img,(0,0),(250,250),(0,0,255),3)
cv2.circle(img, (400,50),100,(255,255,0),1)
cv2.putText(img,"OPEN CV", (200,200),cv2.FONT_HERSHEY_PLAIN,3,(0,150,0),2)

cv2.imshow("img",img)

cv2.waitKey(0)