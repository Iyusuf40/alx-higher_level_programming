#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list = reversed(my_list)

    for _ in my_list:
        print("{:d}".format(_))


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_reversed_list_integer(my_list)
