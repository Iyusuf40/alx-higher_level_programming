#!/usr/bin/python3
"""module contains http request"""


import urllib.request


url = "https://alx-intranet.hbtn.io/status"


def make_request():
    """makes http request with usrllib"""
    with urllib.request.urlopen(url) as res:
        content = res.read()
        utf8 = str(content)
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")


if __name__ == "__main__":
    make_request()
