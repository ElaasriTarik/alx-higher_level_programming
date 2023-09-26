#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """define a size for Square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ return size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ setting size """
        if isinstance(value, int) is False:
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
                return (self.__size ** 2)
    def area(self):
        """calculate area"""
        return (self.__size * self.__size)

    def __less__(self, other):
        return (self.size < other.size)

    def __less_or_eq__(self, other):
        return (self.size <= other.size)

    def __equals__(self, other):
        return (self.size == other.size)

    def __not__(self, other):
        return (self.size != other.size)

    def __greater_or_eq__(self, other):
        return (self.size >= other.size)

    def __greater__(self, other):
        return (self.size > other.size)
