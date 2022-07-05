#!/usr/bin/python3
"""module demonstrates python
inherittance
"""


class MyList(list):
    """MyList inherits from bultin list
    """

    def __init__(self):
        pass

    def print_sorted(self):
        """prints list in sorted manner"""
        list_ = sorted(self)
        print(list_)
