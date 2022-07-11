#!/usr/bin/python3
"""module contains Square class"""


from rectangle import Rectangle


class Square(Rectangle):
    """a special rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id=id, width=size, height=size, x=x, y=y)
        self.size = size

    @property
    def size(self):
        """returns __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets __size atrr"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__size = value
        self.width = value
        self.height = value

    def to_dictionary(self):
        """returns dict rep"""
        dct = {"id": self.id, "size": self.size, "x": self.x,
               "y": self.y}
        return dct

    def update(self, *args, **kwargs):
        """implement positional arguments"""
        if len(args) != 0:
            index = 0
            for item in args:
                if index == 0:
                    self.id = item
                elif index == 1:
                    self.size = item
                elif index == 2:
                    self.x = item
                elif index == 3:
                    self.y = item
                index += 1
        else:
            for item in kwargs:
                if item == "id":
                    self.id = kwargs[item]
                elif item == "size":
                    self.size = kwargs[item]
                elif item == "x":
                    self.x = kwargs[item]
                elif item == "y":
                    self.y = kwargs[item]

    def __str__(self):
        """str rep"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
