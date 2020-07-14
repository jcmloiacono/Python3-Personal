class Coche(): #CLASE COCHE

	def __init__(self): #METODO CONSTRUCTOR SE CREA CON DOS GUIONES BAJOS
		
		self.largoChasis=250  # 4 PROPIEDADES
		self.anchoChasis=120
		self.__ruedas=4   #ESTA ENCAPCULADA CON DOS GUIONES BAJOS
		self.enmarcha=False

	def arrancar(self,arrancamos): #COMPORTAMIENTO ó METODO
		self.enmarcha=arrancamos


		if(self.enmarcha):
			chequeo=self.__chequeo_interno()

		if(self.enmarcha and chequeo):
			return "El Coche esta en Marcha"

		elif(self.enmarcha and chequeo==False):
			return "Algo no esta bien en el Chequeo. No se puede arrancar"
		
		else:
			return "El Coche esta Parado"


	def estado(self): #CARACTERISTICAS IGUAL ES UN METODO
		print ("El Coche tiene ", self.__ruedas, " ruedas. Un Ancho de ", self.anchoChasis, "y un largo de ",
			self.largoChasis)


	def __chequeo_interno(self):
		print("realizando Chequeo Interno...")

		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="Cerradas"

		if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="Cerradas"):

			return True

		else:

			return False

miCoche=Coche() ##Instanciar una clase Llamada miCoche


print (miCoche.arrancar(True))

miCoche.estado()


print("**************************************************************")

miCoche2=Coche()

print(miCoche.arrancar(False))

miCoche2.estado()

