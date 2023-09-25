#!/usr/bin/python3
# 101-locked_class.py
# Ethan Zalta
"""This file creates a locked class called LockedClass"""


class LockedClass:
    """This class is locked from having any attributes except for first_name"""

    __slots__ = ("first_name")
