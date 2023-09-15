#!/usr/bin/python3
# 0-add_integer.py
# Ethan Zalta
"""This is a function for Printing and separating a given Text"""


def text_indentation(text):
    """ This function prints a given text, and separates all instances of . and
    ? and : by two new lines each time. This function only accepts strings"""
    counter = 0
    textlen = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    for character in text:
        if character == ":" or character == "." or character == "?":
            print(character)
            print()
            counter = 0
            textlen += 1
        elif counter == 0 and character == " ":
            counter += 1
            continue
        elif textlen == (len(text) - 1) and character == " ":
            continue
        else:
            print(character, end="")
            counter += 1
        textlen += 1
