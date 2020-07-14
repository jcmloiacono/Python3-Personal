import doctest

def areaTriangulo(base, altura):

	"""
	Calcula el area de un triangulo utilizadon los parametrosb ase y altura

	>>> areaTriangulo(3,6)
	'El area del Triangulo es:9.0'

	"""

	return "El area del Triangulo es:" +str((base*altura)/2)


doctest.testmod()
