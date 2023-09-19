#!/usr/bin/python3
# 100-matrix_mul.py
# Ethan Zalta
"""This is a function for multiplying matrices together"""


def matrix_mul(m_a, m_b):
    """This function multiplies matrix_a by matrix_b"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for innerList in m_a:
        if type(innerList) is not list:
            raise TypeError("m_a must be a list of lists")
    for innerList in m_b:
        if type(innerList) is not list:
            raise TypeError("m_b must be a list of lists")
    for innerList in m_a:
        if innerList == []:
            raise TypeError("m_a can't be empty")
    for innerList in m_b:
        if innerList == []:
            raise TypeError("m_b can't be empty")
    for innerList in m_a:
        for item in innerList:
            if not isinstance(item, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for innerList in m_b:
        for item in innerList:
            if not isinstance(item, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    row1 = len(m_a[0])
    for innerList in m_a:
        if len(innerList) != row1:
            raise TypeError("each row of m_a must be of the same size")
    row2 = len(m_b[0])
    for innerList in m_b:
        if len(innerList) != row2:
            raise TypeError("each row of m_b must be of the same size")
    if row1 > row2:
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []
    for numList in m_a:
        current_matrix_list = [0] * len(m_b[0])
        flag = 0
        i = 0
        for num in numList:
            for j in range(0, len(m_b[i])):
                # print(f"Length {len(m_b[i])}")
                try:
                    current_matrix_list[j] += num * m_b[i][j]
                except Exception as e:
                    print(e)
            i += 1
            flag += 1
        new_matrix.append(current_matrix_list)
    return new_matrix
