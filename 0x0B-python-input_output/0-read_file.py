#!/usr/bin/python3
'''A funtion that a file and prints to stdout'''


def read_file(filename=""):
    '''Function to print'''
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
