#!/usr/bin/python3
from sys import argv

board = []
if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)
if argv[1].isdigit() is False:
    print("N must be a number")
    exit(1)
spots = int(argv[1])
if spots < 4:
    print("N must be at least 4")
    exit(1)

for x in range(spots):
    board.append([x, None])


def check_spot(q):
    for y in range(spots):
        if board[y][1] == q:
            return (True)
    return (False)


def clear_s(x):
    """clear spot.."""
    for s in range(x, spots):
        board[s][1] = None


def state(x, y):
    """approve or reject the solution.."""
    if (check_spot(y)):
        return False
    k = 0
    for k in range(x):
        if abs(board[k][1] - y) == abs(k - x):
            return False
    return True


def queen(x):
    """recursive function to find the solution"""
    for y in range(spots):
        clear_s(x)
        if state(x, y):
            board[x][1] = y
            if (x == spots - 1):
                print(board)
            else:
                queen(x + 1)


queen(0)
