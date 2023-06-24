# Python program for Detection of a
import cv2 as cv
import numpy as np
import time

def nothing(x):
    pass

# Webcamera no 0 is used to capture the frames
cap = cv.VideoCapture(0)

# Create a window
cv.namedWindow('image')

# Create trackbars for color change
# Hue is from 0-179 for Opencv
cv.createTrackbar('HMin', 'image', 0, 179, nothing)
cv.createTrackbar('SMin', 'image', 0, 255, nothing)
cv.createTrackbar('VMin', 'image', 0, 255, nothing)
cv.createTrackbar('HMax', 'image', 0, 179, nothing)
cv.createTrackbar('SMax', 'image', 0, 255, nothing)
cv.createTrackbar('VMax', 'image', 0, 255, nothing)

# Set default value for Max HSV trackbars
cv.setTrackbarPos('HMax', 'image', 179)
cv.setTrackbarPos('SMax', 'image', 255)
cv.setTrackbarPos('VMax', 'image', 255)

# Initialize HSV min/max values
hMin = sMin = vMin = hMax = sMax = vMax = 0
phMin = psMin = pvMin = phMax = psMax = pvMax = 0

# Storage a frame of a video
_, background = cap.read()
time.sleep(2)
_, background = cap.read()

while cap.isOpened:
    # Captures the live stream frame-by-frame
    _, frame = cap.read()

    # get current positions of four trackbars
    hMin = cv.getTrackbarPos('HMin', 'image')
    sMin = cv.getTrackbarPos('SMin', 'image')
    vMin = cv.getTrackbarPos('VMin', 'image')
    hMax = cv.getTrackbarPos('HMax', 'image')
    sMax = cv.getTrackbarPos('SMax', 'image')
    vMax = cv.getTrackbarPos('VMax', 'image')

    # Set minimum and maximum HSV values to display
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

    # Convert to HSV format and color threshold
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, lower, upper)
    result = cv.bitwise_and(frame, frame, mask=mask)

    # Apply the mask to take only those region from the saved background
    # where our clock is present in the current frame
    clock = cv.bitwise_and(background, background, mask=mask)

    # Print if there is a change in HSV value
    if((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
        print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
        phMin = hMin
        psMin = sMin
        pvMin = vMin
        phMax = hMax
        psMax = sMax
        pvMax = vMax
    
    # The bitwise and of the frame and mask is done so
	# that only the blue coloured objects are highlighted
	# and stored in res
    res = cv.bitwise_and(frame,frame, mask=mask)
    # cv.imshow('frame',frame)
    # cv.imshow('mask',mask)
    # cv.imshow('res',res)
    cv.imshow('clock', clock)

    # Press q to quit the window
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()