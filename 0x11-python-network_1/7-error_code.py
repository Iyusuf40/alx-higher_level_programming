#!/usr/bin/python3
"""http request with requests module"""


import requests
import sys


def make_request():
    """makes http request"""
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code == 200:
        print(r.text)
    else:
        print("Error code:", r.status_code)


if __name__ == "__main__":
    make_request()
