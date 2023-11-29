#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1
    digit_lst = number % 10
    print("{}".format(digit_lst), end="")
    return (digit_lst)
