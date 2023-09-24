#!/usr/bin/python3
# 101-add_attribute.py
# Ethan Zalta
"""This is a file creating a function to try to add new attributes to an
object."""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if possible, otherwise, typerror"""
    listOfObjs = (int, float, str, list, tuple, dict, set, bool, complex)
    if isinstance(obj, listOfObjs):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
