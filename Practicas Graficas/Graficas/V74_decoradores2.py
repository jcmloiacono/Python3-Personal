def funcion_decoradora(funcion_parametro):

	def funcion_interior(*args, **kwargs): ##*args es para pueda recibir cualquier parametro

		print ("Vamos a realizar un Calculo")

		funcion_parametro(*args, **kwargs) ## **kwargs permite entrar Clave Valor

		print ("Hemos terminado el Calculo")

	return funcion_interior


@funcion_decoradora
def suma(num1, num2):

	print(num1+num2)

@funcion_decoradora
def resta(num1,num2):

	print(num1-num2)

@funcion_decoradora
def potencia(base, exponente):

	print(pow(base, exponente))

suma(7,3)

resta(6,2)

potencia(base=5, exponente=3)



