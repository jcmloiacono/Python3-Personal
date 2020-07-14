import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    
    for i in range(n):
        i+=1
        print (' '*(n-i),end='#'*i +'\n')
        
    

if __name__ == '__main__':
    n = int(input())

    staircase(n)
