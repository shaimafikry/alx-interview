# 0x04. UTF-8 Validation

# Task:
Write a method that determines if a given data set represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
# plan:
1 - loop through the list
2- turn the int inot binary by using bin()
3- remove first 22 letters tha defines binary (0b)
4- checks for the first bit if its 1 or not
5- if its 1 , check the length of bits (if a num is greater than 1 byte it would give more that 8 bits)
6- checking length only takes the possiblities of only another group since the tassk said its only 1 byte
