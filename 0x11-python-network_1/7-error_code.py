#!/usr/bin/python3
"""error code"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        res = requests.get(url)
        print(res.text)

    except requests.exceptions.RequestException as e:
        res = requests.get(url)
        if res.status_code >= 400:
            print('Error code: {}'.format(res.status_code))
