#!/usr/bin/python3
# 2-matrix_divided.py
# Ethan Zalta
"""This is a function dividing a whole matrix"""


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
    i = 0
    listLen = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(typeerror1)
        if i != 0 and listLen != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        i += 1
        listLen = len(row)
        for number in row:
            if type(number) is not int and type(number) is not float:
                raise TypeError(typeerror1)

    return [[round(x / div, 2) for x in row] for row in matrix]
