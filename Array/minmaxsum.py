#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sumVal = 0
    sumArr = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                sumVal += arr[j]
        sumArr.append(sumVal)
        sumArr.sort()
        sumVal = 0
    print(min(sumArr),end=" ")
    print(max(sumArr)) 
            

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
