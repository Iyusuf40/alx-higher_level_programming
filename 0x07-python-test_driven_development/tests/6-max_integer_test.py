#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    the test fixture
    """

    def test_empty_list(self):
        """
        test for an empty list
        expected result == None
        """

        res = max_integer([])
        self.assertEqual(res, None)

    def test_7_as_max_int(self):
        """
        typical case
        expect 7 as result
        """

        res = max_integer([2, 5, 7, 0])
        self.assertEqual(res, 7)

    def test_several_max_int_in_list(self):
        """
        case with multiple max int
        """

        res = max_integer([20, 10, 7, 0, 20, 10])
        self.assertEqual(res, 20)

    def test_None_in_place_of_list(self):
        """
        expect TypeError error
        """

        with self.assertRaises(TypeError):
            res = max_integer(None)

    def test_list_with_1_member(self):
        """
        expect the member
        """

        res = max_integer([0])
        self.assertEqual(res, 0)

    def test_list_with_1_member_non_int_type(self):
        """
        expect the member
        """

        res = max_integer(["string"])
        self.assertEqual(res, "string")

    def test_list_with_members_of_diff_types(self):
        """
        expect error
        """
        with self.assertRaises(TypeError):
            res = max_integer([2, ["list"], 7, "sting"])



if __name__ == "__main__":
    unittest.main()
