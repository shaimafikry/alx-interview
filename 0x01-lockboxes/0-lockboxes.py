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
    # get the list length
    n = len(boxes)
    # edge cases
    if n == 1:
        return True
    # have first keys as a start
    # make a deep copy of the orginal list
    keys = boxes[0][:]
    # to hold opened boxes
    opened = set([0])
    for i in keys:
        # check if the key is in range
        if i < n:
            # if the box opened
            opened.add(i)
            for x in boxes[i]:
                # add only unique values
                # to prevent infinity loop
                if x not in keys:
                    keys.append(x)
    # check if all boxes opened
    if len(opened) == n:
        return True
    return False
