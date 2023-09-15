#!/usr/bin/python3
# 0-add_integer.py
# Ethan Zalta
"""TThis is a function for printing a square"""


def print_square(size):
    """ This function should print a square with length and width equal to
    input size.
    Size must be an integer of greater than or equal to 0"""
    for i in range(0, size):
        for i in range(0, size):
            print("#", end="")
        print()

