import cv2
import pytesseract

# FOR ISAAC: you can move ur function here :)
def androidCapture():
    image = None
    # cap = cv2.VideoCapture('http://isaacahn01:Yejoon77!@172.26.43.155:8080/video')
    cap = cv2.VideoCapture('http://172.26.115.145:8080/video')
    while(True):

        ret, frame = cap.read()
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            # When pressing Q it will close the window and take an image of what is on the phone
            # and save it to the specified folder
            cv2.imwrite('testImage.png', frame)
            # It will also close the window the camera is on
            cv2.destroyAllWindows()
            print("Picture taken")
            break

    cap.release()

    image = cv2.imread('testImage.png')
    print("STEP1")

    return image

def detect(image):

    # ############### FOR ISAAC: comment out starting here ############
    # # initialize the camera
    # # If you have multiple camera connected with current device, assign a value in cam_port variable according to that
    # cam_port = 0
    # cam = cv2.VideoCapture(cam_port)

    # # reading the input using the camera
    # result, image = cam.read()

    # # If image will be detected without any error, show result
    # if result:
    #     # showing result, it take frame name and image output    
    #     cv2.imshow("testImage", image)

    #     # saving image in local storage
    #     cv2.imwrite("testImage.png", image)

    #     # If keyboard interrupt occurs, destroy image window
    #     cv2.waitKey(0)
    #     cv2.destroyWindow("testImage")

    # # If captured image is corrupted, moving to else part
    # else:
    #     print("No image detected. Please try again!")

    # ############### FOR ISAAC: comment out ending here ############


    image = androidCapture()
    print("STEP2")

    # Convert the image to gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Performing OTSU threshold
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    # Specify structure shape and kernel size.
    # Kernel size increases or decreases the area of the rectangle to be detected.
    # A smaller value like (10, 10) will detect each word instead of a sentence.
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5000, 5000))
    print("STEP3")

    # Applying dilation on the threshold image
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

    # Finding contours
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                                    cv2.CHAIN_APPROX_NONE)

    # Creating a copy of image
    im2 = image.copy()

    # A text file is created and flushed
    file = open("recognized.txt", "w+")
    file.write("")
    file.close()

    # Looping through the identified contours
    # Then rectangular part is cropped and passed on to pytesseract for extracting text from it
    # Extracted text is then written into the text file
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

        return text