#!/usr/bin/python3
i = 122
for _ in range(97, 123):
    if i % 2 == 0:
        print("{}".format(chr(i)), end="")
    else:
        j = i - 32
        print("{}".format(chr(j)), end="")
    i -= 1
