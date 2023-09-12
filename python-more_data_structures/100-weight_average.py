#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list is None or type(my_list) != list:
        return 0
    denominator = 0
    numerator = 0
    for pair in my_list:
        denominator += pair[1]
        numerator += (pair[0] * pair[1])

    return numerator/denominator
