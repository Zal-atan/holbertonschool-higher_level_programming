#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    list_of_keys = []
    for key in a_dictionary:
        if value == a_dictionary[key]:
            list_of_keys.append(key)
    for key in list_of_keys:
        del a_dictionary[key]
    return a_dictionary
