#!/usr/bin/python3
'''Function that decodes JSON'''


import json


def from_json_string(my_str):
    return json.loads(my_str)
