#!/usr/bin/python3
""" convert a class to json """


def class_to_json(obj):
    if isinstance(obj, (int, str, bool)):
        return (obj)

    if isinstance(obj, list):
        return ([object_to_serializable_dict(item) for item in obj])

    if isinstance(obj, dict):
        return ({key: object_to_serializable_dict(value) for key, value in obj.items()})

    return (str(obj))
