#!/usr/bin/python3
"""contains save_to_json_file funtion"""


import json


def load_from_json_file(filename):
    """saves str to a file"""
    with open(filename, "r", encoding='utf-8') as f:
        res = f.read()

    return json.loads(res)
