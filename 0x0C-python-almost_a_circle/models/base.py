#!/usr/bin/python3
"""module contains Base class"""


import json
import csv


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries=None):
        """return json string of list_dictionaries"""
        lst = []
        if list_dictionaries is None:
            return json.dumps(lst)
        if type(list_dictionaries) is str:
            if len(list_dictionaries) == 0:
                return json.dumps(lst)
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string=None):
        """eturns the list of the JSON string
        representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs=None):
        """a class method that writes the JSON string
        representation of list_objs to a file"""

        if "Rectangle" in f"{cls.__dict__['__init__']}":
            file_name = "Rectangle.json"
        elif "Square" in f"{cls.__dict__['__init__']}":
            file_name = "Square.json"

        with open(file_name, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write(json.dumps([]))
            else:
                lst = [item.to_dictionary() for item in list_objs]
                f.write(cls.to_json_string(lst))

    @classmethod
    def create(cls, **dictionary):
        """a class method that returns an instance
        with all attributes already set"""

        if "Rectangle" in f"{cls.__dict__['__init__']}":
            inst = cls(10, 10)
            inst.update(**dictionary)
            return inst
        elif "Square" in f"{cls.__dict__['__init__']}":
            inst = cls(10, 10, 10, 10)
            inst.update(**dictionary)
            return inst

    @classmethod
    def load_from_file(cls):
        """returns a python list of instances"""
        if "Rectangle" in f"{cls.__dict__['__init__']}":
            file_name = "Rectangle.json"
        elif "Square" in f"{cls.__dict__['__init__']}":
            file_name = "Square.json"

        obj_list = []
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                lst = cls.from_json_string(f.read())
                obj_list += [cls.create(**objct) for objct in lst]
                return obj_list
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes to csv"""
        if "Rectangle" in f"{cls.__dict__['__init__']}":
            file_name = "Rectangle.csv"
            with open(file_name, "w", encoding="utf-8") as f:
                tpl = [list((itm.id, itm.width, itm.height,
                             itm.x, itm.y)) for itm in list_objs]
                writer = csv.writer(f)
                for item in tpl:
                    writer.writerow(item)
        elif "Square" in f"{cls.__dict__['__init__']}":
            file_name = "Square.csv"
            with open(file_name, "w", encoding="utf-8") as f:
                tpl = [list((itm.id, itm.size, itm.x,
                             itm.y)) for itm in list_objs]
                writer = csv.writer(f)
                for item in tpl:
                    writer.writerow(item)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes from csv"""
        if "Rectangle" in f"{cls.__dict__['__init__']}":
            file_name = "Rectangle.csv"
            with open(file_name, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                list_of_objs = list(reader)
                lst = []
                for item in list_of_objs:
                    item = [int(itm) for itm in item]
                    args = tuple(item)
                    # objct = cls(*args)
                    objct = cls(id=item[0], width=item[1],
                                height=item[2], x=item[3],
                                y=item[4])
                    lst.append(objct)
                return lst
        elif "Square" in f"{cls.__dict__['__init__']}":
            file_name = "Square.csv"
            with open(file_name, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                list_of_objs = list(reader)
                lst = []
                for item in list_of_objs:
                    item = [int(itm) for itm in item]
                    args = tuple(item)
                    # objct = cls(*args)
                    objct = cls(id=item[0], size=item[1],
                                x=item[2], y=item[3])
                    lst.append(objct)
                return lst
