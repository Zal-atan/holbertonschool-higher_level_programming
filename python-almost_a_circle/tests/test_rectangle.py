#!/usr/bin/python3
# test_rectangle.py
# Ethan Zalta
"""This is a Unittest class for testing the Base Class"""

import unittest
from models.rectangle import Rectangle
import pycodestyle


class TestBase(unittest.TestCase):
    """ Unittests for Base Class"""

    def test_module_docstring(self):
        """Tests module docstring"""
        self.assertTrue(len(__import__("models").rectangle.__doc__) > 0)

    def test_class_docstring(self):
        """Tests the class DocString"""
        self.assertTrue(len(__import__('models').rectangle.Rectangle.__doc__) > 0)

    def test_pycodestyle(self):
        """Tests if model/base is pycodestyle compliant"""
        style = pycodestyle.StyleGuide(quiet=True)
        checkPyC = style.check_files(["models/rectangle.py"])
        self.assertEqual(checkPyC.total_errors, 0,
                         "Found code style errors (and warnings).")

        # Checking test file with PycodeStyle
        checkPyC = style.check_files(["tests/test_rectangle.py"])
        self.assertEqual(checkPyC.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_no_input(self):
        """Check for no input correct output"""
        r1 = Rectangle()
        r2 = Rectangle()
        self.assertEqual(r2.id - r1.id, 1)

    def test_is_instance(self):
        """Testing to make sure Instantiated correctly"""
        r2 = Rectangle()
        self.assertIsInstance(r2, Rectangle)

    def test_input_with_id(self):
        """Testing with input for ID"""
        r3 = Rectangle(12)
        self.assertEqual(r3.id, 12)

    # def test_incorrect_use(self):
