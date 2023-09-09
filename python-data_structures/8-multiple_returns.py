#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence is None:
        return None
    lenSen = len(sentence)
    if lenSen == 0:
        return None, None
    return lenSen, sentence[0]
