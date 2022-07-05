#!/usr/bin/python3
"""contains read_file function"""


def read_file(filename=""):
    """reads a file and print to sdout"""
    with open(filename, encoding='utf-8') as f:
        content = f.read()

    print(content)
