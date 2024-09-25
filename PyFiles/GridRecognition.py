import cv2
import numpy as np

image = cv2.imread("1.jpg")
cv2.imshow("Image", image)

blur = cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("Blur", blur)

thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
cv2.imshow("Thresh", thresh)

