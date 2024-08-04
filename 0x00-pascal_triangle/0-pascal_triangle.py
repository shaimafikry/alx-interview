#!/usr/bin/python3


def pascal_triangle(n):
    # edge casses
    if n <= 0:
        return [[]]
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    all_list = [[1], [1, 1]]
    # loop through every row
    for row in range(2, n):
        # 1 is first value always
        row_list = [1]
        # addabl values == row length
        for i in range(1, row):
            # pascal formula is (n)Cm = (n-1)Cm-1 + (n-1)Cm
            m = all_list[row - 1][i - 1] + all_list[row - 1][i]
            row_list.append(m)
        # 1 last value alaways
        row_list.append(1)
        all_list.append(row_list)
    return all_list
