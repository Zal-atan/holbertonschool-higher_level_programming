#!/usr/bin/python3
# 8-rectangle.py
# Ethan Zalta
"""This is a file creating a class BaseGeometry, then a subclass Rectangle"""


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

class Rectangle(BaseGeometry):
    """Class Rectangle which inherits from class BaseGeometry"""

    def __init__(self, width, height):
        """Initializes Rectangle class with width and height
        Both width and height must be checked by integer_validator method"""
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
