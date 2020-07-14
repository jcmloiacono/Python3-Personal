import re

lista_nombres=['Ana', 
				'Barbara',
				'Carlos',
				'Tomas',
				'Shantal', 
				'Sharon',
				'niños',
				'niñas']

for elemento in lista_nombres:
	if re.findall('[m-u]$', elemento):
		
		print (elemento, "+++++ Prueba 1 +++++")

