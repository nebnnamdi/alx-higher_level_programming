#!/usr/bin/python3
def print_last_digit(number):
    ex = 0
    if number < 0:
        number *= -1
    ex = 1
    last = number % 10
    if ex == 1:
        number *= -1
    print("{:d}".format(last), end="")
    return last
