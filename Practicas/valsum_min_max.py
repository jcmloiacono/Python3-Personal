#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    maxi=0
    mini=0
    
    for i in arr[1:]:
        maxi+=int(i)
       
    for j in arr[:-1]:
        mini += j
     
    
    print(mini, maxi)
if __name__ == '__main__':
    arr = [7, 69, 2, 221, 8974]

    miniMaxSum(arr)
    
