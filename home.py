"""
Senen Bagos, 
This will be our minimal outline to start off 
this code provides michael jackson songs in an extremely simple html
"""

from flask import Flask
import requests, json
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def home():
    endpoint = 'https://www.affirmations.dev'
    payload = {
        'term': 'michael jackson',
        'entity': 'song',
        'limit': 5
    }

    try:
        r = requests.get("https://www.affirmations.dev")
        data = r.json()
        
        print(data)
        print(data["affirmation"])
        return data["affirmation"]
    except:
        return 'Please try again.'

if __name__ == '__main__':
    app.run(debug=True)