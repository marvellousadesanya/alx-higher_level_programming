#!/usr/bin/python3

for ch in reversed(range(97, 123)):
    if ch % 2 != 0:
        ch = ch - 32
    print("{}".format(chr(ch)), end="")
