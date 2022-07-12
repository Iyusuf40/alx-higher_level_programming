#!/usr/bin/python3
"""unittest module"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Base(unittest.TestCase):
    """test base class"""

    @classmethod
    def setUpClass(cls):
        """setup class"""
        print("class set-UP")

    @classmethod
    def tearDownClass(cls):
        """class teardown"""
        print("class tear-down")

    def test_id_is_None(self):
        """test id is None"""
        id_None_instance = Base()
        self.assertEqual(id_None_instance.id, 1)

    def test_id_is_None_sec_time(self):
        """test id is None"""
        id_None_sec_time = Base()
        self.assertEqual(id_None_sec_time.id, 2)

    def test_id_is_1(self):
        """test id is 1"""
        id_is_1 = Base(id=1)
        self.assertEqual(id_is_1.id, 1)


class Test_Rectangle(unittest.TestCase):
    """test Rectanglre class"""

    @classmethod
    def setUpClass(cls):
        """setup class"""

    @classmethod
    def tearDownClass(cls):
        """class teardown"""
        print("class tear-down")

    def setUp(self):
        """sets up each test"""

    def test_set_all_priv_attr_id_is_None(self):
        """test set __x attr"""
        rectangle = Rectangle(width=5, height=2, x=3, y=4, id=7)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)
        self.assertEqual(rectangle.id, 7)

    def test_raise_attr_error(self):
        """test for accessing private attr"""
        with self.assertRaises(AttributeError):
            rectangle = Rectangle(width=5, height=2, x=3, y=4)
            x = rectangle.__height

        with self.assertRaises(AttributeError):
            y = rectangle.__y

    def test_x_validator(self):
        """tests for nonsensical x value input
           raises typeError and valueerror
        """
        with self.assertRaises(TypeError):
            rectangle = Rectangle(width=5, height=2, x=3.0, y=4)

        with self.assertRaises(ValueError):
            rectangle = Rectangle(width=5, height=2, x=-2, y=4)

    def test_y_validator(self):
        """tests for nonsensical y value input
           raises typeError and valueerror
        """
        with self.assertRaises(TypeError):
            rectangle = Rectangle(width=5, height=2, x=3, y="")

        with self.assertRaises(ValueError):
            rectangle = Rectangle(width=5, height=2, x=0, y=-343)

    def test_width_validator(self):
        """tests for nonsensical width value input
           raises typeError
        """
        with self.assertRaises(TypeError):
            rectangle = Rectangle(width=[], height=2, x=3, y=4)

        with self.assertRaises(ValueError):
            rectangle = Rectangle(width=0, height=2, x=2, y=4)

    def test_height_validator(self):
        """tests for nonsensical height value input
           raises typeError
        """
        with self.assertRaises(TypeError):
            rectangle = Rectangle(width=5, height={1: "dct"}, x=3, y=4)

        with self.assertRaises(ValueError):
            rectangle = Rectangle(width=5, height=-1, x=2, y=4)

    def test_area_of_rectangle(self):
        """test cases for area"""
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(6, r1.area())
        self.assertEqual(56, r3.area())

    def test_str_method(self):
        """tests for str method return value"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_method(self):
        r1 = Rectangle(id=1, width=10, height=10, x=10, y=10)
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")



if __name__ == "__main__":
    unittest.main()
