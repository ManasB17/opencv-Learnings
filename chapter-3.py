import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# print(img.shape)
# img[:] = 255, 125, 212 crates background for us

# Drawing line
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.rectangle(img, (0, 0), (250, 350), (255, 0, 255), 2)
cv2.circle(img, (400, 50), 30, (0, 255, 255), 5)

# put text on images
cv2.putText(img, "hey this is text", (250, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 1)

cv2.imshow('img', img)

cv2.waitKey(0)
