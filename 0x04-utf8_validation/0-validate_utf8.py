#!/usr/bin/python3
"""
Main file for func
"""
# data = [125, 125, 545, 458] represent the 4 bytes


def validUTF8(data):
    """method that determines if a given data set
      represents a valid UTF-8 encoding.
    Return: True if data is a valid UTF-8 encoding,
            else False
"""
    seq_left = 0
    for i in data:
        # del the 0b at first and fill 0
        temp = format(i, '#010b')[-8:]
        # case one seq
        if seq_left == 0:
            if temp.startswith('0'):
                continue
            # check for squences
            if temp.startswith('110'):
                # case 2
                seq_left = 1
            elif temp.startswith('1110'):
                # case 3
                seq_left = 2
            elif temp.startswith('11110'):
                # case 4
                seq_left = 3
            else:
                # case not 0 or 110 1110 11110
                return False
        # check if the next bin eqaul 10
        else:
            if not temp.startswith('10'):
                return False
            # if true delete one
            seq_left -= 1
    # if the seq left == 0 means all bytes meats the criteria
    return seq_left == 0
