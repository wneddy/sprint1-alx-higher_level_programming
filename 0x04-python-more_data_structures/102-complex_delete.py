#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for lock in list(a_dictionary.keys()):
        if a_dictionary[lock] == value:
            del a_dictionary[lock]
    return (a_dictionary)
