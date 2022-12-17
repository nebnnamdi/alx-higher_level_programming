#!/usr/bin/python3
"""A script that
fetches https://intranet.hbtn.io/status
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = argv[1]
    pwd = argv[2]
    req = requests.get(url, auth=(user, pwd))
    if (req.status_code == 200):
        user_json = req.json()
        print(user_json['id'])
    else:
        print("None")
