#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    sum = 0
    for i, arg in enumerate(sys.argv):
        if i > 0:
            sum += int(arg)
    print("{}".format(sum))
