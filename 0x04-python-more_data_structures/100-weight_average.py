#!/usr/bin/python3
def weight_average(my_list=[]):
    """ average return of all integers in a list of tuples."""
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    averg = 0
    length = 0
    for tuples in my_list:
        averg += (tuples[0] * tuples[1])
        length += tuples[1]
    return (averg / length)
