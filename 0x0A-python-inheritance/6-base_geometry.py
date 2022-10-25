#!/usr/bin/python3
'''Defines a class with area attribute'''


class BaseGeometry:
    '''Raise exception on area attribute'''
    def area(self):
        raise Exception("area() is not implemented")
