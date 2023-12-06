#!/usr/bin/python3


def roman_to_int(roman_string):
    """Converts a roman numeral to an integer."""
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)

    rmnDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    val = 0

    for x in range(len(roman_string)):
        if rmnDict.get(roman_string[x], 0) == 0:
            return (0)
        if (x != (len(roman_string) - 1) and
                rmnDict[roman_string[x]] < rmnDict[roman_string[x + 1]]):
                val += rmnDict[roman_string[x]] * -1

        else:
            val += rmnDict[roman_string[x]]
    return (val)
