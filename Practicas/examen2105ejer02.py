import random

'''Quizás Jack Aubrey, durante su encierro en Algeciras, pudo pasar las horas muertas 
jugando solitarios con los dados. Uno de estos solitarios consiste en tirar una cantidad 
de dados y sumar los puntos de los dados en los que se obtiene el mismo valor. La puntuación 
obtenida es el valor más alto.

Escriba un programa que solicite el número de dados lanzados y muestre los valores de los 
dados e indique la puntuación obtenida.'''

dados = int(input("¿Cuántos dados quiere tirar? "))
if dados <= 0:
    print("Debe tirar al menos un dado! ")

lista=[]
lista_nueva =[]

repetido = ""
norepetido = ""

while dados > 0:
    resultados= str(random.randrange(1,7))
    print("DADO No.",dados, "= {}".format(resultados))
    dados-=1
    lista.extend(resultados)

numero6=0
numero5=0
numero4=0
numero3=0
numero2=0
numero1=0

for i in lista:

    if i == "6":
        numero6 += int(i)
    elif i == "5":
        numero5 += int(i)
    elif i == "4":
        numero4 += int(i)
    elif i == "3":
        numero3 += int(i)
    elif i == "2":
        numero2 += int(i)
    elif i == "1":
        numero1 += int(i)

lista_nueva = (numero1,numero2,numero3,numero4,numero5,numero6)
maximo= max(lista_nueva)

print (maximo)