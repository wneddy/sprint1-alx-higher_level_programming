#!/usr/bin/python3
for val in range(122, 96, -1):
    print("{:c}".format(val if (val % 2 == 0) else (val - 32)), end='')
