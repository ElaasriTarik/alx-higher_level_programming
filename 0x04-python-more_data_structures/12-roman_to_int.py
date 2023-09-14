#!/usr/bin/python
def roman_to_int(roman_string):
    if isinstance(roman_string, str) == False or roman_string == None:
        return (0)
    roman_obj = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D': 500, 'M': 1000 }
    keys = list(roman_obj)
    total = 0
    prev = 0
    for l in range (len(roman_string)):     
        for r in (keys):
            this = roman_string[l]
            n = roman_obj[r]
            if this == r:
                if n > prev:
                    total -= prev
                    total += n    
                else:
                    total += n
                    prev = n

    return (total)
