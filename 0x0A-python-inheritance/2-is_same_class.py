#!/usr/bin/python3
""" is_same_class Class """


def is_same_class(obj, a_class):
    """ return true if class is the same, False otherwise """

    if isinstance(obj, a_class) and type(obj) == a_class:
        return (True)
    else:
        return (False)
