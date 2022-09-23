#!/usr/bin/python3
"""http request with requests module"""


import requests
import sys


def make_request():
    """makes http request"""
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/\
commits?per_page=10"
    headers = {
            "Accept": "application/vnd.github+json",
        }
    r = requests.get(url, headers=headers)
    try:
        js = r.json()
        count = 0
        dates = []
        # for item in js:
        #     dates.append(item["commit"]["author"]["date"])
        # dates.sort()
        for item in js:
            print(item["sha"], item["commit"]["author"]["name"])
    except Exception as e:
        print(e)


if __name__ == "__main__":
    make_request()
