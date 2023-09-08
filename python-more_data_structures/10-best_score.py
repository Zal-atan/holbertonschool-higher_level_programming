#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_score = 0
    highest = ""
    for key in a_dictionary:
        if a_dictionary[key] > max_score:
            highest = key
            max_score = a_dictionary[key]
    if max_score == 0:
        return None
    return highest
