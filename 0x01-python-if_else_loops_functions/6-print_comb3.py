#!/usr/bin/python3
for first_n in range(0, 10):
    for sec_n in range(0, 10):
        if first_n < sec_n and first_n != sec_n:
            if first_n != 8 or sec_n != 9:
                print("{}{}, ".format(first_n, sec_n), end="")
            elif first_n == 8 and sec_n == 9:
                print("{}{}".format(first_n, sec_n))
