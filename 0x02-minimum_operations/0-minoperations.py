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
    count_h = 1
    # there is always a copy_all and paste at least once
    count_oper = 0
    half_n = n / 2
    copied_h = 1
    goal = 0
    while count_h < n:
        # check if it less tha a half
        if count_h < half_n:
            # copy and paste the value
            count_oper += 2
        elif count_h == half_n:
            # copy , paste
            count_oper += 2
        elif count_h > half_n:
            goal = count_h - half_n
            if goal < copied_h:
                # only paste
                count_oper += 1
        # print(f" before copied_h {copied_h} count_h {count_h}")
        count_h += copied_h
        copied_h = count_h
        # print(f"copied_h {copied_h} count_h {count_h}")
    return count_oper
