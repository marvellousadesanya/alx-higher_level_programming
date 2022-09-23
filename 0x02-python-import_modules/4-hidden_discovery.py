#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for s in dir(hidden_4): # Loop thru all methds
        if s[:2] != "__": # skip those starting with __
            print("{:s}".format(s))
