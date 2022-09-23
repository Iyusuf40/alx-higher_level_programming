#!/usr/bin/python3
"""http request with requests module"""


import requests


def make_request():
    """makes http request"""
    url = "https://alx-intranet.hbtn.io/status"
    r = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.text}")


if __name__ == "__main__":
    make_request()
