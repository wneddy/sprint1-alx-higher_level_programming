#!/usr/bin/python3
for b in range(0, 100):
    if b != 99:
        print("{:02d}, ".format(b), end='')
    else:
        print("{:02d}".format(b))
