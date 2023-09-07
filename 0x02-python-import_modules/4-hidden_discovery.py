#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    count = len(names)
    for n in range(0, count):
        if names[n][0:2] != "__":
            print(names[n])
