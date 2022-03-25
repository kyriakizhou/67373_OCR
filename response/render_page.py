import sys
import requests
from bs4 import BeautifulSoup
from google_images_search import GoogleImagesSearch
import urllib.request
from PIL import Image
import wikipediaapi

import webbrowser

from jinja2 import Environment, FileSystemLoader
import os

def get_wiki_info(query):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(query)
    page_summary = page_py.summary
    return page_summary.encode('utf-8')

def load_page(text, query, path_to_photo):
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'templates')
    env = Environment( loader = FileSystemLoader(templates_dir) )
    template = env.get_template('dynamic.html')
    
    filename = os.path.join(root, 'html', 'index.html')
    with open(filename, 'w') as fh:
        fh.write(template.render(
            title = query,
            h1 = query,
            photo = f'<img src=.{path_to_photo} alt="test">',
            body = text
        ))
    webbrowser.open_new_tab(filename)

def render(path_to_photo, query):
    wiki_content = get_wiki_info(query)
    load_page(wiki_content, query, path_to_photo)