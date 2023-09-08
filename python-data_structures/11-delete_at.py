#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    listLen = len(my_list)
    if listLen <= idx or idx < 0:
        return my_list
    new_list = []
    i = 0
    for num in range(0, listLen):
        if i == idx:
            i += 1
            continue
        new_list.append(my_list[num])
        i += 1

    my_list = new_list
    return new_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)
