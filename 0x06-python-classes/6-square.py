#!/usr/bin/python3
'''Square class with area method'''


class Square:
    '''The initialization'''
    def __init__(self, size=0, position=(0, 0)):
        '''The conditions size must be in'''
        if (type(size) is not int):
            '''Error if not int'''
            raise TypeError("size must be an integer")
        elif (size < 0):
            '''Error if not +'''
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''Retrieve instance attribute size'''
        return self.__size

    @property
    def position(self) -> tuple:
        return self.__position

    @size.setter
    def size(self, value: int):
        '''Set value of size'''
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    @position.setter
    def position(self, value) -> None:
        '''Setting the position attribute'''
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) is not int or type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''The method to find area of square'''
        return (self.__size * self.__size)

    def my_print(self):
        '''Print a square'''
        if self.__size == 0:
            print()
        else:
            # Don't fill spaces when position[1]
            for i in range(self.__position[1]):
                print()

            # Add space when position[0] instead
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
