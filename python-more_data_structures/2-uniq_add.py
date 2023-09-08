#!/usr/bin/python3

def uniq_add(my_list=[]):
    check_list = []
    for num in my_list:
        if num not in check_list:
            check_list.append(num)
        else:
            continue

    sum = 0
    for num in check_list:
        sum += num

    return sum

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
