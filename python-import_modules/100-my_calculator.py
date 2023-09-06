#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

operators = ("+", "-", "*", "/")
if __name__ == "__main__":
    if len(argv) != 4:
        # print("1")
        exit(1)
    if argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        # print("1")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == "+":
        print("{} + {} = {}".format(a, b, add(a,b)))
    elif argv[2] == "-":
        print("{} - {} = {}".format(a, b, sub(a,b)))
    elif argv[2] == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif argv[2] == "/":
        print("{} / {} = {}".format(a, b, div(a,b)))

    exit(0)
