import sys
import webbrowser

from jinja2 import Environment, FileSystemLoader
import os

def load_page(items):
    print('Creating page')
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'templates')
    env = Environment( loader = FileSystemLoader(templates_dir) )
    template = env.get_template('demo.html')
    
    fname = "index.html"
    filename = os.path.join(root, 'html', fname)
    with open(filename, 'w', encoding="utf-8") as fh:
        fh.write(template.render(items = items))
    # chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    # webbrowser.get(chrome_path).open_new_tab(filename)
    webbrowser.open_new_tab(filename)