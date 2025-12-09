"""
cat api: "http.cat" 
we can use routes like "http.cat/100" and get a cat 
gotta get cat jpg

affirmation api: "www.affirmations.dev"
this literally just spits out a random affirmation that we need to pull from the json, store
as a string then print in the HTML

Connor Overbo,
Altered get_cat_image so the return worked like the test and could save the file for use in index.html
this uses a different api as the other had numbers and comments.
"""

import requests
import random as rand
import os

def get_affirmation():
    try:
        r = requests.get("https://www.affirmations.dev")
        data = r.json()
        return data["affirmation"]
    except:
        return 'Please try again.'
    
def get_cat_image():
    cat_url = "https://api.thecatapi.com/v1/images/search"

    r = requests.get(cat_url)
    data = r.json()
    results = data[0]["url"]

    filepath = os.path.join('static', 'cat.jpg')
    img = requests.get(results)

    with open(filepath, 'wb') as f:
        f.write(img.content)
    
    return f"{results}"


#TEST
if __name__ == '__main__':
     print("Testing API functions.\n")
    
