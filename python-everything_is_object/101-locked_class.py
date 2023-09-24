#!/usr/bin/python3
# 101-locked_class.py
# Ethan Zalta
"""This file creates a locked class called LockedClass"""


class LockedClass:
    """This class is locked from having any attributes except for first_name"""

    def __setattr__(self, name, value):
        if name != "first_name":
            message = f"'LockedClass' object has no attribute '{name}'"
            raise AttributeError(message)
        super().__setattr__(name, value)
