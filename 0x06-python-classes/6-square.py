#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """define a size for Square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
    @property
    def size(self):
        """ return size"""
        return self.__size

    @property
    def position(self):
        return (sself.__position)

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and \
           isinstance(value[0], int) and isinstance(value[0], int) and \
           len(value) == 2 and \
           value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
