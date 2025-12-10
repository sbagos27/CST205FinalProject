"""
Senen Bagos, 
This will be our minimal outline to start off 
this code provides michael jackson songs in an extremely simple html
"""

from flask import Flask, render_template
import requests, json
from pprint import pprint
from API import get_affirmation, get_cat_image

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/affirmation')
def affirmation_page():
    affirmation_txt = get_affirmation()
    cat_pic = get_cat_image()

    return render_template("index.html", affirmation=affirmation_txt, cat_image = cat_pic)



if __name__ == '__main__':
    app.run(debug=True)