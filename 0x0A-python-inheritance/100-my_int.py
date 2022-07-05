#!/usr/bin/python3
"""my int module"""


class MyInt(int):
    """custom int class"""

    def __eq__(self, other):
        """invert this method"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """inverts this method"""
        return not super().__ne__(other)
