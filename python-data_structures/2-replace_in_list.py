#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    listLen = len(my_list)
    if listLen <= idx or idx < 0:
        return my_list
    my_list[idx] = element
    return my_list
