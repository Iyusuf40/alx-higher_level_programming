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
        if not isinstance(x, int) or not isinstance(y, int) or y < 0 or x < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints a square"""
        if self.__size == 0:
            print()
        else:
            col = 0
            for height in range(self.position[1]):
                print()
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

    def __str__(self):
        """prints it self"""
        res = ""
        col = 0
        if not self.size:
            return ""
        for height in range(self.position[1]):
            res += "\n"
        for row in range(self.size):
            if col:
                res += "\n"
            for space in range(self.position[0]):
                res += " "
            for col in range(self.__size):
                res += "#"

        return res


if __name__ == "__main__":
    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)

    print("--")

    my_square = Square(0, (10, 10))
    print(my_square)
