import math
import doctest

def raizCuadrada(listaNumeros):

	"""
	La funcion devuelve una lista con la 
	raiz cuadrada de los elementos numericos
	pasados por parametros en otra lista


	>>> lista=[]
	>>> for i in [4,9,16]:
	...		lista.append(i)
	>>> raizCuadrada(lista)
	[2.0, 3.0, 4.0]

	"""

	return [math.sqrt(n) for n in listaNumeros]

doctest.testmod()