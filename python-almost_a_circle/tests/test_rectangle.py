#!/usr/bin/python3
# test_rectangle.py
# Ethan Zalta
"""This is a Unittest class for testing the Base Class"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
import pycodestyle


class TestBase(unittest.TestCase):
    """ Unittests for Base Class"""

    def test_module_docstring(self):
        """Tests module docstring"""
        self.assertTrue(len(__import__("models").rectangle.__doc__) > 0)

    def test_class_docstring(self):
        """Tests the class DocString"""
        self.assertTrue(len(__import__('models')
                        .rectangle.Rectangle.__doc__) > 0)

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

    def test_is_instance(self):
        """Testing to make sure Instantiated correctly"""
        r2 = Rectangle(5, 4)
        self.assertIsInstance(r2, Rectangle)

    def test_rectangle_is_base(self):
        r2 = Rectangle(3, 4)
        self.assertIsInstance(r2, Base)

    def test_no_input_id(self):
        """Check for no input correct output"""
        r1 = Rectangle(5, 4)
        r2 = Rectangle(3, 2)
        self.assertEqual(r2.id - r1.id, 1)

    def test_input_with_id(self):
        """Testing with input for ID"""
        r3 = Rectangle(5, 4, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_correct_width_change(self):
        """Set width, check it, and change it and check"""
        r1 = Rectangle(5, 4)
        self.assertEqual(r1.width, 5)
        r1.width = 10
        self.assertEqual(r1.width, 10)

    def test_incorrect_width(self):
        """Testing string input type into width"""
        r1 = Rectangle(5, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.width = "5"
        """Testing None input into width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.width = None
        """Testing List input into width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.width = [5, 7, 8]

        """Testing 0 input into width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.width = 0
        """Testing -5 input into width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.width = -5

    def test_correct_height_change(self):
        """Set height, check it, and change it and check"""
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.height, 5)
        r1.height = 10
        self.assertEqual(r1.height, 10)

    def test_incorrect_height(self):
        """Testing string input type into height"""
        r1 = Rectangle(5, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.height = "5"
        """Testing None input into height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.height = None
        """Testing List input into height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.height = [5, 7, 8]

        """Testing 0 input into height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.height = 0
        """Testing -5 input into height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.height = -5

    def test_correct_x_change(self):
        """Set x, check it, and change it and check"""
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.x, 0)
        r1.x = 10
        self.assertEqual(r1.x, 10)

    def test_incorrect_x_pos(self):
        """Testing string input type into x"""
        r1 = Rectangle(5, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.x = "5"
        """Testing None input into x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.x = None
        """Testing List input into x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.x = [5, 7, 8]

        """Testing -1 input into x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.x = -1
        """Testing -5 input into x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.x = -5

    def test_correct_y_change(self):
        """Set y, check it, and change it and check"""
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.y, 0)
        r1.y = 10
        self.assertEqual(r1.y, 10)

    def test_incorrect_y_pos(self):
        """Testing string input type into y"""
        r1 = Rectangle(5, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.y = "5"
        """Testing None input into y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.y = None
        """Testing List input into y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.y = [5, 7, 8]

        """Testing -1 input into y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.y = -1
        """Testing -5 input into y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.y = -5

    def test_private_attributes(self):
        """Testing if each attribute is private"""
        r4 = Rectangle(5, 4, 6, 3, 8)
        with self.assertRaises(AttributeError):
            r4.__width
        with self.assertRaises(AttributeError):
            r4.__height
        with self.assertRaises(AttributeError):
            r4.__x
        with self.assertRaises(AttributeError):
            r4.__y

    def test_no_inputs(self):
        """Testing no inputs"""
        with self.assertRaises(TypeError):
            r5 = Rectangle()

    def test_1_inputs(self):
        """Testing 1 inputs"""
        with self.assertRaises(TypeError):
            r5 = Rectangle(5)

    def test_3_inputs(self):
        """Testing 3 inputs"""
        r5 = Rectangle(3, 4, 5)
        self.assertEqual(r5.x, 5)
        self.assertEqual(r5.y, 0)

    def test_4_inputs(self):
        """Testing 4 inputs"""
        r5 = Rectangle(3, 4, 5, 6)
        self.assertEqual(r5.x, 5)
        self.assertEqual(r5.y, 6)

    def test_area_correct_inputs(self):
        r1 = Rectangle(3, 4)
        self.assertEqual(r1.area(), 12)
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.area(), 200)

    def test_print_str(self):
        r1 = Rectangle(3, 4, 2, 3, 10)
        self.assertEqual(print(r1), "[Rectangle] (10) 2/3 - 3/4")

    def test_update_function(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(print(r1), "[Rectangle] (10) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(print(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(print(r1), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(print(r1), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(print(r1), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(print(r1), "[Rectangle] (89) 4/5 - 2/3")
