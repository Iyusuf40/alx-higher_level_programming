#!/usr/bin/python3
"""
module containing a single function: say_my_name that prints name
>>> say_my_name("John", "Smith")
My name is John Smith

"""


def say_my_name(first_name, last_name=""):
    """
    a function that prints names
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
