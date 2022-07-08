#!/usr/bin/python3
"""module contains fmction that serializes python
object __dict__ and returns it"""


def class_to_json(obj):
    """fucntion returns dict of obj"""
    return obj.__dict__
