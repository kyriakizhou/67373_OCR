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