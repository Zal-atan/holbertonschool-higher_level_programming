#!/usr/bin/python3
# 4-from_json_string.py
# Ethan Zalta
import json
"""This is a file creating a function which returns an object from an input
of a json string"""


def from_json_string(my_str):
    """This function creates or a json string from an input, if possible"""
    unserialized = json.loads(my_str)
    return unserialized
