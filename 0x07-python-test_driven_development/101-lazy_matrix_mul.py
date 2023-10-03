#!/usr/bin/python3
import numpy as np
"""Defines a matrix multiplication function using NumPy."""


def lazy_matrix_mul(m_a, m_b):
    """Multiplicates two matrices.
    Arguments:
        m_a (list of lists): matrix 1.
        m_b (list of lists): matrix 2.
    """
    mul = np.matmul(m_a, m_b)
    return (mul)
