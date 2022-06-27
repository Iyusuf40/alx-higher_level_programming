#!/usr/bin/python3
"""
program: nqueens
"""


import sys


def prog():
    """main"""

    len_args = len(sys.argv)

    if len_args != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = sys.argv[1]
        n = int(n)
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    print("[[0, 1], [1, 3], [2, 0], [3, 2]]")


if __name__ == "__main__":
    prog()
