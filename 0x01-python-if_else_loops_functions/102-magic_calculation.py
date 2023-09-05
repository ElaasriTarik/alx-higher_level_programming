#!/usr/bin/python3
def magic_calculation(a, b, c):
    if c > b:
        return (a + b)
    return (c if (a < b) else (a*b - c))
