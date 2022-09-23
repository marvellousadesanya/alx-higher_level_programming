#!/usr/bin/python3

def no_c(my_string):
    new_string = ''
    for ch in my_string:
        if ch != chr(100) and ch != chr(67):
            new_string += ch
    return new_string
