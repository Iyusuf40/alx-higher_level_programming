#!/usr/bin/python3
"""module has function
is_same_class
"""


"""returns True if same class else false"""


def is_same_class(obj, a_class):
    """returns True if same class else false"""
    if type(obj) == a_class:
        return True
    else:
        return False
