#!/usr/bin/python3
'''Function to check for subclass'''


def inherits_from(obj, a_class):
    '''Checks if obj is an inherited class'''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
