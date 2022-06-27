#!/usr/bin/python3
"""
matrix mul module
```example```
>>> print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
[[7, 10], [15, 22]]
>>> print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
[[13, 16]]

"""


def matrix_mul(m_a, m_b):
    """multiplies 2 matrixes"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    def_length = None
    for item in m_a:
        if not isinstance(item, list):
            raise TypeError("m_a must be a list of lists")
        if not len(item):
            raise ValueError("m_a can't be empty")
        if def_length is None:
            def_length = len(item)
        if len(item) != def_length:
            raise TypeError("each row of m_a must be of the same size")
        for typ in item:
            if not isinstance(typ, int) and not isinstance(typ, float):
                raise TypeError("m_a should contain only integers \
or floats")

    def_length = None
    for item in m_b:
        if not isinstance(item, list):
            raise TypeError("m_b must be a list of lists")
        if not len(item):
            raise ValueError("m_b can't be empty")
        if def_length is None:
            def_length = len(item)
        if len(item) != def_length:
            raise TypeError("each row of m_b must be of the same size")
        for typ in item:
            if not isinstance(typ, int) and not isinstance(typ, float):
                raise TypeError("m_b should contain only integers \
or floats")

    if not len(m_a):
        raise ValueError("m_a can't be empty")

    if not len(m_b):
        raise ValueError("m_b can't be empty")

    height = len(m_a)
    width = len(m_b[0])
    par = []
    try:
        for i in range(height):
            child = []
            res = 0
            for j in range(width):
                res = 0
                m = 0
                while m < width:
                    res += m_a[i][m] * m_b[m][j]
                    m += 1
                child.append(res)
            par.append(child)
        return par
    except Exception:
        raise ValueError("m_a and m_b can't be multiplied")
