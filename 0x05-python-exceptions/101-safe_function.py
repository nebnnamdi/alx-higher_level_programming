#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        return fct(*args)
    except Exception as exe:
        print("Exception: {}".format(exe), file=stderr)
        return None
