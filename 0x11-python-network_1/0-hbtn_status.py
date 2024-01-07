#!/usr/bin/python3
"""what is my status """
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
    html = res.read()

    print('Body response:')
    print(f'\t- type: {type(html)}')
    print(f'\t- content: {html}')
    utff = html.decode('utf-8')
    print(f'\t- utf8 content: {utff}')
