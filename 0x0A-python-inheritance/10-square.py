#!/usr/bin/python3
""" square class """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """representation of square """

    def __init__(self, size):
        """ initiating class """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area of the square"""
        return (self.__size * self.__size)
