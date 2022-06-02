#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    list_ = sys.argv
    for _ in list_:
        i += 1
    if i == 1:
        print("{} arguments.".format(i - 1))
    else:
        index = 1
        print("{i} arguments:".format(i=i - 1))
        for _ in range(1, i):
            print("{}: {}".format(index, list_[index]))
            index += 1
