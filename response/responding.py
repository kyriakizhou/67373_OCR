"""
usage: 
in your file, import response
call response.respond("your word")
will display a new custom page

dependencies:
pip install beautifulsoup4
pip install Google-Images-Search
pip install Wikipedia-API
pip install Jinja2
"""

import sys
import requests
from bs4 import BeautifulSoup
from google_images_search import GoogleImagesSearch
import urllib.request
from PIL import Image
import random
import pandas as pd

from response import get_photo
from response import render_page
# import get_photo
# import render_page

demo = True

def respond(query, isIndex):
    """
    if demo is true, query should be a set of terms from preprocess.py
    query string MUST be in demo_terms.csv
    """
    if demo:
        demo_data = pd.read_csv("response/demo_terms.csv")
        path_to_photo = ""+query+".jpg"
        # NOTE: debug
        text = demo_data[demo_data["word"] == query]["description"].iloc[0]
        video_link = demo_data[demo_data["word"]==query]["video_frame"].iloc[0]
        render_page.load_demo_page(text,query,path_to_photo,video_link, isIndex)
    else:
        photo_addr = get_photo.display_photo(query)
        print(photo_addr)
        render_page.render(photo_addr, query)

#for testing purposes
if __name__ == "__main__":
    #term must be in glossary of climate change terms
    query = ' '.join(sys.argv[1:len(sys.argv)])
    if demo:
        respond(query)
    else:
        print(f'Your Query: {query}')
        photo_addr = get_photo.display_photo(query)
        print(f'Downloaded photo of {query}')
        print(photo_addr)
        render_page.render(photo_addr, query)