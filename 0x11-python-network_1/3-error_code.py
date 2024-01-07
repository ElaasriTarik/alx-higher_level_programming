#!/usr/bin/python3
"""error code"""
import urllib.request
import urllib.error
from sys import argv


url = argv[1]
req = urllib.request.Request(url)

try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print('Error code: {}'.format(e.code))
