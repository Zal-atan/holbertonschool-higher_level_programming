#!/usr/bin/python3

def uppercase(str):
    newStr = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            newStr = newStr + (chr(ord(char) - 32))
        else:
            newStr += char
    print("{}".format(newStr))
