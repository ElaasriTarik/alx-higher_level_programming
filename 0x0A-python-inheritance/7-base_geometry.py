#!/usr/bin/python3
""" baseGeometry """


class BaseGeometry:
    """ class baseGeometry """

    def area(self):
        """ area fail """

        raise Exception("area() is not implemented")
  
    def integer_validator(self, name, value):
        """ integer validator """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
