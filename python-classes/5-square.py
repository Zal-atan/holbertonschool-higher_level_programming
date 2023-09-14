#!/usr/bin/python3
# 0-square.py
# Ethan Zalta
"""This is a file creating a class for Square."""


class Square:
    """Currently an empty class to define square"""

    def __init__(self, size=0):
        """Initializes Square with a size"""
        self.__size = size

    @property
    def size(self):
        """Finds the size of self -- Getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value for size -- Setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Prints the area of square"""
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range (0, self.__size):
            for j in range (0, self.__size):
                print("#", end="")
            print("")
