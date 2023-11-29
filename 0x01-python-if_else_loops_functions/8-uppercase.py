#!/usr/bin/python3
def uppercase(str):
    for character in str:
        checker = ord(character)
        if (checker > 96 and checker < 123):
            checker -= 32
        print("{}".format(chr(checker)), end="")
    print()
