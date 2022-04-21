import sys
import requests
from bs4 import BeautifulSoup
from google_images_search import GoogleImagesSearch
import urllib.request
from PIL import Image


_search_params = {
    'q': '',
    'num': 1,
    'fileType': '',
    'rights': '',
    'safe': '', 
    'imgType': '', 
    'imgSize': '', 
    'imgDominantColor': '',
    'imgColorType': ''
}

def display_photo(query):
    _search_params['q'] = query + ' climate'
    gis.search(search_params=_search_params)
    for image in gis.results():
        print(f'Image of {query} found at url: {image.url}')  # image direct url
        image.download('./downloaded_images')  # download image
        image.resize(500, 500)  # resize downloaded image
        #img = Image.open(image.path)
        #img.show()
        return(image.path)