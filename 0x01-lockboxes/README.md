# Lockboxes
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False


# My attemps

- get the list length as n
- check for edge case => list of 1 length
- get the first keys as a start
- define a set to hold the opend boxes (unique values)
- loop through the keys
- check if i in keys within the range of n
- add the i to the opened boxes
- loop through the values of boxes[i] to add a new keys
- make sure that the key isnt repeated in list
- check the len of opend boxes and return the value

# problems faced

الحمدلله, that one was easy. (said that too early >_<)
- tried to choose something tht can hold a unique values from the start
instead od if condtions ( alot of) so i used set for the opened boxes
- faced a problem to do the same for keys, an error called ( set size changed during itrabling) so i had to make it a list with an if condtion to make the value unique
