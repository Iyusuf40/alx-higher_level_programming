#!/usr/bin/python3
"""module has function
is_same_class
"""


def is_kind_of_class(obj, a_class):
    """returns True if same class else false"""
    if type(obj) == a_class or isinstance(obj, a_class):
        return True
    else:
        return False
