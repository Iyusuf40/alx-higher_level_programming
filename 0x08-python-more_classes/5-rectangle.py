#!/usr/bin/python3
"""
a rectangle class
```example```
>>> rec = Rectangle(2, 5)
>>> rec.width
2
>>> rec.height
5
>>> rec.area()
10
>>> rec.perimeter()
14
>>> rec = Rectangle()
Bye rectangle...
>>> rec.width
0
>>> rec.height
0
>>> rec.area()
0
>>> rec.perimeter()
0
>>> print(rec)
<BLANKLINE>
>>> rec = Rectangle(2, 5)
Bye rectangle...
>>> print(rec)
##
##
##
##
##
>>> repr(rec)
'Rectangle(2, 5)'
>>> del rec
Bye rectangle...
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
    def height(self, height):
        """height setter"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """area = width * height"""
        return self.width * self.height

    def perimeter(self):
        """perimeter = width + height"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """string rep"""
        if self.width == 0 or self.height == 0:
            return ""
        cols = self.width * "#"
        _str = ""
        for _ in range(self.height):
            _str += cols
            if _ != self.height - 1:
                _str += "\n"

        return _str

    def __repr__(self):
        """object representation"""
        return "Rectangle({}, {})".format(self.width,
                                          self.height)

    def __del__(self):
        """destructor"""
        print("Bye rectangle...")
