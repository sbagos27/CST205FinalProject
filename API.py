"""
cat api: "http.cat" 
we can use routes like "http.cat/100" and get a cat 
gotta get cat jpg

affirmation api: "www.affirmations.dev"
this literally just spits out a random affirmation that we need to pull from the json, store
as a string then print in the HTML

"""

import requests
import random as rand
import os
from flask import current_app

CAT_CODES = [
    100,101,102,200,201,202,204,206,207,
    300,301,302,303,304,307,308,
    400,401,402,403,404,405,406,408,409,
    410,411,412,413,414,415,416,417,418,
    422,425,426,429,
    500,501,502,503,504,506,507,508,510
]

def get_affirmation():
    try:
        r = requests.get("https://www.affirmations.dev")
        data = r.json()
        return data["affirmation"]
    except:
        return 'Please try again.'
    
def get_cat_image():
    code = rand.choice(CAT_CODES)
    cat_url = f"https://http.cat/{code}"

    filepath = os.path.join(current_app.root_path,'static', 'cat.jpg')
    img = requests.get(cat_url)

    with open(filepath, 'wb') as f:
        f.write(img.content)
    
    return 'cat.jpg'




#TEST
if __name__ == '__main__':
     print("Testing API functions.\n")

    
     print("Affirmation:")
     print(get_affirmation())
     print()

 
     print("Downloading cat image.")
     filename = get_cat_image()
     print(f"Image saved as: {filename}")
     print("\nDone!")
