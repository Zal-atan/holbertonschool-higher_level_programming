#!/usr/bin/python3
# rectangle.py
# Ethan Zalta
"""This is a file creating a Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class as a subclass of Base Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes with super Id, private width, height, x and y"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns private value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Allows width to be set as a new integer"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns private value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Allows height to be set as a new integer"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns private value of x - position"""
        return self.__x

    @x.setter
    def x(self, value):
        """Allows height to be set as a new integer"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns private value of y - position"""
        return self.__y

    @y.setter
    def y(self, value):
        """Allows height to be set as a new integer"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Checks the Area of the rectangle"""
        return self.width * self.height
