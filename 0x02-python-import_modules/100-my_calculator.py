#!/usr/bin/python3

import sys

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    length = len(sys.argv)

    if length != 4:
        print("Usage: ./100-my_calculator.py {}".format(sys.argv))
        exit(1)
