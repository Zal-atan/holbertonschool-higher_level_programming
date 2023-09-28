#!/usr/bin/python3
# base.py
# Ethan Zalta
"""This is a file creating a Base Class"""


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initalizing Base Class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
