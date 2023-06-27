import cv2
import numpy as np

# Function to handle trackbar changes
def on_trackbar_change(value):
    # Update the image with the new intensity value
    global image, window_name
    image = cv2.imread("../img/mikey.jpeg")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    image[:, :, 2] = value
    image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    cv2.imshow(window_name, image)

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300, 512, 3), np.uint8)
img2 = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

# Create a named window
# window_name = "Custom Window"
# cv2.namedWindow(window_name)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

# Create a trackbar
initial_intensity = 128
# cv2.createTrackbar("Intensity", window_name, initial_intensity, 255, on_trackbar_change)

# create trackbars for color change
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

cv2.createTrackbar('HMin', 'image2', 0, 179, nothing)
# cv2.createTrackbar('SMin', 'image', 0, 255, nothing)
# cv2.createTrackbar('VMin', 'image', 0, 255, nothing)
# cv2.createTrackbar('HMax', 'image', 0, 179, nothing)
# cv2.createTrackbar('SMax', 'image', 0, 255, nothing)
# cv2.createTrackbar('VMax', 'image', 0, 255, nothing)
#
# cv2.setTrackbarPos('HMax', 'image', 179)
# cv2.setTrackbarPos('SMax', 'image', 255)
# cv2.setTrackbarPos('VMax', 'image', 255)

# Initialize HSV min/max values
hMin = sMin = vMin = hMax = sMax = vMax = 0
phMin = psMin = pvMin = phMax = psMax = pvMax = 0

# Load and display the image
# image = cv2.imread("../img/mikey.jpeg")
# cv2.imshow(window_name, image)

# Start the event loop
while True:
    cv2.imshow('image', img)
    cv2.imshow('image2', img2)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

        # get current positions of four trackbars
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

    hMin = cv2.getTrackbarPos('HMin', 'image2')
    # sMin = cv2.getTrackbarPos('SMin', 'image')
    # vMin = cv2.getTrackbarPos('VMin', 'image')
    # hMax = cv2.getTrackbarPos('HMax', 'image')
    # sMax = cv2.getTrackbarPos('SMax', 'image')
    # vMax = cv2.getTrackbarPos('VMax', 'image')

    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

# capture.release()
cv2.destroyAllWindows()
