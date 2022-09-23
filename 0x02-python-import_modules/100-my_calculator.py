#!/usr/bin/python3

import sys

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    args = sys.argv
    length = len(args)

    operator = ['+', '-', '*', '/']

    if length == 4:
        a = int(args[1])
        b = int(args[3])
        if operator[0] == args[2]:
            print("{} {} {} = {}".format(a, operator[0], b, add(a, b)))
        elif operator[1] == args[2]:
            print("{} {} {} = {}".format(a, operator[1], b, sub(a, b)))
        elif operator[2] == args[2]:
            print("{} {} {} = {}".format(a, operator[2], b, mul(a, b)))
        elif operator[3] == args[2]:
            print("{} {} {} = {}".format(a, operator[3], b, div(a, b)))
        elif operator[0 or 1 or 2 or 3] != args[2]:
            print(f"Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print(f"./100-my_calculator.py <a> <operator> <b>")
        exit(1)
