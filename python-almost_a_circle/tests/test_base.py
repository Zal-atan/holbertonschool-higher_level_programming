#!/usr/bin/python3
# test_base.py
# Ethan Zalta
"""This is a Unittest class for testing the Base Class"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import pycodestyle
import os


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

    def test_non_integer_id_inputs(self):
        """Testing non-integer-inputs for ID"""
        # No Extra Checks
        self.assertEqual(2.5, Base(2.5).id)
        self.assertEqual("Word", Base("Word").id)
        self.assertEqual(True, Base(True).id)
        self.assertEqual(complex(10), Base(complex(10)).id)
        self.assertEqual([1, 2, 4], Base([1, 2, 4]).id)

    def test_two_inputs_base(self):
        # No Extra Checks
        with self.assertRaises(TypeError):
            Base(30, 10)

    def test_to_json_string(self):
        """Testing json string converter"""
        dic_test = {'x': 2, 'y': 8, 'id': 1, 'height': 7, 'width': 10}
        json_dic = Base.to_json_string([dic_test])
        self.assertEqual(json_dic, '[{"x": 2, "y": 8, "id": 1,'
                         ' "height": 7, "width": 10}]')

    def test_save_to_file(self):
        """Testing saving json string to file"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as file:
            read = file.read()
        correct = '[{"x": 3, "y": 4, "id": 5, "height": 2, "width": 1}]'
        self.assertEqual(read, correct)

        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            read = file.read()
        correct = '[{"x": 3, "y": 4, "id": 5, "height": 2, "width": 1},'\
                  ' {"x": 8, "y": 9, "id": 10, "height": 7, "width": 6}]'
        self.assertEqual(read, correct)

        s1 = Square(1, 2, 3, 4)
        Square.save_to_file([s1])
        with open("Square.json", "r") as file:
            read = file.read()
        correct = '[{"id": 4, "x": 2, "size": 1, "y": 3}]'
        self.assertEqual(read, correct)

        s1 = Square(1, 2, 3, 4)
        s2 = Square(6, 7, 8, 9)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            read = file.read()
        correct = '[{"id": 4, "x": 2, "size": 1, "y": 3},'\
                  ' {"id": 9, "x": 7, "size": 6, "y": 8}]'
        self.assertEqual(read, correct)

    def test_from_json_string(self):
        """Testing from json string to list"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        correct = [{'height': 4, 'width': 10, 'id': 89},
                   {'height': 7, 'width': 1, 'id': 7}]
        self.assertEqual(correct, list_output)

    def test_load_from_file(self):
        """Testing from json in file to creating instances"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        rec_list = [r1, r2]
        Rectangle.save_to_file(rec_list)
        list_rect_return = Rectangle.load_from_file()
        # self.assertEqual(str(list_rect_return), str(rec_list))
        self.assertEqual(str(list_rect_return[0]), str(r1))
        self.assertEqual(str(list_rect_return[1]), str(r2))

        s1 = Square(1, 2, 3, 4)
        s2 = Square(6, 7, 8, 9)
        sqr_list = [s1, s2]
        Square.save_to_file(sqr_list)
        list_sqr_return = Square.load_from_file()
        # self.assertEqual(str(list_sqr_return), str(sqr_list))
        self.assertEqual(str(list_sqr_return[0]), str(s1))
        self.assertEqual(str(list_sqr_return[1]), str(s2))

        """No File"""
        os.remove("Square.json")
        no_file = Square.load_from_file()
        self.assertEqual([], no_file)

        """Too many arguments"""
        with self.assertRaises(TypeError):
            Base.load_from_file("string")
