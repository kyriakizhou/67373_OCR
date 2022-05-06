To run the program:
1. At root directory, run
% python libraryDownload.py
2. Head to detection/detect.py, replace the http url with the one in your Web Cam App on your phone
3. At root directory, run 
% python main.py [index of the word, e.g. 1]


Here we want to explain more about the structure of this repository:

Two folders:
1. detection:
- detect.py includes the main functionalities for capturing the image through your phone, 
processing the image, detecting, and recognizing any text.
- processDetectedText.py includes all processing (striping empty spaces, unify lower/upper cases etc.) 
for the detected text returned by Tesseract engine.
- grid.txt is the output write file for function processGrid in file processDetectedText.py 
- wordDictionary.txt contains a list of standard words which the program uses to correct noisy
text detection from images. This file is extensible, simply adding new standard words into 
this file allows the program to auto correct deformed versions of the standard words.

2. response:


Four root files:
1. main.py: the main file for running the program. Everytime to run the program, cd in the root folder,
run % python main.py [index of the word, e.g. 1]
2. qr.png: the QR code for displaying the generated public web page content.
3. imageCaptured.png: the image captured by Web Cam from your mobile phone.
4. libraryDownloaded: the script to download all required packages before running the progrm. 
