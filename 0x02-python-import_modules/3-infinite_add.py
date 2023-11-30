#!/usr/bin/python3

# Author - Brendon Jeje

if __name__ == '__main__':
    import sys

    # loop through values and add them
    sum = 0
    i = 1
    while i < len(sys.argv):
        sum += int(sys.argv[i])
        i += 1

    print('{}'.format(sum))
