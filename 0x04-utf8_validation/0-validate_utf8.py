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
        # del the 0b at first and fill 0
        temp = temp[2:].zfill(8)
        # print(len(temp))
        # print(temp)
        if temp[0] == '0':
            continue
        # check for squences
        elif temp.startswith('110'):
            # means 2 seq
            # check for the sec seq
            if temp[8:].startswith('10'):
                continue
            else:
                return False
        elif temp.startswith('1110'):
            # means 3 seq
            # check for the sec seq
            if [temp[8:10], temp[16:18]] == ['10', '10']:
                continue
            else:
                return False
        elif temp.startswith('11110'):
            # means 4 seq
            # check for the sec seq
            if [temp[8:10], temp[16:18], temp[32:34]] == ['10', '10', '10']:
                    continue
            else:
                return False
        else:
          return False
    return True
