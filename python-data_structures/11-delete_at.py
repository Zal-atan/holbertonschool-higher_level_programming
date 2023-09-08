#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    listLen = len(my_list)
    if listLen <= idx or idx < 0:
        return my_list
    del my_list[idx]

    return my_list
