"""
Senen Bagos, 
This will be our minimal outline to start off 
this code provides michael jackson songs in an extremely simple html

Connor Overbo,
Altered to make the calls to get the cat image and affirmation and load the index template so the flask app produces the output.
This verion that uses a new cat api with simple images uses API2.py, and Index.html to work.

The previous version (api that has less simple images) works as well, and would have to use API.py, index.html, 
and the "from API2..." line below needs to be changed to "API" to reference the previous file version.
"""

from flask import Flask, render_template
import requests, json
from pprint import pprint
from API2 import get_cat_image, get_affirmation

app = Flask(__name__)

@app.route('/')
def home():
    # Unused - commented out for now
    #payload = {
    #    'term': 'michael jackson',
    #    'entity': 'song',
    #    'limit': 5
    #}

    get_cat_image()
    affirmation = get_affirmation()
    
    return render_template("index.html", affirmation=affirmation)


if __name__ == '__main__':
    app.run(debug=True)
