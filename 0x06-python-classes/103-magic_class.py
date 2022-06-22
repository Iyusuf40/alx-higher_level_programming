#!/usr/bin/python3
import math
"""magic class"""


class MagicClass:
    """testing testing"""

    def __init__(self, radius=0):
        # self.radius = radius

        if type(radius) is not type(4) and type(radius) is not type(4.0):
            raise TypeError("radius must be a number")
        self.radius = radius

    def area(self):
        """area of a circle"""

        return math.pi ** 2 * self.radius

    def circumference(self):
        """return circu,ference of a circle"""

        return 2 * math.pi * self.radius
