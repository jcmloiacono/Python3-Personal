import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    global n
    res=0
    a=0
    b=1
    i=0
    while n !=0:
        res=arr[a]+arr[b]
        print (res)
        a+=2
        b+=2
        n-=2

if __name__ == '__main__':
    n = int(input())

    arr = [-4, 3, -9, 0, 4, 1 ]

    plusMinus(arr)
