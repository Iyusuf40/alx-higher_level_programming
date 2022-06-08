#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_ = []
    if not a_dictionary or not value:
        return
    for x, y in a_dictionary.items():
        if value == y:
            list_.append(y)
    if len(list_) == 0:
        return a_dictionary
    for item in list_:
        del a_dictionary[item]
    return a_dictionary
