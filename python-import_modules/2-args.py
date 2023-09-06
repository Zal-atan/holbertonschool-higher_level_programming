#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = len(argv)
    if args == 1:
        print(("0 arguments"))
    else:
        print("{} {}:".format(args - 1,
                              "argument" if args == 2 else "arguments"))
    for i in range(1, args):
        print("{}: {}".format(i, argv[i]))
