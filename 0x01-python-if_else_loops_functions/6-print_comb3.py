#!/usr/bin/python3
for b in range(0, 90):
    if b % 10 > b / 10:
        if b != 89:
            print("{:02d}, ".format(b), end='')
        else:
            print("{:02d}".format(b))
