#!/usr/bin/python3
""" read_file function """


def read_file(filename=""):
    """ repr of read_file """

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
