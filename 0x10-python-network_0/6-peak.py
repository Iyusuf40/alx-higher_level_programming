#!/usr/bin/python3
"""find_peak: finds a peak in an unsorted list"""


def find_peak(lst):
    """finds a peak in a list"""
    if not lst:
        return
    state = []  # records trend and waits for change
    current_peak = lst[0]
    prev = current_peak
    for item in lst[1:]:
        if item > prev:
            if item > current_peak:
                current_peak = item
            # state.append(1)
            if len(state) > 2:
                if prev < item:
                    return current_peak
            state.append(1)
        else:
            # state.append(0)
            if len(state) > 2:
                if prev > item:
                    return current_peak
            state.append(0)
        prev = item
    return current_peak
