#!/usr/bin/python3
# 8-rectangle.py
# Ethan Zalta
"""This is a file creating a class BaseGeometry, then a subclass Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle which inherits from class BaseGeometry"""

    def __init__(self, width, height):
        """Initializes Rectangle class with width and height
        Both width and height must be checked by integer_validator method"""
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
