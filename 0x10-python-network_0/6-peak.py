#!/usr/bin/python3
"""find_peak: finds a peak in an unsorted list"""


def find_peak(lst):
    """finds a peak in a list"""
    if not lst:
        return
    idx = 0
    current_peak = lst[0]
    prev = current_peak
    while idx < len(lst):
        item = lst[idx]
        if item > prev:
            if item > current_peak:
                current_peak = item
            if idx > 2:
                if prev < item:
                    return current_peak
        else:
            if idx > 2:
                if prev > item:
                    return current_peak
        prev = item
        idx += 1
    return current_peak
