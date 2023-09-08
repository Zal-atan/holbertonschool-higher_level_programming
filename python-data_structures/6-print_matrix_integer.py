#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        listLen = len(list)
        if listLen == 0:
            print()
            continue
        for num in range (0, listLen - 1):
            print("{:d}".format(list[num]), end=" ")
        print("{:d}".format(list[listLen - 1]))
