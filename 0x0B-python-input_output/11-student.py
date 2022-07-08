#!/usr/bin/python3
"""module contains Studen class"""


class Student:
    """a student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """mimics json.dumps"""
        dct = {}

        if attrs is None:
            return self.__dict__

        for item in attrs:
            if item in self.__dict__:
                dct[item] = self.__dict__[item]

        return dct

    def reload_from_json(self, json):
        """deserializes json"""
        if len(json):
            self.__dict__ = json
