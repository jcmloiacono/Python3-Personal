import re

cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje facil de aprender y sensillo"

## METODO 1 SEARCH()

textoBuscar="aprender"

if re.search(textoBuscar, cadena) is not None:
	print ("En la Frace ha una palabra")

else:
	print("no existe esa palabra")

textoEncontrado=re.search(textoBuscar, cadena)

print (textoEncontrado.start())

print (textoEncontrado.end())

print (textoEncontrado.span())

print(re.findall(textoBuscar, cadena))

print (len(re.findall(textoBuscar,cadena)))