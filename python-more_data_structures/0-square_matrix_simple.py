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

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
