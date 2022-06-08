#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_ = []
    if not a_dictionary or len(a_dictionary) == 0:
        return a_dictionary
    if not value:
        return a_dictionary
    for x, y in a_dictionary.items():
        if value == y:
            list_.append(x)
    if len(list_) == 0:
        return a_dictionary
    for item in list_:
        del a_dictionary[item]
    return a_dictionary
