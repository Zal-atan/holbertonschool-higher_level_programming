#!/usr/bin/python3
for character in range(122, 96, -1):
    if character % 2 == 1:
        print("{:c}".format(character - 32), end="")
    else:
        print("{:c}".format(character), end="")
