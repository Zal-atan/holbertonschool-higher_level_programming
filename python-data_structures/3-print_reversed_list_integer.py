#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        listLen = len(my_list)
        for num in range(listLen - 1, -1, -1):
            print("{:d}".format(my_list[num]))
