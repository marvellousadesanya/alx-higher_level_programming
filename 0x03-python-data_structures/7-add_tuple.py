#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len_tuple_a = len(tuple_a)
    len_tuple_b = len(tuple_b)

    # Check if size of tuples is
    # not less or more than 2
    if len_tuple_a < 1:
        tuple_a = (0, 0)
    if len_tuple_a < 2:
        tuple_a = (tuple_a[0], 0)
    if len_tuple_a > 2:
        tuple_a = (tuple_a[0], tuple_a[1])

    if len_tuple_b < 1:
        tuple_b = (0, 0)
    if len_tuple_b < 2:
        tuple_b = (tuple_b[0], 0)
    if len_tuple_b > 2:
        tuple_b = (tuple_b[0], tuple_b[1])

    new_tuple = (tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1])
    return new_tuple
