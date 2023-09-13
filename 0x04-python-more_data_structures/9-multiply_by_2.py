#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nd = {}
    for x in a_dictionary:
        nd[x] = a_dictionary[x] * 2
    return (nd)
