#!/usr/bin/python3
"""what is my status """
import requests


with requests.get('https://alx-intranet.hbtn.io/status') as res:
    res = res.text
    print('Body response:')
    print(f'\t- type: {type(res)}')
    print(f'\t- content: {res}')
