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
    # Write your code here
    diagonal1 = 0
    diagonal2=0
    a=0
    b=0
    for i in arr:
        for j in i:
            if b < n:
                pass
        diagonal1+=i[b]
        a+=1
        b+=1

    a=n-1
    b=n-1
    for i in arr:
        for j in i:
            if b == 0:
                pass
        diagonal2+=i[b]
        a-=1
        b-=1
    
    result = abs(diagonal1-diagonal2)
    print (result)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input('introduzca').strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
