from detection import detect
from response import responding
import cv2

def main():
    image = cv2.imread("testImage.png")
    text_detected = detect.detect(image)
    responding.respond(text_detected)


main()