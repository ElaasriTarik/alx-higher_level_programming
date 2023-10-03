#!/usr/bin/python3
# 0-add_integer.py
"""module for add_integer function"""


def add_integer(a, b=98):
    """ add_integer function, adds two ints or floats 
    return the sum of two values
    raises error when TypeError
    """

    if not isinstance(a, float) and not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, float) and not isinstance(b, int):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
