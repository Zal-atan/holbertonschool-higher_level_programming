#!/usr/bin/python3
# 101-add_attribute.py
# Ethan Zalta
"""This is a file creating a function to try to add new attributes to an
object."""


def add_attribute(obj, name, value):
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
