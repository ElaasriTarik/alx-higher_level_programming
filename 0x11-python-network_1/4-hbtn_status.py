#!/usr/bin/python3
"""what is my status """
import requests


with requests.get('https://alx-intranet.hbtn.io/status') as res:
    ct = res.headers.get('Content-Type')
    content = res.headers.get('Content')
    print('Body response:')
    print(f'\t- type: {type(ct)}')
    print(f'\t- content: {res}')
