#Generador de números pares del 1 al 100
def generador_de_pares():
    for number in range(2, 102, 2):
        yield number

for number in generador_de_pares():
    print(">>>", number)

