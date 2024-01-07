#!/usr/bin/python3
"""response header"""


import requests
from sys import argv


with requests.get(argv[1]) as res:
    val = res.headers.get('X-Request-Id')
    print(val)
