#!/usr/bin/python3
"""json api"""
import requests
from sys import argv


url = 'http://0.0.0.0:5000/search_user'
letter = ""
if len(argv) == 1:
    letters = ""
else:
    letter = argv[1][0]

req = requests.post(url, data={'q': letter})
r = req.json()

try:
    if r:
        print("[{}] {}".format(r.get("id"), r.get("name")))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
