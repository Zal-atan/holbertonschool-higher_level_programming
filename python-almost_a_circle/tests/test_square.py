#!/usr/bin/python3
# test_square.py
# Ethan Zalta
"""This is a Unittest class for testing the Square Class"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import pycodestyle


class TestBase(unittest.TestCase):
    """ Unittests for Square Class"""

    def test_module_docstring(self):
        """Tests module docstring"""
        self.assertTrue(len(__import__("models").square.__doc__) > 0)

    def test_class_docstring(self):
        """Tests the class DocString"""
        self.assertTrue(len(__import__('models')
                        .square.Square.__doc__) > 0)

    def test_pycodestyle(self):
        """Tests if model/base is pycodestyle compliant"""
        style = pycodestyle.StyleGuide(quiet=True)
        checkPyC = style.check_files(["models/square.py"])
        self.assertEqual(checkPyC.total_errors, 0,
                         "Found code style errors (and warnings).")

        # Checking test file with PycodeStyle
        checkPyC = style.check_files(["tests/test_square.py"])
        self.assertEqual(checkPyC.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_is_instance(self):
        """Testing to make sure Instantiated correctly"""
        s2 = Square(5, 4)
        self.assertIsInstance(s2, Square)

    def test_square_is_base(self):
        s2 = Square(3, 4)
        self.assertIsInstance(s2, Base)

    def test_no_input_id(self):
        """Check for no input correct output"""
        s1 = Square(5, 4)
        s2 = Square(3, 2)
        self.assertEqual(s2.id - s1.id, 1)

    def test_input_with_id(self):
        """Testing with input for ID"""
        s3 = Square(5, 0, 0, 12)
        self.assertEqual(s3.id, 12)

    def test_correct_width_change(self):
        """Set width, check it, and change it and check"""
        s1 = Square(5, 4)
        self.assertEqual(s1.width, 5)
        s1.width = 10
        self.assertEqual(s1.width, 10)

    def test_incorrect_width(self):
        """Testing string input type into width"""
        s1 = Square(5, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.width = "5"
        """Testing None input into width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.width = None
        """Testing List input into width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.width = [5, 7, 8]

        """Testing 0 input into width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.width = 0
        """Testing -5 input into width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.width = -5

    def test_correct_height_change(self):
        """Set height, check it, and change it and check"""
        s1 = Square(4, 5)
        self.assertEqual(s1.height, 4)
        s1.height = 10
        self.assertEqual(s1.height, 10)

    def test_incorrect_height(self):
        """Testing string input type into height"""
        s1 = Square(5, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            s1.height = "5"
        """Testing None input into height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            s1.height = None
        """Testing List input into height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            s1.height = [5, 7, 8]

        """Testing 0 input into height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            s1.height = 0
        """Testing -5 input into height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            s1.height = -5

    def test_correct_x_change(self):
        """Set x, check it, and change it and check"""
        s1 = Square(4, 5)
        self.assertEqual(s1.x, 5)
        s1.x = 10
        self.assertEqual(s1.x, 10)

    def test_incorrect_x_pos(self):
        """Testing string input type into x"""
        s1 = Square(5, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.x = "5"
        """Testing None input into x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.x = None
        """Testing List input into x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.x = [5, 7, 8]

        """Testing -1 input into x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1.x = -1
        """Testing -5 input into x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1.x = -5

    def test_correct_y_change(self):
        """Set y, check it, and change it and check"""
        s1 = Square(4, 5)
        self.assertEqual(s1.y, 0)
        s1.y = 10
        self.assertEqual(s1.y, 10)

    def test_incorrect_y_pos(self):
        """Testing string input type into y"""
        s1 = Square(5, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.y = "5"
        """Testing None input into y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.y = None
        """Testing List input into y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.y = [5, 7, 8]

        """Testing -1 input into y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s1.y = -1
        """Testing -5 input into y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s1.y = -5

    def test_private_attributes(self):
        """Testing if each attribute is private"""
        s4 = Square(5, 6, 3, 8)
        with self.assertRaises(AttributeError):
            s4.__width
        with self.assertRaises(AttributeError):
            s4.__height
        with self.assertRaises(AttributeError):
            s4.__x
        with self.assertRaises(AttributeError):
            s4.__y

    def test_no_inputs(self):
        """Testing no inputs"""
        with self.assertRaises(TypeError):
            s5 = Square()

    def test_1_inputs(self):
        """Testing 1 inputs"""
        s1 = Square(5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)

    def test_3_inputs(self):
        """Testing 3 inputs"""
        s5 = Square(3, 4, 5)
        self.assertEqual(s5.x, 4)
        self.assertEqual(s5.y, 5)

    def test_4_inputs(self):
        """Testing 4 inputs"""
        s5 = Square(3, 4, 5, 6)
        self.assertEqual(s5.x, 4)
        self.assertEqual(s5.y, 5)

    def test_area_correct_inputs(self):
        s1 = Square(3, 4)
        self.assertEqual(s1.area(), 9)
        s1 = Square(10, 20)
        self.assertEqual(s1.area(), 100)

    def test_print_str(self):
        s1 = Square(3, 2, 3, 10)
        self.assertEqual(str(s1), "[Square] (10) 2/3 - 3")

    def test_update_function_args(self):
        s1 = Square(10, 10, 10, 10)
        self.assertEqual(str(s1), "[Square] (10) 10/10 - 10")
        s1.update(89)
        self.assertEqual(str(s1), "[Square] (89) 10/10 - 10")
        s1.update(89, 2)
        self.assertEqual(str(s1), "[Square] (89) 10/10 - 2")
        s1.update(89, 2, 3)
        self.assertEqual(str(s1), "[Square] (89) 10/10 - 2")
        s1.update(89, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (89) 4/10 - 2")
        s1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(s1), "[Square] (89) 4/5 - 2")

    def test_update_function_kwargs(self):
        s1 = Square(10, 10, 10, 10)
        self.assertEqual(str(s1), "[Square] (10) 10/10 - 10")
        s1.update(height=1)
        self.assertEqual(str(s1), "[Square] (10) 10/10 - 10")
        s1.update(width=1, x=2)
        self.assertEqual(str(s1), "[Square] (10) 2/10 - 1")
        s1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(s1), "[Square] (89) 3/1 - 2")
        s1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(s1), "[Square] (89) 1/3 - 4")

    def test_update_function_incorrect(self):
        s1 = Square(10, 10, 10, 10)
        with self.assertRaises(KeyError):
            s1.update(1, 2, 3, 4, 5, 6)

    def test_size_setter(self):
        s1 = Square(10, 10, 10, 10)
        self.assertEqual(s1.width, 10)
        s1.size = 7
        self.assertEqual(s1.width, 7)
        self.assertEqual(s1.height, 7)
