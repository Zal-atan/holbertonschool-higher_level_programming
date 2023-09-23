#!/usr/bin/python3
# 6-load_from_json_file.py
# Ethan Zalta
"""This is a file creating a function which retrieves json data from a file
and creates an object"""
import json


def load_from_json_file(filename):
    """This function reads from filename and returns an object"""
    with open(filename, encoding="utf-8", mode="r") as file:
        obj = json.load(file)
        file.close()
    return (obj)
