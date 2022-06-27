#!/usr/bin/python3
"""
```example```
    >>> x = add_integer(4, 5)
    9
"""


def add_integer(a, b=98):
    """
    function add_integer -> adds two integers together and \
    return the value
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
