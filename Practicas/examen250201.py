
dinero = int(input("Escriba una cantidad de dinero (múltiplo de 100)" ))

b5=0
b2=0
b1=0
resultado=0

if dinero%100 != 0:
    print ("No ha indicado una cantidad múltiplo de cien.")
else:

    resultado = int(dinero/100)


    while resultado >= 5:
        b5 +=1
        resultado -= 5
        if resultado/ 2 >= 5:
            pass
    while resultado >= 2:
        b2 +=1
        resultado -= 2
        if resultado/ 2 >= 2:
            pass
    while resultado >=1:
        b1 =+ 1
        resultado -= 1
        if resultado / 2 >= 1:
            pass

    print ("para pagar {} es necesario {} billetes de 500, {} billetes de 200 y {} billete de 100".format(dinero, b5, b2, b1))
