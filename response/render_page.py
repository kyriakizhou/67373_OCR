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
    print(f'Retrieved wikipedia summary')
    return page_summary

def load_page(text, query, path_to_photo):
    # print(path_to_photo)
    print('Creating page')
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'templates')
    env = Environment( loader = FileSystemLoader(templates_dir) )
    template = env.get_template('dynamic.html')
    
    filename = os.path.join(root, 'html', 'index.html')
    with open(filename, 'w', encoding="utf-8") as fh:
        fh.write(template.render(
            title = query,
            h1 = query.capitalize(),
            photo = f'<img src={"../."+str(path_to_photo)} alt="test">',
            body = text
        ))

    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

    webbrowser.get(chrome_path).open_new_tab(filename)
    # webbrowser.open_new_tab(filename)

def load_demo_page(text, query, path_to_photo,video_link):
    print('Creating page')
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'templates')
    env = Environment( loader = FileSystemLoader(templates_dir) )
    template = env.get_template('demo.html')
    
    filename = os.path.join(root, 'html', query+'index.html')
    with open(filename, 'w', encoding="utf-8") as fh:
        fh.write(template.render(
            title = query,
            h1 = query.capitalize(),
            photo = f'<img style="width:500px;" src={"../."+str(path_to_photo)} alt="test">',
            video = video_link,
            body = text
        ))
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

    # webbrowser.get(chrome_path).open_new_tab(filename)
    webbrowser.open_new_tab(filename)

def render(path_to_photo, query):
    wiki_content = get_wiki_info(query)
    load_page(wiki_content, query, path_to_photo)