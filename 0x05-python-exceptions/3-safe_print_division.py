#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = a / b
        print("Inside result: {}".format(res))
        return res
    except ZeroDivisionError:
        res = None
        print("Inside result: {}".format(res))
        return res
    finally:
        return res


if __name__ == "__main__":
    a = 12
    b = 2
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))

    a = 12
    b = 0
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))
