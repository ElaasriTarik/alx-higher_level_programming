#!/usr/bin/python3
""" append_write function """


def append_write(filename="", text=""):
    """ implementation """

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
