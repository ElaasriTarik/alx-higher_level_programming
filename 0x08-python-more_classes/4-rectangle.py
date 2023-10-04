#!/usr/bin/python3
"""create empty class """


class Rectangle:
    """ adding width and height private attributes """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ prop for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ prop for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return (rect)

        rect += "\n".join("#" * self.__width for j in range(self.__height))
        return (rect)

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))
