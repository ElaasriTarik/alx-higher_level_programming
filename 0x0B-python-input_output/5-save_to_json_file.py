#!/usr/bin/python3
""" save to json """

import json


def save_to_json_file(my_obj, filename):
    """ return file """

    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
