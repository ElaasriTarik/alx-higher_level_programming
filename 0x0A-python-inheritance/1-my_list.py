#!/usr/bin/python3
""" myList class """


class MyList(list):
    """ SubClass """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        sortedList = sorted(self)
        print(sortedList)
