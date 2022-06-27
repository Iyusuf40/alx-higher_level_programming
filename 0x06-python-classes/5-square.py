#!/usr/bin/python3
"""an empty class"""


class Square:
    """a square class"""
    def __init__(self, size=0):
        self.size = size

    def my_print(self):
        """prints a square"""
        if self.__size == 0:
            print()
        else:
            col = 0
            for row in range(self.size):
                if col:
                    print()
                for col in range(self.__size):
                    print("#", end="")
            print()

    def area(self):
        """area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """returns self.__size"""
        return self.__size

    @size.setter
    def size(self, size):
        """sets a size private attr"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
