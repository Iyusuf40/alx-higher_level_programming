#!/usr/bin/python3
"""find_peak: finds a peak in an unsorted list"""


def find_peak(lst):
    """finds a peak in a list"""
    if not lst:
        return
    low = 0
    current_low = lst[0]
    prev_low = current_low
    high = len(lst) - 1
    prev_high = lst[high]
    current_high = prev_high
    while True:
        if high == low:
            return current_high
        high -= 1
        low += 1
        if lst[high] < current_high:
            return current_high
        elif lst[low] < current_low:
            return current_low
