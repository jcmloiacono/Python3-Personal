import random
'''Marcus Cubitus y Julius Humerus, legionarios y legendarios aficionados a 
los juegos de dados, prueban un nuevo juego. 
El juego consiste en tirar un dado hasta que se obtengan dos valores iguales seguidos. 
El valor repetido es la puntuación obtenida por el jugador. El jugador que obtenga el valor 
más alto, gana. Escriba un programa que simule una partida de este juego.'''

print ("JUEGO DE DADOS: HASTA REPETIR")


dados1=""


a = False
while a == False:
    jugador1 = str(random.randint(1,6))
    if jugador1 != dados1[-1:]:
        dados1 += " " + jugador1
    else:
        dadomayor1 =  int(jugador1)
        dados1 += " " + jugador1
        print ("Tirada de Cubitus:", dados1)
        a = True

dados2=""
a = False
while a == False:
    jugador2 = str(random.randint(1,6))
    if jugador2 != dados2[-1:]:
        dados2 += " " + jugador2
    else:
        dadomayor2 =  int(jugador2)
        dados2 += " " + jugador2
        print ("Tirada de Humerus:", dados2)
        a = True

if dadomayor1 > dadomayor2:
    print ("Ha ganado Cubitus.")
elif dadomayor1 < dadomayor2:
    print ("Ha ganado Humerus.")
else:
    print ("Han Empatado!!")