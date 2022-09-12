#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as vErr:
        print("Exception: {}".format(vErr), file=sys.stderr)
        return False
    except TypeError as tErr:
        print("Exception: {}".format(tErr), file=sys.stderr)
        return False
