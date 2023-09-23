#!/usr/bin/python3
# 4-inherits_from.py
# Ethan Zalta
"""This is a file creating a function which will deteremine if a given
object is of a given type of inherited class"""


def inherits_from(obj, a_class):
    """This functions returns True if obj is an instance of inherited a_class,
    or False if not."""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
