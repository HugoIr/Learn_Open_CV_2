import cv2
import numpy as np

img = cv2.imread("pic/lena.jpeg")
kernel = np.ones((5,5),np.uint8)

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurImg = cv2.GaussianBlur(grayImg,(7,7),0)
cannyImg = cv2.Canny(img, 150, 200)
dialationImg = cv2.dilate(cannyImg, kernel, iterations=1)
erodedImg = cv2.erode(dialationImg, kernel, iterations=1)

# cv2.imshow("gray image", grayImg)
# cv2.imshow("blur image", blurImg)
cv2.imshow("canny image", cannyImg)
cv2.imshow("dialation image", dialationImg)
cv2.imshow("eroded image", erodedImg)

cv2.waitKey(0)
