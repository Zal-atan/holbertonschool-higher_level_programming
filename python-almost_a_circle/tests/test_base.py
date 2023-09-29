#!/usr/bin/python3
# test_base.py
# Ethan Zalta
"""This is a Unittest class for testing the Base Class"""

import unittest
from models.base import Base
import pycodestyle


class TestBase(unittest.TestCase):
    """ Unittests for Base Class"""

    def test_module_docstring(self):
        """Tests module docstring"""
        self.assertTrue(len(__import__("models").base.__doc__) > 0)

    def test_class_docstring(self):
        """Tests the class DocString"""
        self.assertTrue(len(__import__('models').base.Base.__doc__) > 0)

    def test_pycodestyle(self):
        """Tests if model/base is pycodestyle compliant"""
        style = pycodestyle.StyleGuide(quiet=True)
        checkPyC = style.check_files(["models/base.py"])
        self.assertEqual(checkPyC.total_errors, 0,
                         "Found code style errors (and warnings).")

        # Checking test file with PycodeStyle
        checkPyC = style.check_files(["tests/test_base.py"])
        self.assertEqual(checkPyC.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_no_input(self):
        """Check for no input correct output"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id - b1.id, 1)

    def test_is_instance(self):
        """Testing to make sure Instantiated correctly"""
        b2 = Base()
        self.assertIsInstance(b2, Base)

    def test_input_with_id(self):
        """Testing with input for ID"""
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_to_json_string(self):
        """Testing json string converter"""
        dic_test = {'x': 2, 'y': 8, 'id': 1, 'height': 7, 'width': 10}
        json_dic = Base.to_json_string([dic_test])
        self.assertEqual(json_dic, '[{"x": 2, "y": 8, "id": 1,'
                         ' "height": 7, "width": 10}]')
