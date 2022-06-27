#!/usr/bin/python3
"""
module contains py function that prints a square
of a size passed as argument

```example```
>>> print_square(2)
##
##
"""


def print_square(size):
    """
    prints a square of # of size size
    """

    if not isinstance(size, int) and not isinstance(size, float):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    size = int(size)
    cols = "#" * size
    for rows in range(size):
        print(cols)

    # for row in range(size):
    #    for col in range(size):
    #        if col == size - 1:
    #            print("#")
    #        else:
    #            print("#", end="")
