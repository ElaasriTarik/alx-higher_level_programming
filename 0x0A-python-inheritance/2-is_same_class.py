#!/usr/bin/python3
""" is_same_class Class """


def is_same_class(obj, a_class):
    """ return true if class is the same, False otherwise """
    return (True if isinstance(obj, a_class) else False)
