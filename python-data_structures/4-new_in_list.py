#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    listLen = len(my_list)
    if listLen <= idx or idx < 0:
        return my_list
    new_list = []
    for item in my_list:
        new_list.append(item)
    new_list[idx] = element
    return new_list
