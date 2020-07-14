'''Jack Aubrey, al que algunos imaginan descendiente lejano de Marcus Cubitus o de
Julius Humerus, prefirió hacer carrera en la Armada británica antes que en el ejército.
Una de las primeras cosas que tuvo que aprender fue el a menudo impreciso sistema de unidades
naúticas.

Escriba un programa que convierta una cantidad de centímetros en millas naúticas,
cables y brazas (con un decimal). Este programa no tendrá en cuenta la opinión de Jack Aubrey 
sobre el sistema métrico, que como mínimo podría ser considerada como escéptica.

Se recuerda que aproximadamente una braza son 182,91 cm, un cable son 100 brazas y 
una milla naútica son 10,125 cables.'''

print ("CONVERTIDOR DE CENTÍMETROS EN MILLAS NAÚTICAS, CABLES Y BRAZAS")


centimetros= float(input("Escriba la cantidad de centímetros : "))

if centimetros <= -1:
    print("Por favor, escriba un número positivo.")
else:
    braza = centimetros/182.91
    cable = int(braza/100)
    milla_nautica= int(cable/10.125)
    

    print('{} cm son {} milla nautica, {} cables y {} brazas'.format(centimetros, milla_nautica, cable, braza))