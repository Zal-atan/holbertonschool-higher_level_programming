#!/usr/bin/python3
# 5-save_to_json_file.py
# Ethan Zalta
"""This is a file creating a function which takes an object, converts it to
json, and then writes it to a file"""
import json


def save_to_json_file(my_obj, filename):
    """This function makes an object(my_obj) into json format, then writes it
    to a given filename"""
    serialized = json.dumps(my_obj)
    with open(filename, encoding="utf-8", mode="w") as file:
        chars = file.write(serialized)
        file.close
