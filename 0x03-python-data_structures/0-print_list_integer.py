#!/usr/bin/python3

def print_list_integer(my_list=[]):
    '''print elements of list: my_list'''

    for elem in my_list:
        print('{:d}'.format(int(elem)))