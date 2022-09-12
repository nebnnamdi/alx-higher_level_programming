#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = int_print = 0
    while True:
        try:
            if index > x:
                print("{:d}".format.(mylist[index]), end="")
                index += 1
                int_print += 1
            else:
                print()
                return print_int
        except (ValueError, TypeError):
            index += 1
