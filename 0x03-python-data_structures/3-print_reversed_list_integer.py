#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        le = len(my_list)
        my_list.reverse()
        for x in range(le):
            print("{:d}".format(my_list[x]))
