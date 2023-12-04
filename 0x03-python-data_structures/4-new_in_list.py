#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    size = len(my_list)
    list_copy = my_list.copy()
    if (idx < 0 or idx >= size):
        return (list_copy)
    list_copy[idx] = element
    return (list_copy)
