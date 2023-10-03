#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_unord_list(self):
        """Test an unordered list of integers."""
        unord = [1, 4, 2, 3]
        self.assertEqual(max_integer(unord), 4)

    def test_ord_list(self):
        """Test an ordered list of integers."""
        ord_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(ord_list), 4)

    def test_max_at_start(self):
        """Test a list with a start max value."""
        max_at_start = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_start), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_ints_mixed_list(self):
        """Test a list of ints and floats."""
        mixed_list = [1.53, 15.5, -9, 15, 7]
        self.assertEqual(max_integer(mixed_list), 15.5)

    def test_str(self):
        """Testing a string."""
        str = "walter"
        self.assertEqual(max_integer(str), 'w')

    def test_one_ele_list(self):
        """Test a list with a single element."""
        one_ele = [7]
        self.assertEqual(max_integer(one_ele), 7)

    def test_floats(self):
        """Test a list of floats."""
        float_list = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(float_list), 15.2)

    def test_empty_str(self):
        """Test an empty str."""
        self.assertEqual(max_integer(""), None)

    def test_list_strings(self):
        """Test a list of strs."""
        strs = ["Walter", "is", "my", "name"]
        self.assertEqual(max_integer(strs), "name")

if __name__ == '__main__':
    unittest.main()
