#!/usr/bin/python3
"""module contains http request"""


import urllib.request
import urllib.parse
import sys


def make_request():
    """makes http request with usrllib"""
    url = sys.argv[1]
    email = sys.argv[2]
    dct = {"email": email}
    data = urllib.parse.urlencode(dct)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        payload = res.read()
        print(payload.decode('utf-8'))


if __name__ == "__main__":
    make_request()
