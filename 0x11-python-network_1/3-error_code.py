#!/usr/bin/python3
"""module contains http request"""


import urllib.request
import urllib.parse
import urllib.error
import sys


def make_request():
    """makes http request with usrllib"""
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            payload = res.read()
            print(payload.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    make_request()
