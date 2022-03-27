#To use the code, get IPwebcam app from app store
#Start the server (button to start located at bottom)
#Copy and paste the IP address shown on phone (varies with users) and add "/shot.jpg" to the url

import cv2

imgURL = "http://172.26.43.155:8080/shot.jpg"

capture = cv2.VideoCapture(imgURL)

while (True):
    _, frame = capture.read()
    cv2.imshow('MobileCam', frame)

    if cv2.waitKey(1) == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()
