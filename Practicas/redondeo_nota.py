#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

# forma compacta return [ i if (i < 38 or i % 5 < 3) else (i + (5 - i%5)) for i in grades]


def gradingStudents(grades):
    # Write your code here
    lista=[]
    for i in grades:    
        if int(i) < 38:
            lista.append(int(i))
        else:

            redondeo = int(i) +2
            if redondeo % 5 == 0:
                lista.append(redondeo)
            else:
                lista.append(int(i))

    print( lista)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = 10

    grades = ['60','64','24','68','14','53','49','45','99','55','24']

    # for _ in range(grades_count):
    #     grades_item = int(input().strip())
    #     grades.append(grades_item)

    result = gradingStudents(grades)

    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
