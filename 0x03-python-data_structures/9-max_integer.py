#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"

    max_number = my_list[0]
    for i in my_list:
        if max_number < i:
            max_number = i
        else:
            continue
    return max_number
