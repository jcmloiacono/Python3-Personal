# import math

# def area(radio):
#     global area 
#     area= math.pi*(radio**2)
#     print ( area)
    
# def inverted(nombre):
#     print (nombre[::-1])

# def area_triangulo(base, altura):
#     area= (base*altura)/2
#     print (area)

# valor_cambio=math.pi
# print ("el valor de pi con 2 decimales es %.2f" %valor_cambio)

# area(float(input ("introduzca el radio para calcular el area ")))
# inverted(str(input("Introduzca su nombre ")))

# base =float(input("Introduzca el tamaño de la base : "))
# altura = float(input("Introduzca la altura del triangulo : "))

# area_triangulo(base, altura)

# conjunto = {'Aceituna', 'Aceituna', 'Mandarina', 'Naranja'}

# lista= 'a,b,c,d,e,f,g,a,a,a,a'
# lista.split(",")
# print (lista)
# lista2 = {lista}
# # print (conjunto)
# print (lista2)


# convertir una lista a una tupla

lista= ['a','b','c','d','e','c','d','e']
tupla = tuple(lista)

print (type(tupla))
print (tupla)

# invertir el contenido de una tupla
print (tupla [::-1])


# crear seleccion de una lista con slising

print (tupla [2:])

# eliminar elemento de una tupla

tupla = list(tupla)
tupla.remove("a")
print (tupla)

# remover elementos duplicados de una lista

print (set(lista))

# Encontrar palabras en una lista  que tienen al menos 5 caracteres

lista2 = ["palabras", "arbol","palabras", "arbol" "amanecer", "ara"]
lista4 = ["palabras", "arbol","palabras", "arbol" "amanecer", "ara"]

resultado =[]
for i in lista2:
    if len(i) >= 5:
        resultado.append(i)
print (resultado)

# SOLUCION 2 CON LISTA POR COMPRENCION

resultado = [i for i in lista4 if len(i)>=5]

print (resultado)


# #seleccionar de forma aleatoria elemento de una lista
import random
n = random.randrange(len(lista2))

print (lista2[n])

# calcular la cantidad de ocurrencias que hay en una lista 
lista2 = ["palabras", "arbol","palabras", "arbol" ,"amanecer", "ara"]
for i in set(lista2):
    print ("la palabra", i, " esta ", lista2.count(i))
    
# opcion 2
from collections import Counter

contador_peteciones = Counter(lista2)
print (contador_peteciones)
    

#F2 Para refactorizar

# sumar todos los valores de un diccionario 

diccionario = {"a":2, "b":3, "c":6}

suma = sum(diccionario.values())
print (suma)

#reversed en tuplas 
lista3 = ('a','b','c','d','e','c','d','e')
lista3 = tuple(reversed(lista3))

print (lista3)
dic= {}
for i in range(len(lista3)):
    addic = {i:lista3}
    dic.update(addic)
    
print (dic)


# remover todos los elementos duplicados de un diccionario

# opcion 1
diccionario3 = {"a":2, "b":3, "c":6,"a":2, "b":3, "c":6,"a":2, "b":3, "c":6}


diccionario2=set(diccionario3)

print ("este es el resultado del diccionario sin repeticiones",diccionario3)

#opcion 2
diccionario4 = {"a":2, "b":3, "c":6,"a":2, "b":3, "c":6,"a":2, "b":3, "c":6}
diccionario_sr= {}
for i, v in diccionario4.items():
    if i not in diccionario_sr:
        diccionario_sr[i] = v

print (diccionario_sr)


# encontrar 3 valores mayores en el diccionario
from heapq import nlargest

diccionario5 = {"a":2, "b":3, "c":6,"d":7, "e":1, "f":9,"g":12, "h":43, "i":6}
diccionario_max={}

diccionario_max = nlargest(3, diccionario5, key=diccionario5.get)


print ("Estos son los mayores de la lista", diccionario_max)

# ejercicios de conjuntos

#realizar operacion de interseccion de conjuntos

numeros = {5,6,3,2,1,4}
numeros2 = {9,8,4,5,6,7}

resultado = numeros.union(numeros2)


print (resultado)

# diferencia entre dos conjuntos

escritorio= {'escritorio', 'mesa', 'sillas', 'recetas' }
portatil = {'escritorio', 'casa', 'mesa', 'cama', 'juegos'}

resultado = escritorio.difference(portatil)

print ('los programas que hacen falta en el computador portatil son:' , resultado)


# diferencia simetrica  entre dos conjuntos

escritorio= {'escritorio', 'mesa', 'sillas', 'recetas' }
portatil = {'escritorio', 'casa', 'mesa', 'cama', 'juegos'}

resultado = escritorio.symmetric_difference(portatil)

print (resultado)
