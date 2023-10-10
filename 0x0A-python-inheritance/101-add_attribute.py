#!/usr/bin/python3
""" add_attribute function"""


def add_attribute(obj, name, value):
    """ adds an attribute if possible """

    if hasattr(obj, '__dict__') == False:
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
