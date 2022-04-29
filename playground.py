import cv2

# FOR ISAAC: you can move ur function here :)
def androidCapture():
    image = None
    cap = cv2.VideoCapture('http://172.26.99.158:8080/video')
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

if __name__ == "__main__":
    androidCapture()