#!/usr/bin/python3
"""
a rectangle class
```example```
>>> Rectangle.number_of_instances
0
>>> rec = Rectangle(2, 5)
>>> rec.width
2
>>> rec.height
5
>>> rec.area()
10
>>> rec.perimeter()
14
>>> print(rec)
##
##
##
##
##
>>> Rectangle.print_symbol = "x"
>>> print(rec)
xx
xx
xx
xx
xx
>>> Rectangle.number_of_instances
1
>>> sec_rec = Rectangle(0, 5)
>>> Rectangle.number_of_instances
2
>>> del sec_rec
Bye rectangle...
>>> Rectangle.number_of_instances
1

"""


class Rectangle:
    '''a class of rectangle'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes each instance"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        cols = self.width * type(self).print_symbol
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
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
