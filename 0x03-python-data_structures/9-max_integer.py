#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        mx = my_list[0]
        le = len(my_list)
        for i in range(le):
            if my_list[i] > mx:
                mx = my_list[i]
        return (mx)
    return (None)
