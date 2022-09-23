#!/usr/bin/python3
"""http request with requests module"""


import requests
import sys


def make_request():
    """makes http request"""
    user = sys.argv[1]
    passwd = sys.argv[2]
    url = f"https://api.github.com/users/{user}"
    headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {passwd}"
        }
    r = requests.get(url, headers=headers)
    try:
        js = r.json()
        print(js.get("id"))
    except Exception:
        print(None)


if __name__ == "__main__":
    make_request()
