#!/usr/bin/python3
# 2-is_same_class.py
# Ethan Zalta
"""This is a file creating a function which will deteremine ifa given
object is of a given type of class"""


def is_same_class(obj, a_class):
    """This functions returns True if obj is an instance of a_class,
    or False if not."""
    if type(obj) == a_class:
        return True
    return False
