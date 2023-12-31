#!/usr/bin/python3
""" rectangle """
from models.base import Base


class Rectangle(Base):
    """ rectangle definition """

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' init everything '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        """ setter for width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ prop for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ prop for x """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ setter for x """
        if isinstance(value, int) is False:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ prop for y """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ setter for y """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        ''' area of rectangle'''
        return (self.__width * self.__height)

    def display(self):
        """ displays the triangle to the stdout """
        space = ' '
        star = '#'
        for y in range(self.y):
            print()
        for column in range(self.height):
            for x in range(self.x):
                print(space, end='')
            for row in range(self.width):
                print(star, end='')
            print()

    def __str__(self):
        ''' str '''
        return ("[Rectangle] ({}) {}/{} - {}/{}".
                format(
                    self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        ''' update args in the class '''

        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        '''
        setting each arg to its appropriate item
        '''
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]

        except IndexError:
            pass

    def to_dictionary(self):
        ''' dictionary '''
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
