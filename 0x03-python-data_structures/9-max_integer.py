#!/usr/bin/python3

def max_integer(my_list=[]):
    max_number = 0
    if len(my_list) == 0:
        return "None"
    else:
        for i in my_list:
            if i > max_number:
                max_number = my_list[i]
            else:
                continue
        return max_number
