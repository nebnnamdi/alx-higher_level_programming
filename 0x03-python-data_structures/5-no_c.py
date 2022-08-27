#!/usr/bin/python3
def no_c(my_string):
    rep_str = ""
    for i in my_string:
        if i is not 'c' and i is not 'C':
            rep_str += i
        return (rep_str)
