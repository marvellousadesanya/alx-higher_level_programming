#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squares = [[x**2 for x in elem] for elem in matrix]

    return squares
