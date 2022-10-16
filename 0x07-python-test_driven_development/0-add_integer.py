#!/usr/bin/python3

'''
Function to add two integers'''

def add_integer(a, b=98):
    '''Return addition of two ints'''
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    elif type(a) is float:
        a = int(a)
    elif type(b) is float:
        b = int(b)
    return a + b
