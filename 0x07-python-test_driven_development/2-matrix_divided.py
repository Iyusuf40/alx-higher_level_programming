#!/usr/bin/python3
"""
matrix_divided is a function that divides a list of lists
items by a divisor and returns the new list while preserving
the initial list
```example```
>>> matrix_divided = __import__().matrix_divided
>>> matrix = [[2, 4], [6, 8]]
>>> res = matrix_divided(matrix, 2)
>>> print(res)
[[1.00, 2.00], [3.00, 4.00]]
>>> print(matrix)
[[2, 4], [6, 8]]
"""


def matrix_divided(matrix, div):
    """
    divides a 2d list items by a divisor and returns the new list
    """

    if matrix is None or not isinstance(matrix, list):
        raise TypeError("""matrix must be a matrix (list of lists) \
of integers/floats""")
    for item in matrix:
        if not isinstance(item, list):
            raise TypeError("""matrix must be a matrix \
(list of lists) of integers/floats""")

    default_length = len(matrix[0])
    for item in matrix:
        if len(item) != default_length:
            raise TypeError("""Each row of the matrix must \
have the same size""")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise TypeError("division by zero")

    parent_list = []
    for row in matrix:
        child = []
        # parent_list.append(child)
        for col in row:
            x = col / div
            x = round(x, 2)
            child.append(x)
        parent_list.append(child)

    return parent_list
