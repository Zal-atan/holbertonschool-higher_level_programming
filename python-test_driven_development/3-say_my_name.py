#!/usr/bin/python3
# 0-add_integer.py
# Ethan Zalta
"""This is a function printing a given first and last name"""


def say_my_name(first_name, last_name=""):
    """ This function should print 'My name is {first_name}
    {last_name}' but only prints strings"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
