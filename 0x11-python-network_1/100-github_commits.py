#!/usr/bin/python3
"""http request with requests module"""


import requests
import sys


def make_request():
    """makes http request"""
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {
            "Accept": "application/vnd.github+json",
        }
    r = requests.get(url, headers=headers)
    try:
        js = r.json()
        count = 0
        for item in js:
            print(item["sha"], item["commit"]["author"]["name"])
            count += 1
            if count == 10:
                break
    except Exception as e:
        print(e)


if __name__ == "__main__":
    make_request()
