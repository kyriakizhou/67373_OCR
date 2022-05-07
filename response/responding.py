"""
usage: 

dependencies:
pip install Jinja2
"""

import sys
import pandas as pd
import render_page

def respond(query):
    """
    if demo is true, query should be a set of terms from preprocess.py
    query string MUST be in demo_terms.csv
    """
    demo_data = pd.read_csv("response/demo_terms.csv")
    # demo_data = pd.read_csv("demo_terms.csv")
    terms_list = []
    for recognized_word in query:
        item = dict(
            term = f'<h2>{recognized_word.capitalize()}</h2>',
            image = f'<img src={"../."+recognized_word+".jpg"} alt="image for word">',
            # image = f'<img src="{recognized_word+".jpg"}" alt="image for word">',
            video_link = demo_data[demo_data["word"]==recognized_word]["video_frame"].iloc[0],
            text = demo_data[demo_data["word"] == recognized_word]["description"].iloc[0]
        )
        terms_list.append(item)
    render_page.load_page(terms_list)

# #for testing purposes
# if __name__ == "__main__":
#     #term must be in glossary of climate change terms
#     # query = ' '.join(sys.argv[1:len(sys.argv)])
#     query = ["gulfstream","icecore",'iceage','carbon','argo','climate','methane','maunaloa','freon','carbondiet','adaptation','earthshine','ozonelayer','solarwind','adaptation','biomass','aerosol']
#     respond(query)