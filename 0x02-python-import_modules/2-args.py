#!/usr/bin/python3
import sys
i = 0
list_ = sys.argv
for _ in list_:
    i += 1
if i == 1:
    print("0 arguments.")
else:
    index = 1
    print("{i} arguments:".format(i = i - 1))
    for _ in range (1, i):
        print("{}: {}".format(index, list_[index]))
        index += 1
