#!/usr/bin/python3
stat = False
c = ""
for code in range(122, 96, -1):
    if stat:
        c = chr(code - 32)
        stat = False
    else:
        c = chr(code)
        stat = True
    print("{}".format(c), end="")
