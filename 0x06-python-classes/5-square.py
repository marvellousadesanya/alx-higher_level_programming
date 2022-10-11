#!/usr/bin/python3
'''Square class with area method'''


class Square:
    '''The initialization'''
    def __init__(self, size=0):
        '''The conditions size must be in'''
        if (type(size) is not int):
            '''Error if not int'''
            raise TypeError("size must be an integer")
        elif (size < 0):
            '''Error if not +'''
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        '''Retrieve instance attribute size'''
        return self.__size

    @size.setter
    def size(self, value: int):
        '''Set value of size'''
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        '''The method to find area of square'''
        return (self.__size * self.__size)

    def my_print(self):
        '''Print a square'''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.size)
