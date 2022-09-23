#!/usr/bin/python3
"""http request with requests module"""


import requests
import sys


def make_request():
    """makes http request"""
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    data = {"q": q}
    r = requests.post(url, data=data)
    try:
        js = r.json()
        if "id" in js:
            print(f'[{js.get("id")}]', f'{js.get("name")}')
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")


if __name__ == "__main__":
    make_request()
