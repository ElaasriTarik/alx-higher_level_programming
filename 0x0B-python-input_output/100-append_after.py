#!/usr/bin/python3
""" add after a specific string """


def append_after(filename="", search_string="", new_string=""):
    """ implementation """

    with open(filename, "r+", encoding="utf-8") as file:
        lines = file.readlines()
        for line in file:
            if line.find(sear_string) != -1:
                line.insert(line.find(search_string), new_string)

        file.seek(0)
        file.write("".join(lines))
