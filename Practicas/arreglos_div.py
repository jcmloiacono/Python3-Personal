#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    global n
    res=0
    negativo =0
    positivo=0
    cero =0
    for i in arr:
        if i < 0:
            negativo+=1
        elif i> 0:
            positivo+=1
        else:
            cero+=1
    
    print ( positivo / n)
    print (negativo/n)
    print (cero/n)
            

if __name__ == '__main__':
    n = 6

    arr = [-4, 3, -9, 0, 4, 1 ]

    plusMinus(arr)
