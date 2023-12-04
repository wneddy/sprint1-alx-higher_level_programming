#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    if sentence == "":
        first = None
    else:
        first = sentence[0:1]
    return ((size, first))
