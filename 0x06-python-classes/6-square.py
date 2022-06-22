#!/usr/bin/python3
"""an empty class"""


class Square:
    """a square class"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def position(self):
        """returns self.position, serves as a getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets position attribute"""
        if not isinstance(value, tuple) or len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints a square"""
        if self.__size == 0:
            print()
        else:
            col = 0
            for row in range(self.size):
                if col:
                    print()
                for space in range(self.position[0]):
                    print(" ", end="")
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
    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 4, 4))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")
