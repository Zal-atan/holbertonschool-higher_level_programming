#!/usr/bin/python3
# 7-add_item.py
# Ethan Zalta
"""This is a file creating a function which saves Vargs as a list and then
writes them to a file"""
import json
from sys import argv
load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file


try:
    newList = load("add_item.json")

except Exception as e:
    newList = []

for obj in argv[1:]:
    newList.append(obj)

save(newList, "add_item.json")
