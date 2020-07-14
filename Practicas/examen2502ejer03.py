''' Escriba un programa que pida tres números y escriba cuál es mayor.'''

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

if (numero1>numero2>numero3):
    print ("El Mayor numero es el primer numero {}".format(numero1))
elif (numero2>numero1>numero3):
    print ("El Mayor numero es el segundo numero {}".format(numero2))
else:
    print ("El Mayor numero es el tercer numero {}".format(numero3))