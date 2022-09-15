import cv2
import numpy as np

img = cv2.imread("Resources/photo1.jpg")
kernel = np.ones((5, 5), np.uint8)

imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert image
imgBlur = cv2.GaussianBlur(imgGrey, (5,5), 0)
imgCanny = cv2.Canny(img, 150, 150) #edge detection in image /also known as canny edge detector
imgDialation = cv2.dilate(imgCanny, kernel, iterations= 1)
imgErode = cv2.erode(imgDialation, kernel, iterations= 1)

cv2.imshow("Gray Img", imgGrey) #displays the image
cv2.imshow("Blur Img", imgBlur)
cv2.imshow("Canny Img", imgCanny)
cv2.imshow("Dilation Img", imgDialation)
cv2.imshow("Erosion Img", imgErode)


cv2.waitKey(0)  #adds delay
