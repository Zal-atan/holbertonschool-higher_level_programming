#!/usr/bin/python3
for character in range(97, 123):
    if chr(character) == "e" or chr(character) == "q":
        continue
    else:
        print("{:c}".format(character), end= "")
