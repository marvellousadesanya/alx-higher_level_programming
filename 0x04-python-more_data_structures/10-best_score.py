#!/usr/bin/python3

def best_score(a_dictionary):
    max_score = 0
    winner = None
    if type(a_dictionary) is dict:
        for key, value in a_dictionary.items():
            if value > max_score:
                max_score = value
                winner = key
    return winner
