#!/usr/bin/python3
"""an empty class"""


class Square:
    """a square class"""
    def __init__(self, size=0):
        self.size = size

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

    def __eq__(self, other):
        """checks for equality"""
        return self.area() == other.area()

    def __lt__(self, other):
        """cecks for equality"""
        return self.area() < other.area()

    def __le__(self, other):
        """cecks for equality"""
        return self.area() <= other.area()

    def __ne__(self, other):
        """cecks for equality"""
        return self.area() != other.area()

    def __gt__(self, other):
        """cecks for equality"""
        return self.area() > other.area()

    def __ge__(self, other):
        """cecks for equality"""
        return self.area() >= other.area()


if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
