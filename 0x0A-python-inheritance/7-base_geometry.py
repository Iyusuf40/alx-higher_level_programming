#!/usr/bin/python3
"""a base class of BaseGeometry"""


class BaseGeometry:
    """base class"""

    def __init__(self):
        pass

    def area(self):
        """not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
        check if int type
        """
        if not isinstance(value, int) or type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
