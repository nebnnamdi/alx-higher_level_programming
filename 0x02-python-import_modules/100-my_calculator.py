#!/usr/bin/python3
from calculator_1 import add, sub, div, mul

def arg_calc(argv):
    n = len(argv) - 1
    if n != 3:
        print("Usage: {:s} <a> <operator> <b>".format(sys.argv[str]))
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    x = int(sys.argv[2])
    if x == '+'
        print("{:d} {:s} {:d} = {:d}".format(a, x, b, add(a, b)))
    elif x == '-'
        print("{:d} {:s} {:d} = {:d}".format(a, x, b, sub(a, b)))
    elif x == '/'
        print("{:d} {:s} {:d} = {:d}".format(a, x, b, div(a, b)))
    elif x == '*'
        print("{:d} {:s} {:d} = {:d}".format(a, x, b, mul(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

if __name__ == "__main__":
import sys
arg_calc(sys.argv)
