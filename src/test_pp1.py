import cv2
import numpy as np

image = cv2.imread("../img/mikey.jpeg")

cv2.imshow('', image)

# Set minimum and maximum HSV values to display
lower = np.array([20, 100, 100])
upper = np.array([30, 255, 255])

# Convert to HSV format and color threshold
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow('', result)

cv2.waitKey(0)