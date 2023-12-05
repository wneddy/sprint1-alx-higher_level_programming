#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        x = add(a, b)
        for j in range(4, 6):
            x = add(x, j)
        return x
    else:
        return sub(a, b)
