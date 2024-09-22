#!/usr/bin/python3
"""
Main file for function
"""


def makeChange(coins, total):
    '''function for change
    Return: fewest number of coins needed to meet total
    '''
    # handle total edge cases
    if total <= 0:
        return 0
    count = 0
    # sort the list in descending order
    coins.sort(reverse=True)
    for coin in coins:
        # subtrct the same coin till its less than total
        while total >= coin:
            total -= coin
            count += 1
    return count
