print ("LAS MISMAS CIFRAS")

numero1 = (input("Escriba un número positivo menor que 1000: "))
if int(numero1) > 1000 or int(numero1) < 0:
    print ("¡No ha escrito un número positivo menor que 1000 ni mayor de 0")

numero2 = (input("Escriba un número positivo menor que 1000: "))
if int(numero2) > 1000 or int(numero2) < 0:
    print ("¡No ha escrito un número positivo menor que 1000 ni mayor de 0")

lista=list(numero1)
lista2=list(numero2)



if len(numero1) < 3:
    print ("Las cifras del primer número son, {} y {}.".format(lista[0],lista[1]))
elif len(numero1)<2:
    print ("Las cifras del primer número son, {} y {}.".format(lista[0]))
else:
    print ("Las cifras del primer número son {}, {} y {}.".format(lista[0],lista[1],lista[2]))


if len(numero2) < 3:
    print ("Las cifras del primer número son, {} y {}.".format(lista2[0],lista2[1]))
elif len(numero2)<2:
    print ("Las cifras del primer número son, {} y {}.".format(lista2[0]))
else:
    print ("Las cifras del primer número son {}, {} y {}.".format(lista2[0], lista2[1], lista2[2]))

cont=0
cont2=0
for i in numero1:
    if len(numero1) == len(numero2):
        if i in numero2:
            cont+=1
        else:
            cont2+=1

if cont == 3:
    print ("¡Son las mismas cifras!")
else:
    print ("¡Las cifras son distintas!")