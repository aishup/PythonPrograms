#!/bin/python

import math
import os
import random
import re
import sys


import math
#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    arr.sort()
    #print(arr)
    arrLen = len(arr)
    medianVal = math.floor(arrLen/2)
    medianVal = int(medianVal)
    #print(medianVal)
    return arr[medianVal]

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)
