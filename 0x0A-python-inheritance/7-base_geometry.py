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
        """validates int"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
