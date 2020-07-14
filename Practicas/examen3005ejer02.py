import random
'''Quizás Jack Aubrey, durante su encierro en Boston, pudo pasar las horas muertas 
jugando solitarios con los dados. Uno de estos solitarios consiste en elegir tres valores 
tirar una cantidad de dados y contar los dados obtenidos de esos tres valores. Si se han 
obtenido más de la mitad de los dados lanzados, se ha ganado.

Escriba un programa que simule una partida de este solitario. El programa dejará elegir 
al jugador valores repetidos o fuera del intervalo del 1 al 6 (el jugador se está perjudicando 
a sí mismo, porque le será más difícil ganar).'''

print ("JUEGO DE DADOS: TRES VALORES")

valor1 = int(input("Elija un valor del 1 al 6:"))
valor2 = int(input("Elija otro valor del 1 al 6:"))
valor3 = int(input("Elija otro valor del 1 al 6:"))

d= True
while d == True:
    dados = int(input("¿Cuántos dados quiere tirar?"))
    if dados < 1:
        print("¡Imposible!")
    else:
        d= False


dados_final = dados
lista=""
cont=0
puntoganador =0

while dados > 0:
    cont = 0
    cont = random.randrange(1,7)
    lista += str(cont)
    dados -= 1

lista2=list(lista)

for i in lista2:
    if str(valor1) in lista2:
        puntoganador +=1
        lista2.remove(str(i))
    elif str(valor2) in lista2:
        puntoganador +=1
        lista2.remove(str(i))
    elif str(valor3) in lista2:
        puntoganador +=1
        lista2.remove(str(i))

if puntoganador > (dados_final/2):
    print ("Ha sacado {} dados de los valores elegidos. Ha ganado.".format(puntoganador))
elif puntoganador == (dados_final/2):
    print ("Ha sacado {} dados de los valores elegidos. Ni ha ganado ni perdido.".format(puntoganador))
else:
    print("Ha sacado {} dados de los valores elegidos. Has perdido.")

