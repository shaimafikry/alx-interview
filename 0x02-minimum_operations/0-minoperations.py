#!/usr/bin/python3
"""In a text file, there is a single character H.
Your text editor can execute only two operations
in this file: Copy All and Paste. Given a number
n, write a method that calculates the fewest number
of operations needed to result in
exactly n H characters in the file.
Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
  """


def minOperations(n):
    """
    method that calculates the fewest number
    of operations needed to result in
    exactly n H characters in the file
    Args:
        n (integer): num of operation
    Return: 0 if n is impossible to achieve
          : n
    """
    # edge casses
    if n <= 0 or n == 1:
        return 0
    if n == 2:
        return 2
    # define varibales
    # i have an H as default
    h = 1
    # there is always a copy_all and paste at least once
    operation = 0
    third_n = n / 3
    copy = 1
    goal = 0
    while h < n:
        # check if it less tha a half
        if h < third_n:
            # copy and paste the value
            operation += 2
            copy = h
        elif h == third_n:
            # copy , paste
            operation += 2
            copy = h
        elif h > third_n:
            goal = h - third_n
            if goal <= copy:
                # only paste
                if (h + copy) >= n:
                    operation += 1
                else:
                    operation += 2
                    copy = h
        h += copy
    return operation
