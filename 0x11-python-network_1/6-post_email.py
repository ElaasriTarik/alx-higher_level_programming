#!/usr/bin/python3
"""post email"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}

    with requests.get(url, data=email) as res:
        print(res)
