a = [1,6,3]
b= [4,6,1]


punto_a=0
punto_b=0

for i, j in zip(a,b):
    if i > j:
        punto_a +=1
    elif j> i:
        punto_b +=1
print (punto_a, punto_b)



punto_a=0
punto_b=0
for i ,j in zip(a,b):
    if a > b:
        punto_a +=1
    elif b > a:
        punto_b +=1
print (punto_a, punto_b)

