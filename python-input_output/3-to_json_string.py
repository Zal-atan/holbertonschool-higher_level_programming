#!/usr/bin/python3
# 3-to_json_string.py
# Ethan Zalta
"""This is a file creating a function which creates a json string from
a given input"""
import json


def to_json_string(my_obj):
    """This function creates or a json string from an input, if possible"""
    serialized = json.dumps(my_obj)
    return serialized
