#!/usr/bin/python3
"""contains write_file function"""


def write_file(filename="", text=""):
    """writes text to file"""
    with open(filename, 'w', encoding='utf-8') as f:
        bytes_written = f.write(text)

    return bytes_written
