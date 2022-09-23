#!/usr/bin/python3
"""http request with requests module"""


import requests
import sys


def make_request():
    """makes http request"""
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))


if __name__ == "__main__":
    make_request()
