#!/usr/bin/python3
# 0-add_integer.py
# Ethan Zalta
"""This is a function for adding two integers or floats"""


def matrix_divided(matrix, div):
    """ This function divides an input matrix by a given integer or float (div)
    Each list in the matrix must only contain integers and floats and must be
    of equal size. Can not divide by 0"""
    return [[round(x / div, 2) for x in row] for row in matrix]
