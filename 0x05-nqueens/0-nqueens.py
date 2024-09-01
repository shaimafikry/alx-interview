#!/usr/bin/python3
""" N QUEESN solve quiz"""
from sys import argv


def main ():
    """ main func"""
    # If the user called the program with the wrong number of arguments,
    # print Usage: nqueens N, followed by a new line,
    # and exit with the status 1
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    # handle n cases:
    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)
    # n -> number of queens
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)
    row = [i for i in range(n)]
    column = [i for i in range(n)]
    print(n)






if __name__ == "__main__":
     main()
