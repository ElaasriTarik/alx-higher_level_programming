#!/usr/bin/python3
"""save args to a file """
import sys
import os.path
import json


save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file


file = "add_item.json"
list = [sys.argv[1:]]
if os.path.isfile(file):
    load_from_json(file)
    save_to_json(list, file)
