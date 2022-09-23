#!/usr/bin/python3
"""http request with requests module"""


import requests
import sys


def make_request():
    """makes http request"""
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    r = requests.post(url, data=data)
    print(r.text)


if __name__ == "__main__":
    make_request()
