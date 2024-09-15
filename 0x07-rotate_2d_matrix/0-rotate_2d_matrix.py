#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """mtrix rotate func"""
    # make the verticl horzintal
    length = len(matrix)
    for r in range(length):
        # to only conver the column at a loop not all the row
        for c in range(r, length):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    for i in matrix:
        i.reverse()
