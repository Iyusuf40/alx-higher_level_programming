#!/usr/bin/python3
"""find_peak: finds a peak in an unsorted list"""


def find_peak(lst):
    """finds a peak in a list"""
    if not lst:
        return
    idx = 0
    current_peak = lst[0]
    prev = current_peak
    len_ = len(lst)
    while idx < len_:
        item = lst[idx]
        if item > current_peak:
            current_peak = item
        if idx > 1:
            # if prev > item and lst[idx - 2] < prev:
            if prev > item:
                if prev > current_peak:
                    return prev
                else:
                    return current_peak
            # elif prev < item and lst[idx - 2] > prev:
                # return current_peak
        prev = item
        idx += 1
    return current_peak
