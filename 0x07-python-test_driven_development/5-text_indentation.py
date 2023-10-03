#!/usr/bin/python3
"""
This is the "5-test_indentation" module.
"""


def text_indentation(text):
    """ prints two line after ., ?, : """

    
    if type(text) is not str:
        raise TypeError("text must be a string")

    char = 0
    for a in text:
        if char == 0 and a == ' ':
            continue
        else:
            char = 1
        if char == 1:
            if a in (".", "?", ":"):
                print(a)
                print()
                char = 0
            else:
                print(a, end="")
