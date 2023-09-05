#!/usr/bin/python3

def remove_char_at(str, n):
    newStr = ""
    i = 0
    for char in str:
        if i == n:
            i += 1
            continue
        else:
            i += 1
            newStr += char

    return newStr
