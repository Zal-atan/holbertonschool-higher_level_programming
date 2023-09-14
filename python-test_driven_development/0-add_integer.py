#!/usr/bin/python3
# 0-add_integer.py
# Ethan Zalta
"""This is a function for adding two integers or floats"""

def add_integer(a, b=98):
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
