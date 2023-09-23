#!/usr/bin/python3
# 0-read_file.py
# Ethan Zalta
"""This is a file creating a function which reads from a file"""

def read_file(filename=""):
    """This function imports filename and reads the file to STDIN"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
        file.close()
