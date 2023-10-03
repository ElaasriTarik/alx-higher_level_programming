#!/usr/bin/python3
def magic_string(static={"n": 0}):
    static["n"] += 1
    return (str("BestSchool, " * static["n"])[:-2])
