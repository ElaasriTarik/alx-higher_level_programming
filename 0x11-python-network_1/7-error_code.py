#!/usr/bin/python3
"""error code"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    with requests.get(url) as res:
        if res.status_code >= 400:
            print('Error code: {}'.format(res.status_code))
        else:
            print(res.text)
