#!/usr/bin/python3
# 1-write_file.py
# Ethan Zalta
"""This is a file creating a function which writes to a file"""


def write_file(filename="", text=""):
    """This function creats or overwrites a file with the given text"""
    with open(filename, encoding="utf-8", mode="w") as file:
        numChars = file.write(text)
        file.close
    return numChars
