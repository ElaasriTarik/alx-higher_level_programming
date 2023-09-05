#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last *= -1
print(f"Last digit of {number} is {last} ", end="")

if last > 5:
    print(f"and is greater than 5")
elif last == 0:
    print(f"and is 0")
else:
    print(f"and is less than 6 and not 0")
