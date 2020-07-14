import time

nombre=input("¿Cual es tu Nombre: ")
print ("Hola " +nombre, " Vamos a Jugar el Ahorcado")
print (" ")

time.sleep(1)
print ("Comienza a adivinar")
time.sleep(0.5)

palabra="venezuela"

tupalabra=""
vidas=5

while vidas>0:

    fallas=0
    for letra in palabra:
        if letra in tupalabra:
            print(letra, end="")
        else:
            print("*",end="")
            fallas+=1
    if fallas==0:
        print(" Felicidades has Ganado")
        break

    tuletra=input("Intruduce una Letra: ")
    tupalabra+=tuletra

    if tuletra not in palabra:
        vidas-=1
        print("Esta letra no esta en la Palabra")
        print("Te Quedan ", + vidas, " Vidas")
    if vidas==0:
        print("Has Perdido, la Palabra era: " +palabra)
    else:
        print("Proxima Letra")

