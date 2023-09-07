#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    args = sys.argv
    length = len(args)
    if length == 4:
        a = int(args[1])
        b = int(args[3])
        if args[2] == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif args[2] == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif args[2] == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif args[2] == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
