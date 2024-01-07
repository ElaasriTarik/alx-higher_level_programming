#!/usr/bin/python3
"""post email"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        res = res.read().decode('utf-8')
        print(res)
