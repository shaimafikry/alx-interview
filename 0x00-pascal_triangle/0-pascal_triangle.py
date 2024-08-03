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
    # row = length
    # start_row = 1
    # n = n - 2
    for row in range(2, n):
        # initiizing new row
        row_list = []
        # list_length = prev row + 1
        # list_length = start_row + 1
        # loop through every row
        # length decided by the row umber
        # idx is the start point of new added elements
        idx = row - 1
        start_row = row
        for i in range(start_row):
            target_row = start_row - 1
            # add the old nums
            for m in range(start_row):
              row_list.append(all_list[target_row][m])
              # how to make it only limitid to the new elemnts
              if m >= idx and m < start_row:
                # i want to add oly the new num
                  row_list[m] = all_list[target_row][m - 1] + all_list[target_row][m]
        start_row += 1
        all_list.append(row_list)
    return all_list
