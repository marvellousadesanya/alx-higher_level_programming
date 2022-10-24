#!/usr/bin/python3
'''
Check if obj is an instance
'''


def is_same_class(obj, a_class):
    '''
    Checks if obj is an instance of the a_class
    '''
    if type(obj) == a_class:
        return True
    return False
