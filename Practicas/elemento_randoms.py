import random

lista =['Eduardo', 'Raquel', 'Roberto', 'Marines', 'Isabel']
numero = 0

for i in range(len(lista)):
    numero_lista=len(lista)
    numero+=1
    n= random.randrange(numero_lista)
    x = lista[n]
    lista.pop(n)
    print (numero,"-", x)

##### SEGUNDA OPCION #####



if __name__ == '__main__':
    usuarios = ['Eduardo', 'Raquel', 'Roberto', 'Marines', 'Isabel']

    random.shuffle(usuarios) ## shuffle desorganiza la lista

    for posicion, usuario in enumerate(usuarios):
        print(f'{posicion + 1} - {usuario}')