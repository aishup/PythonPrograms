#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    arrL = list(arr)
    positiveVal,negativeVal,zeroVal = 0,0,0
    for i in arrL:
        if i > 0:
            positiveVal +=1        
        elif i < 0:
            negativeVal +=1
        else:
            zeroVal +=1
    print("%.6f" % (positiveVal/len(arrL)))
    print("%.6f" % (negativeVal/len(arrL)))
    print("%.6f" %(zeroVal/len(arrL)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = map(int, input().rstrip().split())

    plusMinus(arr)