#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    '''print list passed in reverse order'''

    '''if list is None'''
    if my_list is None:
        return

    # print in reverse
    idx = len(my_list) - 1
    while idx >= 0:
        print('{:d}'.format(my_list[idx]))
        idx -= 1
