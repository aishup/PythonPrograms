#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    arrPSum,arrSSum,i = 0,0,0
    arrLen = len(arr) 
    while i < arrLen:
        arrPSum += arr[i][i]
        i+=1
    i = 0
    while arrLen > 0:
        arrLen -=1
        arrSSum += arr[i][arrLen]
        i+=1
    #print(arrSSum)
    print(arrPSum)
    print(arrSSum)
    arrSum = abs(arrPSum-arrSSum)
    return arrSum
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)