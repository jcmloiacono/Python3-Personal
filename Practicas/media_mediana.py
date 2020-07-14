cant = (input())
cant= int(cant)
lista=['64630', '11735' ,'14216' ,'99233' ,'14470','4978', '73429', '38120', '51135', '67060']
lista_sumada = 0
lista_num=[]
media=0
mediana= 0

for i in lista:
    lista_sumada+=int(i)
    lista_num.append(int(i))

lista_num.sort()

media = lista_sumada/cant

x = round(cant/2)

mediana = (lista_num[x]+lista_num[x-1])/2

print (media)
print(mediana)
print (min(lista_num))