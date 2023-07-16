import cv2
import numpy as np
import time

WINDOW_NAME = "Image"


def nothing(x):
    pass


def show_hsv():
    global phMin, psMin, pvMin, phMax, psMax, pvMax
    # Print if there is a change in HSV value
    if (phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax):
        print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (
            hMin, sMin, vMin, hMax, sMax, vMax))
        phMin = hMin
        psMin = sMin
        pvMin = vMin
        phMax = hMax
        psMax = sMax
        pvMax = vMax


def get_trackbar_values():
    global hMin, sMin, vMin, hMax, sMax, vMax
    hMin = cv2.getTrackbarPos('HMin', WINDOW_NAME)
    sMin = cv2.getTrackbarPos('SMin', WINDOW_NAME)
    vMin = cv2.getTrackbarPos('VMin', WINDOW_NAME)
    hMax = cv2.getTrackbarPos('HMax', WINDOW_NAME)
    sMax = cv2.getTrackbarPos('SMax', WINDOW_NAME)
    vMax = cv2.getTrackbarPos('VMax', WINDOW_NAME)


def init_setup():
    global hMin, sMin, vMin, hMax, sMax, vMax, phMin, psMin, pvMin, phMax, psMax, pvMax

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
    cv2.setTrackbarPos('HMin', WINDOW_NAME, 90)
    cv2.setTrackbarPos('SMin', WINDOW_NAME, 50)
    cv2.setTrackbarPos('VMin', WINDOW_NAME, 70)
    cv2.setTrackbarPos('HMax', WINDOW_NAME, 128)
    cv2.setTrackbarPos('SMax', WINDOW_NAME, 255)
    cv2.setTrackbarPos('VMax', WINDOW_NAME, 255)
    # Initialize HSV min/max values
    hMin = sMin = vMin = hMax = sMax = vMax = 0
    phMin = psMin = pvMin = phMax = psMax = pvMax = 0


init_setup()

# Web camera no 0 is used to capture the frames
cap = cv2.VideoCapture(0)

# Store the background
_, background = cap.read()
time.sleep(2)

while cap.isOpened():
    # Get the frame in realtime
    _, frame = cap.read()

    # Get current positions of all trackbars
    get_trackbar_values()

    # Set minimum and maximum HSV values to display
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

    # Convert to HSV format and color threshold
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Apply the mask in image
    mask_color = cv2.inRange(hsv, lower, upper)
    cv2.imshow("Mask color", mask_color)

    # Using Morphological Transformations to remove noise from the cloth and unnecessary Details.
    mask1 = cv2.morphologyEx(mask_color, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask1 = cv2.morphologyEx(mask_color, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)
    mask2 = cv2.bitwise_not(mask1)

    # Combining the masks and showing them in one frame
    # The basic work of bitwise_and is to combine these background and store it in background_with_mask
    background_with_mask = cv2.bitwise_and(background, background, mask=mask1)
    frame_with_mask = cv2.bitwise_and(frame, frame, mask=mask2)

    # Blend background and frame with applied masks
    # Calculates the weighted sum of two arrays
    final_output = cv2.addWeighted(src1=background_with_mask, alpha=1, src2=frame_with_mask, beta=1, gamma=0)

    # Show result
    cv2.imshow(WINDOW_NAME, final_output)

    # Just show de HSV value
    show_hsv()

    # Press q to quit
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
