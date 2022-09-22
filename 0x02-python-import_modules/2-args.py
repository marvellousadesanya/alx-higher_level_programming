#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    length = len(sys.argv)

    if length == 1:
        print(f"0 arguments.")
    elif length == 2:
        print("{:d} argument:".format(length - 1))
    elif length >= 2:
        print("{:d} arguments:".format(length - 1))

    for i, arg in enumerate(sys.argv):
        if i > 0:
            print("{:d}: {:s}".format(i, arg))
