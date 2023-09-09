#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list) - 1
    copy = [x for x in my_list]
    if idx < 0 or idx > length:
        return (copy)
    copy[idx] = element
    return (copy)
