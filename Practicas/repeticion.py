#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    # result=''
    # cont = n

    # if len(s) <= 1:
    #     print (n)
    # else:
    #     while cont > 0:
    #         for j in s:
    #             if len(result) == n:
    #                 break
    #             else:
    #                 result+=j 
    #                 cont-=1
    #     print (result.count('a'))
    #s, n = input().strip(), int(input().strip())
    print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    # fptr.write(str(result) + '\n')

    # fptr.close()
