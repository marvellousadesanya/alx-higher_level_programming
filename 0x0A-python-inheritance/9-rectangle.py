#!/usr/bin/python3
'''Defines a Rectangle subclass'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Representation of a rectangle'''
    def __init__(self, width, height):
        '''instantiation of the rectangle'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        '''informal string rep of the rectangle'''
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
