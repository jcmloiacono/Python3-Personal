import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    
    ''' aqui ya logro ver si esta el primer y segundo 0 iguales, y luego entrar en el for
    falta que en el for comience  a hacer las verificaciones'''
    salto = 0
    if c[0]==c[1] and c[2]== 0:
        salto+=1
        c.pop(0)
        c.pop(0)
        
    for i in c:
        if i != 1:
            salto+=1

    print (salto-1)
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 7

    c = [0, 0, 1, 0, 0, 1, 0]

    result = jumpingOnClouds(c)

    #fptr.write(str(result) + '\n')

    #fptr.close()
