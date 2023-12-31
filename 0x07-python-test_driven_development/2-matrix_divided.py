#!/usr/bin/python3
""" Module matrix_devided """


def matrix_divided(matrix, div):
    """ devides each element of matrix by div
    div must be an int/float and not 0
 """
    
    new_list = []
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    list_len = len(matrix)
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if type(item) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    res = 0
    for row in matrix:
        n_row = []
        for item in row:
            try:
                res = item / div
            except ZeroDivisionError as e:
                raise ZeroDivisionError("division by zero") from e
            else:
                n_row.append(round(res, 2))
        new_list.append(n_row)
    return (new_list)
