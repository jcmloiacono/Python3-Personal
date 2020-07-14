class Vehiculos():
    
    def __init__(self, marca, modelo):
    
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
        
    def arrancar(self):
        
        self.enmarcha=True
    
    def acelera(self):
        self.acelera=True
        
    def frena(self):
        self.frena=True
        
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
              self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

class Furgoneta(Vehiculos):

    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"

        else:
            return "La Furgoneta no esta Cargada"


class Moto(Vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo el Caballito"
        
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
              self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)



class VElectrico(Vehiculos):
    def __init__(self, marca, modelo):
        
        super().__init__(marca, modelo)
    
        self.autonomia=100
        
    def cargarEnergia(self):
      
        self.cargando=True
        



print ("EJEMPLO MOTO")

miMoto=Moto("Honda", "CBR")

miMoto.caballito()

miMoto.estado()

print("=============================================")

print("EJEMPLO FURGONETA")

miFurgoneta=Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print (miFurgoneta.carga(True))

print("=============================================")

class BicicletaEletrica(VElectrico, Vehiculos):
    pass

print("EJEMPLO BICICLETA")
          
miBici=BicicletaEletrica("Orbea", "Ob1430")
miBici.estado()
    