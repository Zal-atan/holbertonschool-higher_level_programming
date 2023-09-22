#!/usr/bin/python3
# 0-lookup.py
# Ethan Zalta
"""This is a file creating a function which can look up available attributes
and methods of an object."""


def lookup(obj):
    """Takes any object as input and returns list of all available
    attributes and methods"""
    return dir(obj)
