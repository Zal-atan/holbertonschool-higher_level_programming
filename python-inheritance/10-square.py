#!/usr/bin/python3
# 10-square.py
# Ethan Zalta
"""This is a file creating a class BaseGeometry, then a subclass Rectangle,
finally a sublass of rectangle: Square"""


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

    def area(self):
        """This function returns the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Changes the str representation of Rectangle class"""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Class Square which is a subclass of Rectangle"""

    def __init__(self, size):
        """Initializes Square with sides of length size"""
        if self.integer_validator("size", size):
            super().__init__(size, size)
            self.__size = size
