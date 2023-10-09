#!/usr/bin/python3

def no_c(my_string):
    res = ""
    for x in my_string:
        if x not in ('C', 'c'):
            res += x
    return res
