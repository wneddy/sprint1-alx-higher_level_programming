#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        latest_str = str[:n] + str[n + 1:]
        return latest_str
    else:
        return str
