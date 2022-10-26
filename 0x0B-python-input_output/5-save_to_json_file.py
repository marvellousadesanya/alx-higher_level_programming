#!/usr/bin/python3
'''Function that writes object to JSON file'''

import json


def save_to_json_file(my_obj, filename):
    '''Writes object to JSON file'''
    with open(filename, mode="w") as f:
        json.dump(my_obj, f)

