#!/usr/bin/python3
"""adds argv to a list and save to
add_item.json
"""


from sys import argv
save_to_json_file = __import__("5-save_to_json_file").\
    save_to_json_file

load_from_json_file = __import__("6-load_from_json_file").\
    load_from_json_file

index = 1
try:
    lst = list(argv[1:]) + load_from_json_file("add_item.json")
except Exception:
    lst = list(argv[1:])

save_to_json_file(lst, "add_item.json")
