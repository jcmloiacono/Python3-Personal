'''Definir una función la cual nos permita conocer cuantos dígitos posee un número.

La función debe tener por nombre cantidad_digitos.
La función debe poseer el parámetro numero.
La función debe retornar la cantidad de dígitos del parámetro.
No es posible utilizar la función str.
Ejemplos

>>> cantitdad_digitos(10)
2

>>> cantitdad_digitos(2019)
4

>>> cantitdad_digitos(1234567890)
10'''


def cantidad_digitos(numero):
    cont=1
    while numero >1:
        cont+=1
        numero = numero // 10
    print (cont)

cantidad_digitos(123456789)