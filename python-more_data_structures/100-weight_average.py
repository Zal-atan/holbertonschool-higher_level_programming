#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list is None:
        return 0
    denominator = 0
    numerator = 0
    for pair in my_list:
        if pair[1] == 0:
            return 0
        denominator += pair[1]
        numerator += (pair[0] * pair[1])

    return numerator/denominator
