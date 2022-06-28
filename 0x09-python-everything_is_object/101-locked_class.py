#!/usr/bin/python3
"""advanced lesson module"""


class LockedClass:
    """no attrributes"""

    def __init__(self):
        self.first_name = None

    def __setattr__(self, name, value):
        """prevents unwanted attribute"""
        if name != "first_name":
            raise AttributeError("'LockedClass' object \
has no attribute '{}'".format(name))


if __name__ == "__main__":
    lc = LockedClass()
    lc.first_name = "John"
    try:
        lc.bado_name = "Snow"
        print(lc.last_name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
