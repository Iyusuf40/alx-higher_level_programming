#!/usr/bin/python3
"""module contains class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """returns the area of the rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints # rep of the rectangle"""
        wideness = "#" * self.width
        x_axis_offset = " " * self.x
        y_axis_offset = "\n" * self.y
        print(y_axis_offset, end="")
        wideness = x_axis_offset + wideness
        for item in range(self.height):
            print(wideness)

    def update(self, *args, **kwargs):
        """implement positional arguments"""
        if len(args) != 0:
            index = 0
            for item in args:
                if index == 0:
                    self.id = item
                elif index == 1:
                    self.width = item
                elif index == 2:
                    self.height = item
                elif index == 3:
                    self.x = item
                elif index == 4:
                    self.y = item
                index += 1
        else:
            for item in kwargs:
                if item == "id":
                    self.id = kwargs[item]
                elif item == "height":
                    self.height = kwargs[item]
                elif item == "width":
                    self.width = kwargs[item]
                elif item == "x":
                    self.x = kwargs[item]
                elif item == "y":
                    self.y = kwargs[item]

    def to_dictionary(self):
        """returns __dict__ attr"""
        dct = {"id": self.id, "width": self.width,
               "height": self.height, "x": self.x, "y": self.y}
        return dct

    @property
    def x(self):
        """returns private inst attr __x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets private inst attr __x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns private inst attr __y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets private inst attr __y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def width(self):
        """returns private inst attr __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets private inst attr __width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns private inst attr __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets private inst attr __height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    def __str__(self):
        """return str rep of rectangle"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} \
- {self.width}/{self.height}"
