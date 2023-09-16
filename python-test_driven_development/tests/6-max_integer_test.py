#!/usr/bin/python3
# 6-max_integer_test.py
# Ethan Zalta
"""This is a Unittest class for testing file 6-max_integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer
import pycodestyle


class TestMaxInteger(unittest.TestCase):
    """ Unittests for max_integer function"""

    def test_correct_use(self):
        # Testing with positive integers
        self.assertEqual(max_integer([3, 4, 5, 6]), 6)
        # Testing for negative integers
        self.assertEqual(max_integer([-5, -24, -98]), -5)
        #Testing single integer
        self.assertEqual(max_integer([4]), 4)
        #Testing float
        self.assertEqual(max_integer([5.8, 9.6, 18.1]), 18.1)
        #Testing float and int
        self.assertEqual(max_integer([25, 9.6, 18.1]), 25)
        #Testing string
        self.assertEqual(max_integer("hello world"), "w")
