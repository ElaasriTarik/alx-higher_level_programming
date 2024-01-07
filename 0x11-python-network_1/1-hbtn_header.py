#!/usr/bin/python3
"""response header"""


import urllib.request
import sys


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as res:
        val = res.headers.get('X-Request-Id')
        print(val)
