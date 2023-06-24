import cv2

# image = cv2.imread("../img/mikey.jpeg")
# cv2.imshow("origin", image)
# cv2.waitKey(0)

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    if ret == True:
        # Display the resulting frame
        # cv2.imshow('Frame', frame)
        frameCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("video", frame)
        cv2.imshow("video2", frameCinza)
          
        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
  
    # Break the loop
    else:
        break

# When everything done, release
# the video capture object
capture.release()

# Closes all the frames
cv2.destroyAllWindows()