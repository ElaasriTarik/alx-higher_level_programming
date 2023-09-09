#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    le = len(my_list)
    arr = []
    for x in range(le):
        if x % 2 == 0:
            arr.append(True)
        else:
            arr.append(False)
    return (arr)
