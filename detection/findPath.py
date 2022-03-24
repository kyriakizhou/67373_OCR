import os


for r,s,f in os.walk("/"):
    for i in f:
        if "tesseract" in i:
            print(os.path.join(r,i))

print("Done")