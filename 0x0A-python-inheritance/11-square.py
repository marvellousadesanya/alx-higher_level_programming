#!/usr/bin/python3
'''Defines of a subclass Square of subclass Rectangle'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A subclass of Rectangle'''
    def __init__(self, size):
        '''Initializing values of size and validation'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
