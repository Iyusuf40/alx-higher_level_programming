#!usr/bin/python3
"""module contains func pascal_triangle(n)"""


def pascal_triangle(n):
    """returns a nested list of pascal triangle"""
    if n <= 0:
        return []
    res = []
    i = 1
    while i <= n:
        child = []
        max_items_in_child = i
        j = 1
        while j <= max_items_in_child:
            if j == 1 or j == max_items_in_child:
                item = 1
            else:
                item = prev[j - 1] + prev[j - 2]
            child.append(item)
            j += 1
        prev = child
        res.append(child)
        i += 1
    return res
