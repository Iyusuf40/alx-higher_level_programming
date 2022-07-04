#!/usr/bin/python3
"""
prints attrributes of an object
"""


def lookup(obj):
    """prints attrributes of an object"""
    res = [item for item in obj.__dict__]
    return res


if __name__ == "__main__":
    """doc"""
    class MyClass1(object):
        """simple class"""
        pass

    class MyClass2(object):
        """doc"""
        my_attr1 = 3

        def my_meth(self):
            """method"""
            pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
