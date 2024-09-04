#!/usr/bin/python3
""" N QUEESN solve quiz"""
from sys import argv


def check_constrains(queen, queens):
    """ check for constrains"""
    # check if the queen is only in a row
    # check if the queen in a column
    for old_queen in queens:
        if old_queen[0] == queen[0] or old_queen[1] == queen[1]:
            return False

    # check if the  queen in diagonal
    for old_queen in queens:
        if abs(queen[0] - old_queen[0]) == abs(queen[1] - old_queen[1]):
            return False
    return True
    # # check diagnoal x (increase the x and decrease the y)
    # # check diagnoal y (increase the y and decrease the x)
    # limit = 0
    # while True:
    #     x = queen[0]
    #     y = queen[1]
    #     # check for borders
    #     if x != 0 and y != chess_board - 1:
    #         while True:
    #             # check diagnoal up right ( decrease x , increase y)
    #             x -= 1
    #             y += 1
    #             check_queen = [x, y]
    #             if check_queen in queens:
    #                 return False
    #             if x == 0:
    #                 break
    #     if x != 0 and y != 0:
    #         x = queen[0]
    #         y = queen[1]
    #         while True:
    #             # check diagnoal up left ( decrease x , decrease y)
    #             x -= 1
    #             y -= 1
    #             check_queen = [x, y]
    #             if check_queen in queens:
    #                 return False
    #             if x == 0:
    #                 break

    #     if x != chess_board - 1 and y != chess_board - 1:
    #         x = queen[0]
    #         y = queen[1]
    #         while True:
    #             # check diagnoal down right ( increase x , increase y)
    #             x += 1
    #             y += 1
    #             check_queen = [x, y]
    #             if check_queen in queens:
    #                 return False
    #             if x == chess_board - 1:
    #                 break
    #     if x != chess_board - 1 and y != 0:
    #         x = queen[0]
    #         y = queen[1]
    #         while True:
    #             # check diagnoal down left ( increase x , decrease y)
    #             x += 1
    #             y -= 1
    #             check_queen = [x, y]
    #             if check_queen in queens:
    #                 return False
    #             if x == chess_board - 1:
    #                 break
    #     return True


def place_queen(n, row, queens):
    """ to place queen"""
    # loop exit
    if row == n:
        print(queens)
        return
    for col in range(n):
        queen = [row, col]
        # if the queen  not under attack
        if check_constrains(queen, queens):
            place_queen(n, row + 1, queens + [queen])


def main():
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

    # n = 4
    place_queen(n, 0, [])


if __name__ == "__main__":
    main()
