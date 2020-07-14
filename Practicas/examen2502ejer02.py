'''Escriba un programa que pida una cantidad de dinero a pagar y el número de 
billetes de 200 y 100 € entregados y que responda cuánto dinero sobra o falta.'''


billete100=-1
billete200=-1
pagar = 0
vuelto= 0


while pagar <= 0:
    pagar=int(input("Introduzca el monto a pagar: \n>"))
    if pagar <=-1:
        print("Ha indicado una cantidad negativa.")

while billete200 < 0:
    billete200 = int(input("¿Cuántos billetes de 200 € entrega?"))
    if billete200 >= 0:
        billete200 *=200
    else:
        print ("Ha indicado una cantidad negativa.")

while billete100 < 0:
    billete100 = int(input("¿Cuántos billetes de 100 € entrega?"))
    if billete100 >= 0:
        billete100 *=100
    else:
        print ("Ha indicado una cantidad negativa.")

vuelto = billete100+billete200

if vuelto > pagar:
    vuelto -= pagar
    print ("Su vuelto es {}¢".format(vuelto))

elif vuelto < pagar:
    pagar = abs(pagar - vuelto)
    print ("todavia me debe {}¢".format(vuelto))

else:
    print ("Ha entregado la cantidad exacta.")
