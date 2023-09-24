#!/usr/bin/python3
# 100-magic_string.py
# Ethan Zalta
"""This function prints "BestSchool more times each time it is called"""


def magic_string():
    try:
        magic_string.counter += 1
    except Exception as e:
        magic_string.counter = 1
    string = ""
    for i in range(magic_string.counter, 1, -1):
        string += "BestSchool, "
    string += "BestSchool"
    return string
