#!/usr/bin/python3
# 2-square.py
# Ethan Zalta
"""This is a file creating a class for Square."""


class Square:
    """Currently an empty class to define square"""

    def __init__(self, size=0):
        """Now Initializing Square with a size"""
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
