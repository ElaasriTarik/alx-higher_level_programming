#!/usr/bin/python3
""" inherits_from """


def inherits_from(obj, a_class):
    """ return true or false """

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return (True)
    return (False)
