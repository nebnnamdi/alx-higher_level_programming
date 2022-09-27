#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """ Append a text to the end of a file """
    with open(filename, mode="a", encoding="utf-8") as writer:
        return writer.write(text)
