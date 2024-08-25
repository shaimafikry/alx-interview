#!/usr/bin/python3
"""
Main file for func
"""


def validUTF8(data):
    """method that determines if a given data set
      represents a valid UTF-8 encoding.
    Return: True if data is a valid UTF-8 encoding,
            else False
"""
    for i in data:
        temp = bin(i)
        # del the 0b at first
        temp = temp[2:]
        # print(len(temp))
        # to check if its one byte or two (more than 8 bits)
        if temp[0] == '1':
            if len(temp) < 9:
                continue
            else:
                if len(temp) == 9:
                    # to check for 10xxxxxx 10xxxxxx
                    if temp[8] == '1':
                      if temp[9] == '1' or temp[9] == 0:
                        continue
                    else:
                        return False
    return True
