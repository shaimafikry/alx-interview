#!/usr/bin/python3
'''script that reads stdin line by line and
computes metrics
'''
import sys
line = 'hello'
s_line = line.split(' ')
# print(s_line)
# <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
# <status code> <file size>
print(len(s_line))
