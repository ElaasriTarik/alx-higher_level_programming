#!/usr/bin/python3
""" class student """


class Student:
    """ implementation of class """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        stat = True
        if type(attrs) is list:
            for att in attrs:
                if type(att) is not str:
                    stat = False
            if stat:
                return ({k: getattr(self, k)\
                         for k in attrs \
                         if hasattr(self, k)})
        return (self.__dict__)

    def reload_from_json(self, json_data):
        if isinstance(json_data, dict):
            for key, value in json_data.items():
                if hasattr(self, key):
                    setattr(self, key, value)
