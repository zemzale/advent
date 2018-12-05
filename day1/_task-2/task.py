#!/usr/bin/env python

inputFile = open("puzzle-input", "r")
resultThings = []
results = []
lastRes = 0
i = 0

# Need to calculate number and then compare to all the numbers in the saved array
for num in inputFile:
    resultThings.append(num)


while True:
    for num in resultThings:
        if num[0] == "+":
            lastRes = lastRes + int(num[1:])
        else:
            lastRes = lastRes - int(num[1:])

        if lastRes in results:
            print lastRes
            exit()
        results.append(lastRes)


