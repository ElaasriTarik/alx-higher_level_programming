#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    my_list.reverse()
    for x in range(0, length):
        print(my_list[x])
