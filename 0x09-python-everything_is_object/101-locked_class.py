#!/usr/bin/python3
""" LockedClss Module """


class LockedClass:
    """
    Prevents the user from instantiatingadding a new attributes
    except for 'first_name'.
    """


    __slots__ = ["first_name"]
