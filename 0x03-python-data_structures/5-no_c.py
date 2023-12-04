#!/usr/bin/python3
def no_c(my_string):
    copyStr = ""
    for character in my_string:
        if (character == 'c' or character == 'C'):
            continue
        copyStr += character
    return (copyStr)
