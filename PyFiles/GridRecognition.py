import cv2
import numpy as np

image = cv2.imread("1.jpg")
cv2.imshow("Image", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)

blur = cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("Blur", blur)

thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
cv2.imshow("Thresh", thresh)



max_area = 0
c = 0
for i in contours:
        area = cv2.contourArea(i)
        if area > 1000:
                if area > max_area:
                    max_area = area
                    best_cnt = i
                    image = cv2.drawContours(image, contours, c, (0, 255, 0), 3)
        c+=1

mask = np.zeros((gray.shape), np.uint8)
cv2.drawContours(mask, [best_cnt], 0, 255, -1)
cv2.drawContours(mask, [best_cnt], 0, 0, 2)
cv2.imshow("mask", mask)


out = np.zeros_like(gray)
out[mask == 255] = gray[mask == 255]
cv2.imshow("New image", out)