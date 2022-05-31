#!/usr/bin/python3
for _ in range(0, 100):
    if _ != 99:
        print("{:0>2d}, ".format(_), end="")
    else:
        print("{:0>2d}".format(_))
