#!/usr/bin/python3

import unittest
from models.square import Square
import sys
from io import StringIO
from models.base import Base
import json
from models.rectangle import Rectangle
import os


class TestBase(unittest.TestCase):
    ''' test cases for class Base '''

    def tearDown(self):
        ''' clean all '''

        sys.stdout = sys.__stdout__

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_json_string(self):

        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string(None), '[]')
        with self.subTest():
            r1 = Rectangle(10, 7, 2, 8, 1)
            r1_dict = r1.to_dictionary()
            json_dict = Base.to_json_string([r1_dict])
            self.assertEqual(r1_dict, {'x': 2, 'width': 10,
                                       'id': 1, 'height': 7,
                                       'y': 8})
            self.assertIs(type(r1_dict), dict)
            self.assertIs(type(json_dict), str)
            self.assertEqual(json.loads(json_dict), json.loads('[{"x": 2, '
                                                               '"width": 10, '
                                                               '"id": 1, '
                                                               '"height": 7, '
                                                               '"y": 8}]'))

    def test_square(self):
        ''' test square '''

        square1 = Square(44, 55, 66, 77)
        square1_dict = square1.to_dictionary()
        S2 = Rectangle.create(**square1_dict)
        self.assertNotEqual(square1, S2)


    def test_rectangle(self):
        ''' test rectangle '''

        rect1 = Rectangle(4, 5, 6)
        rect1_dict = rect1.to_dictionary()
        R2 = Rectangle.create(**rect1_dict)
        self.assertNotEqual(rect1, R2)

    def test_file_rectangle(self):
        ''' test file load from rect '''

        Rect1 = Rectangle(33, 34, 35, 26)
        Rect2 = Rectangle(202, 2)
        lR = [Rect1, Rect2]
        Rectangle.save_to_file(lR)
        lR2 = Rectangle.load_from_file()
        self.assertNotEqual(lR, lR2)

    def test_file_square(self):
        ''' test file load from square '''

        sq1 = Square(22)
        sq2 = Square(44, 44, 55, 66)
        lS = [sq1, sq2]
        Square.save_to_file(lS)
        lS2 = Square.load_from_file()
        self.assertNotEqual(lS, lS2)

if __name__ == "__main__":
    unittest.main()
