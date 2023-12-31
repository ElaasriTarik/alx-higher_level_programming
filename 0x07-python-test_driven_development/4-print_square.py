#!/usr/bin/python3
def print_square(size):
    if type(size) is not int:
        if type(size) is float:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
