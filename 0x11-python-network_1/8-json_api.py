#!/usr/bin/python3
"""json api"""
import requests
from sys import argv


url = 'http://0.0.0.0:5000/search_user'
letter = ""
if len(argv) == 1:
    print('No result')
else:
    letter = argv[1]

req = requests.post(url, params={'q': letter})
r = req.json()

if (r >= 400):
    print("Not a valid JSON")
elif (r.lenght == 0):
    print('No result')
else:
    print('[{}] {}'.format(r.get("id"), r.("name")))
