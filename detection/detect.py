import cv2
import pytesseract

def androidCapture():
    image = None
    # Note: replace the http url with the one your WebCam app
    cap = cv2.VideoCapture('http://isaacahn01:Yejoon77!@172.26.66.37:8080/video')
    while(True):

        ret, frame = cap.read()
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            # When pressing Q it will close the window and take an image of what is on the phone
            # and save it to the specified folder
            cv2.imwrite('imageCaptured.png', frame)
            # It will also close the window the camera is on
            cv2.destroyAllWindows()
            print("Picture taken...\n")
            break

    cap.release()

    image = cv2.imread('imageCaptured.png')

    return image

def detect(image):
    image = androidCapture()

    # Convert the image to gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Performing OTSU threshold
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    # Specify structure shape and kernel size.
    # Kernel size increases or decreases the area of the rectangle to be detected.
    # A smaller value like (10, 10) will detect each word instead of a sentence.
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5000, 5000))

    # Applying dilation on the threshold image
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

    # Finding contours
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                                    cv2.CHAIN_APPROX_NONE)

    # Creating a copy of image
    im2 = image.copy()

    # Looping through the identified contours
    # Then rectangular part is cropped and passed on to pytesseract for extracting text from it
    # Extracted text is then written into the text file
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        
        # Drawing a rectangle on copied image
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Cropping the text block for giving input to OCR
        cropped = im2[y:y + h, x:x + w]
        
        # Apply OCR on the cropped image
        text = pytesseract.image_to_string(cropped)

        return text


