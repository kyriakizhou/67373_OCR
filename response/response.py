import sys
import requests
from bs4 import BeautifulSoup
from google_images_search import GoogleImagesSearch
import urllib.request
from PIL import Image

import get_photo
import render_page

"""
dependencies:
pip install beautifulsoup4
pip install Google-Images-Search
pip install Wikipedia-API
pip install Jinja2
"""

if __name__ == "__main__":
    #term must be in glossary of climate change terms
    query = ' '.join(sys.argv[1:len(sys.argv)])
    print(query)
    photo_addr = get_photo.display_photo(query)
    render_page.render(photo_addr, query)