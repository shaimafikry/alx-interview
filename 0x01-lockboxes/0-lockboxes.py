#!/usr/bin/python3
"""
  module for the functon (canUnlockall)
"""


def canUnlockAll(boxes):
    """_summary_
        method that determines
        if all the boxes can be opened.
    Args:
        boxes (list): list of lists
    Return:
        boolen: true if all opened
                false if not
    """
    # edge cases
    if len(boxes) == 1:
        return True
    # get the list length
    n = len(boxes)
    # have first keys as a start
    # make a deep copy of the orginal list
    keys = boxes[0][:]
    # get the keys based on index
    for i in range (1, n):
        # check for i in existing keys
        if i in keys:
            keys += boxes[i]
    for i in range(1, n):
        # check if i in the list of keys
        if i not in keys:
            return False
    return True
