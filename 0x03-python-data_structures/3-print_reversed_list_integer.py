#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    my_list = reversed(my_list)
    for _ in my_list:
        print("{:d}".format(_))


if __name__ == "__main__":
    my_list = []
    print_reversed_list_integer(my_list)
