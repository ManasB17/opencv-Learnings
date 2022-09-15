import cv2

import numpy as np

img = cv2.imread("Resources/photo4.jpg")
print(img.shape)

imgResize = cv2.resize(img, (300, 500))
print(imgResize.shape)

#cropping image
imgCropped = img[200:380, 350:500]

cv2.imshow("img", img)
cv2.imshow("image resized", imgResize)
cv2.imshow("image Cropped", imgCropped)

cv2.waitKey(0)
