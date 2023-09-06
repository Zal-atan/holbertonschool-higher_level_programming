#!/usr/bin/python3
import hidden_4

for word in dir(hidden_4):
    if word[0] != "_":
        print(word)
