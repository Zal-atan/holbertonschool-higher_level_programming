#!/usr/bin/python3
# base.py
# Ethan Zalta
"""This is a file creating a Base Class"""
import json


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

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries:
            return []
        return json.dumps(list_dictionaries)
