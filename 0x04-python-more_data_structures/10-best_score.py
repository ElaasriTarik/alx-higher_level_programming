#!/usr/bin/pyhton3
def best_score(a_dictionary):
    mx = 0
    name = ""
    if a_dictionary is None or len(a_dictionary) == 0:
        return (None)
    else:
        key = list(a_dictionary)
        for k in key:
            if a_dictionary[k] > mx:
                mx = a_dictionary[k]
                name = k
    return (name)
