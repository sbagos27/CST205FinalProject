"""
Senen Bagos, 
This will be our minimal outline to start off 
this code provides michael jackson songs in an extremely simple html
"""

from flask import Flask
import requests, json, random 
from pprint import pprint

app = Flask(__name__)

status_codes = [
    100, 101, 102, 200, 201, 202, 204, 206, 207,
    300, 301, 302, 303, 304, 307, 308,
    400, 401, 402, 403, 404, 405, 406, 408, 409,
    410, 411, 412, 413, 414, 415, 416, 417, 418,
    422, 425, 426, 429,
    500, 501, 502, 503, 504, 506, 507, 508, 510
]

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