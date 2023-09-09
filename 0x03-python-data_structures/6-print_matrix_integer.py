#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m in matrix:
        for i in m:
            print("{}".format(i), end=" " if i != m[-1] else "\n")
