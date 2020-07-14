import math

numero = int(input())
lista= list(map(int, input().split()))

lista.sort()

q1= (lista[1]+lista[2])//2
q2= math.floor(numero//2)
q3= (lista[-2]+lista[-3])//2

print (q1)
print (lista[q2])
print (q3)


##### OTRA OPCION IMPORTANDO NUMPY ######

import statistics as s

n = input()

num = sorted(list(map(int, str.rsplit(input(), " "))))
midpoint = int(n)//2

print(int(s.median(num[:midpoint])))
print(int(s.median(num)))
print(int(s.median(num[-midpoint:])))
