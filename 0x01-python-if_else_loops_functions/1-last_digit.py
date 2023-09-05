#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
nLen = len(str(number))
l = int(str(number)[nLen - 1])
last = l if number >= 0 else l*-1

if last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif last < 6 and last > 0:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last} and is 0")
