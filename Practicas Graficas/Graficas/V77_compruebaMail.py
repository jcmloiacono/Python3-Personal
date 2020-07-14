import doctest

def compruebaMail(mailUsuario):

	"""
	la funcion comprueba Mail evalua un mail recibido
	en busca de la @. si tiene una @ es correcto, si tiene mas de un
	@ es incorrecto, sila @ esta al final es incorrecto
	
	>>> compruebaMail('jcmartinez@gmail.com')
	True
	
	>>> compruebaMail('jcmartinez@gmail@.com')
	False

	>>> compruebaMail('jcmartinezgmail.com')
	False
	
	>>> compruebaMail('jcmartinezgmail.com@')
	False
	
	



	"""

	arroba=mailUsuario.count('@')

	if(arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
		return False

	else:
		return True



doctest.testmod()
