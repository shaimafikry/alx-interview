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
        boolen: 
    """
	  n = len(boxes)
	  keys = boxes[0][:]
	  for i in range (1, n):
	    if i in keys:
	      keys += boxes[i]
	    else:
	      return False	      
	  return True
	    
