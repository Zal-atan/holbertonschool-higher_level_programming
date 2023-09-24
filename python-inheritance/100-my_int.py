#!/usr/bin/python3
# 100-my_int.py
# Ethan Zalta
"""This is a file creating a class myInt"""


class MyInt(int):
    """Class MyInt inherits from int"""

    def __eq__(self, value):
        if self.numerator == value:
            return False
        else:
            return True

    def __ne__(self, value):
        if self.numerator == value:
            return True
        else:
            return False
