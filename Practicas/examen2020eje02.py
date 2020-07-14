#Escriba un programa que pida tres números distintos, de manera que el segundo sea múltiplo 
# del primero y el tercero sea divisor del segundo. El programa avisará al usuario cuando no 
# se cumplan las condiciones solicitadas.

numero1 = int(input("Escriba un número entero positivo \n>"))
numero2 = int(input("Introduzca un numero multiple de {} \n>".format(numero1)))

if numero2 < 0:
    print("¡No ha escrito un número entero positivo!")

if numero2 < numero1:
    print ("¡El múltiplo debe ser mayor que {}!".format(numero1))

numero3 = int(input("Escriba un divisor de {} distinto de {}\n>".format(numero2, numero1)))

if numero3 == numero1:
    print("¡Le he pedido un número distinto de 20!")
elif numero3 > numero2:
    print("¡El divisor debe ser menor que 100!")

if numero3%2 >= 1:
    print("¡Gracias por su colaboración!")
else:
    print ("{} no es divisor de {}!".format(numero3, numero2))


