#!/usr/bin/python3

def element_at(my_list, idx):
    listLen = len(my_list)
    if listLen <= idx or idx < 0:
        return None
    return (my_list[idx])
