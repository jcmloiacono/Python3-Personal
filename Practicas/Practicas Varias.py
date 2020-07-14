'''
Created on 7 nov. 2019

@author: jean
'''
from _ast import Pass
import random

list=[] 
for i in range(5)[::-1]:
    list.append(i)
print (list[1])


0,1,2,3,4

try:
    s=['a','c']
    n=[0,2]
    s[1:1]='b'
    n[1:1]=1
except:
    pass
    print(s[1],n[1])

print("Vamos a Jugar Loteria")
for i in range(0,2):
    x=random.randint(0,5)
if x==3:
    print(x,"tu has ganado la loteria")
else:   
    print(x,"Tu has perdido") 
    
    
a=[0,1,0]
b=[1,1,0]
s=0
for x in(a,b,a):
    s+=x.count(1)
    print (s)