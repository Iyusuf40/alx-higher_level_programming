#!/usr/bin/python3
"""advanced task"""


def append_after(filename="", search_string="", new_string=""):
    """advanced function"""

    lst = []
    lines = []
    nums = 0
    with open(filename, "r+", encoding="utf-8") as f:
        for line in f:
            lines.append(line)
            if search_string in line:
                lst.append(nums)
            nums += 1

    idx = 0
    i = 0
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            if i < len(lst) and idx == lst[i]:
                f.write(line)
                f.write(new_string)
                i += 1
            else:
                f.write(line)
            idx += 1
