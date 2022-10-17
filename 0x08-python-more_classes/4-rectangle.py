#!/usr/bin/python3
'''
Rectangle class with height and width
'''


class Rectangle:
    '''A Rectangle class init declaration'''
    def __init__(self, width=0, height=0):
        '''Initializing values'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Getter for private instance attribute width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter for private instance attribute width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''getter for private instance attribute height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for private instance attribute height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Returns area of rectangle'''
        return self.width * self.height

    def perimeter(self):
        '''Returns perimeter of rectangle'''
        perimeter = 2 * (self.width + self.height)
        if (self.width == 0 or self.height == 0):
            perimeter = 0
        return perimeter

    def __str__(self):
        '''Returns a string of characters printing rect'''
        string = ""
        if self.__width != 0 and self.__height != 0:
            # Print the width for every line of the height
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        '''Returns a string representation of the rectangle class'''
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
