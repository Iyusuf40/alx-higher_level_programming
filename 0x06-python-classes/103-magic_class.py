#!/usr/bin/python3
"""magic class"""
import math


class MagicClass:
    """testing testing"""

    def __init__(self, radius=0):
        # self.radius = radius

        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        self.radius = radius

    def area(self):
        """area of a circle"""

        return math.pi ** 2 * self.radius

    def circumference(self):
        """return circu,ference of a circle"""

        return 2 * math.pi * self.radius
