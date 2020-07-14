import re

lista_nombres=['Ana Gomez', 
				'Maria Martin',
				'Sandra Lopez',
				'Santiago Martin',
				'Shantal Ibañez', 
				'Sharon Ibañez',
				'niños',
				'niñas']

for elemento in lista_nombres:
	if re.findall('Martin$', elemento) or re.findall('^San', elemento):

		print (elemento, "+++++ Prueba 1 +++++")

for elemento in lista_nombres:
	if re.findall('[ñ]', elemento):

		print (elemento, "++++ Prueba 2 ++++++")

for elemento in lista_nombres:
	if re.findall('niñ[oa]s', elemento):

		print (elemento, "++++ Prueba 3 ++++++")