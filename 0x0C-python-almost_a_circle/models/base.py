#!/usr/bin/python3
""" class Base """


import json
import csv
import turtle


class Base:
    """ base description """

    __nb_objects = 0

    def __init__(self, id=None):
        ''' initiating the class Base '''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' return th json representation of list_dictionaries '''

        return (json.dumps(list_dictionaries)
                if (list_dictionaries != "[]" and
                list_dictionaries is not None) else "[]")

    @classmethod
    def save_to_file(cls, list_objs):
        ''' save list_objs to cls file '''

        file = cls.__name__ + '.json'
        with open(file, 'w', encoding='utf-8') as f:
            if list_objs is not None:
                list_dic = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dic))
            else:
                file.write('[]')

    @staticmethod
    def from_json_string(json_string):
        ''' return list of json string representing json_string '''

        return (json.loads(json_string) if (json_string != "[]" and
                                            json_string is not None) else "[]")

    @classmethod
    def create(cls, **dictionary):
        new = cls(1, 2, 3, 4)
        new.update(**dictionary)

        return (new)

    @classmethod
    def load_from_file(cls):
        ''' load from file '''

        file = cls.__name__ + '.json'
        try:
            with open(file, 'w', encoding='utf-8') as f:
                list_dic = Base.from_json_string(f.read())
                return ([cls.create(**dic) for dic in list_dic])
        except IOError:
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        ''' save file to csv '''

        name = cls.__name__ + ".csv"
        with open(name, 'w', newline='') as csvf:
            if list_objs == [] or list_objs is None:
                csvf.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                writer = csv.writer(csvf)
                writer.writerow(fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        ''' load from file csv '''
