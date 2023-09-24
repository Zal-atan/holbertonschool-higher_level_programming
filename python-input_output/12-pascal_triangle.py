#!/usr/bin/python3
# 12-pascal_triangle.py
# Ethan Zalta
"""This is a file creating a function which returns a list of numbers to be
interpretted as a pascal triangle"""

def pascal_triangle(n):
    """Returns a list of lists of n length, which can be printed to create
    a pascal triangle"""
    triangle = []
    if n <= 0:
        return triangle
    for i in range(0, n):
        next_row = []
        for j in range(0, i + 1):
            if j is 0 or j is i:
                next_row.append(1)
            else:
                next_num = triangle[i - 1][j - 1] + triangle[i - 1][j]
                next_row.append(next_num)
        triangle.append(next_row)
    return triangle
