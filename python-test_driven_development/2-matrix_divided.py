#!/usr/bin/python3
# 0-add_integer.py
# Ethan Zalta
"""This is a function for adding two integers or floats"""


def matrix_divided(matrix, div):
    """ This function divides an input matrix by a given integer or float (div)
    Each list in the matrix must only contain integers and floats and must be
    of equal size. Can not divide by 0"""
    typeerror1 = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(typeerror1)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if type(row) is not list:
            raise TypeError(typeerror1)
    return [[round(x / div, 2) for x in row] for row in matrix]
