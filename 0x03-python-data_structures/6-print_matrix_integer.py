#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for _ in matrix:
        lent = len(_) - 1
        i = 0
        for item in _:
            print("{:d}".format(item), end="")
            if i != lent:
                print(" ", end="")
            i += 1
        print()


# if __name__ == "__main__":
#    matrix = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#    ]
#
#    print_matrix_integer(matrix)
#    print("--")
#   print_matrix_integer()
