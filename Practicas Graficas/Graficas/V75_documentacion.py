class Areas:
	"""Esta Clase calcula las arias de diferentes figuras Geometricas"""
	
	def areacuadrado(lado):

		"""Calcula el area de un cuadrado 
		elevado al cuadrado el lado pasando por parametro"""

		return "el area del cuadrado es: "+str(lado*lado)

	def areaTriangulo(base, altura):

		"""Calcula el area de un triangulo utilizadon los parametros
		base y altura"""

		return "el area del triangulo es: " +str((base*altura)/2)



	print(areaTriangulo(2,7))
	print(areacuadrado.__doc__)
	help(areacuadrado)
	help(areaTriangulo)

help(Areas)