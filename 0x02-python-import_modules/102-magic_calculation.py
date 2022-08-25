#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add,
    if a > b:
        c = add(a, b)
        for n in rang(4, 6):
            c = add(c, n)
        return c
    else:
        return sub(a, b)
