#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    list_ = sys.argv
    for _ in list_:
        i += 1
    if i == 1:
        print("{}".format(0))
    else:
        index = 1
        j = 0
        for _ in range(1, i):
            j += int(list_[index])
            index += 1
        print("{}".format(j))
