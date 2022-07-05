#!/usr/bin/python3
"""contains append_write function"""


def append_write(filename="", text=""):
    """appends text to file"""
    with open(filename, 'a', encoding='utf-8') as f:
        bytes_written = f.write(text)

    return bytes_written
