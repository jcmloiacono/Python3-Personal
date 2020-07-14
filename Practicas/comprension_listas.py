#comprension de listas


# tradicionalmente

lista =[]
for letra in 'casa':
	lista.append(letra)
print(lista)

#Metodo con comprension

lista = [letra for letra in 'Casa']
print (lista)

# ********************************+
# ejemplo Potencia de 2

# tradicionalmente

lista= []
for numero in range(0,11):
	lista.append(numero**2)
print(lista)

# Metodo con comprension

lista =[numero**2 for numero in range(0,11)]
print (lista)

# Lista con multiple de 2 de 0 a 10

# Metodo Tradiconal

lista= []
for numero in range(0,11):
	if numero % 2 == 0: 
		lista.append(numero)
print (lista)

# Metodo con Comprension

lista=[numero for numero in range(0,11) if numero % 2 == 0]
print(lista)

# Metodo Tradiconal
# buscar los numeros pares a partir de la potencia de 2

lista= []
for numero in range(0,11):
	if numero % 2 == 0: 
		lista.append(numero)
pares =[]
for numero in lista:
	if numero % 2 == 0: 
		lista.append(numero)
print (pares)

# Metodo con Comprension

lista =[numero for numero in range(0,11) if numero %2 == 0]
pares =[ numero for numero in lista if numero %2 == 0]
print("estos son los pares",pares)

# METODO COMPRENSION MAS REDUCIDO

pares=[ numero for numero in [numero**2 for numero in range(0,11)]if numero %2 == 0]