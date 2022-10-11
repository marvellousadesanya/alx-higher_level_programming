#!/usr/bin/python3
'''Square class with all properties'''


class Square:
    '''Show all properties of square'''
    def __init__(self, size=0):
        '''Conditionals of size'''
        if type(size) is not int:
            '''Check if the passed size is an int'''
            raise TypeError("size must be an integer")
        elif (size < 0):
            '''
            Size mst be positive integer else throw error
            '''
            raise ValueError("size must be >= 0")

        self.__size = size
