#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    c = ""
    if length == 0:
        c = None
    else:
        c = sentence[0]
    return ((length, c))
