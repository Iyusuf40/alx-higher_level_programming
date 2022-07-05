#!/usr/bin/python3
"""module has function
inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """returns True if obj inherits class else false"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
