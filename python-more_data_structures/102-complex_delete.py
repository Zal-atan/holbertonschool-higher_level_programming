#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_dict = dict(sorted(a_dictionary.items()))
    for key in sorted_dict:
        print("{}: {}".format(key, sorted_dict[key]))


def complex_delete(a_dictionary, value):
    list_of_keys = []
    for key in a_dictionary:
        if value == a_dictionary[key]:
            list_of_keys.append(key)
    for key in list_of_keys:
        del a_dictionary[key]
    return a_dictionary

a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
new_dict = complex_delete(a_dictionary, 'C')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = complex_delete(a_dictionary, 'Low')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
