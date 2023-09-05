#!/usr/bin/python3
for n in range(0, 100):
    if n < 10:
        print("0", end="")
    if n == 99:
        print("{}".format(n))
    else:
        print("{}, ".format(n), end="")
