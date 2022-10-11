#!/usr/bin/python3
'''Square class with area method'''


class Square:
    '''The initialization'''
    def __init__(self, size=0):
        '''The conditions size must be in'''
        if (type(size) is not int):
            '''Error if not int'''
            raise TypeError("size must be an integer")
        elif size < 0:
            '''Error if not +'''
            raise ValueError("size must be >= 0")
        '''Private instantiation of size'''
        self.__size = size

    def area(self):
        '''The method to find area of square'''
        return (self.__size * self.__size)
