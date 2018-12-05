#!/usr/bin/env python

inputFile = open("puzzle-input", "r")
res = 0

for num in inputFile:
    if num[0] == "+":
        res = res + int(num[1:])
    else:
        res = res - int(num[1:])

print res
