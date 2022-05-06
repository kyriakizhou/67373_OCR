packages = '''pip install opencv-python\n
brew install tesseract\n
pip install pytesseract\n
pip install Jinja2
'''

def downloadAllPackages():
    import os
    cmd = packages
    os.system(cmd)

downloadAllPackages()