#!/usr/bin/python3
# base.py
# Ethan Zalta
"""This is a file creating a Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle Class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return(f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """returns the size of each side of the square"""
        return self.width

    @size.setter
    def size(self, value):
        "Changes the width and height to be equal to size"
        self.width = value
        self.height = value
