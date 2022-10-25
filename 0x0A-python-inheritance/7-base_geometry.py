#!/usr/bin/python3
'''Defines a class with area attribute'''


class BaseGeometry:
    '''A Geometry class with area an integer validator'''
    def area(self):
        '''Raises exception saying no area'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Function for integer validation'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
