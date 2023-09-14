#!/usr/bin/python3
# 0-square.py
# Ethan Zalta
"""This is a file creating a class for Square."""


class Square:
    """Currently an empty class to define square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes Square with an initial size and position"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        "Finds the current position -- Getter"
        return self.__position

    @position.setter
    def position(self, value):
        """Sets a new value for position -- Setter"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value [1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) > 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Prints the area of square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints shape of a square with #'s
            Position is shown by blank spaces"""
        if self.__size == 0:
            print("")
            return
        for y in range(0, self.position[1]):
            print("")
        for i in range(0, self.__size):
            for x in range(0, self.position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print("")
