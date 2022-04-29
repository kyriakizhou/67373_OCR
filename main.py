from detection import detect, processDetectedText
from response import responding, preprocess
import cv2
import random
from webpageScript import pushToGit

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
def demo3(index):
    print("\n")
    print("Program starting...\n")
    image = cv2.imread("testImage.png")
    text_detected = detect.detect(image)
    print("OCR detects as: \n", text_detected, "\n")
    processDetectedText.processGrid(text_detected)
    print("Processed grid: \n")
    f = open("detection/grid.txt", "r")
    grid = f.read()
    print(grid, "\n")
    word_list = preprocess.extract_words("detection/grid.txt")
    print("Detected words: \n", word_list, "\n")
    print(word_list)
    print("Program responding with a detected word %d..." % index, "\n")
    # responding.respond(random.choice(list(word_list)))
    responding.respond(list(word_list)[index])
    pushToGit()


import sys
index = int(sys.argv[1])
index = index-1
assert(0 <= index)
demo3(index)
