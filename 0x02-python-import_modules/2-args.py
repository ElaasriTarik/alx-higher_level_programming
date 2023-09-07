#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    print("{}".format(length), end=" ")
    if length > 1:
        print("arguments:")
        for a in range(1, length + 1):
            print("{}: {}".format(a, sys.argv[a]))
    elif length == 1:
        print("argument:")
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("arguments.")
    
