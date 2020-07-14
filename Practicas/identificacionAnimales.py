# practica identificacion de aninales


sonido = ('Grr Grr Guau Ssss Prig nooo')

lista= sonido.split()

record= { 'Grr':'Lyon', 'Guau':'Dog', 'Ssss':'Snake', 'Prig':'Twitter' }
lista2=""

for i in lista:
	for y in record:
		if i == y:
			lista2 += record[y]	
			lista2 += " "		
 			#print (record[y])

print(lista2)



