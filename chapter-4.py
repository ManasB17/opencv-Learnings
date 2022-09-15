import cv2
import numpy as np

img = cv2.imread("Resources/photo5.jpg")

width, height = 460, 460
pts1 = np.float32([[123, 213], [262, 224], [250, 420], [97, 407]])
pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix,(width, height))




# cv2.imshow("Image", img)
cv2.imshow("output", imgOutput)

cv2.waitKey(0)
