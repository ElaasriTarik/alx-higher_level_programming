#!/usr/bin/python3
""" making a pascale_triangle function """


def pascal_triangle(n):
    """ implementing the function """

    pascal = []
    if n <= 0:
        return ([])

    for i in range(n - 1):
        if i == 0:
            pascal.append([1])
            continue
        if i == 1:
            pascal.append([1, 1])

        nxt = [1]
        ps = pascal[i]

        for x in range(len(ps)):
            y = x + 1
            length = len(ps)
            if y < length:
                nxt.append(ps[x] + ps[y])

        nxt.append(1)
        pascal.append(nxt)

    return (pascal)
