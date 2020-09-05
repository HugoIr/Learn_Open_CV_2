import cv2
import numpy as np

img = cv2.imread("pic/card2.jpg")

width, height = 250, 350
pts1 = np.float32([[479,137],[782,358],[128,539],[444,790]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
transformedImg = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img, transformedImg,(width,height))


cv2.imshow("image", img)
cv2.imshow("cool", imgOutput)

cv2.waitKey(0)