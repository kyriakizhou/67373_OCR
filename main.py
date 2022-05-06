from detection import detect, processDetectedText
from response import responding, preprocess
import cv2
import random
import os

# system call to push to GitHub after processing the new detection
def pushToGit():
    import os
    cmd = 'git add . \ngit commit -m "web page updated!"\ngit push'
    os.system(cmd)

# This program is robustness in misspell, letter-drop, uppercase for detecting a single word
def detectSingleWord():
    print("\n")
    print("Program starting...")
    image = cv2.imread("imageCaptured.png")
    text_detected = detect.detect(image)
    print("OCR detects as: ", text_detected)
    text_detected = processDetectedText.processDetectedText(text_detected)
    print("Program recognizes as: ", text_detected)
    responding.respond(text_detected)

# detect text grid
def detectGrid(index):
    print("\n")
    print("Program starting...\n")
    image = cv2.imread("imageCaptured.png")
    text_detected = detect.detect(image)
    print("OCR detects as:\n")
    print(text_detected, "\n")
    processDetectedText.processGrid(text_detected)
    print("Processed grid:\n")
    f = open("detection/grid.txt", "r")
    grid = f.read()
    print(grid)
    print("\n")
    word_list = list(preprocess.extract_words("detection/grid.txt"))
    print("Detected words:\n")
    print(word_list)
    print("\n")
    i = index + 1
    print("Program responding with %dth detected word..." % i, "\n")
    for word in word_list:
        responding.respond(word, False)
    print("index", index, "type(index)", type(index))
    responding.respond(word_list[index], True)
    cmd = 'open qr.png'
    os.system(cmd)
    print("Program finishing...\n\n\n\n\n\n")
    pushToGit()


import sys
index = int(sys.argv[1])
index = index-1
assert(0 <= index)
detectGrid(index)