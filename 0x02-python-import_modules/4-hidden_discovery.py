#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    hidden = dir(hidden_4)
    length = len(hidden)
    x = 0
    while x < length:
        if hidden[i][0:2] != "__":
            print(hidden[i])
            x += 1
