# N QUEENS

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

Usage: nqueens N
If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
The program should print every possible solution to the problem
One solution per line
Format: see example
You don’t have to print the solutions in a specific order
You are only allowed to import the sys module

# Concepts Needed:
Backtracking Algorithms:

Understanding how backtracking algorithms work to explore all potential solutions to a problem and backtrack when a solution cannot be completed.
Backtracking Introduction
Recursion:

Using recursive functions to implement backtracking algorithms.
Recursion in Python
List Manipulations in Python:

Creating and manipulating lists, especially to store the positions of queens on the board.
Python Lists
Python Command Line Arguments:

Handling command-line arguments with the sys module.
Command Line Arguments in Python


``` in chess concept ```

To solve the N Queens problem, you need to place N queens on an N×N chessboard such that no two queens can attack each other. This means that no two queens can be placed in the same row, column, or diagonal.

# SOLVE
N  -> represents the numer of queens
result ->  every solution in a line
