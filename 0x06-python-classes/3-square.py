#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """define a size for Square"""
    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
    def area(self):
        return (self.__size * self.__size)
