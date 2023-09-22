#!/usr/bin/python3
# 1-my_list.py
# Ethan Zalta
"""This is a file creating a class MyList that inherits from list"""


class MyList(list):
    """ Class MyList inherits from list"""

    def print_sorted(self):
        """Sorts then prints list"""
        print(sorted(self))
