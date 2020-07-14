''' Escriba un programa que pida tres números y escriba cuál está en medio de los otros dos'''

a = 0


while a == 0:
    numero1=int(input("Escriba un número entero: "))
    a +=1

    while a == 1:
        numero2 = int(input("Escriba otro número entero distinto a {} :".format(numero1)))

        if numero2 == numero1:
            print("Debe ingresar un numero distinto a {} ".format(numero1))
            a = 1
        else:
            a +=1

    while a == 2:
        numero3 = int(input("Escriba otro número entero distinto a {} o {}:".format(numero1,numero2)))

        if numero3 == numero1:
            print("Debe ingresar un numero distinto a {} o {} ".format(numero1,numero2))
            a = 2
        elif numero3 == numero2:
            print("Debe ingresar un numero distinto a {} o {} ".format(numero1,numero2))
            a = 2
        else:
            a=3

print ("Todo ha salido bien procederemos a realizar los calculos")

mayor=0
menor=0
medio=0

lista=(numero1,numero2,numero3)

for i in lista:
    if i == max(lista):
        mayor = i
    elif i == min(lista):
        menor = i
    else:
        medio = i

print ("El numero {} esta entre {} y {}".format(medio, menor, mayor))