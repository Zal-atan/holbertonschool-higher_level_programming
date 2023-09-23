#!/usr/bin/python3
# 2-append_write.py
# Ethan Zalta
"""This is a file creating a function which appends to the end of a file"""


def append_write(filename="", text=""):
    """This function creates or appends a file with the given text"""
    with open(filename, encoding="utf-8", mode="a") as file:
        numChars = file.write(text)
        file.close
    return numChars
