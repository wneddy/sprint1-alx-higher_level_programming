#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for entity in set(my_list):
        result += entity
    return (result)
