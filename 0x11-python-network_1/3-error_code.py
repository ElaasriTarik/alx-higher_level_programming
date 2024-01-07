#!/usr/bin/python3
"""error code"""
import urllib.request
import urllib.error
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as res:
            print(res.read().decode('utf-8'))

    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
