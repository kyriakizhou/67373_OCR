import sys
import requests
from bs4 import BeautifulSoup
from google_images_search import GoogleImagesSearch
import urllib.request
from PIL import Image

#key for google image api
gis = GoogleImagesSearch('AIzaSyCg1SymAm6-P-FM0dIEMpvXOvt-eNd9bH0', 'c0090d82ebd453980')

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
        print(f'image url: {image.url}')  # image direct url
        image.download('./downloaded_images')  # download image
        image.resize(500, 500)  # resize downloaded image
        #img = Image.open(image.path)
        #img.show()
        return(image.path)