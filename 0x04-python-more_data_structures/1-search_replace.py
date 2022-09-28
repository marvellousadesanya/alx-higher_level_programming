#!/usr/bin/python3

def search_replace(my_list, search, replace):
    copied_list = my_list.copy()
    for i in range(len(copied_list)):
        if copied_list[i] == search:
            copied_list[i] = replace
    return copied_list
