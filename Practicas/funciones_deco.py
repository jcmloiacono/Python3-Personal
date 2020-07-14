def monitorizar_args(funcion):

	def decorar(*args, **kwargs):
		print('\t Se esta ejecutando la funcion: ', funcion.__name__)

		funcion(*args, **kwargs)

		print('\t  Se ha finalizado la funcion: ',funcion.__name__)

	return decorar

@monitorizar_args
def hola(nombre):
	print ("Hola {}!".format(nombre))

@monitorizar_args
def adios(nombre):
	print("adios {}!".format(nombre))


hola('Jean Carlo')