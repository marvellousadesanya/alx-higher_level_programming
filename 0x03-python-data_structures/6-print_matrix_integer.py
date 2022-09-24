#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # Loop all individual lists in matrix list
    for li in matrix:
        # Loop thru all the inner lists
        for new_li in li:
            print("{:d}".format(new_li), end="")
            # Adds space inbetween all elements
            # except the last element. The -1 is
            # critical
            if new_li != li[len(li) - 1]:
                print(" ", end="")
        print("")
