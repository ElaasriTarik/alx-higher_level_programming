#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 5:
            print("fizzBuzz", end=" ")
        elif x % 3 == 0:
            print("fizz", end=" ")
        elif x % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(f"{x}", end=" ")
