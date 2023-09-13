#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            n_list.append(replace)
            i += 1
        else:
            n_list.append(my_list[i])
            i += 1
    return (n_list)
