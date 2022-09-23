#!/usr/bin/python3
"""module contains http request"""


import urllib.request
import sys


def make_request():
    """makes http request with usrllib"""
    url = sys.argv[1]
    with urllib.request.urlopen(url) as res:
        info = res.info()
        print(info.get('X-Request-Id'))


if __name__ == "__main__":
    make_request()
