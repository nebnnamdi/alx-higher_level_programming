#!/usr/bin/python3
def max_integer(my_list=[]):
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
        else:new_list.append(False)
    return new_list
