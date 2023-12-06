#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return ([list(map(lambda c: c * c, rec)) for rec in matrix])
