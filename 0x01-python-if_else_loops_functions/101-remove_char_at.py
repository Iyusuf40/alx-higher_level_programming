#!/usr/bin/python3
def remove_char_at(str, n):
    n_str = ""
    i = 0
    for char in str:
        if i != n:
            n_str += char
        i += 1

    return n_str
