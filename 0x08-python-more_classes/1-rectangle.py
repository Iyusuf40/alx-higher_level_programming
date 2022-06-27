#!/usr/bin/python3
"""
a rectangle class
"""


class Rectangle:
    '''an empty class'''

    def __init__(self, width=0, height=0):
        """initializes each instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """sets private attr __width"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """sets private attr __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.___height = height
