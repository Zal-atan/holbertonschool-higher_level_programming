#!/usr/bin/python3
# 6-rectangle.py
# Ethan Zalta
"""This is a file creating a class for Rectangle."""


class Rectangle():
    """Creates a class of Rectangle with a width and a height."""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes Rectangle with a width and a size"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        """Returns the area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width + 2 * self.height)

    def __str__(self):
        """Returns a str version of the printout of the rectangle"""
        print_display = ""
        if self.height == 0 or self.width == 0:
            return print_display
        for y in range(0, self.height):
            for x in range(0, self.width):
                print_display += "#"
            if y < (self.height - 1):
                print_display += "\n"
        return print_display

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
