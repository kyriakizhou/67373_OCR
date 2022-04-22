from detection import detect, processDetectedText
from response import responding, preprocess
import cv2
import random

# demo1: Sunday's detection and Charles' response are combined!
# demo2: The program is robustness in misspell, letter-drop, uppercase etc.
def demo12():
    print("\n")
    print("Program starting...")
    image = cv2.imread("testImage.png")
    text_detected = detect.detect(image)
    print("OCR detects as: ", text_detected)
    text_detected = processDetectedText.processDetectedText(text_detected)
    print("Program recognizes as: ", text_detected)
    responding.respond(text_detected)

# demo3: Charles' program could read grid omnidirectionally
def demo3():
    print("\n")
    print("Program starting...")
    image = cv2.imread("testImage.png")
    text_detected = detect.detect(image)
    print("OCR detects as: ", text_detected)
    processDetectedText.processGrid(text_detected)
    print("Processed grid: ")
    f = open("detection/grid.txt", "r")
    grid = f.read()
    print(grid)
    word_list = preprocess.extract_words("detection/grid.txt")
    print("Detected words: ", word_list)
    print(word_list)
    print("Program responding with a random detected word...")
    responding.respond(random.choice(list(word_list)))
    

# demo12()
demo3()

