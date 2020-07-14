numero = int(input())
matriz1 =list(map(int, input().split()))
matriz2= list(map(int, input().split()))

x = 0
w = 0
media_ponderada = 0

for i, j in  zip(matriz1,matriz2):
    x += i*j
    w += j

media_ponderada = x / w

print (media_ponderada)

### OPCION 2 #####

print(format((sum(p*q for p,q in zip(x,w)))/sum(j for j in w),'.1f'))

