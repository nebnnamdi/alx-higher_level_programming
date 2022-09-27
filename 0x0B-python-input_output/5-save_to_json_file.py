#!/usr/bin/python3
"""A function that writes an Object
    to a text file using a JSON
    representation
"""


import json


def save_to_json_file(my_obj, filename):
    """Write JSON object to the file text
    """
    with open(filename, mode="w", encoding="utf-8") as writer:
        json.dump(my_obj, writer)
