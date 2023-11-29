#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    new_num = number * -1
    digit_lst = (-1) * (new_num % 10)
else:
    digit_lst = number % 10
if digit_lst > 5:
    print(f"Last digit of {number:d} is {digit_lst:d} and is greater than 5")
elif digit_lst == 0:
    print(f"Last digit of {number:d} is {digit_lst:d} and is 0")
elif digit_lst < 6 and digit_lst != 0:
    print(f"Last digit of {number:d} is {digit_lst:d} and is less than 6\
 and not 0")
