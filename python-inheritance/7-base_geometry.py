#!/usr/bin/python3
# 5-base_geometry.py
# Ethan Zalta
"""This is a file creating a class BaseGeometry"""


class BaseGeometry:
    """This is a class BaseGeometry"""

    def area(self):
        """Empty area function which raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if value is an integer, True if integer,
        error if false"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return True
