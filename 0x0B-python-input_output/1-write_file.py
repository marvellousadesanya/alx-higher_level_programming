#!/usr/bin/python3
'''Function that writes to file'''


def write_file(filename="", text=""):
    ''' Write command'''
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
