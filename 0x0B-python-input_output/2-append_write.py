#!/usr/bin/python3
'''A function that appends a string to a file'''


def append_write(filename="", text=""):
    '''Append string to end of file'''
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
