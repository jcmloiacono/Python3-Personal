import math
from math import sqrt

n = 15000
s = 0
p1 = 0

while n >= 1:
    n-=1
    s=s+1/pow(n+1 , 2)

pi = math.sqrt(6*s)

print('Valor de pi con 2 Decimales: {0:.2f}'.format(pi))
print('Valor de pi con 6 Decimales: {0:.6f}'.format(pi))


print ('Valor de pi con 6 Decimales: {0:.6f}'.format(math.pi))