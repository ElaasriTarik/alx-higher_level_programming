#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict = sorted(a_dictionary)
    for k in dict:
        print("{}: {}".format(k, a_dictionary[k]))

