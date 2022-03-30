#To use the code, get IPwebcam app from app store
#Start the server (button to start located at bottom)
#Copy and paste the IP address shown on phone (varies with users) and add "/shot.jpg" to the url

import cv2
import pytesseract

imgURL = "http://172.26.43.155:8080/shot.jpg"

capture = cv2.VideoCapture(imgURL)

while (True):
    _, frame = capture.read()
    cv2.imshow('MobileCam', frame)
    cv2.imwrite("textImg.jpg", capture)

    if cv2.waitKey(1) == ord("q"):
        capture.release()
        cv2.destroyAllWindows()
        break

gray = cv2.cvtColor(capture, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2000, 2000))

dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                                 cv2.CHAIN_APPROX_NONE)

im2 = capture.copy()

file = open("recognized.txt", "w+")
file.write("")
file.close()

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
     
    # Drawing a rectangle on copied image
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
     
    # Cropping the text block for giving input to OCR
    cropped = im2[y:y + h, x:x + w]
     
    # Open the file in append mode
    file = open("recognized.txt", "a")
     
    # Apply OCR on the cropped image
    text = pytesseract.image_to_string(cropped)
     
    # Appending the text into file
    file.write(text)
    file.write("\n")
     
    # Close the file
    file.close
