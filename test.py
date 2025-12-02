import random
import requests, os

status_codes = [100, 101, 102, 200, 201, 202, 204, 206, 207,
                300, 301, 302, 303, 304, 307, 308,
                400, 401, 402, 403, 404, 405, 406, 408, 409,
                410, 411, 412, 413, 414, 415, 416, 417, 418,
                422, 425, 426, 429,
                500, 501, 502, 503, 504, 506, 507, 508, 510]

code = random.choice(status_codes)
url = f"https://http.cat/{code}"

filename = f"cat.jpg"
filepath = os.path.join("static", filename)

response = requests.get(url)

with open(f"static/cat.jpg", "wb") as f:
    f.write(response.content)

print(f"Saved random HTTP cat: {code}.jpg")