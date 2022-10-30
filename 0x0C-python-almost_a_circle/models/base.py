#!/usr/bin/python3

'''Declaring base class'''

class Base:
    '''Instances declarations'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Assigning id attribute'''
        if id is not None:
            self.id = id
        else: 
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
