#!/usr/bin/python3
# 8-class_to_json.pycp
# Ethan Zalta
"""This is a file creating a function which turns an instance of a class into
a json version"""


def class_to_json(obj):
    """Takes input obj(instance of a class) and returns a json format
    string of the information"""
    return obj.__dict__
