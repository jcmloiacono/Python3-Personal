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

def gradingStudents(grades):
    # Write your code here
    lista=[]
    for i in grades:    
        if int(i) < 38:
            lista.append(i)
        else:

            redondeo = int(i) +2
            if redondeo % 5 == 0:
                lista.append(redondeo)
            else:
                lista.append(i)

    print( lista)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = 10

    grades = ['60','64','24','68','14','53','49','45','99','55','24',
            '59','67','8','76','37','24','24','73','81','37','47','63',
            '99','63','40','54','82','9','80','84','15','32','51','18',
            '70','4','86','59','32','68','22','1','71','51','81','22',
            '35','65','9','17','94','69','40','39','52','94','84','13',
            '68','95']

    # for _ in range(grades_count):
    #     grades_item = int(input().strip())
    #     grades.append(grades_item)

    result = gradingStudents(grades)

    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
