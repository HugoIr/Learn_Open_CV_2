import cv2

img = cv2.imread('pic/lambo.jpg')
# print(img.shape)

imgResize = cv2.resize(img,(500,300))

imgCropped = img[0:500, 300:600]

cv2.imshow("lambo", img)
cv2.imshow("lambo resize", imgResize)
cv2.imshow("lambo cropped", imgCropped)
cv2.waitKey(0)
