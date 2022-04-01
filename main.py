from detection import detect, processDetectedText
from response import responding
import cv2

# demo1: Sunday's detection and Charles' response are combined!
# demo2: The program is robustness in misspell, letter-drop, uppercase etc.
def demo12():
    image = cv2.imread("testImage.png")
    text_detected = detect.detect(image)
    print("OCR detects as: ", text_detected)
    text_detected = processDetectedText.processDetectedText(text_detected)
    print("Program recognizes as: ", text_detected)
    responding.respond(text_detected)

# demo3: Charles' program could read grid omnidirectionally
def demo3():
    image = cv2.imread("testImage.png")
    text_detected = detect.detect(image)
    print("OCR detects as: ", text_detected)
    processDetectedText.processGrid(text_detected)
    # AT THIS POINT THE DETECTED GRID CONTENT HAS BEEN WRITTEN INTO grid.txt
    print("Processed grid: ")
    f = open("detection/grid.txt", "r")
    grid = f.read()
    print(grid)
    # FOR CHARLES: call your grid processing program here. grid.txt has been generated, it's under detection folder. 
    


# demo12()
demo3()

