#!/usr/bin/python3
""" load from json file """


import json


def load_from_json_file(filename):
    """ implementation """
    with open(filename, "r") as file:
        return (json.load(file))
