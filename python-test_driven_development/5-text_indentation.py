#!/usr/bin/python3
# 0-add_integer.py
# Ethan Zalta
"""This is a function for Printing and separating a given Text"""


def text_indentation(text):
    """ This function prints a given text, and separates all instances of . and
    ? and : by two new lines each time. This function only accepts strings"""
    counter = 0
    for character in text:
        if character == ":" or character == "." or character == "?":
            print(character)
            print()
            counter = 0
        elif counter == 0 and character == " ":
            counter += 1
            continue
        else:
            print(character, end="")
            counter += 1
