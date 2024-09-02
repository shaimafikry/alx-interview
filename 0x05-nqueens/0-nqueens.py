#!/usr/bin/python3
""" N QUEESN solve quiz"""
from sys import argv

queens = []
def check_constrains(queen, chess_board):
    """ check for constrains"""
    # check if the queen is only in a row
    for old_queen in queens:
      if old_queen[0] == queen[0]:
          return False

    # check if the queen in a column
    for old_queen in queens:
      if old_queen[1] == queen[1]:
          return False

    # check if the  queen in diagonal
    # check diagnoal x (increase the x and decrease the y)
    # check diagnoal y (increase the y and decrease the x)
    limit = 0
    while True:
        x = queen[0]
        y = queen[1]
        # check for borders
        if x != 0 and y != chess_board - 1:
            while True:
                # check diagnoal up right ( decrease x , increase y)
                x -= 1
                y += 1
                check_queen = [x, y]
                if check_queen in queens:
                    return False
                if x == 0:
                    break
        if x != 0 and y != 0:
            x = queen[0]
            y = queen[1]
            while True:
                # check diagnoal up left ( decrease x , decrease y)
                x -= 1
                y -= 1
                check_queen = [x, y]
                if check_queen in queens:
                    return False
                if x == 0:
                    break

        if x != chess_board - 1 and y != chess_board - 1:
            x = queen[0]
            y = queen[1]
            while True:
                # check diagnoal down right ( increase x , increase y)
                x += 1
                y += 1
                check_queen = [x, y]
                if check_queen in queens:
                    return False
                if x == chess_board - 1:
                    break
        if x != chess_board - 1 and y != 0:
            x = queen[0]
            y = queen[1]
            while True:
                # check diagnoal down left ( increase x , decrease y)
                x += 1
                y -= 1
                check_queen = [x, y]
                if check_queen in queens:
                    return False
                if x == chess_board - 1:
                    break
        return True


def main ():
    """ main func"""
    # If the user called the program with the wrong number of arguments,
    # print Usage: nqueens N, followed by a new line,
    # and exit with the status 1
    # if len(argv) != 2:
    #     print("Usage: nqueens N")
    #     exit(1)

    # # handle n cases:
    # if not argv[1].isdigit():
    #     print("N must be a number")
    #     exit(1)
    # # n -> number of queens
    # n = int(argv[1])
    # if n < 4:
    #     print("N must be at least 4")
    #     exit(1)

    n = 4
    row = 0
    outer_row = 0
    colm = 0
    while (len(queens) != 4):
        row = outer_row
        while (row < n):
            while (colm < n):
              queen = [row, colm]
              # if the queen  not under attack
              # move to the nex column
              if check_constrains(queen, n):
                  queens.append(queen)
                  break
              else:
                  colm += 1
            row += 1
        print (queens) 
        outer_row += 1



if __name__ == "__main__":
     main()
