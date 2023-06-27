import cv2
import numpy as np
import time

WINDOW_NAME = "Image"


def nothing(x):
    pass


def show_hsv():
    global phMin, psMin, pvMin, phMax, psMax, pvMax
    # Print if there is a change in HSV value
    if ((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax)):
        print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (
            hMin, sMin, vMin, hMax, sMax, vMax))
        phMin = hMin
        psMin = sMin
        pvMin = vMin
        phMax = hMax
        psMax = sMax
        pvMax = vMax


# Load image
image = cv2.imread("../img/fish.jpg")

# Create a window
cv2.namedWindow(WINDOW_NAME)

# Create trackbars for color change
# Hue is from 0-179 for Opencv
cv2.createTrackbar('HMin', WINDOW_NAME, 0, 179, nothing)
cv2.createTrackbar('SMin', WINDOW_NAME, 0, 255, nothing)
cv2.createTrackbar('VMin', WINDOW_NAME, 0, 255, nothing)
cv2.createTrackbar('HMax', WINDOW_NAME, 0, 179, nothing)
cv2.createTrackbar('SMax', WINDOW_NAME, 0, 255, nothing)
cv2.createTrackbar('VMax', WINDOW_NAME, 0, 255, nothing)

# Set default value for Max HSV trackbars
cv2.setTrackbarPos('HMax', WINDOW_NAME, 179)
cv2.setTrackbarPos('SMax', WINDOW_NAME, 255)
cv2.setTrackbarPos('VMax', WINDOW_NAME, 255)

cv2.setTrackbarPos('HMin', WINDOW_NAME, 11)
cv2.setTrackbarPos('SMin', WINDOW_NAME, 76)
cv2.setTrackbarPos('VMin', WINDOW_NAME, 18)
cv2.setTrackbarPos('HMax', WINDOW_NAME, 78)
cv2.setTrackbarPos('SMax', WINDOW_NAME, 255)
cv2.setTrackbarPos('VMax', WINDOW_NAME, 255)


# Initialize HSV min/max values
hMin = sMin = vMin = hMax = sMax = vMax = 0
phMin = psMin = pvMin = phMax = psMax = pvMax = 0

# Web camera no 0 is used to capture the frames
cap = cv2.VideoCapture(0)

# Store the background
_, background = cap.read()
time.sleep(2)

while (1):
    # Get current positions of all trackbars
    hMin = cv2.getTrackbarPos('HMin', WINDOW_NAME)
    sMin = cv2.getTrackbarPos('SMin', WINDOW_NAME)
    vMin = cv2.getTrackbarPos('VMin', WINDOW_NAME)
    hMax = cv2.getTrackbarPos('HMax', WINDOW_NAME)
    sMax = cv2.getTrackbarPos('SMax', WINDOW_NAME)
    vMax = cv2.getTrackbarPos('VMax', WINDOW_NAME)

    # Set minimum and maximum HSV values to display
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

    # Convert to HSV format and color threshold
    hsv = cv2.cvtColor(background, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(background, background, mask=mask)

    # Just show de HSV value
    show_hsv()

    # Display result image
    cv2.imshow(WINDOW_NAME, result)
    cv2.imshow("Mask", mask)

    # Press q to quit
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
