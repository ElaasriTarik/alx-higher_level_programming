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

    def area(self):
        """calculate area"""
        return (self.__size * self.__size)

    def my_print(self):
        ss = self.__size
        if ss == 0:
            print()
        else:
            for x in range(ss):
                for y in range(ss):
                    print("#", end="")
                ss = self.__size
                print()
