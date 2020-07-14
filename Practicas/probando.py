'''Generar una lista de 50 números aleatorios.

Dada la lista, mostrar en pantalla todos los números mayores a 50 pares.'''

import random

num = 0
lista = []
cont = 0

while cont < 10:
    cont+=1
    num = random.randint(1,1000)
    if num%2 == 0:
        lista.append(num)


print (lista)