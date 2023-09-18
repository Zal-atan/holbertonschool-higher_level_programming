#!/usr/bin/python3
# 0-square.py
# Ethan Zalta
"""This is a file creating a class for Square."""


class Square:
    """Currently an empty class to define square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes Square with an initial size and position"""
        self.size = size
        self.position = position

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
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
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

    def __str__(self):
        """Returns a string of a square to print"""
        return_str = ""
        if self.__size == 0:
            return return_str
        for y in range(0, self.position[1]):
            return_str += "\n"
        for i in range(0, self.__size):
            for x in range(0, self.position[0]):
                return_str += " "
            for j in range(0, self.__size):
                return_str += "#"
            if i < (self.__size - 1):
                return_str += "\n"
        return return_str

    def __lt__(self, other_square):
        """Returns True if self.area is less than other_square.area"""
        return self.area() < other_square.area()

    def __le__(self, other_square):
        """Returns True if self.area is less than or = other_square.area"""
        return self.area() <= other_square.area()

    def __eq__(self, other_square):
        """Returns True if self.area is equal to other_square.area"""
        return self.area() == other_square.area()

    def __ne__(self, other_square):
        """Returns True if self.area is not equal to other_square.area"""
        return self.area() != other_square.area()

    def __gt__(self, other_square):
        """Returns True if self.area is greater than other_square.area"""
        return self.area() > other_square.area()

    def __ge__(self, other_square):
        """Returns True if self.area is greater than or = other_square.area"""
        return self.area() >= other_square.area()
