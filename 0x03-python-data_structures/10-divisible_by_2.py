#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = []
    lenA = len(my_list)
    lenB = len(new_list)
    lenB = lenA
    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
