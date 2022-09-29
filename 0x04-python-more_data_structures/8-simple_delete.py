#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    for key_e in a_dictionary.items():
        if key_e == key:
            del a_dictionary.items[key_e]
        else:
            return a_dictionary
