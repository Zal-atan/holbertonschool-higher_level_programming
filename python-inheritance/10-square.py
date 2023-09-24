#!/usr/bin/python3
# 10-square.py
# Ethan Zalta
"""This is a file creating a class BaseGeometry, then a subclass Rectangle,
finally a sublass of rectangle: Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square which is a subclass of Rectangle"""

    def __init__(self, size):
        """Initializes Square with sides of length size"""
        if self.integer_validator("size", size):
            super().__init__(size, size)
            self.__size = size
