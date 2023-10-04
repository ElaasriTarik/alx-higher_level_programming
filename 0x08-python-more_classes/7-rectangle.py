#!/usr/bin/python3
"""create empty class """


class Rectangle:
    """ adding width and height private attributes """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        w = self.__width
        h = self.__height
        rect += "\n".join(str(self.print_symbol) * w for j in range(h))
        return (rect)

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
