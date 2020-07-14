def funcion_decoradora(funcion_parametro):

	def funcion_interior():

		print ("Vamos a realizar un Calculo")

		funcion_parametro()

		print ("Hemos terminado el Calculo")

	return funcion_interior




@funcion_decoradora
def suma():

	print(15+20)

@funcion_decoradora
def resta():

	print(20-15)

suma()

resta()