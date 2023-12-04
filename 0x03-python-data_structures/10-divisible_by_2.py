#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divisors = []
    for pos in range(len(my_list)):
        if (my_list[pos] % 2 == 0):
            divisors.append(True)
        else:
            divisors.append(False)
    return (divisors)
