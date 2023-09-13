#!/usr/bin/python3
def uniq_add(my_list=[]):
    list = set(my_list)
    res = 0
    for n in list:
        res += n
    return (res)
