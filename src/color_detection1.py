import cv2
import numpy as np


captura = cv2.VideoCapture(0)

while (1):

    _, imagen = captura.read()
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

    lower_green = np.array([49, 50, 50])
    upper_green = np.array([107, 255, 255])


    lower_red1 = np.array([0, 65, 75], dtype=np.uint8)
    upper_red1 = np.array([12, 255, 255], dtype=np.uint8)
    lower_red2 = np.array([240, 65, 75], dtype=np.uint8)
    upper_red2 = np.array([256, 255, 255], dtype=np.uint8)

    lower_yellow = np.array([16, 76, 72], dtype=np.uint8)
    upper_yellow = np.array([30, 255, 210], dtype=np.uint8)

    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)

    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

    kernel = np.ones((6, 6), np.uint8)

    mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_CLOSE, kernel)
    mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_OPEN, kernel)

    mask_yellow = cv2.morphologyEx(mask_yellow, cv2.MORPH_CLOSE, kernel)
    mask_yellow = cv2.morphologyEx(mask_yellow, cv2.MORPH_OPEN, kernel)

    mask_red1 = cv2.morphologyEx(mask_red1, cv2.MORPH_OPEN, kernel)
    mask_red1 = cv2.morphologyEx(mask_red1, cv2.MORPH_OPEN, kernel)

    mask_red2 = cv2.morphologyEx(mask_red2, cv2.MORPH_OPEN, kernel)
    mask_red2 = cv2.morphologyEx(mask_red2, cv2.MORPH_OPEN, kernel)


    mask1 = cv2.add(mask_red1, mask_red2)
    mask2 = cv2.add(mask_green,mask_yellow)


    cv2.imshow('red', mask1)
    cv2.imshow('green', mask2)
    cv2.imshow('Camara', imagen)

    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break

cv2.destroyAllWindows()