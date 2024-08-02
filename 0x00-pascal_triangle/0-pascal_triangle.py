#!/usr/bin/python3

# n represent num of row
def pascal_triangle(n):
    if n <= 0:
        return []
    all_list = [[1],[1, 1]]
    # pascal formula is (n)Cm = (n-1)Cm-1 + (n-1)Cm
    #plan
    # loop through every row
    # start row = 1
    start_row = 1
    n = n - 2
    for row in range(n):
        # initiizing new row
        row_list = []
        # list_length = prev row + 1
        list_length = start_row + 1
        for i in range(list_length):
            target_row = start_row - row
            idx = 0
            element = all_list[target_row][idx] - 1 + all_list[target_row][idx]
            row_list.append(element)
            idx += 1
        start_row += 1
        all_list.append(row_list)
    return all_list
