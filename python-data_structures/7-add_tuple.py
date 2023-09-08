#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    lenA = len(tuple_a)
    lenB = len(tuple_b)
    if lenA < 2:
        if lenA < 1:
            a0 = 0
        else:
            a0 = tuple_a[0]
        a1 = 0
    else:
        a0 = tuple_a[0]
        a1 = tuple_a[1]
    if lenB < 2:
        if lenB < 1:
            b0 = 0
        else:
            b0 = tuple_a[0]
        b1 = 0
    else:
        b0 = tuple_b[0]
        b1 = tuple_b[1]

    new_tuple = (a0 + b0, a1 + b1)
    return new_tuple
