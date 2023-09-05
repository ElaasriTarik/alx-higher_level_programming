#!/usr/bin/python3
for n in range(0, 100):
    if n == 99:
        print("{}".format(n))
    else:
        print("{}, ".format(n if n > 9 else f"0{n}"), end="")
