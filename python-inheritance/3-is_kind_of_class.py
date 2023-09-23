#!/usr/bin/python3
# 3-is_kind_of_class.py
# Ethan Zalta
"""This is a file creating a function which will deteremine if a given
object is of a given type of class"""


def is_kind_of_class(obj, a_class):
    """This functions returns True if obj is an instance of a_class or an
    inherited class,
    or False if not."""
    return (isinstance(obj, a_class))
