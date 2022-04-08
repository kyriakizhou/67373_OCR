#Instructions
#1) Download IP Webcam
#2) Go to the bottom of the app and press "Start Server"
#3) At the bottom of the screen look for "IP Address"
#4) Type in "http://ip address" in browser to see what it looks like
#5) Rest of instructions in code

import cv2
import pytesseract

#This will open the link to the ip address from the app
#If there is a username and password for the link, put "username:password@ip address here/video"
cap = cv2.VideoCapture('http://isaacahn01:Yejoon77!@172.26.43.155:8080/video')
while(True):

    ret, frame = cap.read()
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        #When pressing Q it will close the window and take an image of what is on the phone
        #and save it to the specified folder
        cv2.imwrite('Desktop\Mobile OCR\img.png', frame)
        #It will also close the window the camera is on
        cv2.destroyAllWindows()
        break

cap.release()

image = cv2.imread('Desktop/Mobile OCR/img.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2000, 2000))

dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                                 cv2.CHAIN_APPROX_NONE)

im2 = image.copy()

file = open("Desktop/Mobile OCR/recognized.txt", "w+")
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