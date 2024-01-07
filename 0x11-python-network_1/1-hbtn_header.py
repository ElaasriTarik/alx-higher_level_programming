#!/usr/bin/python3
"""response header"""


import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as res:
    headers = res.info()
    val = headers.get('X-Request-Id')
    print(val)
