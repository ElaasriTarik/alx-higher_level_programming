#!/usr/bin/env python3
def uppercase(str):
    s = ""
    for c in str:
        if 'a' <= c <= 'z':
            s += chr(ord(c) - 32)
        else:
            s += c
    print("{}".format(s))
