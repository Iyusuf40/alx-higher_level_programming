#!/usr/bin/python3
"""contains save_to_json_file funtion"""


import json


def save_to_json_file(my_obj, filename):
    """saves str to a file"""
    serialized = json.dumps(my_obj)
    with open(filename, "w", encoding='utf-8') as f:
        res = f.write(serialized)

    return res
