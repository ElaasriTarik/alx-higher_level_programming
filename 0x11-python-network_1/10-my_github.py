#!/usr/bin/python3
""" my github """
import requests
from sys import argv


username = argv[1]
token = argv[2]

url = f'https://api.github.com/users/{username}'
headers = {"Authorization": f"token {token}"}

res = requests.get(url, headers=headers)

userData = res.json()
userId = userData.get("id")

print(userId)
