import sys
import pandas as pd
import requests
from bs4 import BeautifulSoup
from google_images_search import GoogleImagesSearch
import urllib.request
from PIL import Image

#calling get_data will scrape terms from the glossary of climate change wiki
def get_data():
    #getting content
    response = requests.get(
	    url="https://en.wikipedia.org/wiki/Glossary_of_climate_change"
    )
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'status: {response.status_code}')

    #getting terms
    term_dict = dict()
    terms = soup.find_all('dfn')
    for term_dfn in terms:
        if (term_dfn.find('a')):
            term_dict[term_dfn.a.string] = 'https://en.wikipedia.org'+term_dfn.a['href']
        else:
            term_dict[term_dfn.string] = "n/a"
    print(term_dict)
    df = pd.DataFrame.from_dict(term_dict.items())
    print(df.head())
    df.to_csv("climate_change_terms.csv",index=False)