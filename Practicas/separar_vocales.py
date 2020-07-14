vocales = ['a','e','i','o','u']
l1=[]
l2=[]
l3 =[]
 
s1 = str(input("introduce la primera palabra: "))
s2 = str(input("introduce la segunda palabra: "))


for v in s1:
    if v in vocales:
        l1.append(v)

for c in s2:
    if c not in vocales:
        l2.append(c)


for i,j in zip(l1,l2):
    l3.append(i)
    l3.append(j)

print (l1)
print (l2)
print (l3)


