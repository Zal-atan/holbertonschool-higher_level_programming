#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for list in matrix:
        listLen = len(list)
        if listLen == 0:
            print()
            continue
        new_list = []
        for num in list:
            new_list.append(num ** 2)
        new_matrix.append(new_list)

    return new_matrix
