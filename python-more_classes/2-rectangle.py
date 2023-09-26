#!/usr/bin/python3
# 2-rectangle.py
# Ethan Zalta
"""This is a file creating a class for Rectangle."""


class Rectangle:
    """Creates a class of Rectangle with a width and a height."""

    def __init__(self, width=0, height=0):
        """Initializes Rectangle with a width and a size"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Returns the size of width - Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the size of width - Setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the size of width - Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the size of width - Setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width + 2 * self.height)
